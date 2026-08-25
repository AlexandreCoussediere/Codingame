# Main game loop: continuously fetch and compare enemy distances
while True:
    # Fetch enemy data
    enemy_1 = input()  # Name of enemy 1
    dist_1 = int(input())  # Distance to enemy 1

    enemy_2 = input()  # Name of enemy 2
    dist_2 = int(input())  # Distance to enemy 2

    # Compare distances to determine the closest enemy
    if dist_1 < dist_2:
        # If enemy 1 is closer, print its name
        print(enemy_1)
    else:
        # Otherwise, print enemy 2's name (handles equal distances as well)
        print(enemy_2)
