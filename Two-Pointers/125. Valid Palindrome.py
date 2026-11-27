"""
Problem: 125. Valid Palindrome
Platform: LeetCode
Difficulty: Easy
Topic: Two Pointers, String
Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Problem Link:
https://leetcode.com/problems/valid-palindrome
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                p = p+char


        for char in range(len(p)/2):
            if (p[char] != p[len(p)-char-1]):
                return False
            
        return True