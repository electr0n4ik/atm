class ATM:
    def __init__(self):
        self.container_banknotes  = [0, 0, 0, 0, 0]
        self.value_banknotes = [10, 50, 100, 200, 500]

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        Временная сложность:
            O(1), поскольку обновление количества банкнот происходит 
            со списком одной длины и она не меняется.
        Пространственная сложность:
            Константная.
        """

        for i in range(5):
            self.container_banknotes[i] += banknotesCount[i]

        return

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        Временная сложность:
            O(1), поскольку процесс прохода по номиналам и вычитания 
            банкнот происходит со списками одной и той же длины.
        Пространственная сложность:
            Константная.
        """

        withdraw_count = [0] * 5

        for i in range(4, -1, -1):
            num_banknotes = min(amount // self.value_banknotes[i], 
                                self.container_banknotes[i])
            withdraw_count[i] = num_banknotes
            amount -= num_banknotes * self.value_banknotes[i]

            if amount == 0:
                break

        if amount > 0:
            return [-1]

        for i in range(5):
            self.container_banknotes[i] -= withdraw_count[i]

        return withdraw_count


obj = ATM()
obj.deposit([0,0,1,2,1])
print(obj.withdraw(600))  # [0,0,1,0,1]
obj.deposit([0,1,0,1,1])
print(obj.withdraw(600))  # [-1]
print(obj.withdraw(550))  # [0,1,0,0,1]
