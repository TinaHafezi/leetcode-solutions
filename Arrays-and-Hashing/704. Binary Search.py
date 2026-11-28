"""
Problem: 704. Binary Search
Platform: LeetCode
Difficulty: Easy
Topic: 
Description:Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
 
Problem Link:
https://leetcode.com/problems/binary-search/
"""
class Solution(object):
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
    

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = self.binary_search(nums, target)

        return result
    