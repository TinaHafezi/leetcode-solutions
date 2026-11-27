"""
Problem: 1. Two Sum
Platform: LeetCode
Difficulty: Easy
Topic: Array, Hash Table
Description: You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Problem Link:
https://leetcode.com/problems/two-sum/
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[i]+nums[j]==target:
        #                 return [i,j]
        checked = {}
        for i in range(len(nums)):
            needed = target-nums[i]
            if needed in checked:
                return [ checked[needed],i]
            else:
                checked[nums[i]]=i