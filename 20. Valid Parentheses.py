20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        # Check if the number of opening and closing brackets for each type is equal
        if not (s.count("(") == s.count(")") and s.count("{") == s.count("}") and s.count("[") == s.count("]")):
            return False
        
        # Initialize an empty stack to keep track of opening brackets
        stack_brackets = []
        
        # Define a mapping of closing brackets to their corresponding opening brackets
        open_close = {"}": "{", "]": "[", ")": "("} 
        
        # Iterate through each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in ")}]":
                # Check if the stack is empty (no matching opening bracket)
                if not stack_brackets:
                    return False
                # Check if the last opening bracket on the stack matches the current closing bracket
                if stack_brackets.pop() != open_close[char]:
                    return False
            # If the character is an opening bracket, push it onto the stack
            elif char in "({[":
                stack_brackets.append(char)
        
        # If the stack is empty, all brackets are properly matched
        return not stack_brackets
