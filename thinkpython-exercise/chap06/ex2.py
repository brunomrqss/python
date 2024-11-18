def is_between(x, y, z):
    if y > x and y < z: 
        return True 
    elif y > z and y < x:
        return False
    
result = is_between(5, 4, 3)
print(result)
result = is_between(1, 2, 3)
print(result)