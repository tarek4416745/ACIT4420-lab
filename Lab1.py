# TASK 1
name = raw_input("whats your name ?")
nocookie = int(raw_input("how many cookie do you want ?"))
cookie = " cookie" * nocookie
print "Hi,", name ,"the nummber of your cookies is : ", nocookie , "her is your cookies: ", cookie


# TASK 2
name = raw_input("whats your name ?")
numcookie = int(raw_input("How many cookie do you want ?"))
cookie = " cookie" * numcookie
if 0<numcookie<10:
    print "Hi", name , "Are you sure it's enough" ,"her is your cookies: ", cookie
elif 10 <= numcookie < 20:
    print "Hi", name, "I agree cookies is delicious", "her is your cookies: ", cookie
elif 20 <= numcookie < 51:
    print "Hi", name, "Be careful, it's getting too much", "her is your cookies: ", cookie
elif  numcookie > 50:
    print "Hi", name, "Its getting too much, and modify the value to be 50", "her is your cookies: ", cookie
else:
    print "Hi", name, "Something must be wrong, i give you 10 cookies, and modify nummber to 10"


# task 3
acnum = int(raw_input("How many numbers do you have ? "))
sum = 0
for i in range(acnum):
 num = float(raw_input("Wht is the nummber ? "))
 sum += num
avr = sum/acnum
print "The average is: ",avr
