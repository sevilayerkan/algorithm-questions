# Link: https://leetcode.com/problems/two-sum/
# Time complexity: O(n^2)
# Week: 1
# Explanation: In this approach, we will use two for loops. The outer for loop will iterate through the array and the inner for loop will start from i+1 index and iterate through the array. If the sum of the elements at i and j index is equal to the target, we will append the indices to the result list and return the result list.


def twoSum(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)

    return result


"""
#2nd approach : Hashmap
#Explanation: https://www.youtube.com/watch?v=luicuNOBTAI&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&feature=emb_imp_woyt
#Time complexity: O(n) (apporximately)
#Further explanation: In this approach we will use a hashmap to store the elements of the array as key and their indices as values. We will iterate through the array and check if the difference of the target and the element at i index is present in the hashmap. If it is present, we will return the indices of the element at i index and the element at the difference index. If it is not present, we will add the element at i index as key and its index as value in the hashmap.

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
"""

list = [3,2,4]
target = 6
print(twoSum(list, target))