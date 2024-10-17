from typing import Dict, List


def deduplicate(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    unique_records = []
    seen_emails = set()
    
    for record in records:
        email = record["email"]
        if email not in seen_emails:
            unique_records.append(record)  # Keep the first occurrence
            seen_emails.add(email)  # Mark this email as seen
    
    return unique_records
records = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
    {"id": "3", "name": "Alice", "email": "alice@example.com"}
]

output = deduplicate(records)
print(output)
