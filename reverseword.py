#!/usr/bin/python
# -*- coding: utf-8 -*-
"""@package docstring
Reverse Word.

Receives as a paramenter one sentence. As a result, it prints the sentence in a reverse order.
"""


def reverse(user_input):
    """Function Reverse.
    Receives user_input as a sentence
    """

    user_input_array = user_input.split(' ')
    word_result = ''
    for i in range(1, len(user_input_array) + 1):
        word_result += user_input_array[len(user_input_array) - i]
        if i < len(user_input_array):
            word_result += ' '
    return word_result


if __name__ == '__main__':
    user_input = input('Ingrese una oracion: ')
    print reverse(user_input)