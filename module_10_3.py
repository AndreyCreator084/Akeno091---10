from random import randint
from time import sleep
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            deposit = randint(50, 500)
            self.balance += deposit
            print(f"Пополнение: {deposit}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)


    def take(self):
        for i in range(100):
            removal = randint(50, 500)
            print(f"Запрос на {removal}")
            if removal <= self.balance:
                self.balance -= removal
                print(f"Снятие: {removal}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')