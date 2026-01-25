from fastapi import FastAPI
from pydantic import BaseModel
from problem_parser import parse_problem
from reasoner import Reasoner
from workers import spawn_workers
from simulator import Simulator

app = FastAPI()

# Initialize instances
reasoner = Reasoner()
sim = Simulator()

class ProblemInput(BaseModel):
    text: str

@app.post("/solve")
async def solve_problem(input: ProblemInput):
    problem = parse_problem(input.text)
    hypotheses = reasoner.reason(problem)
    worker_results = spawn_workers(hypotheses)
    sim_output = sim.simulate(worker_results)
    return sim_output

# Run: uvicorn api:app --reload