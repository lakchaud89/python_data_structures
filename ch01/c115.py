# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def distinct_pairs(data):

    y = len(data)
    dup_status = False

    for i in range(0,y-1):
        for j in range(i+1,y):
            if ((data[i] == data[j])):
                dup_status = True
                return "list contains duplicates"

    return "list does not contain duplicates"


data1=[1,2,3,5]
data2 = [1,3,5,6,7]
data3 = [5,3,1,7,9,10]
data4=[5,5,1,2,5,6]
data5= [7,5,7,8,9,7,9,3]
str1 = distinct_pairs(data1)
str2 = distinct_pairs(data2)
str3 = distinct_pairs(data3)
str4 = distinct_pairs(data4)
str5 = distinct_pairs(data5)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
