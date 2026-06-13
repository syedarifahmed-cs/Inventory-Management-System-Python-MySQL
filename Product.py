class Product:

    def __init__(self,product_id,product_name,category_id,suppliers_id,quantity,price):

        self.product_id=product_id
        self.product_name=product_name
        self.category_id=category_id
        self.suppliers_id=suppliers_id
        self.quantity=quantity
        self.price=price

    def display_product(self):

        print("Product ID:",self.product_id)
        print("Product Name:",self.product_name)
        print("Category ID:",self.category_id)
        print("Supplier ID:",self.suppliers_id)
        print("Quantity:",self.quantity)
        print("Price:",self.price)

    def update_price(self,new_price):

        self.price=new_price

    def update_quantity(self,new_quantity):

        self.quantity=new_quantity