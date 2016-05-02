#!/usr/bin/env python

"""
Problem 4: Largest palindrome product
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x):
    return x.__str__() == x.__str__()[::-1]

def largest_palindrome():
    num, x, y, z = 0, 999, 999, 99
    while(x>z):
        while(y>z):
            k = x*y
            if k < num:
                break
            if is_palindrome(k):
                num = k
                z = y
                break
            y -= 1
        x -= 1
        y = x
    print num

if __name__ == "__main__":
    largest_palindrome()