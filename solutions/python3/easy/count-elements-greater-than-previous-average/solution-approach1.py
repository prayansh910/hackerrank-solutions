# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 01:51 a.m.
# Technique   running-sum-average-comparison
# Time        O(n)
# Space       O(1)
# Insight     The algorithm maintains a running sum to calculate the average of all elements up to the current index, comparing each element against its preceding average to determine if it exceeds that value.
# Interview   Before: "I would calculate the average for every prefix by iterating through the array repeatedly." After: "I optimized this to O(n) time by maintaining a running sum, which allows constant-time average calculation at each step, correctly handling the empty array case where n=0 results in zero counts."
# Pitfalls    (1) The problem requires skipping the first element, but the provided code incorrectly includes the first element in the comparison logic.  (2) Using integer division (//) instead of floating-point division may lead to incorrect comparisons if the average is not an integer.
# ──────────────────────────────────────────────────

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    count=0
    avgsum=0
    for i in range(len(responseTimes)):
        avgsum+=responseTimes[i]
        current_average=avgsum//(i+1)
        if responseTimes[i]>current_average:
            count+=1
    return count
        

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
