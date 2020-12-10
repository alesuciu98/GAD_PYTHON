class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numarator(self):
        return self.numarator

    def get_numitor(self):
        return self.numitor

    def __str__(self):
        return str(self.numarator) + '/' + str(self.numitor)

    @classmethod
    def __add__(cls, fractie1, fractie2):
        result = Fractie(0, 0)
        if fractie1.numitor == fractie2.get_numitor():
            result.numarator = fractie1.numarator + fractie2.get_numarator()
            result.numitor = fractie1.get_numitor()
        else:
            result.numarator = (fractie1.numarator * fractie2.get_numitor()) + (fractie2.numarator * fractie1.numitor)
            result.numitor = fractie1.numitor * fractie2.get_numitor()
        x = 0
        if result.numarator > result.numitor:
            x = result.numarator
        else:
            x = result.numitor
        for i in range(1, x):
            if result.numarator % i == 0 and result.numitor % i == 0:
                result.numarator = result.numarator / i
                result.numitor = result.numitor / i
        return result

    @classmethod
    def __sub__(cls, fractie4, fractie5):
        result = Fractie(0, 0)
        if fractie4.numitor == fractie5.get_numitor():
            result.numarator = fractie4.numarator - fractie5.get_numarator()
            result.numitor = fractie4.get_numitor()
        else:
            result.numarator = (fractie4.numarator * fractie5.get_numitor()) - (fractie5.numarator * fractie4.numitor)
            result.numitor = fractie4.numitor * fractie5.get_numitor()
        x = 0
        if result.numarator > result.numitor:
            x = result.numarator
        else:
            x = result.numitor
        for i in range(1, x):
            if result.numarator % i == 0 and result.numitor % i == 0:
                result.numarator = result.numarator / i
                result.numitor = result.numitor / i
        return result

    @staticmethod
    def inverse(fractie):
        return Fractie(fractie.get_numitor(), fractie.get_numarator())


if __name__ == '__main__':
    fractie1 = Fractie(2, 3)
    fractie2 = Fractie(5, 3)
    fractie3 = Fractie(2, 4)

    print('Afisam prima fractie: ' + fractie1.__str__())

    print('Afisam adunarea a doua fractii: ' + fractie1.__str__() + ' + ' + fractie2.__str__() + ' = ' + Fractie.__add__(fractie1=fractie1, fractie2=fractie2).__str__())
    print('Afisam adunarea a doua fractii: ' + fractie1.__str__() + ' + ' + fractie2.__str__() + ' = ' + Fractie.__add__(fractie1=fractie2, fractie2=fractie3).__str__())

    fractie4 = Fractie(2, 2)
    fractie5 = Fractie(2, 3)
    print('Afisam scaderea a doua fractii: ' + fractie4.__str__() + ' + ' + fractie5.__str__() + ' = ' + Fractie.__sub__(fractie4=fractie4, fractie5=fractie5).__str__())
    print('Afisam scaderea a doua fractii: ' + fractie4.__str__() + ' + ' + fractie5.__str__() + ' = ' + Fractie.__sub__(fractie4=fractie5, fractie5=fractie4).__str__())
    fractie6 = Fractie.inverse(fractie5)
    print(fractie6.__str__())