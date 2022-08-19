"""Problem:
Find the longest sub sequence between 2 sequences.
Example:
    sequence1 = 'serendipitous'
    sequence2 = 'precipitation'
    output = 'reipito', length: 7

`subsequence` is a sequence obtained by deleting 0 or more elements from
another sequence. Example: `edpt` is a subsequence of 'serendipitous'
"""


def LongestCommonSubSequence(sequence1, sequence2, idx1=0, idx2=0):
    # Complexity: O(2 ^ m + n)
    if idx1 == len(sequence1) or idx2 == len(sequence2):
        return 0
    elif sequence1[idx1] == sequence2[idx2]:
        length = LongestCommonSubSequence(
            sequence1, sequence2, idx1=idx1 + 1, idx2=idx2 + 1)
        return length + 1
    else:
        option1 = LongestCommonSubSequence(
            sequence1, sequence2, idx1=idx1 + 1, idx2=idx2)
        option2 = LongestCommonSubSequence(
            sequence1, sequence2, idx1=idx1, idx2=idx2 + 1)
        return max(option1, option2)


def LongestCommonSubSequenceMemo(sequence1, sequence2):
    # Complexity: O(m * n)
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(sequence1) or idx2 == len(sequence2):
            memo[key] = 0
        elif sequence1[idx1] == sequence2[idx2]:
            memo[key] = 1 + recurse(idx1=idx1 + 1, idx2=idx2 + 1)
        else:
            memo[key] = max(recurse(idx1=idx1 + 1, idx2=idx2),
                            recurse(idx1=idx1, idx2=idx2 + 1))

        return memo[key]

    return recurse(0, 0)


def LongestCommonSubSequenceDP(sequence1, sequence2):
    # Complexity: O(m * n)
    n1, n2 = len(sequence1), len(sequence2)
    matrix = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if sequence1[idx1] == sequence2[idx2]:
                matrix[idx1 + 1][idx2 + 1] = 1 + matrix[idx1][idx2]
            else:
                matrix[idx1 + 1][idx2 + 1] = max(
                    matrix[idx1][idx2 + 1], matrix[idx1 + 1][idx2])
    return matrix[-1][-1]


if __name__ == '__main__':

    test_cases = {
        'T1': {
            'args': {
                'sequence1': 'serendipitous',
                'sequence2': 'precipitation',
            },
            'output': 'reipito',
            'length': 7,
        },
        'T2': {
            'args': {
                'sequence1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
                'sequence2': [6, 2, 4, 7, 1, 5, 6, 2, 3],
            },
            'output': '',
            'length': 5,
        },
        'T3': {
            'args': {
                'sequence1': 'longest',
                'sequence2': 'stone',
            },
            'output_str': '',
            'length': 3,
        },
        'T4': {
            'args': {
                'sequence1': 'asdfwevad',
                'sequence2': 'opkpoiklklj',
            },
            'output_str': '',
            'length': 0,
        },
        'T5': {
            'args': {
                'sequence1': 'dense',
                'sequence2': 'condensed',
            },
            'output_str': '',
            'length': 5,
        },
        'T6': {
            'args': {
                'sequence1': '',
                'sequence2': 'opkpoiklklj',
            },
            'output_str': '',
            'length': 0,
        },
        'T7': {
            'args': {
                'sequence1': '',
                'sequence2': '',
            },
            'output_str': '',
            'length': 0,
        },
        'T8': {
            'args': {
                'sequence1': 'abcdef',
                'sequence2': 'badcfe',
            },
            'output_str': '',
            'length': 3,
        },
    }
    for t_case, item in test_cases.items():
        recursion_result = LongestCommonSubSequence(**item['args'])
        memo_result = LongestCommonSubSequenceMemo(**item['args'])
        dp_result = LongestCommonSubSequenceDP(**item['args'])
        assert item['length'] == recursion_result
        assert item['length'] == memo_result
        assert item['length'] == dp_result
