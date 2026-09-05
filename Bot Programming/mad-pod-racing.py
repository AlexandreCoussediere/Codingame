BOOST = True

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    angle = abs(next_checkpoint_angle)

    # --- Thrust ---
    if angle > 90:
        thrust = 20
    elif angle > 60 and next_checkpoint_dist < 1500:
        thrust = 40
    else:
        thrust = 100

    # --- Cible : toujours le checkpoint réel, jamais de décalage ---
    target_x = next_checkpoint_x
    target_y = next_checkpoint_y

    # --- Boost ---
    thrust_str = str(thrust)
    if next_checkpoint_dist > 5000 and next_checkpoint_angle == 0 and BOOST:
        thrust_str = "BOOST"
        BOOST = False

    print(f"{target_x} {target_y} {thrust_str}")
