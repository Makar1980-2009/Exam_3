class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Финальная стоимость: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def __str__(self):
        return SmallHouse.default_area


class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__money, self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)

    def earn_money(self, money):
        self.__money += money
        print(f'Получено: {money}.Текущий счёт: {self.__money}')

    def by_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.make_deal(house, price)
        else:
            print("No money!")
    def make_deal(self, house, price):
        self.__money -= price
        self.__house = house

sm_house = SmallHouse(7000)
Human.default_info()
Katerina = Human('Katerina', 18)
Katerina.info()
Katerina.earn_money(5000)
Katerina.by_house(sm_house, 5)
Katerina.earn_money(20000)
Katerina.by_house(sm_house, 5)
Katerina.info()
