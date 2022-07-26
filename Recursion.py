# Task 1

def to_power(x: int | float, exp: int) -> int | float:
    if exp == 1:
        return x
    elif exp < 0:
        raise ValueError('This function works only with exp > 0.')
    return x * to_power(x, exp - 1)


##############################################################################
# Task 2

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if looking_str[index] == looking_str[len(looking_str)-1]:
        return is_palindrome(looking_str[1:len(looking_str)-1])


###########################################################################
# Task 3

def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError("This function works only with postive integers")
    if n == 0:
        return 0
    if n == 1:
        return a
    return a + mult(a, n-1)


#############################################################################
# Task 4

def reverse(input_str: str) -> str:
    if len(input_str) < 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:-1])


#############################################################################
# Task 5

def sum_of_digits(digit_string: str) -> int:
    if digit_string.isalpha():
        raise ValueError("input string must be digit string")
    if len(digit_string) == 1:
        return int(digit_string)
    else:
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])


def main():
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    # print(to_power(2, -1))

    print('#'*80)
    print(is_palindrome('sassas'))
    print(is_palindrome('mom'))
    print(is_palindrome('o'))

    print('#' * 80)
    print(mult(2, 4))
    print(mult(2, 0))
    # print(mult(2, -4))

    print('#' * 80)
    print(reverse("hello"))

    print('#' * 80)
    print(sum_of_digits('26'))
    print(sum_of_digits('1234'))
    # print(sum_of_digits('test'))


if __name__ == '__main__':
    main()
