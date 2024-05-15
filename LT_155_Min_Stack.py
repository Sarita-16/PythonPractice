class MinStack:

    def __init__(self):
        self.stack = []       # Initialize a stack to store values
        self.minStack = []    # Initialize a stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)  # Append the value to the main stack
        if self.minStack:       # If minStack is not empty
            val = min(self.minStack[-1], val)  # Update val to be the minimum of the current val and the top of minStack
        self.minStack.append(val)  # Append the minimum value to the minStack

    def pop(self) -> None:
        self.stack.pop()      # Remove the top element from the main stack
        self.minStack.pop()   # Remove the corresponding minimum value from the minStack

    def top(self) -> int:
        return self.stack[-1]  # Return the top element of the main stack

    def getMin(self) -> int:
        return self.minStack[-1]  # Return the top element of the minStack


# Example usage:

# Create a MinStack object
obj = MinStack()

# Push elements into the stack
obj.push(5)
obj.push(2)
obj.push(7)
obj.push(1)

# Current stack: [5, 2, 7, 1]
# Current minStack: [5, 2, 2, 1]

# Get the top element of the stack
top_element = obj.top()  # Returns 1
print("Top element:", top_element)

# Get the minimum element in the stack
min_element = obj.getMin()  # Returns 1
print("Minimum element:", min_element)

# Pop an element from the stack
obj.pop()

# Current stack: [5, 2, 7]
# Current minStack: [5, 2, 2]

# Get the top element of the stack after popping
top_element = obj.top()  # Returns 7
print("Top element after popping:", top_element)

# Get the minimum element in the stack after popping
min_element = obj.getMin()  # Returns 2
print("Minimum element after popping:", min_element)
