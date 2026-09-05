import sys
import math

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

# on stocke la position des ascenseurs : elevators[floor] = pos
elevators = {}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])
    clone_pos = int(inputs[1])
    direction = inputs[2]

    if clone_floor == -1:
        # pas de clone de tête disponible pour l'instant
        print("WAIT")
        continue

    on_elevator = elevators.get(clone_floor) == clone_pos

    if on_elevator:
        # on laisse toujours monter le clone quand il est sur un ascenseur
        print("WAIT")
        continue

    # cible à atteindre sur cet étage : la sortie si c'est l'étage final,
    # sinon l'ascenseur de cet étage (s'il y en a un) pour continuer à monter
    if clone_floor == exit_floor:
        target_pos = exit_pos
    elif clone_floor in elevators:
        target_pos = elevators[clone_floor]
    else:
        target_pos = None

    if target_pos is not None:
        moving_away = (direction == "RIGHT" and clone_pos >= target_pos) or \
                      (direction == "LEFT" and clone_pos <= target_pos)
    else:
        moving_away = False

    if moving_away:
        # inutile d'attendre le bord, on bloque tout de suite pour faire
        # rebondir les prochains clones vers la cible
        action = "BLOCK"
    else:
        # position suivante si on ne bloque pas
        if direction == "RIGHT":
            next_pos = clone_pos + 1
        else:
            next_pos = clone_pos - 1

        about_to_die = next_pos < 0 or next_pos >= width
        action = "BLOCK" if about_to_die else "WAIT"

    print(action)
