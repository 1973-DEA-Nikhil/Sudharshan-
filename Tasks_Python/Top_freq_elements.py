from collections import Counter
from typing import List


def top_n_frequent_words(words: List[str], n: int) -> List[str]:
    # Step 1: Count the frequency of each word
    word_count = Counter(words)
    
    # Step 2: Sort by frequency (descending) and lexicographically (ascending)
    sorted_words = sorted(word_count.keys(), key=lambda word: (-word_count[word], word))
    
    # Step 3: Return the top N words
    return sorted_words[:n]

# Example usage:
if __name__ == "__main__":
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    n = 2

    result = top_n_frequent_words(words, n)
    print(result)
