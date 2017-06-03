from mastermind import count_cracked


def test_unique_digits_and_exact_match_should_give_all_blacks():
    code  = [1,2,3,4]
    guess = '1234'

    blacks, whites = count_cracked(guess, code)

    assert blacks == 4
    assert whites == 0


def test_unique_digits_and_two_switched_should_give_two_blacks_two_whites():
    code  = [1,2,3,4]
    guess = '4231'

    blacks, whites = count_cracked(guess, code)

    assert blacks == 2
    assert whites == 2


def test_duplicates_in_guess_have_one_match_should_give_one_white():
    code  = [1,2,3,4]
    guess = '6111'

    blacks, whites = count_cracked(guess, code)

    assert blacks == 0
    assert whites == 1


def test_duplicates_in_code_have_one_match_should_give_one_white():
    code  = [1,1,1,4]
    guess = '6321'

    blacks, whites = count_cracked(guess, code)

    assert blacks == 0
    assert whites == 1


def test_duplicates_in_code_have_two_matches_should_give_one_white_one_black():
    code  = [1,1,1,4]
    guess = '6121'

    blacks, whites = count_cracked(guess, code)

    assert blacks == 1
    assert whites == 1
