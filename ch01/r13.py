#R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#one or more numbers, and returns the smallest and largest numbers, in the
#form of a tuple of length two. Do not use the built-in functions min or
#max in implementing your solution.

def minmax(data):
    min = data[0]
    max = data[0]
    l = len(data)
    for i in range(l):
        if(data[i] > max):
            max = data[i]
            print 'max', max
        elif (data[i] < min):
            min = data[i]
            print 'min', min
    return min,max


eg_list1 = [4,5,6,2,1,0]
print(minmax(eg_list1))
eg_list2 = [0,1,2,100,28]
print(minmax(eg_list2))
eg_list3 = [-99,90,2,7,99]
print(minmax(eg_list3))
