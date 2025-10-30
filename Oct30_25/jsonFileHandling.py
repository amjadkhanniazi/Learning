import json
def save_json( config_data,filename="config.json"):
    try:
        with open(filename, 'w') as json_file:
            json.dump(config_data, json_file, indent=4)
            return True
    except Exception as e:
        print(f"Error Saving Json Data: {e}")
        return False
    
def load_json(filename="config.json"):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {"debug": "File not found", "Port": 5000}


config = {
    "dataUrl" : "https://api.example.com/data",
    "retryAttempts" : 5,
    "timeout" : 30
}

var=save_json(config)
print(var)

loaded_config = load_json()
print(loaded_config)