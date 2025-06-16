import random, requests, time 

def generate_random_data():
    data = {
        "id": str(random.randint(100, 999)),
        "model_params": {
            "is_apartment": random.choice([True, False]),
            "studio": random.choice([True, False]),
            "has_elevator": random.choice([True, False]),
            "building_type_int": random.randint(1, 10),
            "floor": random.randint(1, 30),
            "kitchen_area": round(random.uniform(5.0, 20.0), 3),
            "living_area": round(random.uniform(20.0, 150.0), 3),
            "rooms": random.randint(1, 5),
            "total_area": round(random.uniform(30.0, 200.0), 3),
            "build_year": random.randint(1950, 2023),
            "latitude": round(random.uniform(55.0, 56.0), 6),
            "longitude": round(random.uniform(37.0, 38.0), 6),
            "ceiling_height": round(random.uniform(2.5, 3.5), 3),
            "flats_count": random.randint(50, 500),
            "floors_total": random.randint(1, 25)
        }
    }
    return data

def query_endpoint(n): 
    url = "http://127.0.0.1:8000/api/score_estate/"
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    cnt_queries_executed = 0
    for _ in range(n): 
        data = generate_random_data()
        requests.post(url, params={"id": data['id']}, headers=headers, json=data['model_params'])
        cnt_queries_executed += 1 
        time.sleep(.01)
    return cnt_queries_executed

if __name__ == "__main__":
    cnt_queries_executed = query_endpoint(1000)
    print(f'finished, {cnt_queries_executed} queries sent')