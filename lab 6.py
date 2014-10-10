total = 0
print "How many numbers do you want to add together"
userinput = int(raw_input())
for add in range (userinput):
    print "enter number"
    num = int(raw_input())
    total = total + num
print total


total1 = []
print "How many numbers do you want to add together"
userinput = int(raw_input())
for add in range (userinput):
    print "enter number"
    num = int(raw_input())
    total1.append(num)
print sum(total1)

total = 1
print "what number do you want to take the factorial of?"
 
