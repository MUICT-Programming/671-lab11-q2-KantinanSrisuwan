def summation(l1,l2):
    updated_list = []
    for i in range(n):
        updated_list.append(l1[i] + l2[i])
    return updated_list

def find_min_max(updated_list):
    min1 = min(updated_list)
    max1 = max(updated_list)
    return min1,max1

n = int(input())

lst1=[int(input()) for i in range(n)]
lst2=[int(input()) for i in range(n)]

print(summation(lst1,lst2))
print(find_min_max(summation(lst1,lst2)))
