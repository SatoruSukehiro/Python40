def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if num  <= 100 and num  >= 0 :
        multi_phrase = phrase[::]* num
        return multi_phrase
    else : 
        return 'invalid number '
    
''' dont understand why when the if statment is wrong it doenst push to else and return invalid number rather it gives me an unbound localerror stating that multphrase is refrence before assignment'''