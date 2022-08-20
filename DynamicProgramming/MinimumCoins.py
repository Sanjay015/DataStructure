"""Problem:
Given a sum to be find with minimum number of coins. Example:
    sum = 18
    coins = [7, 5, 1]
    result = 4 (7+5+5+1)
"""
from datetime import datetime


def MinimumCoinsRecursion(coins, total, idx=0):
    # Complexity: O(2 ^ m + n)
    # base case
    if total == 0 or idx == len(coins):
        return 0
    # if coins value is greater proceed with next coin value
    elif coins[idx] > total:
        return MinimumCoinsRecursion(coins, total, idx=idx + 1)
    else:
        # do not accept the solution
        option1 = MinimumCoinsRecursion(coins, total, idx=idx + 1)
        # accept the solution
        option2 = 1 + MinimumCoinsRecursion(coins, total - coins[idx])
        if option1 != 0:
            option2 = min(option1, option2)
        return option2


def MinimumCoinsMemoize(coins, total):
    # Complexity: O(m * n)
    memo = {}

    def recurse(_total, idx=0):
        key = (_total, idx)
        if key in memo:
            return memo[key]
        elif idx == len(coins) or _total == 0:
            memo[key] = 0
        elif coins[idx] > _total:
            return recurse(_total, idx=idx + 1)
        else:
            # do not accept the solution
            option1 = recurse(_total, idx=idx + 1)
            # accept the solution
            option2 = 1 + recurse(_total - coins[idx])
            if option1 != 0:
                option2 = min(option1, option2)
            memo[key] = option2
        return memo[key]

    return recurse(total)


def MinimumCoinsDP(coins, total):
    # Complexity: O(n(length of coins) * w(total capacity))
    if total == 0:
        return 0

    matrix = [float('inf') for _ in range(total + 1)]
    matrix[0] = 0

    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] > i:
                continue
            res = matrix[i - coins[j]]
            if res != float('inf') and res + 1 < matrix[i]:
                matrix[i] = res + 1

    if matrix[-1] == float('inf'):
        return -1
    return matrix[-1]


if __name__ == '__main__':
    test_cases = {
        'T1': {
            'args': {
                'coins': [9, 6, 5, 1],
                'total': 11,
            },
            'output': 2,
        },
        'T2': {
            'args': {
                'coins': [7, 5, 1],
                'total': 18,
            },
            'output': 4,
        },
    }

    start = datetime.now()
    for test_case_num, params in test_cases.items():
        result = MinimumCoinsRecursion(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Recursion Time: ', end - start)

    start = datetime.now()
    for test_case_num, params in test_cases.items():
        result = MinimumCoinsMemoize(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Memoize Time: ', end - start)

    start = datetime.now()
    for test_case_num, params in test_cases.items():
        result = MinimumCoinsDP(**params['args'])
        assert params['output'] == result
    end = datetime.now()
    print('Dynamic Programming Time: ', end - start)
