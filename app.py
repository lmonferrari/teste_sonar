import pytz
from datetime import datetime

dt = pytz.timezone('America/New_York').localize(datetime(2022, 1, 1)) 

print(3 != 1)

class Teste:
    @staticmethod
    def teste():
        return 1
    
    def teste2(self):
        return 2
    
print(Teste.teste())
print(Teste().teste2())

print(dt)

print(1 == 1)
print(2 == 2)
print(3 == 3)
print(4 == 4)
print(5 == 5)
print(6 == 6)
print(7 == 7)
print(8 == 8)
print(9 == 9)