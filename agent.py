import json
import yaml
import random
import uuid

# Mock MCP client execution
def execute_ability(ability_name, server, state):
    print(f"[MCP:{server}] Executing ability: {ability_name}")
    if ability_name == "solution_evaluation":
        return random.randint(50, 100)
    if ability_name in ["parse_request_text", "extract_entities"]:
        return f"{ability_name}_result"
    if ability_name in ["knowledge_base_search", "enrich_records"]:
        return f"{ability_name}_data"
    if ability_name == "clarify_question":
        return "Need more info from customer"
    if ability_name == "extract_answer":
        return "Customer answer captured"
    return f"{ability_name}_done"

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_input():
    with open("demo_input.json", "r") as f:
        return json.load(f)

def save_output(state):
    with open("output_payload.json", "w") as f:
        json.dump(state, f, indent=2)

def main():
    config = load_config()
    stages = config["stages"]
    state = load_input()

    print("\n🚀 Starting Lang Graph Agent Execution...\n")

    for stage in stages:
        stage_name = stage["name"]
        mode = stage.get("mode", "deterministic")
        abilities = stage.get("abilities", [])

        print(f"--- Stage: {stage_name} ({mode}) ---")

        if mode == "non-deterministic":
            for ability in abilities:
                result = execute_ability(ability["name"], ability["server"], state)
                if ability["name"] == "solution_evaluation":
                    state["solution_score"] = result
                    print(f"Score: {result}")
                    if result < 90:
                        print("Decision: Escalate to human agent")
                else:
                    state[ability["name"]] = result
        else:
            for ability in abilities:
                result = execute_ability(ability["name"], ability["server"], state)
                state[ability["name"]] = result

    print("\n✅ Final Structured Payload:")
    print(json.dumps(state, indent=2))

    save_output(state)
    print("\n🎉 Agent Execution Complete! Output saved to output_payload.json")

if __name__ == "__main__":
    main()
