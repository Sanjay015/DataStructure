"""Problem:
You are in charge of selecting a football team from a large pool of players.
Each player has a cost and a rating. You have a limited budget. What is the
highest total rating of a team that fits within your budget. Assume that
there is no minimum or maximum team size.

Example:
    profit/rating = [2, 3, 2, 5, 4, 7]
    weight/cost = [4, 5, 1, 3, 2, 5]
    weight/capacity = 15
    Output: 19

    Best Solution:
    profit/rating = [2, `3`, 2, `5`, `4`, `7`]
    weight/cost =   [4, `5`, 1, `3`, `2`, `5`]
    maximum rating is: 3 + 5 + 4 + 7 = 19
    cost             : 5 + 3 + 2 + 5 = 15(which is our capacity)
"""
from datetime import datetime


def KnapSackProblemRecursion(weights, profits, capacity, idx=0):
    # Complexity: O(2 ^ n)
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return KnapSackProblemRecursion(weights, profits, capacity, idx=idx + 1)
    else:
        option1 = KnapSackProblemRecursion(
            weights, profits, capacity, idx=idx + 1)
        option2 = profits[idx] + KnapSackProblemRecursion(
            weights, profits, capacity - weights[idx], idx=idx + 1)
        return max(option1, option2)


def KnapSackProblemMemoize(weights, profits, capacity):
    # Complexity: O(m * n)
    memo = {}

    def recursive(_capacity, idx=0):
        key = (_capacity, idx)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > _capacity:
            return recursive(_capacity, idx=idx + 1)
        else:
            memo[key] = max(
                recursive(_capacity, idx=idx + 1),
                profits[idx] + recursive(_capacity - weights[idx], idx=idx + 1))
        return memo[key]

    return recursive(capacity, idx=0)


def KnapSackProblemDP(weights, profits, capacity):
    # Complexity: O(n(length of weights) * w(total capacity))
    n = len(weights)
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                matrix[i + 1][c] = matrix[i][c]
            else:
                matrix[i + 1][c] = max(
                    matrix[i][c],
                    profits[i] + matrix[i][c - weights[i]]
                )
    return matrix[-1][-1]


if __name__ == '__main__':
    test_cases = {
        'T1': {
            'input': {
                'capacity': 165,
                'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
                'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
            },
            'output': 309,
        },
        'T2': {
            'input': {
                'capacity': 3,
                'weights': [4, 5, 6],
                'profits': [1, 2, 3],
            },
            'output': 0,
        },
        'T3': {
            'input': {
                'capacity': 4,
                'weights': [4, 5, 1],
                'profits': [1, 2, 3],
            },
            'output': 3,
        },
        'T4': {
            'input': {
                'capacity': 170,
                'weights': [41, 50, 49, 59, 55, 57, 60],
                'profits': [442, 525, 511, 593, 546, 564, 617],
            },
            'output': 1735,
        },
        'T5': {
            'input': {
                'capacity': 15,
                'weights': [4, 5, 6],
                'profits': [1, 2, 3],
            },
            'output': 6,
        },
        'T6': {
            'input': {
                'capacity': 15,
                'weights': [4, 5, 1, 3, 2, 5],
                'profits': [2, 3, 1, 5, 4, 7],
            },
            'output': 19,
        },
    }

    start = datetime.now()
    for test_case, item in test_cases.items():
        result = KnapSackProblemRecursion(**item['input'])
        assert result == item['output']
    end = datetime.now()
    print('Recursion Time: ', end - start)

    start = datetime.now()
    for test_case, item in test_cases.items():
        result = KnapSackProblemMemoize(**item['input'])
        assert result == item['output']
    end = datetime.now()
    print('Memoize Time: ', end - start)

    start = datetime.now()
    for test_case, item in test_cases.items():
        result = KnapSackProblemDP(**item['input'])
        assert result == item['output']
    end = datetime.now()
    print('Dynamic Programing Time: ', end - start)
