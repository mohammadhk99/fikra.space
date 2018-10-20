def compain2list(L1,L2):       #creat function with two variables the first for the first list and the second for the second list
    result=[]      #make a none list to append the result in it
    n=len(L1)    #here we take the lenght for the first list
    for i in range(n):   #loop equal the number of items found in the list
        result.append(L1[i])   #append the item of list 1 that has the index of i in result (i=0 , i=1 , .....)
        result.append(L2[i])   #append the item of list 2 that has the index of i in result (i=0 , i=1 , .....)

    print(result)  #print result
print(compain2list([1,2,3],["a","b","c"]))   #now we run the function and give it an example