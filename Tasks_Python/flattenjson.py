from typing import Any, Dict


def flatten_json(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    items = {}
    for key, value in nested_dict.items():
        # Create a new key by combining the parent key with the current key
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        # If the value is a dictionary, recurse into it
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key, sep=sep))
        else:
            # If the value is not a dictionary, add it to the result
            items[new_key] = value
            
    return items

# Example usage:
if __name__ == "__main__":
    nested_dict = {
        "user": {
            "id": 1,
            "details": {
                "name": "Alice",
                "address": {
                    "city": "New York",
                    "zipcode": 10001
                }
            }
        }
    }

    flattened = flatten_json(nested_dict)
    print(flattened)
