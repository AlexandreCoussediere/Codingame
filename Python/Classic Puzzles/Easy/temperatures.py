n = int(input())  # Read the number of inputs (though not used in the logic)

output = None  # Initialize output as None to handle the first number

for i in input().split():  # Split the input into individual numbers
    num = int(i)  # Convert the current number to an integer

    if output is None:  # If this is the first number, set it as output
        output = num
    else:
        # Compare absolute values
        if abs(num) < abs(output):  # If current number has a smaller absolute value
            output = num
        elif abs(num) == abs(output) and num > output:  # If absolute values are equal and current number is larger
            output = num

# Handle the case where no valid input was provided (e.g., empty input)
if output is None:
    output = 0

print(output)  # Print the result
