from typing import List


def sliding_window_sum(transactions: List[int], k: int) -> List[int]:
    result = []
    
    # Loop through the list, stopping when there are no more complete windows
    for i in range(len(transactions) - k + 1):
        window_sum = sum(transactions[i:i + k])
        result.append(window_sum)
    
    return result

# Example usage:
if __name__ == "__main__":
    transactions = [10, 20, 30, 40, 50]
    k = 3

    output = sliding_window_sum(transactions, k)
    print(output)
