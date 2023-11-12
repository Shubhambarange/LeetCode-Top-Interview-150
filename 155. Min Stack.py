
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2class MinStack:

    def __init__(self):
        # Initialize the main stack and the auxiliary stack to keep track of the minimum element at each level.
        self.stack = []      # Main stack to store elements
        self.minStack = []   # Auxiliary stack to keep track of the minimum element

    def push(self, val: int) -> None:
        # Push the value onto the main stack.
        self.stack.append(val)

        # If the auxiliary stack is not empty, update the minimum value by comparing the current value with the previous minimum.
        if self.minStack:
            val = min(self.minStack[-1], val)

        # Push the updated minimum value onto the auxiliary stack.
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop the top element from both the main stack and the auxiliary stack.
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack.
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the auxiliary stack, which represents the minimum element in the main stack.
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
