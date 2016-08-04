class Divisible:
    def __init__(self, n):
        self.n = n
    def run(self):
        Somme = 0
        for i in range(1, self.n + 1):
            if i % 3 == 0 or i % 5 == 0:
                Somme += i
        return Somme

def get_classes():
    li = [Divisible]
    return li

print (Divisible(5).run())
