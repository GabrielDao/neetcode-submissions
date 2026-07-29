class Account:
    def __init__(self, title: str, balance: int):
        self.title = title          # Public Attribute
        self._balance = balance     # Protected Attribute
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
