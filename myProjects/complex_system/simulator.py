import numpy as np
from workers import spawn_workers
from reasoner import Reasoner
from problem_parser import parse_problem

class Simulator:
    def simulate(self, results: list[str], num_runs: int = 100) -> dict:
        # Explicit: Model as random walks or optimizations
        scores = {}
        for result in results:
            # Fake sim: Mean score from normal dist (replace with real physics/math)
            sim_scores = np.random.normal(80, 10, num_runs)  # Input -> Process
            scores[result] = float(np.mean(sim_scores))  # Convert to Python float
        
        best = max(scores, key=lambda k: scores[k])
        return {"best_solution": best, "score": round(scores[best], 2), "all": scores}

# Usage
problem = parse_problem("Optimize delivery routes for 10 trucks in a city with traffic")
reasoner = Reasoner()
hypotheses = reasoner.reason(problem)
worker_results = spawn_workers(hypotheses)

sim = Simulator()
simulation_output = sim.simulate(worker_results)
print(simulation_output)  # {'best_solution': '...', 'score': 82.3, ...}