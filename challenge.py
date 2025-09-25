input_string = "QUEUESTACK"
stack = []

# Step 1: Push each character onto stack
for char in input_string:
    stack.append(char)

# Step 2: Pop characters to reverse
reversed_string = ""
while stack:
    reversed_string += stack.pop()

print("Reversed:", reversed_string)

# Using a queue
from collections import deque

queue = deque(["Patient1", "Patient2", "Patient3"])
queue.append("Patient4")  # New patient arrives

# Serve patients
print("Serving from queue:", queue.popleft())  # Patient1 is served first
