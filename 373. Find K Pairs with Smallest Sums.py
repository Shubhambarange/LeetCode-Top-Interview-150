You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

class Pair:
    def __init__(self, n1, n2):
        self.pair = [n1,n2]
        self.sum = n1 + n2
    
    def __lt__(self, other):
        # max heap
        return self.sum > other.sum

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k == 1:
            return [nums1[0], nums2[0]]

        ret = []

        for n1 in nums1:
            for n2 in nums2:
                if len(ret) < k:
                    heapq.heappush(ret, Pair(n1,n2))
                    continue
                
                if (n1 + n2) >= ret[0].sum:
                    break
                
                heapq.heappop(ret)
                heapq.heappush(ret, Pair(n1,n2))
                
        return [p.pair for p in ret]
        
