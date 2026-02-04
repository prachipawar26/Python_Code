class Money:
    def __init__(self, amount: float, currency: str = "USD"):
        self.amount = amount
        self.currency = currency

    # Overloading the + operator
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies!")
        return Money(self.amount + other.amount, self.currency)

    def __repr__(self):
        return f"{self.amount} {self.currency}"

m1 = Money(50)
m2 = Money(25)
m3 = m1 + m2 # Triggers __add__
print(m3)    # 75 USD