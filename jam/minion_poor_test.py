import minion_poor as minion


def test_extract_vowels():
    word = "NANANA"
    vowels = minion.extract_vowels(word)
    assert vowels == ['A', 'A', 'A']


def test_extract_vowels_empty_word():
    word = ""
    vowels = minion.extract_vowels(word)
    assert vowels == []


def test_extract_consonants():
    word = "NANANA"
    vowels = minion.extract_consonants(word)
    assert vowels == ['N', 'N', 'N']


def test_count_occurances():
    word = "NANANA"
    counted = minion.count_occurances(word, "NA")
    assert counted == 3


def test_count_occurances_many_overlaps():
    word = "NNNNNA"
    counted = minion.count_occurances(word, "NNN")
    assert counted == 3


def test_create_all_substr():
    word = "NANANA"
    substrs = minion.create_all_substrings(word, 1)
    assert substrs == ["A", "AN", "ANA", "ANAN", "ANANA"]


def test_create_all_substr_single_letter_word():
    word = "N"
    substrs = minion.create_all_substrings(word, 0)
    assert substrs == ["N"]


def test_create_all_substr_empty_word():
    word = ""
    substrs = minion.create_all_substrings(word, 0)
    assert substrs == []


def test_calculate_score():
    word = "NN"
    score = minion.calculate_score(word, minion.extract_vowels)
    assert score == 0
    score = minion.calculate_score(word, minion.extract_consonants)
    assert score == 3


def test_calculate_score_empty_word():
    word = ""
    score = minion.calculate_score(word, minion.extract_vowels)
    assert score == 0
    score = minion.calculate_score(word, minion.extract_consonants)
    assert score == 0


def test_calculate_score_all_unique():
    word = "ABCDEFGHI"
    score = minion.calculate_score(word, minion.extract_vowels)
    assert score == 15
    score = minion.calculate_score(word, minion.extract_consonants)
    assert score == 30


def test_calculate_score_two_repeating():
    word = "NNAANNAA"
    score = minion.calculate_score(word, minion.extract_vowels)
    assert score == 14
    score = minion.calculate_score(word, minion.extract_consonants)
    assert score == 22
