def sum_array(array):
    if len(array)== 1:
        return array[0]
    else:
        return array[0]+ sum_array(array[1:])

    '''Return sum of all items in array'''

def fibonacci(n):
    if n == 0 :
        return 0
    elif n <=2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

    '''Return nth term in fibonacci sequence'''


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n-1)

    '''Return n!'''


def reverse(word):


    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
    '''Return word in reverse'''
