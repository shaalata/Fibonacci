def fibonacci(x):
    """calculating the value of any number in fibonacci sequences
    user call the function with position of x to get the its value
    assumption the sequence start in the same order like that
     [1,1,2,3,5,8,....] 0 in not considered in that function"""

    if type(x) != int or x<0:    #check the value of x is an integer number
        print("please enter positive integer number")
        raise TypeError("x must be a positive int")

    if x == 0:
        print("The value of  "+ str(x) + " in the Fibonacci sequence is  "+str(0))

    if x == 1 or x==2:
        print("The value of  "+ str(x) + " in the Fibonacci sequence is  "+str(1))

    if x >2:
        fib = [1, 1]
        while x != len(fib):
            fib.append(fib[-1]+fib[-2])
        print(fib)
        print("The value of  "+ str(x) + " in the Fibonacci sequence is  "+str(fib[-1]))


    
fibonacci(100)