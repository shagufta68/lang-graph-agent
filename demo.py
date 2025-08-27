import json 
 
with open("demo_input.json", "r") as f: 
    data = json.load(f) 
 
print("Customer Name:", data["customer_name"]) 
print("Full JSON Payload:", data) 
