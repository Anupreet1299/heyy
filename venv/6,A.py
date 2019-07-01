#functions
#f(x) = x*x
#methods/ procedures/ routines

"""
functions
1. name
2. inputs (may or may nt) parameters | arguments
3. return  (may or may nt) |acknowledgement
4. defination (may or may nt) --> sequence

why functions ?
group of statements / logics which has to be executed again and again


modularization

"""
#defination of addNumber function
#num1 and num2 are inputs
def addNumbers(num1, num2):
    num3 = num1 + num2
    #print("sum of {} and {} is {}".format(num1, num2, num3))
    return num3
result = addNumbers(10, 20)  #execution of function
print("sum is ", result)
print(addNumbers(10, 20))
print("sum is ", addNumbers(10, 20))
del addNumbers
#addNumbers(20, 39)

#create a function which applies promocode on the basis of these conditions
1. flat 50