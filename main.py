from inventory import Inventory

inv=Inventory()

while True:

    print("\n1.View Products")
    print("2.Search Product")
    print("3.Add Product")
    print("4.Delete Product")
    print("5.Update Price")
    print("6.Increase Stock")
    print("7.Decrease Stock")
    print("8.Low Stock Alert")
    print("9.Highest Price Product")
    print("10.Total Inventory Value")
    print("11.Exit")

    choice=int(input("Enter Your Choice: "))

    if choice==1:

        inv.view_products()

    elif choice==2:

        product_id=int(input("Enter Product ID: "))

        inv.search_product(product_id)

    elif choice==3:

        product_id=int(input("Enter Product ID: "))
        product_name=input("Enter Product Name: ")
        category_id=int(input("Enter Category ID: "))
        suppliers_id=int(input("Enter Supplier ID: "))
        quantity=int(input("Enter Quantity: "))
        price=int(input("Enter Price: "))

        inv.add_product(
            product_id,
            product_name,
            category_id,
            suppliers_id,
            quantity,
            price
        )

    elif choice==4:

        product_id=int(input("Enter Product ID: "))

        inv.delete_product(product_id)

    elif choice==5:

        product_id=int(input("Enter Product ID: "))
        new_price=int(input("Enter New Price: "))

        inv.update_price(product_id,new_price)

    elif choice==6:

        product_id=int(input("Enter Product ID: "))
        quantity=int(input("Enter Quantity To Add: "))

        inv.increase_stock(product_id,quantity)

    elif choice==7:

        product_id=int(input("Enter Product ID: "))
        quantity=int(input("Enter Quantity To Remove: "))

        inv.decrease_stock(product_id,quantity)

    elif choice==8:

        inv.low_stock_alert()

    elif choice==9:

        inv.highest_price_product()

    elif choice==10:

        inv.total_inventory_value()

    elif choice==11:

        print("Program Closed")
        break

    else:

        print("Invalid Choice")