array1 = [true, true, true, false,
    true, true, true, true,
    true, false, true, false,
    true, false, false, true,
    true, true, true, true,
    false, false, true, true
]

function countTrue(arr) {
    return arr.count();
}

Array.prototype.count = function () {
    return this.filter(item => item).length;
}

console.log(countTrue(array1));

console.log(countTrue(array1) === 17)