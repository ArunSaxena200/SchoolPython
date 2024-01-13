def asteroid_collision(asteroids):
    stack = []

    if not asteroids:
        return[]
    stack = []
    stack.append(asteroids[0])

    for a in range(1,len(asteroids)): 
        while stack and stack[-1] > 0 and asteroids[a] < 0 and abs(asteroids[a])>stack[-1]: #check to pop off explode smaller one
            stack.pop()
    # cond to check append or explode this will add elemeents to stack
        if not stack:
            stack.append(asteroids[a])
            
        elif stack[-1] > 0 and asteroids[a] < 0 and  stack[-1] == abs(asteroids[a]): #explode both same size
            stack.pop()
        elif stack[-1] < 0 or asteroids[a] > 0 or abs(stack[-1]) < abs(asteroids[a]): ##check if the value is negative, value[1] is positive as they will move opposite and the size of right moving is bigger they wont collide
          
            stack.append(asteroids[a])
    return stack




# Example usage:
asteroids = [10,2,-5]
result = asteroid_collision(asteroids)
print(result)
