import utils
from time import time

Monkeys = []

class Monkey:
    business = 0
    def __init__(self,Items,OperationNew,Test,TestTrue,TestFalse, factor):              ##Construktor
        self.Items = Items                                                      #ItemList
        self.OperationNew = OperationNew                                        #Operation of Monkey
        self.Test = Test                                                        #TestNumber to devide by
        self.TestTrue = TestTrue                                                #To Monkey if test = true
        self.TestFalse = TestFalse                                              #To Monkey if test = false
        self.factor = factor

    def testItems(self):
        for item in self.Items:
            self.business += 1
            item = self.OperationNew(item)
            if (self.factor == None):
                item = item // 3
            else:
                item = item % self.factor
            if item % self.Test == 0:
                Monkeys[self.TestTrue].Items.append(item) #Add to Monkey True
            else:   
                Monkeys[self.TestFalse].Items.append(item)#Add to Monkey False
        
        self.Items = []

def evalMonkeyFunc(s):
    s = s.split()
    if(s[1] == "old"):
        if (s[0] == '+'):
            return lambda number: number + number
        else:
            return lambda number: number * number
    else:
        if (s[0] == '+'):
            return lambda number: number + int(s[1])
        else:
            return lambda number: number * int(s[1])


def getMonkeysInitial(input, part):
    StartingItems = []
    OperationNew = 0
    Test =0
    TrueDo = 0
    FalseDo = 0
    for lines in input:
        if "Starting items:" in lines:   #fills object
            StartingItems = [int(x) for x in lines.split('Starting items: ')[1].split(", ")]
        elif "Operation: new = old " in lines:   #fills object
            OperationNew = evalMonkeyFunc(lines.split('Operation: new = old ')[1])
        elif "Test: divisible by " in lines:   #fills object
            Test = int(lines.split('divisible by ')[1])
        elif "If true: throw to monkey " in lines:   #fills object
            TrueDo = int(lines.split('If true: throw to monkey ')[1])
        elif "If false: throw to monkey " in lines:   #fills object
            FalseDo = int(lines.split('If false: throw to monkey ')[1])
            Monkeys.append(Monkey(StartingItems,OperationNew,Test,TrueDo,FalseDo, part))


def part1(input):
    start = time()

    getMonkeysInitial(input, None)
    for i in range(20):
        for monkey in Monkeys:
            monkey.testItems()

    businesses = []

    for monkey in Monkeys:
        businesses.append(monkey.business)
    maxBusiness = max(businesses)
    businesses.remove(maxBusiness)
    secondMaxBusiness = max(businesses)
    
    result = maxBusiness * secondMaxBusiness

    end = time()
    print(f"Part 1: {result}")
    print(f"Runtime Part 1: {end - start}")


def part2(input):
    Monkeys.clear()
    start = time()
    getMonkeysInitial(input, None)
    summe = 1
    for monkey in Monkeys:
        summe *= monkey.Test
    for monkey in Monkeys:
        monkey.factor = summe

    for i in range(10000):
        for monkey in Monkeys:
            monkey.testItems()

    businesses = []

    for monkey in Monkeys:
        businesses.append(monkey.business)
    maxBusiness = max(businesses)
    businesses.remove(maxBusiness)
    secondMaxBusiness = max(businesses)
    
    result = maxBusiness * secondMaxBusiness

    end = time()
    print(f"Part 2: {result}")
    print(f"Runtime Part 2: {end - start}")
        


if __name__ == "__main__":
    input = utils.get_input_as_lines(test=False)
    part1(input)
    part2(input)
