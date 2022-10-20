"""
Help ATM to split given amount into banknotes/coins.
1. Write a function, which splits a given amount into the least amount of banknotes/coins.
  The function should receive two parameters:
    `amount` - a number which an ATM user wants to cashout (this value has to be split into banknotes).
    `banknotes` - a list of available banknotes/coins, lets use [1, 2, 5] as a default value for this list.
  The function should return:
    a list, consisting of biggest banknotes/coins, which can be used to split the amount.
    False - if its not possible to split the amount into banknotes.
  For example,
    if amount is 13, available banknotes - [1, 2, 5], the returned value should be [5, 5, 2, 1].

2. Update the function (and add new test) to work with any list of banknotes.
  For example,
    if amount is 13, available banknotes - [1, 10], the returned value should be [10, 1, 1, 1].
    if amount is 13, available banknotes - [2, 5], the returned value should be False.

3. Update the function (and add new test) to work with cents, i.e. banknotes/coins can be floating point numbers.
  For example,
    if amount is 11.5, available banknotes - [0.5, 1, 10], the returned value should be [10, 1, 0.5].

4. Write a primitive unit tests for your function.

5. Make sure your code works with `amount = 11, banknotes = [5,2]`, solution is `5, 2, 2, 2`.
"""


def split_amount(amount: int, banknotes=[5, 2, 1]):
    banknotes.sort(reverse=True)
    banknotes_list = []
    min_banknote = min(banknotes)
    initial_amount = amount
    for i in banknotes:
        while amount >= i:
            if i != min_banknote and\
            amount - i < min_banknote and\
            amount - i > 0:
                break
            banknotes_list.append(i)
            amount -= i
    if amount > 0 or initial_amount == 0:
        return False
    return banknotes_list


if __name__ == "__main__":
    assert(split_amount(11, [5, 2, 1])) == [5, 5, 1]
    assert(split_amount(13, [5, 2, 1])) == [5, 5, 2, 1]
    assert(split_amount(0, [5, 2, 1])) == False
    assert(split_amount(26, [5, 2, 1])) == [5, 5, 5, 5, 5, 1]
    assert(split_amount(26, [10, 5, 2, 1])) == [10, 10, 5, 1]
    assert(split_amount(26.5, [10, 5, 2, 1, 0.5])) == [10, 10, 5, 1, 0.5]
    assert(split_amount(28.5, [10, 5, 2, 1, 0.5])) == [10, 10, 5, 2, 1, 0.5]
    assert(split_amount(26.7, [10, 5, 2, 1, 0.5])) == False
    assert(split_amount(11, [5, 2])) == [5, 2, 2, 2]
    assert(split_amount(13, [5, 2])) == False
    print("ALL TESTS PASSED")
