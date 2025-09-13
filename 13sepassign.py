
def max_min_sum(list1):
    max_element=list1[0]
    min_element=list1[0]
    sum=0
    for i in list1:
        sum+=i
        if i>max_element:
            max_element=i
        if i<min_element:
            min_element=i
    return f" min element:{min_element},max element:{max_element},sum:{sum}"
list1=[1,3,5,-9,13,50,79,32]
print(max_min_sum(list1))
# max_element = 0 → fails if all elements are negative, because the maximum will incorrectly remain 0.
# min_element = 0 → fails if all elements are positive, because the minimum will incorrectly remain 0.

    
