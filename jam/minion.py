"""
minion game

https://www.hackerrank.com/challenges/the-minion-game
"""


def extract_consonants(word):
    import re
    pattern = re.compile(r'[^AEIOU]')
    return pattern.findall(word)


def extract_vowels(word):
    import re
    pattern = re.compile(r'[AEIOU]')
    return pattern.findall(word)


def count_occurances(word, substr):
    '''
    count all non-overlapping and overlapping matches
    '''
    score = 0
    for ix in range(len(word) - len(substr) + 1):
        if word[ix:ix+len(substr)] == substr:
            score += 1
    return score


def create_all_substrings(word, pos):
    substrs = []
    for ix in range(len(word) - pos):
        substrs.append(word[pos:pos + ix+1])
    return substrs


def score(word, extract_starting):
    score = 0
    all_substr = []

    starting_chars = extract_starting(word)
    for v in set(starting_chars):
        ix = word.find(v, 0)
        while ix >= 0:
            pos = ix + 1
            all_substr.extend(create_all_substrings(word, ix))
            ix = word.find(v, pos)

    for substr in set(all_substr):
            score += count_occurances(word, substr)

    return score


def minion(word):
    return score(word, extract_vowels), score(word, extract_consonants)


if __name__ == "__main__":
    print(minion("BANANA"))

