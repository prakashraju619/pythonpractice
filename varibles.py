#variables: Variables are case senstive AGE,age, AgE these are different

#EX1

x=5
y="hello welcome to python"
print(y)
print(x)

#EX2
x="hello"
print("welcome "+x)

#EX3 variables numberic types
x=25
y=2.5
z=1j
print(type(x))
print(type(y))
print(type(z))

#EX  Casting
a=int(25.33)
print(a)

#EX String literals 
#prints the first leter 
a="hello welcome"
print(a[1])

#Sub String
a="hello welcome to python"
print(a[2:9])

#Strip Method The strip() method removes any whitespace from the beginning or the end
z="  hello welcome to python      "
print(a.strip())

#Len Meathod: The len() method returns the length of a string
z="  hello welcome to python      "
print(len(z))

#Lower Method and upper Method
a="HELLO WELCOME TO PYTHON"
a="hell welcome to python"
print(a.lower())
print(a.upper())

#The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))
print(a)

#Split() its used to slipts string
y="hello, welcome to "
print(y.split(","))


x = 5

print(x > 3 and x < 10)


#python collections(arrays)-List, tupple,set , dictionary
thislist=["apple","banana","orange"]
print(thislist)
print(thislist[1])   #in this 1 will apper as output
thislist[1]="apple"  #repalce the item
print(thislist)


tlist=["apple","banana","orange"]
if "apple" in tlist:
	print("apple , in this list apple availabel")

for i in range(1,10):
	print(i)

#if condition
prakash= "java"
if prakash=="python":
	print("its was python")
elif prakash=="java":
	print('its was java')
else:
	print("its was not correct")
#Example
a=[1, 2,3]
b=a
print(id(a))
print(id(b))
print(a==b)

condition = 10

if condition:
	print("evaluted is correct")
else:
	print("evaluted is wrong")

nums=[1, 2, 3,4, 5, 6, 8]
for num in nums:
	if num ==3:
		print('found!')
		break
print(num)

x=0
while x<30:
	print(x)
	x +=1


def prakash():
	return("hello welcome to")
print(prakash())



def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

