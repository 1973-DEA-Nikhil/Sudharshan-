from typing import List


def reformat_dates(dates: List[str]) -> List[str]:
    reformatted_dates = []
    
    # Iterate over each date in the list
    for date in dates:
        # Split the date into day, month, and year
        day, month, year = date.split('-')
        
        # Reformat the date to "YYYY-MM-DD" and append to the result list
        reformatted_dates.append(f"{year}-{month}-{day}")
    
    return reformatted_dates

# Example usage:
dates = ["31-12-2024", "01-01-2024"]
output = reformat_dates(dates)
print(output)
