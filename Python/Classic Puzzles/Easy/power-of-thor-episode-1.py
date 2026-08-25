# Read initial positions: light (light_x, light_y) and Thor (thor_x, thor_y)
light_x, light_y, thor_x, thor_y = [int(i) for i in input().split()]

# Game loop
while True:
    # Read remaining turns (unused in logic)
    remaining_turns = int(input())

    output = ""

    # Move vertically (Y-axis)
    if thor_y > light_y:
        output += "N"  # Move North (up)
        thor_y -= 1
    elif thor_y < light_y:
        output += "S"  # Move South (down)
        thor_y += 1

    # Move horizontally (X-axis)
    if thor_x > light_x:
        output += "W"  # Move West (left)
        thor_x -= 1
    elif thor_x < light_x:
        output += "E"  # Move East (right)
        thor_x += 1

    print(output)  # Print direction (e.g., "N", "NE", "S", etc.)
