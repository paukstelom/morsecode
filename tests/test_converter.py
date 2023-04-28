from engine import converter


def test_one_word_input():
    result = converter(text_input='hello')
    print(result)
    assert result == ['*', '*', '*', '*', '3 Units', '*', '3 Units', '*', '---', '*', '*', '3 Units', '*', '---', '*',
                      '*', '3 Units', '---', '---', '---']


def test_input_with_spaces():
    result = converter(text_input=' hello   ')
    print(result)
    assert result == ['*', '*', '*', '*', '3 Units', '*', '3 Units', '*', '---', '*', '*', '3 Units', '*', '---', '*',
                      '*', '3 Units', '---', '---', '---']


def test_input_with_many_words():
    result = converter(text_input='hello world')
    print(result)
    assert result == ['*', '*', '*', '*', '3 Units', '*', '3 Units', '*', '---', '*', '*', '3 Units', '*', '---', '*',
                      '*', '3 Units', '---', '---', '---', '7 Units', '*', '---', '---', '3 Units', '---', '---', '---',
                      '3 Units', '*', '---', '*', '3 Units', '*', '---', '*', '*', '3 Units', '---', '*', '*']


def test_input_with_many_spaces_between_words():
    result = converter(text_input='hello    world')
    print(result)
    assert result == ['*', '*', '*', '*', '3 Units', '*', '3 Units', '*', '---', '*', '*', '3 Units', '*', '---', '*',
                      '*', '3 Units', '---', '---', '---', '7 Units', '*', '---', '---', '3 Units', '---', '---', '---',
                      '3 Units', '*', '---', '*', '3 Units', '*', '---', '*', '*', '3 Units', '---', '*', '*']


def test_input_with_various_symbols():
    result = converter(text_input='hel/'']lo    world][]')
    print(result)
    assert result == ['*', '*', '*', '*', '3 Units', '*', '3 Units', '*', '---', '*', '*', '3 Units', '*', '---', '*',
                      '*', '3 Units', '---', '---', '---', '7 Units', '*', '---', '---', '3 Units', '---', '---', '---',
                      '3 Units', '*', '---', '*', '3 Units', '*', '---', '*', '*', '3 Units', '---', '*', '*']


def test_empty_input():
    result = converter(text_input='')
    print(result)
    assert result is None
