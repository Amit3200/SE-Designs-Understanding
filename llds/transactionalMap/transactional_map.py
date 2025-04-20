class TransactionalMap:
    def __init__(self):
        self.main_data = {}
        self.transactional_data = {}
        self.in_transaction = False

    def begin(self):
        if self.in_transaction:
            print("Transaction already in progress.")
            return
        self.transactional_data.clear()
        self.in_transaction = True

    def set(self, key, value):
        if self.in_transaction:
            self.transactional_data[key] = value
        else:
            self.main_data[key] = value
    
    def erase(self, key):
        if self.in_transaction:
            self.transactional_data[key] = None
        else:
            self.main_data.pop(key, None)
    
    def get(self, key):
        if self.in_transaction and key in self.transactional_data:
            return self.transactional_data.get(key)
        else:
            return self.main_data.get(key)
    
    def commit(self):
        if not self.in_transaction:
            print("No active Transactions.")
            return

        for key, value in self.transactional_data.items():
            if value is None:
                self.main_data.pop(key, None)
            else:
                self.main_data[key] = value
        
        self.transactional_data.clear()
        self.in_transaction = False
    
    def rollback(self):
        if not self.in_transaction:
            print("No Transaction in Progress.")
            return
        self.transactional_data.clear()
        self.in_transaction = False
    
    def print(self):
        print("Current State:")
        for k, v in self.main_data.items():
            print(f"{k} : {v}")

if __name__ == "__main__":
    tm = TransactionalMap()
    tm.set("a", 1)
    tm.set("b", 2)
    tm.print()

    tm.begin()
    tm.set("a", 100)
    tm.erase("b")
    tm.set("c", 3)

    print("\nBefore Commit [in transaction]")
    tm.print()

    tm.commit()

    print("\nAfter Commit [in transaction]")
    tm.print()

    tm.begin()
    tm.set("a", 500)
    tm.rollback()

    print("\nAfter Rollback")
    tm.print()
