#!/usr/bin/env python3
class Dog:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def __str__(self):
        return 'Name: ' + self.n + ' Age: ' + str(self.a)

    def aged(self, yearsolder):
        self.a = self.a + yearsolder

class JackRussell(Dog):
    def __init__(self, name, age, isWirehair, isHunter):
        Dog.__init__(self, name, age)
        self.wh = isWirehair
        self.h = isHunter

    def __str__(self):
        retStr = Dog.__str__(self)
        retStr += ' Wirehaired: ' + str(self.wh) + ' Trained to hunt: ' + str(self.h)
        return retStr

mutt = Dog('Derpy', 3)
print(mutt)

eddie = JackRussell('Eddie', 4, False, True)
print(eddie)

eddie.aged(3)
print(eddie)
