def amount_and_sum_of_even_nums(input_list):
    amount_result = 0
    sum_result = 0
    for i in input_list:
        if i % 2 == 0 and i > 0:
            amount_result += 1
            sum_result += i
    return {'amount': amount_result, 'sum': sum_result}


if __name__ == '__main__':
    print(amount_and_sum_of_even_nums([1, 2, 3, 4]))


def test_amount_and_sum_of_even_nums():
    assert amount_and_sum_of_even_nums([1, 2, 3, 4]) == {'amount': 2, 'sum': 6}
