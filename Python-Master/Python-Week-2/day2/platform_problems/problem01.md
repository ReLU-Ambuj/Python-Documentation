# Problem 1: Maximum Average Subarray I

## Problem Statement
You are given an integer array `nums` consisting of `n` elements, and an integer `k`. Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.

## Solution Outline
- Approach: Fixed Window.
- Instead of computing average repeatedly, compute the max sum.
- Divide by K at the end.

## Complexity
- Time: O(N)
- Space: O(1)
