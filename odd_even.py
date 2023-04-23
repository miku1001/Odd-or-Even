# Write a Python program that reads a text file named numbers.txt that contains 20 integers.
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers
# extracted from the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from 
# the numbers.txt.

def odd_even():
    # open integers.txt(read), odd(append), even(append)
    with open("integers.txt") as input_file, open("odd_int.txt", "a") as odd_output, open("even_int.txt", "a") as even_output:
        # read integers.txt line by line
        for integers in input_file:
            # remove newline character and convert strings to integers
            input_num = int(integers)
            # if even,
            if input_num % 2 == 0:
                # write to even.txt
                even_output.write(str(input_num) + "\n")
            # if odd,
            else:
                # write to odd.txt
                odd_output.write(str(input_num) + "\n")
        print("Odd and Even numbers are seperated successfully")
        print(f"Odd numbers: {len(odd_output.readlines())}" )
        print(f"Even numbers: {len(even_output.readlines())}")
# start
odd_even