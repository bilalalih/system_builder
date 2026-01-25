import re
from dataclasses import dataclass

@dataclass
class Problem:
    goal: str
    constraints: list[str]
    variables: dict[str, str]  # e.g., {'num_trucks': '10', 'city': 'New York'}

def parse_problem(input_text: str) -> Problem:
    # Explicit regex for extraction (improve with NLP later)
    goal_match = re.search(r"(?:Optimize|Solve|Find) (.*?)(?= with| for|$)", input_text)
    constraints = re.findall(r"with ([^,\.]+)", input_text)
    variables = {v: k for k, v in re.findall(r"(\d+)\s+(\w+)", input_text)}  # Swap: word->key, number->value
    
    return Problem(
        goal=goal_match.group(1).strip() if goal_match else "Unknown",
        constraints=[c.strip() for c in constraints],
        variables=variables
    )

# Test: Input -> Process -> Output
problem = parse_problem("Optimize delivery routes for 10 trucks in a city with traffic")
print(problem)  # Output: Problem(goal='delivery routes', constraints=['traffic'], variables={'trucks': '10'})