class Elf():
    population = 0 # 종족 정보

    def __init__(self, name, health):
        self.ear = 'long'
        self.name = name
        self.health = health
        Elf.population += 1

    def arrow(self):
        print('=====SHOOT====>>')

    def talk(self):
        print(f'이 몸은 {self.name}님 이시다!!!')

e1 = Elf('legolas', 100)
e2 = Elf('smeagol', 100)
e2.ear ='short'
print(e1.ear, e2.ear)


