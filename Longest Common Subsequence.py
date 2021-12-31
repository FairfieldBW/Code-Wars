"""
Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

Subsequence
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.
"""

def lcs(x, y):
    longest = ""
    for p in range(len(y)):
        newY = y[:p+1]
        if y[:p+1] in x and y[:p+1] > longest:
            longest = y[:p+1]
        for l in newY:
            if newY[l:] in x and newY[l:] > longest:
                longest = newY[l:]

    return longest

print(lcs("324234acf12124", "acf"))