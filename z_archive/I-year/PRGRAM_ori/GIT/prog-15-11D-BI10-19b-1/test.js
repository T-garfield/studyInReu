console.log(100 % 2)
console.log(101 % 2)
console.log(1013 % 2)

function N12(A) {
    let sum = 0

    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < A[i].length; j++) {
            sum += A[i][j]
        }
    }
    if (sum % 2 === 0) {
        console.log("сумма элементов матрицы - четное число")
    }
    else console.log("сумма элементов матрицы - нечетное число")

    console.log(sum);
    console.log(sum % 2);
}

N12([
    [2, 4, 6],
    [8, 6, 4],
    [2, 0, -2]
])

N12([
    [2, 4, 6],
    [8, 7, 4],
    [2, 11, -2]
])
