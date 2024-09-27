# ZyLabs 5.19
# Write a program that takes in an integer in the range 11-99 (inclusive) as input. 
# The output of the program is a countdown starting from the input integer until an integer where 
# both digits are identical.

unum = input()

while True:
    if 11 <= int(unum) <= 99:
        if str(unum[:-1]) == str(unum[0:]):
            print('all done!')
            break
        else:
            int(unum) = unum - 1
            print(unum)
    else:
        print('Input must be 11-99')