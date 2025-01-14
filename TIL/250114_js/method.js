const person = {
  name: '철수철수',
  greet: function () {
    console.log('안녕하세요. 반갑습니다.');
},
  greet1: () => console.log('헬로우,안녕,ㅋ'),
  greet2() {
    console.log('긔긔' )
  }
}

person.greet()
person.greet1()
person.greet2()


var books = ['python', 'javascript']
var games = ['maple','cart']

var myHobby = {
  books,
  games,
}
