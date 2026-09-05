const surfaceN = parseInt(readline());

let landX1, landY1, landX2, landY2;

for (let i = 0; i < surfaceN; i++) {
    const inputs = readline().split(' ');
    const landX = parseInt(inputs[0]);
    const landY = parseInt(inputs[1]);

    if (i > 0 && landY === landY1) {
        // Found the flat landing zone
        landX2 = landX;
        landY2 = landY;
    }

    landX1 = landX;
    landY1 = landY;
}

while (true) {
    const inputs = readline().split(' ');

    const X = parseInt(inputs[0]);
    const Y = parseInt(inputs[1]);
    const hSpeed = parseInt(inputs[2]);
    const vSpeed = parseInt(inputs[3]);
    const fuel = parseInt(inputs[4]);
    const rotate = parseInt(inputs[5]);
    const currentPow = parseInt(inputs[6]);

    let power;

    // Basic vertical-speed control
    if (vSpeed < -40) {
        power = 4;
    } else if (vSpeed < -20) {
        power = 3;
    } else {
        power = 2;
    }

    console.log("0 " + power);
}
