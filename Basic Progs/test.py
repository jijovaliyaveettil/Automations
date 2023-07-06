# nums = [1,1,1,2,2,3]

# print(len(nums))


# def solution():
#     k =1
#     q=2
#     return [k,q]

# print(solution())

# def add(x):
#     print(x+2)
#     return x+2

# added = add(8)
# print(added)


# a = [[]] * 5
# a[1].append(1)

# print(a)


# tuple = (1,2,3,4,1,2)
# b = set(tuple)
# c = list(b)
# print(list)
# print(tuple)
# print(c)

arr = [2, 3, 2, 3, 5]
N=5
hashmap = {}
for i in range(N):
    if(arr[i] in hashmap ):
        count = count + 1
        hashmap[i] = count
    else:
        count = 1
        hashmap[i] = count
        
for i in range(N):
    print(hashmap[arr[i]])