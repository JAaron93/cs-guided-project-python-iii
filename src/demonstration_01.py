"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
# def two_sum(nums, target):
#     # Your code here
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#         # Could have i or j in there == target, doesn't matter
#             if nums[j] == target - nums[i]:
#                 return [i, j]

#     return []

# print(two_sum(nums = [2,5,9,13], target = 7))
# print(two_sum(nums = [4,3,5], target = 8))


def two_sum(nums, target):   # O(n)
  # create an empty dictionary 'd'
  d = {}  # O(1)

  # iterate over nums using 'i' as the index.
  for i in range(len(nums)):  # O(n)
    # set 'd' at key of 'nums' at the index of 'i' to 'i'
    d[nums[i]] = i  # O(1)

    # iterate over nums using 'i' as the index.
    for i in range(len(nums) - 1):   # O(n)
      # set a var 'c' to equal 'target' minus 'nums' at index of 'i'
      c = target - nums[i]
      # check if 'v' is in 'd' and if the 'd' at the key of 'c' is not equal to 'i'
      if c in d and d[c] != i:
        # return a sorted list ['i', 'd' at key of 'c']
        return sorted([i, d[c]])

    # return an empty list
  return []  # O(1)

print(two_sum(nums = [4, 3, 5], target = 8))


# def two_sum(nums, target):   # O(n)
#     # create an empty dictionary 'd'
#     d = {}  # O(1)

#      # iterate over nums using 'i' as the index.
#     for i in range(len(nums)):   # O(n)
#           # set a var 'c' to equal 'target' minus 'nums' at index of 'i'
#             c = target - nums[i]
#             # check if 'v' is in 'd' and if the 'd' at the key of 'c' is not equal to 'i'
#             if c in d and d[c] != i:
#                 # return a list ['i', 'd' at key of 'c']
#                 return [i, d[c]]
#             # here we do the build of dictionary inline with a single for loop
#             d[nums[i]] = i

#     # return an empty list
#     return []  # O(1)


# print(two_sum(nums=[4, 3, 5], target= 8))
