Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def foo(x: int, y: int) -> List[str]:
            """Generate strings with x '(' and y ')'

            :param x: Number of '('
            :param y: Number of ')'
            """
            # If no '(' remaining, return a list with y ')' concatenated
            if x == 0:
                return [')' * y]

            # If there are more '(' than ')' remaining, generate strings starting with ')'
            ret = [')' + t for t in foo(x, y - 1)] if x < y else []

            # Always generate strings starting with '('
            return ret + ['(' + t for t in foo(x - 1, y)]

        return foo(n, n)
