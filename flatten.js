function flatten(arr) {
    counter = arr.length

    for (i = 0; i < counter; i++) {
        if (typeof (arr[i]) == 'object') {
            for (z = 0; z < arr[i].length; z++) {
                if (arr[i][z] != null) {
                    arr.push(Number([arr[i][z]]));
                }
            }
        }
        else {
            arr.push(arr[i]);
        }
    }
    // console.log(arr);
    for (i = 0; i < counter; i++) {
        arr.shift(arr[i]);
    }
    return arr;
}


console.log(flatten([1, 2, 3, []],[[4, 5], [6, 7, 8], 9, 10]));

arrtest = ([1,2,3,], [4,5,6])

function median(arr1, arr2) {
    median = 0;
    average = 0;
    arr1.push(arr2);
    // console.log(arr1);
    flatten(arr1)
    // console.log(arr1)
    arr1.sort()
    console.log(arr1)
    if (arr1.length % 2 == 1) {
        median = Math.floor(arr1.length / 2)
        return arr1[median];
    }
    else {
        median = Math.floor((arr1.length - 1) / 2)
        average = (arr1[median] + arr1[median + 1]) / 2
        return average;
    }
}
arrb=[1,3,8,2,3]
arra=[4,5,6,1,2,3]

console.log(median(arrb,arra));

function fib(val) {
    arr = [0,1];
    fib = 0;
    if (val <= 1) { return 0; } 
    if (val == 2) { return 1; }
    for (var i = 0; i < val - 1; i++) {
        fib = arr[0] + arr[1]
        arr.push(fib)
         arr.shift();
        }
    }
    return fib;
// console.log(fib(14));
// console.log(fib(2));
// console.log(fib(3));
// console.log(fib(4));
// console.log(fib(5));
// console.log(fib(6));
// console.log(fib(7));
