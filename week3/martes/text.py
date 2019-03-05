def is_palindrome(word):
    """
    A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward,
    such as madam or racecar or the number 10801.

    :param word:
    :return: True or False
    Remarkably, a 2018 paper has demonstrated that every positive integer can be written as
    the sum of three palindromic numbers in every number system with base 5 or greater.

    """
    if word != "":
        if word.strip() == "": # or word.isspace():
            return False
        else:
            if word == word[::-1]:
                return True
            else:
                return False
    else:
        return False


