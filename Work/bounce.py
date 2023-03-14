# bounce.py
#
# Exercise 1.5

# 3/5 is 60%

height = 100 # meters
bounce_factor = 0.6
num_bounces = 0

while num_bounces < 11:
    print(num_bounces, height)
    height = round(height * bounce_factor, 4)
    num_bounces = num_bounces + 1
