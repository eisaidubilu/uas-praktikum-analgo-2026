import json

def load_delivery_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return {
            "locations": data["locations"],
            "weights": data["packages_weight"],
            "matrix": data["distance_matrix"],
            "scenarios": data["scenarios"]
        }
    except FileNotFoundError:
        print(f"Error: File {filepath} tidak ditemukan!")
        return None