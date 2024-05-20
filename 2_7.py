class Wallet:
    def __init__(self, id, holder, funds=0.0):
        self.id = id
        self.holder = holder
        self.funds = funds

    def add_funds(self, sum):
        if sum > 0:
            commission = sum * 0.01
            self.funds += (sum - commission)
            print(f"Пополнено: {sum}, Комиссия: {commission}, Баланс: {self.funds:.2f}")
        else:
            print("Нет денег для пополнения")

    def spend_funds(self, sum):
        if sum > 0 and (sum + sum * 0.01) <= self.funds:
            commission = sum * 0.01
            self.funds -= (sum + commission)
            print(f"Списано: {sum}, Комиссия: {commission}, Баланс: {self.funds:.2f}")
        else:
            print("Недостаточно средств")

    def check_funds(self):
        print(f"Текущий баланс: {self.funds}")
        return self.funds

wallet1 = Wallet("1251253342", "Lev", 4125)
wallet1.add_funds(2134)
wallet1.spend_funds(5216)
wallet1.check_funds()
