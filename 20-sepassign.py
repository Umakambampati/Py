def check_duplicates(list1):
    l2=[]
    for i in list1:
        has_duplicate=False
        seen=set()
        while i>0:
            rem=i%10
            if rem in seen:
                has_duplicate=True
                break
            seen.add(rem)
            i=i//10
        l2.append(has_duplicate)
    return l2
list1=[202,89,112,88,676]
print(check_duplicates(list1))


def matrix(matrix1):
    total_sum=0
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            total_sum+=matrix1[i][j]
    return total_sum
matrix1=[
    [1,2,3],
         [2,3,4]
         ]
print(matrix(matrix1))
