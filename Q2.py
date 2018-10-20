def convert(num):        #creat function with one variable for the list we went to convert its numbers
    word=" "          #empty varible that will take the name of number
    result = []       #none list thah will have the final result and it will print in the end
    for i in num:     #we make a loop in the list that we entered and went to convert
        if i == 1:            #we use if condition To distinguish all the numbers
            word = "One"
        if i == 2:
            word = "Two"
        if i == 3:
            word = "Three"
        if i == 4:
            word = "Four"
        if i == 5:
            word = "Five"
        if i == 6:
            word = "Six"
        if i == 7:
            word = "Seven"
        if i == 8:
            word = "Eight"
        if i == 9:
            word = "Nine"

        result.append(word)     #we append the word of numbers to the none list
    print(result)     #print the list that have the words written


convert([1,2,3,4,5,6])     #run the function