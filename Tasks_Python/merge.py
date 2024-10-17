from typing import Dict, List, Union


def merge_data(employees: List[Dict[str, Union[str, int]]], departments: List[Dict[str, str]]) -> List[Dict[str, Union[str, int]]]:
    # Step 1: Create a dictionary mapping department_id to department_name
    department_mapping = {dept['id']: dept['department_name'] for dept in departments}
    
    # Step 2: Merge department_name into each employee's data
    for employee in employees:
        department_id = employee['department_id']
        employee['department_name'] = department_mapping.get(department_id, "Unknown")  # Add department_name
        
    return employees

# Example usage:
if __name__ == "__main__":
    employees = [
        {"id": 1, "name": "Alice", "department_id": 2},
        {"id": 2, "name": "Bob", "department_id": 1}
    ]
    
    departments = [
        {"id": 1, "department_name": "Engineering"},
        {"id": 2, "department_name": "Marketing"}
    ]
    
    result = merge_data(employees, departments)
    print(result)
