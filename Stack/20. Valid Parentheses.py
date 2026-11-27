"""
Problem: 20. Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Topic: String, Stack, Bracket Sequences
Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Problem Link:
https://leetcode.com/problems/valid-parentheses/
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_char = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        new_s = ""
        for cha in s:
            if cha.isalnum():
                print()
            else:
                new_s += cha

        left_l = []

        for i in new_s:
            if i in left_char:
                if not left_l:
                    return False

                if left_char[i] == left_l[-1]:
                    left_l.pop()
                else:
                    return False
            else:
                left_l.append(i)

        return len(left_l) == 0