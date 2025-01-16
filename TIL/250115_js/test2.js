const movies = [
  {title: 'matrix', isAdult:false},
  {title: 'kingsman', isAdult:true},
  {title: 'zootopia', isAdult:false},
]

let baby = movies.reduce(function(acc, movie) {
  if (!movie.isAdult) {acc.push(movie.title)}
  return acc
},[])

console.log(baby, typeof(baby));


// let baby = movies.filter(movie => movie.isAdult === false.map(movie => movie.title))