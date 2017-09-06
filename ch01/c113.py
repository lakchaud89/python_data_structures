# C1.13 Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, and
# compare this method to an equivalent Python function for doing the same thing.

#custom function
def seq_reverse(data):
    l = len(data)
    for i in range(l/2):
        #tmp = data[i]
        #data[i] = data[l-i-1]
        #data[l-i-1] = tmp
        data[i],data[l-i-1] = data[l-i-1],data[i] #here no need of temp
    print("Reversed Sequence:",data)

data1 = [1,2,3,4,5]
seq_reverse(data1)
data2 = [5,4,6,7,8]
seq_reverse(data2)

# print("using slicing")
# print(x for x in data1[,,-1])
# print(x for x in data2[,,-1])

#OOTB function reverse

#print(data1.reverse()) #this reverses the original list
#print(data1)

print("using reversed method")
y = reversed(data1)
z= reversed(data2)
print(type(data1)) #list
print(type(data2)) #list
print(data1)
print(data2)
