Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
      dictionary = defaultdict(set)
      for i in range(len(points)):
        for j in range(i+1, len(points)):
          x1, y1 = points[i][0], points[i][1]
          x2, y2 = points[j][0], points[j][1]
          if x1 == x2:
            k = float("inf")
            b = x1
          else:
            k = (y2-y1) / (x2 - x1)
            b = y1 - k*x1
          dictionary[(k, b)].add(i)
          dictionary[(k, b)].add(j)
      max_size = 1
      for key, value in dictionary.items():
        max_size = max(max_size, len(value))
      return max_size


        
