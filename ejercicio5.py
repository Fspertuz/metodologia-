class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Atributo privado para el titular de la cuenta
        if initial_balance < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.__balance = initial_balance  # Atributo privado para el saldo de la cuenta
    
    # Método para depositar dinero en la cuenta
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.__balance += amount
    
    # Método para retirar dinero de la cuenta
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if amount > self.__balance:
            raise ValueError("Fondos insuficientes.")
        self.__balance -= amount
    
    # Método para consultar el saldo de la cuenta
    def check_balance(self):
        return self.__balance
    
    # Método para consultar el titular de la cuenta
    def check_holder(self):
        return self.__account_holder


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        if interest_rate < 0:
            raise ValueError("El porcentaje de interés no puede ser negativo.")
        self.__interest_rate = interest_rate  # Atributo privado para el porcentaje de interés
    
    # Método para aplicar el interés anual al saldo de la cuenta
    def apply_interest(self):
        interest = (self.check_balance() * self.__interest_rate) / 100
        self.deposit(interest)
    
    # Método para consultar el porcentaje de interés
    def check_interest_rate(self):
        return self.__interest_rate


# Ejemplo
try:
    # Crear una cuenta de ahorro con un saldo inicial de 1500 y un interés anual del 3.5%
    savings_account = SavingsAccount("Carlos Gómez", 1500, 3.5)
    
    # Consultar el titular y saldo inicial
    print(f"Titular de la cuenta: {savings_account.check_holder()}")
    print(f"Saldo inicial: ${savings_account.check_balance():.2f}")
    
    # Aplicar el interés anual
    savings_account.apply_interest()
    print(f"Saldo después de aplicar el interés: ${savings_account.check_balance():.2f}")
    
    # Consultar el porcentaje de interés actual
    print(f"Porcentaje de interés anual: {savings_account.check_interest_rate()}%")
    
    # Realizar un depósito
    savings_account.deposit(700)
    print(f"Saldo después del depósito: ${savings_account.check_balance():.2f}")
    
    # Realizar un retiro
    savings_account.withdraw(400)
    print(f"Saldo después del retiro: ${savings_account.check_balance():.2f}")
    
except ValueError as e:
    print(e)
