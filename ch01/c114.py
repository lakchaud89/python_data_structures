def odd_prod_pairs(data):
    list_tuples = []
    y = len(data)
    for i in range(0,y-1):
        for j in range(i+1,y):
            if ((data[i]*data[j] % 2) == 1):
                sorted_tuple = tuple(sorted( (data[i], data[j]) ))
                if sorted_tuple not in list_tuples:
                    list_tuples.append(sorted_tuple)
    print(list_tuples)


data1=[1,2,3,5]
data2 = [1,3,5,6,7]
data3 = [5,3,1,7,9,10]
data4=[5,5,1,2,5,6]
data5= [7,5,7,8,9,7,9,3]
odd_prod_pairs(data1)
odd_prod_pairs(data2)
odd_prod_pairs(data3)
odd_prod_pairs(data4)
odd_prod_pairs(data5)
