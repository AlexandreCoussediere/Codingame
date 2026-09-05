/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

var inputs = readline().split(' ');
const light_x = parseInt(inputs[0]); // the X position of the light of power
const light_y = parseInt(inputs[1]); // the Y position of the light of power
let thor_x = parseInt(inputs[2]); // Thor's starting X position
let thor_y = parseInt(inputs[3]); // Thor's starting Y position

// game loop
while (true) {
    const remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.

    output = ""

    if (thor_y > light_y){
        output += "N"
        thor_y -= 1}
    else if (thor_y < light_y){
        output += "S"
        thor_y += 1}

    if (thor_x > light_x){
        output += "W"
        thor_x -= 1}
    else if (thor_x < light_x){
        output += "E"
        thor_x += 1}
    console.log(output);
}
