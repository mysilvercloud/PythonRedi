print('HElLO, THIS IS MY RANDOM PASSWORD GENERATOR, PLEASE INPUT YOUR PASSWORD LENGTH')
# to create RANDOM password you need to import RANDOM MODULE from Python
import random
# create input for user 
length = int(input('\nEnter the length of password: '))
# create variable from module RANDOM, the maxium length of the password depends on your computer
temp = random.sample(all,length)
# join the temp to password
password = "".join(temp)
# execution
print(password)


