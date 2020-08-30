## Iterate through List with While
nolist = [1, 2, 4, 5, 6, 7, 9, 10, 13, 14, 15, 16]
i = 0
listlength = len(nolist)
while i < listlength:
    if nolist[i] % 2 == 0:
        print("Printing the value " + str(nolist[i]))
    i += 1 

## Function Operation
def my_function(stringone, stringtwo, integer):
## =============
## This function was written by Riley Curtis
    lengthstrone = len(stringone)
    lengthstrtwo = len(stringtwo)
    if lengthstrone == lengthstrtwo:
        print("Equal lengths")
    else:
        print("Unequal lengths")

    newno = integer + lengthstrone
    print(newno)

stringone = "words"
stringtwo = "stuff"
integer = 5

my_function(stringone, stringtwo, integer)

## Lambda Operation
testlambda = lambda a, b, c : len(a) + len(b) - c

testlambda(stringone, stringtwo, integer)