"""
Problem: 242. Valid Anagram
Platform: LeetCode
Difficulty: Easy
Topic: Hash Table, String, Sorting
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Problem Link:
https://leetcode.com/problems/valid-anagram/
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return (sorted(s)==sorted(t))
        frequency_s = {}
        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1
        frequency_t = {}
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1
        return frequency_t==frequency_s