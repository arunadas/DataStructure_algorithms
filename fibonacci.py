# def bad_fibonacci(n):
#     """Return the nth Fibonacci number."""
#     if n <= 1:
#         return n
#     else:
#         return bad_fibonacci(n-2) + bad_fibonacci(n-1)



# def good_fibonacci(n):
#     """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
#     if n <= 1:
#         return (n,0)
#     else:
#         (a, b) = good_fibonacci(n-1)
#         print('a,b,n,a+b',a,b,n-1,a+b)
#         return (a+b, a)

#print(bad_fibonacci(10))
#print(good_fibonacci(5))

# def linear_sum(seq,n):
#     if n==0:
#         print(n)
#         return 0
#     else:
#         print('n,seq[n-1]',n , seq[n-1])
#         return linear_sum(seq,n-1) + seq[n-1]

# seq=[1,2,3,4,5,6,7,8,9,10]    
# print(linear_sum(seq,10)) 


# def power2(x,n):
#     if n== 0:
#         return 1
#     else:
#         partial = power2(x,n//2)
#         result = partial * partial
#         if n%2==1:
#             result *= x
#         return result
# print(power2(2,13))


# def max_min(seq,n):
#     if n == 1:
#         return seq[0] ,seq[0]
#     else:
#         min_c,max_c = max_min(seq,n-1)
#         return min(min_c ,seq[n-1]) , max(max_c ,seq[n-1])

# seq = [3,16,2,59,1,2,6]  
# print(max_min(seq, len(seq)))


# def unique3(S, start, stop,step=1):
#     #temp = sorted(S)
#     print(f'Step = 0, Stop = {stop} and Start = {start}')
#     if stop - start <= 1:
#         print(f'Step = {step}, Stop = {stop} and Start = {start}')
#         return True
#     elif not unique3(S, start, stop-1,2):
#         return False
#     elif not unique3(S, start+1, stop,3):
#         return False
#     else: 
#         print(f'Step = 4, Stop = {stop}, Start = {start}')
#         return S[start] != S[stop-1]
    
# # S =  [ 1, 7, 1,2]
# # print(unique3(S,0,len(S)))

# S =  [ 6, 7, 5]
# print(unique3(S,0,len(S)))


# UNK = chr(1000)



# def sub_rec(U, S):
#     """
#     U is the current set
#     S is the remaining sequence
#     """
#     if len(S) == 0:
#         print('{', str([x for x in U if x!= UNK])[1:-1], '}')
        
#     else:
#         val = S.pop()
#         U.append(UNK)
#         sub_rec(U, S)
#         U.pop()
        
#         U.append(val)
#         sub_rec(U, S)
#         U.pop()
#         S.append(val)

# def print_subsets (U):
#     sub_rec([], list(U))
    
    
# print_subsets({1,2})

# def reversestring(S,index=0):
#     if index == len(S)-1:
#         return [S[index]]
#     else:
#         ans = reversestring(S,index + 1)
#         ans.append (S[index])
#         if index == 0:
#             ans = ''.join(ans)
#         return ans

    
    
# reversestring('pots')  


# def palindrome(S,index=0):
#     orig = list(S)
#     if index == len(S)-1:
#         return [S[index]]
#     else:
#         ans = palindrome(S,index+1)
#         ans.append(S[index])
#         if orig == ans:
#             return True
#         return ans 

# palindrome('racecar')    
# 
#      

# VOWELLS = {'a','e','i','o','u'}

# # sol 1 having single counter , sol2 counting both vowel and constant  

# def c_or_v(S, index = 0):
#     a = -1 if S[index] in VOWELLS else 1
#     if index == len(S)-1:
#         return a
#     else:
#         return (a+ c_or_v(S, index +1))
    
# def check_vowells(S):
#     ans = c_or_v(S)
#     if ans>0:
#         return (f'There are more consonants by {ans}')
#     elif ans<0:
#         return (f'There are more vowells by {ans}')
#     else:
#         return (f'There are an equal number of each {ans}')
    
    

     
    
# check_vowells('aeiost')

# def even_odd(S, index=0):
#     if index == len(S)-1:       
#         if len(S) == 1:
#             return S
#         elif S[index]%2 == 0:
#             return [S[index]],[]
#         else:
#             return [],[S[index]]
#     else:
#         even,odd = even_odd(S,index+1)
#         if S[index]%2 == 0:
#             even.append(S[index])
#         else:
#             odd.append(S[index])
#         if index == 0:
#             return even+odd
#         else:
#             return even,odd

# print(even_odd([1,2,3,4]))


# VOWELLS = {'a','e','i','o','u'}
# def c_or_v2(S,index=0):
#     v_c,c_c = 0,0
#     if index == len(S)-1:
#         return v_c,c_c
#     if S[index] in VOWELLS:
#         v_c += 1
#         return v_c,c_c
#     else:
#         c_c += 1
#         return v_c,c_c    
#     return (  c_or_v2(S, index+1)) 

# def check_vowells(S):
#     v_c, c_c = c_or_v2(S)
#     if v_c > c_c:
#         return (f'There are more vowells by {v_c}')
#     elif v_c==c_c:
#         return (f'There are an equal number of each {c_c}')
#     else:
#         return (f'There are more consonents by {c_c}')
    
# check_vowells('aeiost') 

def find_pair(S, target, key_set = None, index=0):
    if key_set is None:
        key_set = set()
    
    
    key = target - S[index]
    if len(S) <= 1:
        return None
    
    elif index == len(S)-1:
        if key in key_set: return (key, S[index])
        else: return None
        
    else:
        if key in key_set: return (key, S[index])
        else:
            key_set.add(S[index])
            return find_pair(S, target, key_set, index+1)
    
S=[1,2,3,4]
k=4
print(find_pair(S,k))