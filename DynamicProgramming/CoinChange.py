"""Problem:
Given an unlimited supply of coins of given denominations, find the total
number of distinct ways to get the desired change.

Input: S = { 1, 3, 5, 7 }, target = 8

The total number of ways is 6

{ 1, 7 }
{ 3, 5 }
{ 1, 1, 3, 3 }
{ 1, 1, 1, 5 }
{ 1, 1, 1, 1, 1, 3 }
{ 1, 1, 1, 1, 1, 1, 1, 1 }


Input: S = {1, 2, 3}, target = 4

The total number of ways is 4

{1, 3 }
{2, 2}
{1, 1, 2}
{1, 1, 1, 1}
"""
from datetime import datetime


def CoinChangeRecursion(source, target, idx=0):
    if target == 0:
        return 1

    if target < 0 or idx == len(source):
        return 0

    incl = CoinChangeRecursion(source, target - source[idx], idx=idx)
    excl = CoinChangeRecursion(source, target, idx=idx + 1)

    return incl + excl


def CoinChangeMemoize(source, target):
    memo = {}

    def recurse(_target, idx=0):
        key = (idx, _target)
        if key in memo:
            return memo[key]
        elif idx == len(source) or _target < 0:
            memo[key] = 0
        elif _target == 0:
            memo[key] = 1
        else:
            # do not accept the solution
            option1 = recurse(_target, idx=idx + 1)
            # accept the solution
            option2 = recurse(_target - source[idx], idx=idx)
            memo[key] = option1 + option2
        return memo[key]

    return recurse(target)


def CoinChangeDP(source, target):
    n = len(source)
    matrix = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        matrix[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if source[i - 1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - source[i - 1]]
    return matrix[-1][-1]


if __name__ == '__main__':
    test_cases = {
        'T1': {
            'args': {
                'source': [1, 2, 3],
                'target': 4,
            },
            'output': 4,
        },
        'T2': {
            'args': {
                'source': [1, 3, 5, 7],
                'target': 8,
            },
            'output': 6,
        },

    }

    start = datetime.now()
    for test_case, params in test_cases.items():
        result = CoinChangeRecursion(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Recursion Time: ', end - start)

    start = datetime.now()
    for test_case, params in test_cases.items():
        result = CoinChangeMemoize(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Memoize Time: ', end - start)

    start = datetime.now()
    for test_case, params in test_cases.items():
        result = CoinChangeDP(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Dynamic Programming Time: ', end - start)
