# store options with strings

class Menu:
    def __init__(self):
        self._options = str()
        self._count = 0
    
    def addOptions(self, option):
        self._count += 1
        if self._count != 1:
            self._options += '\n'
        self._options += (option)
    
    def getInput(self):
        done = False
        while not done:
            for i in range(self._count):
                print('%d %s' %(i + 1, self._options.split('\n')[i]))
            userChoice = int(input())
            if userChoice >= 1 and userChoice < len(self._options):
                done = True
        return userChoice


main = Menu()
main.addOptions('O1')
main.addOptions('O2')
main.addOptions('O3')
main.addOptions('O4')
choice = main.getInput()
print("Input:", choice)