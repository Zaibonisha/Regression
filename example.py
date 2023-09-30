def recursive_function(n):
    if n == 0:
       return 42
    else:
        return 42 + 43**271 + recursive_function(n-1)

result_n0 = recursive_function(0)   
result_n1 = recursive_function(1)   
result_n2 = recursive_function(2)    

print ("Result when n=0:", result_n0)
print ("Result when n=1:", result_n1)
print ("Result when n=2:", result_n2)
       

