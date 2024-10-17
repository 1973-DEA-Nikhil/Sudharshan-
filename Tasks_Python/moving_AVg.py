from collections import deque


class MovingAverage:
    def __init__(self, k: int):
        # Initialize with window size k
        self.k = k
        self.window = deque()  # A deque to hold the sliding window values
        self.window_sum = 0  # Keep track of the sum of the values in the window

    def next(self, val: int) -> float:
        # Add new value to the window
        self.window.append(val)
        self.window_sum += val
        
        # If the window exceeds size k, pop the oldest value
        if len(self.window) > self.k:
            oldest_val = self.window.popleft()
            self.window_sum -= oldest_val
        
        # Return the moving average
        return self.window_sum / len(self.window)

# Example usage:
if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(10))  # returns 10.0
    print(ma.next(20))  # returns 15.0
    print(ma.next(30))  # returns 20.0
    print(ma.next(40))  # returns 30.0
