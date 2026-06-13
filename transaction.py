class Transaction:

    def __init__(self,transaction_id,product_id,transaction_type,quantity,transaction_date):

        self.transaction_id=transaction_id
        self.product_id=product_id
        self.transaction_type=transaction_type
        self.quantity=quantity
        self.transaction_date=transaction_date

    def display_transaction(self):

        print("Transaction ID:",self.transaction_id)
        print("Product ID:",self.product_id)
        print("Transaction Type:",self.transaction_type)
        print("Quantity:",self.quantity)
        print("Transaction Date:",self.transaction_date)