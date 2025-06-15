import random
import copy
import requests
import json

def generate_random_data():
    # Original template
    data = {
        "id": "123",
        "model_params": {
            "is_apartment": False,
            "studio": False,
            "has_elevator": True,
            "building_type_int": 4,
            "floor": 5,
            "kitchen_area": 8.0,
            "living_area": 56.0,
            "rooms": 2,
            "total_area": 52.0,
            "build_year": 2007,
            "latitude": 55.72347640991211,
            "longitude": 37.903202056884766,
            "ceiling_height": 2.740000009536743,
            "flats_count": 376,
            "floors_total": 11
        }
    }
    
    # Create a deep copy to modify
    modified_data = copy.deepcopy(data)
    
    # Define ranges for each numerical parameter
    ranges = {
        "building_type_int": (1, 10),
        "floor": (1, 30),
        "kitchen_area": (5.0, 20.0),
        "living_area": (20.0, 150.0),
        "rooms": (1, 5),
        "total_area": (30.0, 200.0),
        "build_year": (1950, 2023),
        "latitude": (55.0, 56.0),
        "longitude": (37.0, 38.0),
        "ceiling_height": (2.5, 3.5),
        "flats_count": (50, 500),
        "floors_total": (1, 25)
    }
    
    # Randomly modify each numerical value
    for key in ranges:
        if key in modified_data["model_params"]:
            min_val, max_val = ranges[key]
            
            if isinstance(modified_data["model_params"][key], int):
                modified_data["model_params"][key] = random.randint(min_val, max_val)
            else:
                modified_data["model_params"][key] = round(random.uniform(min_val, max_val), 3)
    
    # Also randomize the ID
    modified_data["id"] = str(random.randint(100, 999))
    
    return modified_data

def query_endpoint(n_queries): 
    url = "http://127.0.0.1:8000/api/score_estate/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    for i in range(n_queries): 
        random_data = generate_random_data()
        response = requests.post(
            url, 
            params={"id":random_data['id']}, headers=headers, json=random_data['model_params']
        )


# Example usage
if __name__ == "__main__":
    query_endpoint(500)
    print('finished')