import threading
import time
from reasoner import Reasoner
from problem_parser import parse_problem

class Worker:
    def __init__(self, name: str, task: str):
        self.name = name
        self.task = task
    
    def execute(self) -> str:
        # Simulate work (replace with real logic, e.g., API calls)
        time.sleep(1)  # Process
        return f"{self.name} completed: {self.task} with result Y"

def spawn_workers(hypotheses: list[str]) -> list[str]:
    threads = []
    results = []
    lock = threading.Lock()  # For shared output
    
    def worker_thread(worker: Worker):
        result = worker.execute()
        with lock:
            results.append(result)
    
    for i, hypo in enumerate(hypotheses):
        worker = Worker(f"Agent-{i}", hypo)
        t = threading.Thread(target=worker_thread, args=(worker,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return results

# Usage
problem = parse_problem("Optimize delivery routes for 10 trucks in a city with traffic")
reasoner = Reasoner()
hypotheses = reasoner.reason(problem)

worker_results = spawn_workers(hypotheses)
print(worker_results)  # Output: ['Agent-1 completed...', ...]