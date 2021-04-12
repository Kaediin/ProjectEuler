def is_palindrome(word):
    return word == word[::-1]

def is_prime(n):
    """
    Retourneer True als n (int) een priemgetal is, anders False. Je kunt gebruik maken van de functie 'div(n)'
    om te bepalen of n een priem is.
    Optioneel: bedenk een efficiënter alternatief.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True