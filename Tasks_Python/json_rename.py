from typing import Dict, List, Union


def rename_fields(data: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    # Iterate over each dictionary in the list
    for record in data:
        # If the 'location' key exists, rename it to 'city'
        if 'location' in record:
            record['city'] = record.pop('location')
    
    return data

# Example usage:
data = [
    {"name": "Alice", "age": 25, "location": "New York"},
    {"name": "Bob", "age": 30, "location": "San Francisco"}
]

output = rename_fields(data)
print(output)
