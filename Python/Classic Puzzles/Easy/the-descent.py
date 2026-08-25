# Initialize an empty list to store the heights of the mountains
mountain_h = []

# Start an infinite loop to continuously process mountain heights
while True:
    # Clear the list for each new iteration (to avoid storing old data)
    mountain_h = []

    # Read 8 mountain heights from input and store them in the list
    for i in range(8):
        mountain_h.append(int(input()))

    # Find the index of the tallest mountain in the list
    index_max = mountain_h.index(max(mountain_h))

    # Print the index of the tallest mountain
    print(index_max)
