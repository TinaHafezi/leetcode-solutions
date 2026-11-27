"""
Problem: 217. Contains Duplicate
Platform: LeetCode
Difficulty: Easy
Topic: Array, Hash Table, Sorting
Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Problem Link:
https://leetcode.com/problems/contains-duplicate/
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False
        return len(nums) != len(set(nums))
        