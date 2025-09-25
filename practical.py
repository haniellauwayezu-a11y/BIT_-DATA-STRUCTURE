# Stack operations
stack = []

# Push operations
stack.append("PIN")
stack.append("Amount")
stack.append("Confirm")

# Undo = Pop
stack.pop()

# Result
print("Current Stack:", stack)
# Stack operations
stack = []

# Push
stack.append("Quiz1")
stack.append("Quiz2")
stack.append("Quiz3")

# Pop two
stack.pop()
stack.pop()

# Check top
top = stack[-1] if stack else None
print("Top of Stack:", top)

from collections import deque

# Citizens queue (example IDs for clarity)
queue = deque(["Citizen1", "Citizen2", "Citizen3", "Citizen4", "Citizen5", "Citizen6", "Citizen7", "Citizen8"])

# Serve 2
queue.popleft()
queue.popleft()

# Who is next
next_client = queue[0]
print("Next to be served:", next_client)

from collections import deque

# Queue of 10 clients
queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7", "Client8", "Client9", "Client10"])

# Second client
second_client = queue[1]
print("Second client in queue:", second_client)
