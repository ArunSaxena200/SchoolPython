def enqueue(stack1, item):
    stack1.append(item)

def dequeue(stack1, stack2):
    if not stack2:
        # If stack2 is empty, transfer elements from stack1
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        # If both stacks are empty, queue is empty
        return None
    return stack2.pop()

def peek(stack1, stack2):
    if not stack2:
        # If stack2 is empty, transfer elements from stack1
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        # If both stacks are empty, queue is empty
        return None
    return stack2[-1]

def is_empty(stack1, stack2):
    return not stack1 and not stack2

def size(stack1, stack2):
    return len(stack1) + len(stack2)

# Example usage:
stack1 = []
stack2 = []

enqueue(stack1, 1)
enqueue(stack1, 2)
enqueue(stack1, 3)

print("Size of queue:", size(stack1, stack2))
print("Front element:", peek(stack1, stack2))

print("Dequeue:", dequeue(stack1, stack2))
print("Dequeue:", dequeue(stack1, stack2))

enqueue(stack1, 4)
print("Size of queue:", size(stack1, stack2))

print("Dequeue:", dequeue(stack1, stack2))
print("Is queue empty?", is_empty(stack1, stack2))
