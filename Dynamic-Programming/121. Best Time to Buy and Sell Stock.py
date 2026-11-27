"""
Problem: 121. Best Time to Buy and Sell Stock
Platform: LeetCode
Difficulty: Easy
Topic: 
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Problem Link:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        profit = 0
        for i in prices[1:]:
            max_price=i
            if min_price>i:
                min_price = i
            if  min_price<max_price:
                profit = max(profit, max_price - min_price)
            
        return profit