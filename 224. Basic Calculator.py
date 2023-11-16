Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

class Solution:
    def calculate(self, s):
        if not s:
            return 0        
        stack = []  # Stack for handling parentheses
        num = 0  # Variable to store the current number being formed
        sign = 1  # Variable to store the sign (+1 or -1)
        result = 0  # Variable to store the final result   
        for i in range(len(s)):
            if s[i].isdigit():  # If the character is a digit
                num = num * 10 + int(s[i])  # Form the number by combining digits
                
            elif s[i] == '+':  # If the character is a plus sign
                result += sign * num  # Add the current number to the result with the appropriate sign
                num = 0  # Reset num to 0 for the next number
                sign = 1  # Set the sign to positive
                
            elif s[i] == '-':  # If the character is a minus sign
                result += sign * num  # Add the current number to the result with the appropriate sign
                num = 0  # Reset num to 0 for the next number
                sign = -1  # Set the sign to negative
                
            elif s[i] == '(':  # If the character is an opening parenthesis
                stack.append(result)  # Push the current result to the stack
                stack.append(sign)  # Push the current sign to the stack
                result = 0  # Reset result to 0 for calculations inside the parentheses
                sign = 1  # Reset the sign inside the parentheses
                
            elif s[i] == ')':  # If the character is a closing parenthesis
                result += sign * num  # Add the current number to the result with the appropriate sign
                num = 0  # Reset num to 0 for the next number
                
                # Calculate the result inside the parentheses
                result *= stack.pop()  # Multiply with the sign from the stack
                result += stack.pop()  # Add the previous result from the stack
               # Ignore whitespace characters        
        result += sign * num  # Add the final number (if any) to the result with the appropriate sign
        return result  # Return the final evaluated result
