# Write a Python program that reads a text file named numbers.txt that contains 20 integers.
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers
# extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from 
# the numbers.txt.

def odd_even():
    # open integers.txt(read), odd(append), even(append)
    with open("integers.txt") as input_file, open("odd_int.txt", "a") as odd_output, open("even_int.txt", "a") as even_output:
# read integers.txt line by line
# remove newline character and convert strings to integers
# if even,
# write to even.txt
# if odd,
# write to odd.txt
# start