import json
from typing import Dict, List, Union


def transform_data(rows: List[Dict[str, Union[str, int]]]) -> Dict[int, Dict[str, Union[str, int]]]:
    transformed_data = {}
    for row in rows:
        user_id = row.pop("user_id")  # Extract the user_id and remove it from the row
        transformed_data[user_id] = row  # Assign the remaining data to the user_id key
    return transformed_data
rows = [
    {"user_id": 1, "name": "Alice", "age": 25, "city": "New York"},
    {"user_id": 2, "name": "Bob", "age": 30, "city": "San Francisco"}
]

output = transform_data(rows)



# Assuming output is the result from transform_data(rows)
print(json.dumps(output, indent=2))
