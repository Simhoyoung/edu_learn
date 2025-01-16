let arr = [1,2,3]

let sum = arr.reduce(function (acc,num){
  acc.push(num*2)
  return acc
}, [])
console.log(sum)

let sum = arr.reduce((acc,num)=> acc.push(num*2))