def addition_nxn(data):
    sum = 0
    for i in range(len(data)):
        for j in range(len(data)):
            sum += data[i][j]
    return sum


list_of_lists = [list(range(i, i+10)) for i in range(1,50, 10)]
print(list_of_lists)
#print(addition_nxn(list_of_lists)) 
# 
# 
# [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# 

for i in range(len(list_of_lists)):
    for j in range(len(list_of_lists)):
        print(j)   