const movies = [
  {title: 'matrix', isAdult:false},
  {title: 'kingsman', isAdult:true},
  {title: 'zootopia', isAdult:false},
]

let babyMovies = movies.filter(function(movie){
  return !movie.isAdult;
})