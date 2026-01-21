import threading

class Account:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        self.lock = threading.Lock()

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.id] = account

    def transfer(self, from_id, to_id, amount):
        if from_id == to_id:
            return False

        acc_a = self.accounts.get(from_id)
        acc_b = self.accounts.get(to_id)

        if not acc_a or not acc_b:
            return False

        first, second = (acc_a, acc_b) if acc_a.id < acc_b.id else (acc_b, acc_a)

        with first.lock:
            with second.lock:
                if acc_a.balance >= amount:
                    acc_a.balance -= amount
                    acc_b.balance += amount
                    return True
                return False

    def get_balances(self):
        return {id: acc.balance for id, acc in self.accounts.items()}
