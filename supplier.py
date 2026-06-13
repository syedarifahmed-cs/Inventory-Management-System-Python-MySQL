class Suppliers:

    def __init__(self,supplier_id,supplier_name,contact,city):

        self.supplier_id=supplier_id
        self.supplier_name=supplier_name
        self.contact=contact
        self.city=city

    def display_supplier(self):

        print("Supplier ID:",self.supplier_id)
        print("Supplier Name:",self.supplier_name)
        print("Contact:",self.contact)
        print("City:",self.city)