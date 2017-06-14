"""
minion game
https://www.hackerrank.com/challenges/the-minion-game

this is an example how a hack can go wrong
decomposed the problem and created small functions which do one simple thing
wrote calculate_score() to put it all together

see the warning signs of a poor solution:
    iterating over the word and slicing it two times
    find a character in the word, forget the position;
        find the character again to get the position
    have the solution, remove parts of it using set(),
        recreate the deleted parts

lesson learned:
    write tests for calculate_score() first
    calculate the results by hand
"""


def extract_consonants(word):
    ''' find all upper-case consonants in a word '''
    import re
    pattern = re.compile(r'[^AEIOU]')
    return pattern.findall(word)


def extract_vowels(word):
    ''' find all upper-case vowels in a word '''
    import re
    pattern = re.compile(r'[AEIOU]')
    return pattern.findall(word)


def count_occurances(word, substr):
    ''' count all non-overlapping and overlapping matches '''
    counter = 0
    for ix in range(len(word) - len(substr) + 1):
        if word[ix:ix+len(substr)] == substr:
            counter += 1
    return counter


def create_all_substrings(word, pos):
    ''' create all substrings starting at pos
    MINION, 3
    ["I", "IO", "ION"]
    '''
    substrs = []
    for ix in range(len(word) - pos):
        substrs.append(word[pos:pos + ix+1])
    return substrs


def calculate_score(word, extract_starting):
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


def play_minion(word):
    return calculate_score(word, extract_vowels), calculate_score(word, extract_consonants)
