# Read the number of landing surfaces
surface_n = int(input())

# Read the coordinates of each landing surface
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]  # (x, y) coordinates of the landing zone

# Main game loop
while True:
    # Read the current state of the ship
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Adjust engine power based on vertical speed and altitude
    if v_speed > 20 or y - land_y < 500:
        pow = 4  # Full power to slow descent
    else:
        pow = 3  # Reduced power for stable landing

    # Send commands: 0° rotation and the calculated power
    print(f"0 {pow}")
