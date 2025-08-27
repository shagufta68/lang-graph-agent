import json

# Load the input JSON
with open("demo_input.json", "r") as f:
    data = json.load(f)

# Add extra fields (simulating agent's output)
data["solution_score"] = 95
data["decision"] = "Resolved automatically"
data["response"] = "We apologize for the delay. Your order is on the way."

# Pretty print the final JSON
print(json.dumps(data, indent=2))

