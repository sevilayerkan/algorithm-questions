# Link : https://leetcode.com/problems/apply-transform-over-each-element-in-array/
# Time complexity: O(n)
# Week: 1

def map(arr, fn):
    result = []
    for i in range(len(arr)):
        result.append(fn(arr[i]))
    return result

# Test Example 1


def plusone(n):
    # Change following line to apply any transformation over each element in the array
    return n + 1


arr = [1, 2, 3]
newArray = map(arr, plusone)
print(newArray)  # Output: [2, 3, 4]
