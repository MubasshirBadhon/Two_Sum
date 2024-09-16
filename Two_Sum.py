class Solution:
    def twoSum(self, nums, target):
        # Create a hash map to store the difference and it's index
        hash_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference is already in the hash map
            if diff in hash_map:
                # If found, return the indices
                return [hash_map[diff], i]
            
            # Otherwise, add the number and its index to the hash map
            hash_map[num] = i

# Example usage:
solution = Solution()
nums1 = [2, 7, 11, 15]
target1 = 9
nums2 = [3, 2, 4]
target2 = 6
nums3 = [3, 3]
target3 = 6

print(solution.twoSum(nums1, target1))  # Output: [0, 1]
print(solution.twoSum(nums2, target2))  # Output: [1, 2]
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
