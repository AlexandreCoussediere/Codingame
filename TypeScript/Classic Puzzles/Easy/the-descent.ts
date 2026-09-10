let mountainH: Array<number> = []

// game loop
while (true) {

    mountainH = []

    for (let i = 0; i < 8; i++) {
        mountainH.push(parseInt(readline())); // represents the height of one mountain.
    }

    const maxHeight: number = Math.max(...mountainH); // Spread operator to pass array elements
    const indexMax: number = mountainH.indexOf(maxHeight); // Find the index of the max height


    console.log(indexMax);     // The index of the mountain to fire on.

}
