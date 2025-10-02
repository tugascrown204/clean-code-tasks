# Example Task - Fibonacci Sequence

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    A clean code implementation should be clear about the intended approach.
    """
    if n<0:
        raise ValueError('Input should be a non-negative integer.')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    import sys
    try:
        n = int(sys.argv[1])
        print(f'The {n}th Fibonacci number is: {fibonacci(n)}')
    except IndexError:
        print('Please provide an integer as an argument.')
    except ValueError as e:
        print(e)
