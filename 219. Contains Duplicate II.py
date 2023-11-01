Problem:

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary to store values and their corresponding indices
        hashmap = {}
        
        # Iterate through the elements of the 'nums' list
        for i in range(len(nums)):
            # If the current element is not in the dictionary
            if nums[i] not in hashmap:
                # Store the element and its index in the dictionary
                hashmap[nums[i]] = i
            else:
                # If the element is already in the dictionary
                pastIdx = hashmap[nums[i]]
                
                # Check if the absolute difference between the current index and the past index
                # is less than or equal to 'k'
                if abs(pastIdx - i) <= k:
                    # If the condition is met, return True (there is a nearby duplicate)
                    return True
                else:
                    # Otherwise, update the index of the element in the dictionary
                    hashmap[nums[i]] = i
        
        # If no nearby duplicates were found, return False
        return False
