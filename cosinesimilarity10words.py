####################################
##### cosinesimilarity_test.py #####
####################################

'''

This is is the test script from original source to see how accurate are the predictions with some examples.
It does not need any input argument. Just run. To introduce an argument for predic, better run in command prompt:
cosinesimilarityprediction.py + wordTarget

'''



######
# 1) # Loading required libraries
######

from typing import Any, Iterable, List, Optional, Set, Tuple

from load import load_words
import math
import vectors as v
from vectors import Vector
from word import Word

# Timing info for most_similar (100k words):
# Original version: 7.3s
# Normalized vectors: 3.4s




######
# 2) # Declaring functions
######

# 2.1
def most_similar(base_vector: Vector, words: List[Word]) -> List[Tuple[float, Word]]:
    """Finds n words with smallest cosine similarity to a given word"""
    words_with_distance = [(v.cosine_similarity_normalized(base_vector, w.vector), w) for w in words]
    # We want cosine similarity to be as large as possible (close to 1)
    sorted_by_distance = sorted(words_with_distance, key=lambda t: t[0], reverse=True)
    return sorted_by_distance

# 2.2

def print_most_similar(words: List[Word], text: str) -> None:
    base_word = find_word(text, words)

    if not base_word:
        print(f"Uknown word: {text}")
        return
    print(f"\n\tWords related to {base_word.text}:")
    sorted_by_distance = [
        word.text for (dist, word) in
            most_similar(base_word.vector, words)
            if word.text.lower() != base_word.text.lower()
        ]
    print(', '.join(sorted_by_distance[:10]))





# 2.4

def find_word(text: str, words: List[Word]) -> Optional[Word]:
    try:
       return next(w for w in words if text == w.text)
    except StopIteration:
       return None

# 2.5

def closest_analogies(
    left2: str, left1: str, right2: str, words: List[Word]
) -> List[Tuple[float, Word]]:
    word_left1 = find_word(left1, words)
    word_left2 = find_word(left2, words)
    word_right2 = find_word(right2, words)
    if (not word_left1) or (not word_left2) or (not word_right2):
        return []
    vector = v.add(
        v.sub(word_left1.vector, word_left2.vector),
        word_right2.vector)
    closest = most_similar(vector, words)[:10]
    def is_redundant(word: str) -> bool:
        """
        Sometimes the two left vectors are so close the answer is e.g.
        "shirt-clothing is like phone-phones". Skip 'phones' and get the next
        suggestion, which might be more interesting.
        """
        word_lower = word.lower()
        return (
            left1.lower() in word_lower or
            left2.lower() in word_lower or
            right2.lower() in word_lower)
    closest_filtered = [(dist, w) for (dist, w) in closest if not is_redundant(w.text)]
    return closest_filtered

#2.6

def print_analogy(left2: str, left1: str, right2: str, words: List[Word]) -> None:
    analogies = closest_analogies(left2, left1, right2, words)
    if (len(analogies) == 0):
        print(f"\t{left2}-{left1} is like {right2}-?\n")
    else:
        (dist, w) = analogies[0]
        #alternatives = ', '.join([f"{w.text} ({dist})" for (dist, w) in analogies])
        print(f"\t{left2}-{left1} is like {right2}-{w.text}\n")




######
# 3) # Executing functions
######

#O# words = load_words('data/words.vec')
words = load_words('data/wordvectors/words_test2.vec') #Running the biggest wordvector provided by fasttext




if __name__ == "__main__":
    #a = int(sys.argv[1])
    #b = int(sys.argv[2])
    #hello(a, b)

    print_most_similar(words, str(sys.argv[1]))
