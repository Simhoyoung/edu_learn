let info = [
  {
      "name": "김철수",
      "age": 30,
      "city": "서울"
  },
  {
      "name": "박영희",
      "age": 25,
      "city": "부산"
  },
  {
      "name": "이민수",
      "age": 35,
      "city": "대구"
  },
  {
      "name": "최은영",
      "age": 28,
      "city": "인천"
  }
]

// 새 배열안에 이름만 집어느
let names = []
for(let i of info){
  names.push(i.name)
}

console.log(names);
