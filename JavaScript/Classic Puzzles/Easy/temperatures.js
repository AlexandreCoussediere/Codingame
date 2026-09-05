const n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');
let a = null;
for (let i = 0; i < n; i++) {
    const t = parseInt(inputs[i]);
    if (a == null){
        a = t
    }
    else if (Math.abs(t) < Math.abs(a) || Math.abs(t) == Math.abs(a) && t > a){
        a = t
    }
}
if (a == null){
    a = 0
}

console.log(a);
