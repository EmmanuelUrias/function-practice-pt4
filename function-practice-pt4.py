from math import factorial


def max_num(num1, num2, num3):
    answer = max(num1, num2, num3)
    return answer


# print(max_num(1, 4, 1))

def mult_list(lst):
    product = lst[0]
    for i in range(1, len(lst)):
        product *= lst[i]
    print(product)


# mult_list([2, 3, 5, 6])

def rev_string(s):
    s = list(s)
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[-i-1]
        s[-i-1] = temp
    print(''.join(s))


# rev_string("yooo")

def num_within(num1, num2, num3):
    if num1 > num2 and num1 <= num3:
        return True
    else:
        return False


# print(num_within(4, 2, 5))

# (x + y) ** n
# n! / r!(n - r)!

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


def pascal(n):
    for i in range(n):
        for j in range(n-i+1):

            print(end=" ")

        for j in range(i+1):

            # nCr = n!/((n-r)!*r!)
            x = i - j
            print(factorial(i)//(factorial(j)*factorial(x)), end=" ")

        # for new line
        print()


pascal(5)
