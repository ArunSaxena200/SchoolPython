'''
AlgoLIFO to FIFO
1. take 2 stacks s1, s2 
2. apply enqueue s1 = 1,2,3,4 (top) enqueue
3. apply dequeue if s2 is empty s2 = 4,3,2,1(top) (dequeue)
4. pop elements from s2, res = 1,2,3,4
'''
def enqueue(stack,item):
    stack.append(item)
def dequeue(stack1,stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        return None
    return stack2.pop()
def look(stack1,stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    if not stack2:
        return None
    return stack2[-1]
s1 = []
s2 = []
enqueue(s1,4)
enqueue(s1,5)
enqueue(s1,6)
print(f"top element {look(s1,s2)}")
print(f"deque element {dequeue(s1,s2)}") 
print(f"deque element {dequeue(s1,s2)}") 
print(f"deque element {dequeue(s1,s2)}")  
print(f"deque element {dequeue(s1,s2)}")  # shud return None
enqueue(s1,7)
print(f"top element {look(s1,s2)}")