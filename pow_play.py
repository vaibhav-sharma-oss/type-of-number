
print("enter a number :- ")
num=eval(input())
for i in range(1,101):
   if num%2 == 0 and pow(2,i) == num:
       print(num,"is not a prime number")  
       print(num,"is even number")
       print(num," is ",i," time multipule of 2" )
       break    
            

   if num%2 != 0 and pow(2,i) != num:
        print(num," is prime number")  
        print(num," is odd")
        break
           
    