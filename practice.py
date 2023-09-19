x = 5
y = "John"
print(type(x))
print(type(y))


num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))


# create a set named student_id
student_id = {112, 114, 116, 118, 75}

# display student_id elements
print(student_id)

# display type of student_id
print(type(student_id))


#Using single quotes  
str1 = 'Hello Python'  
print(str1)  
#Using double quotes  
str2 = "Hello Python"  
print(str2)  
  
#Using triple quotes  
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''   
print(str3)



str = "HELLO"  
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4])  


# Given String  
str = "python"  
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7])


str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello


# using triple quotes  
print('''''They said, "What's there?"''')  
  
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"")  


# Using Curly braces  
print("{} and {} both are the best friend".format("adwik prasad","sravya"))  
  
#Positional Argument  
print("{1} and {0} best players ".format("Virat","Rohit"))  
  
#Keyword Argument  
print("{a},{b},{c}".format(a = "sravan", b = "mani", c = "anil"))  

Integer = 18;    
Float = 1.190    
String = "kohli"    
print("Hi I am Integer ... My value is %d\nHi I am float ... My value is %f\nHi I am string ... My value is %s"%(Integer,Float,String))    



