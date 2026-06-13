from db_connection import connection,cursor

class Inventory:

    def view_products(self):

        cursor.execute("select * from Products")

        for row in cursor:
            print(row)

    def search_product(self,product_id):

        cursor.execute(
            "select * from Products where product_id=%s",
            (product_id,)
        )

        result=cursor.fetchone()

        if result:
            print(result)

        else:
            print("Product Not Found")

    def add_product(self,product_id,product_name,category_id,suppliers_id,quantity,price):

        cursor.execute(
            "insert into Products values(%s,%s,%s,%s,%s,%s)",
            (product_id,product_name,category_id,suppliers_id,quantity,price)
        )

        connection.commit()

        print("Product Added Successfully")

    def delete_product(self,product_id):

        cursor.execute(
            "delete from Products where product_id=%s",
            (product_id,)
        )

        connection.commit()

        print("Product Deleted Successfully")

    def update_price(self,product_id,new_price):

        cursor.execute(
            "update Products set price=%s where product_id=%s",
            (new_price,product_id)
        )

        connection.commit()

        print("Price Updated Successfully")

    def increase_stock(self,product_id,quantity):

        cursor.execute(
            "update Products set quantity=quantity+%s where product_id=%s",
            (quantity,product_id)
        )

        connection.commit()

        print("Stock Increased Successfully")

    def decrease_stock(self,product_id,quantity):

        cursor.execute(
            "update Products set quantity=quantity-%s where product_id=%s",
            (quantity,product_id)
        )

        connection.commit()

        print("Stock Decreased Successfully")

    def low_stock_alert(self):

        cursor.execute(
            "select * from Products where quantity<10"
        )

        for row in cursor:
            print(row)

    def highest_price_product(self):

        cursor.execute(
            "select * from Products order by price desc limit 1"
        )

        result=cursor.fetchone()

        print(result)

    def total_inventory_value(self):

        cursor.execute(
            "select sum(quantity*price) from Products"
        )

        result=cursor.fetchone()

        print("Total Inventory Value:",result[0])