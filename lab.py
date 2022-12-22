def fun1(x):
    
	x += 3
    
	return x 

def fun2(fun, x):
    
	y = x - 1
    
	return fun(y)

print(fun1)

print(fun2(fun1, 5))
