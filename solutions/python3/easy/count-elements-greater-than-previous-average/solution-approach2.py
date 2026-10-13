# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average/problem?isFullScreen=true
# Problem     Count Elements Greater Than Previous Average
# Difficulty  Easy
# Subdomain   Software Engineer Prep Kit
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-14, 02:05 a.m.
# Technique   running-sum-average-tracking
# Time        O(n)
# Space       O(1)
# Insight     The algorithm maintains a running sum of all elements encountered so far to calculate the average of previous elements in constant time for each subsequent index.
# Pitfalls    (1) Failing to handle the n=0 case where the loop range is empty, resulting in an incorrect return value of 0.  (2) Using integer division instead of floating-point division when calculating the average, which would lead to incorrect comparisons for non-integer averages.
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
    current_sum=0
    for i,current_time in enumerate(responseTimes):
        if i>0:
            previous_average=current_sum/i
            if current_time>previous_average:
                count+=1
        current_sum+=current_time
    return count
        

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
