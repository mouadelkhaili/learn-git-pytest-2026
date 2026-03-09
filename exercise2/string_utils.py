# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    reversed_str=""
    for p in s:
        reversed_str= p + reversed_str
    return reversed_str    
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
    vowels = set('aeiou')
    return sum(1 for char in s if char.lower() in vowels)
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    phrase=''.join(p.lower() for p in s if p.isalnum())
    return phrase==phrase[::-1]
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    result = []
    i = 0
    n = len(s)
    while i < n:
        if s[i].isspace():
            result.append(s[i])
            i += 1
        else:
            start = i
            while i < n and not s[i].isspace():
                i += 1
            word = s[start:i]
            if word:
                capitalized = word[0].upper() + word[1:]
                result.append(capitalized)
    return ''.join(result)
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """      
                

    # TODO: Implement this function
    pass
