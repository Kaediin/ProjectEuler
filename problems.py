from utils import *
import math


def problem_1():
    """ Answer: 233168 """
    print(sum([e for e in range(1000) if e % 3 == 0 or e % 5 == 0]))


def problem_2():
    """ Answer: 4613732 """
    last, current, total = 1, 1, 0
    while current < 4000000:
        new = last + current
        last = current
        current = new
        total += new if new % 2 == 0 else 0
    print(total)


def problem_3():
    """ Answer: 6857 """
    n = 600851475143
    i = 2
    factor = 0
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factor = i
    if n > 1:
        factor = n
    print(factor)


def problem_4():
    """ Answer: 906609 """
    n1 = 999
    n2 = 999
    largest = 0
    while n2 != 899:
        if is_palindrome(str(n1 * n2)):
            pal = n1 * n2
            if pal > largest:
                largest = pal
        n1 -= 1
        if n1 == 899:
            n1 = 999
            n2 -= 1
    print(largest)


def problem_5():
    """ Answer: 232792560 """
    n = 0
    while True:
        broke = False
        n += 1
        for div in range(1, 21):
            if n % div != 0:
                broke = True
                break
        if broke:
            continue
        else:
            print(n)
            return


def problem_6():
    """ Answer: 25164150 """
    print(sum([e for e in range(1, 101)]) ** 2 - sum([e ** 2 for e in range(1, 101)]))


def problem_7():
    """ Answer: 104743 """
    num, counter = 0, 0
    while counter != 10001:
        num += 1
        counter += 1 if is_prime(num) else 0

    print(num)


# def problem_8():

def problem_9():
    print(math.sqrt(1000))


def problem_10():
    """ Answer: 142913828922 """
    print(sum([e for e in range(2000000) if is_prime(e)]))


def problem_12():
    n = 1000000000
    while True:
        counter = []
        i = 1
        while True:
            if i <= n:
                if n % i == 0:
                    counter.append(i)
                i += 1
            else:
                break
        if len(counter) >= 500:
            print(counter)
            print(n)
            return
        print(n, i, len(counter))
        n += 1


problem_12()
