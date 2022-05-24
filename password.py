print('HElLO, THIS IS MY RANDOM PASSWORD GENERATOR, PLEASE INPUT YOUR PASSWORD LENGTH, MAXIMUM 36')
# to create RANDOM password you need to import RANDOM MODULE from Python
import random
# create input for user 
length = int(input('\nEnter the length of password: '))
# create variable from module RANDOM, the maxium length of the password is 36
x = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
temp = random.sample(sorted(x),length)
# join the temp to password
password = "".join(temp)
# execution
print(password)


