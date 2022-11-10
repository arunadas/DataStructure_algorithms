#Lambda is anonymous function
import functools

nums = lambda x,y:2*x
#print(nums(2))


n2 = lambda x,y:x+y
#print(n2(9,1))

#print(list(map(nums,[1,2,6,7])))
print(functools.reduce(nums,[1,2,8,5]))
lis = [1, 3, 5, 6, 2]
print(functools.reduce(lambda a, b: a if a > b else b, lis))