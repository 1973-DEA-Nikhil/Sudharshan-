from datetime import datetime
from typing import Dict, List


def process_logs(logs: List[str]) -> Dict[int, int]:
    user_durations = {}
    start_times = {}
    
    for log in logs:
        # Split the log by the first "]" to separate the timestamp
        timestamp_str, rest = log.split("] ", 1)
        timestamp_str = timestamp_str[1:]  # Remove the leading "["
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        
        # Now split the rest of the string to get user_id and action
        user_id_str, action = rest.split(" ", 1)
        user_id = int(user_id_str)
        
        if action == "start":
            start_times[user_id] = timestamp
        elif action == "stop":
            start_time = start_times.pop(user_id)  # Get the start time
            duration = (timestamp - start_time).total_seconds()  # Calculate duration in seconds
            if user_id in user_durations:
                user_durations[user_id] += int(duration)
            else:
                user_durations[user_id] = int(duration)
    
    return user_durations

logs = [
    "[2024-01-01 10:00:00] 1 start",
    "[2024-01-01 10:05:00] 1 stop",
    "[2024-01-01 10:00:00] 2 start",
    "[2024-01-01 10:10:00] 2 stop"
]

output = process_logs(logs)
print(output)
