print("hi I am Y.Sai Sidhardh")
print("i have edited this using git hub from online")
print("this print line i have edited using pycharm")
"""i am giving a code using python IDE (Py Charm) for finding prime numbers"""
num = int(input("enter the number you want to check: "))
half = num//2
for i in range(2,half):
    if num % i == 0:
        print("{} is not a prime number".format(num))
        break
else:
    print("{} is a prime number".format(num))
print("hope you got the right output")
print("thank you!")