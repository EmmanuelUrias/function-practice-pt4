def max_num(num1, num2, num3):
    answer = max(num1, num2, num3)
    return answer


# print(max_num(1, 4, 1))

def mult_list(lst):
    product = lst[0]
    for i in range(1, len(lst)):
        product *= lst[i]
    print(product)


mult_list([2, 3, 5, 6])
