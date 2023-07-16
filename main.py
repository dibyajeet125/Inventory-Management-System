import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Excommunicado100%",
    database="inventory"
)

mycursor = mydb.cursor()

def login_user():
    supplier_id = supplier_id_entry.get()
    supplier_password = supplier_password_entry.get()
    mycursor.execute('select * from supplier where supplier_id=%s and supplier_password=%s;', (supplier_id, supplier_password))
    mycursor.fetchall()
    if mycursor.rowcount == 1:
        def product():
            product_window = Toplevel(newWindow)
            product_window.geometry('800x500')
            product_window.title('Product')

            product_window.iconbitmap('icon.ico')

            item_id = Label(product_window, text='ITEM ID')
            item_id.grid(row=0, column=0)

            supp_id = Label(product_window, text='SUPPLIER ID')
            supp_id.grid(row=0, column=1)

            item_name = Label(product_window, text='ITEM NAME')
            item_name.grid(row=0, column=2)

            item_desc = Label(product_window, text='ITEM DESCRIPTION')
            item_desc.grid(row=0, column=3)

            item_price = Label(product_window, text='ITEM PRICE')
            item_price.grid(row=0, column=4)

            item_quan = Label(product_window, text='ITEM QUANTITY')
            item_quan.grid(row=0, column=5)

            mycursor.execute("SELECT * FROM product WHERE supplier_id=%s", (supplier_id,))
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(product_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            bt = Button(product_window, text="ADD PRODUCT", command=lambda: add_product())
            bt.grid(row=i + 2, column=1)

            bt = Button(product_window, text="DELETE PRODUCT", command=lambda: remove_product())
            bt.grid(row=i + 2, column=2)

            bt = Button(product_window, text="RESTOCK ITEM", command=lambda: restock_item())
            bt.grid(row=i + 2, column=3)

        def add_product():
            add_product_window = Toplevel(newWindow)
            add_product_window.geometry('800x500')
            add_product_window.title('Add Product')

            add_product_window.iconbitmap('icon.ico')

            l1 = Label(add_product_window, text="Enter Supplier Id")
            l1.place(x=20, y=20)

            l1 = Label(add_product_window, text="Enter Item Name")
            l1.place(x=20, y=80)

            l1 = Label(add_product_window, text="Enter Item Description")
            l1.place(x=20, y=140)

            l1 = Label(add_product_window, text="Enter Item Price")
            l1.place(x=20, y=200)

            l1 = Label(add_product_window, text="Enter Item Quantity")
            l1.place(x=20, y=260)

            e1 = Entry(add_product_window)
            e1.place(x=200, y=20)

            e2 = Entry(add_product_window)
            e2.place(x=200, y=80)

            e3 = Entry(add_product_window)
            e3.place(x=200, y=140)

            e4 = Entry(add_product_window)
            e4.place(x=200, y=200)

            e5 = Entry(add_product_window)
            e5.place(x=200, y=260)

            bt = Button(add_product_window, text='INSERT PRODUCT', command=lambda: insert_product(e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
            bt.place(x=300, y=320)

        def insert_product(supp_id, item_name, item_desc, item_price, item_quan):
            mycursor.execute('insert into product(supplier_id, item_name, item_description, item_price, item_quantity) values(%s, %s, %s, %s, %s)', (supp_id, item_name, item_desc, item_price, item_quan))
            mydb.commit()

        def remove_product():
            remove_product_window = Toplevel(newWindow)
            remove_product_window.geometry('800x500')
            remove_product_window.title('Remove Product')

            remove_product_window.iconbitmap('icon.ico')

            l1 = Label(remove_product_window, text="Enter Item ID to be deleted: ")
            l1.place(x=20, y=20)

            e1 = Entry(remove_product_window)
            e1.place(x=200, y=20)

            bt = Button(remove_product_window, text='DELETE PRODUCT', command=lambda: delete_product(e1.get()))
            bt.place(x=60, y=80)

        def delete_product(item_id):
            mycursor.execute('delete from product where item_id=%s', (item_id,))
            mydb.commit()

        def restock_item():
            restock_item_window = Toplevel(newWindow)
            restock_item_window.geometry('800x500')
            restock_item_window.title('Item Restock')

            restock_item_window.iconbitmap('icon.ico')

            l1 = Label(restock_item_window, text="Enter Item ID to be restocked: ")
            l1.place(x=20, y=20)

            e1 = Entry(restock_item_window)
            e1.place(x=200, y=20)

            bt = Button(restock_item_window, text="RESTOCK ITEM", command=lambda: restock_query(e1.get()))
            bt.place(x=60, y=80)

        def restock_query(item_id):
            mycursor.execute('update product set item_quantity = item_quantity + 10 where item_id = %s', (item_id,))
            mydb.commit()

        def order_():
            order_window = Toplevel(newWindow)
            order_window.geometry('800x500')
            order_window.title('Order')

            order_window.iconbitmap('icon.ico')

            or_id = Label(order_window, text='ORDER ID')
            or_id.grid(row=0, column=0)

            or_id = Label(order_window, text='ITEM ID')
            or_id.grid(row=0, column=1)

            cust_id = Label(order_window, text='CUSTOMER ID')
            cust_id.grid(row=0, column=2)

            supp_id = Label(order_window, text='SUPPLIER ID')
            supp_id.grid(row=0, column=3)

            or_date = Label(order_window, text='ORDER DATE')
            or_date.grid(row=0, column=4)

            or_quan = Label(order_window, text='ORDER QUANTITY')
            or_quan.grid(row=0, column=5)

            t_price = Label(order_window, text='TOTAL PRICE')
            t_price.grid(row=0, column=6)

            mycursor.execute("SELECT * FROM order_ WHERE supplier_id=%s", (supplier_id,))
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(order_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(0, x[j])
                i = i + 1

            bt = Button(order_window, text='VIEW ORDER DETAILS', command=lambda: view_order())
            bt.grid(row=i + 2, column=1)

            bt = Button(order_window, text='ADD ORDER', command=lambda: add_order_())
            bt.grid(row=i + 2, column=2)

            bt = Button(order_window, text="DELETE ORDER", command=lambda: remove_order_())
            bt.grid(row=i + 2, column=3)

            def view_order():
                view_order_window = Toplevel(newWindow)
                view_order_window.geometry('800x500')
                view_order_window.title('Order Details')

                view_order_window.iconbitmap('icon.ico')

                def payment():
                    order_id = order_id_entry.get()
                    customer_id = customer_id_entry.get()
                    mycursor.execute("SELECT * FROM payment WHERE order_id = %s AND customer_id = %s", (order_id, customer_id))
                    payment_data = mycursor.fetchall()

                    payment_window = Toplevel(newWindow)
                    payment_window.geometry('800x500')
                    payment_window.title('Payment')

                    payment_window.iconbitmap('icon.ico')

                    item_id = Label(payment_window, text='ITEM ID')
                    item_id.grid(row=0, column=0)

                    or_id = Label(payment_window, text='ORDER ID')
                    or_id.grid(row=0, column=1)

                    cust_id = Label(payment_window, text='CUSTOMER ID')
                    cust_id.grid(row=0, column=2)

                    pay_date = Label(payment_window, text='PAYMENT DATE')
                    pay_date.grid(row=0, column=3)

                    pay_meth = Label(payment_window, text='PAYMENT METHOD')
                    pay_meth.grid(row=0, column=4)

                    pay_amt = Label(payment_window, text='PAYMENT AMOUNT')
                    pay_amt.grid(row=0, column=5)

                    i = 1
                    for x in payment_data:
                        for j in range(len(x)):
                            e = Entry(payment_window, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, x[j])
                        i = i + 1

                def shipment():
                    order_id = order_id_entry.get()
                    customer_id = customer_id_entry.get()
                    mycursor.execute("SELECT * FROM shipment WHERE order_id = %s AND customer_id = %s", (order_id, customer_id))
                    shipment_data = mycursor.fetchall()

                    shipment_window = Toplevel(newWindow)
                    shipment_window.geometry('800x500')
                    shipment_window.title('Shipment')

                    shipment_window.iconbitmap('icon.ico')

                    item_id = Label(shipment_window, text='ITEM ID')
                    item_id.grid(row=0, column=0)

                    or_id = Label(shipment_window, text='ORDER ID')
                    or_id.grid(row=0, column=1)

                    cust_id = Label(shipment_window, text='CUSTOMER ID')
                    cust_id.grid(row=0, column=2)

                    ship_date = Label(shipment_window, text='SHIPMENT DATE')
                    ship_date.grid(row=0, column=3)

                    ship_stat = Label(shipment_window, text='SHIPMENT STATUS')
                    ship_stat.grid(row=0, column=4)

                    i = 1
                    for x in shipment_data:
                        for j in range(len(x)):
                            e = Entry(shipment_window, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, x[j])
                        i = i + 1

                def invoice():
                    order_id = order_id_entry.get()
                    customer_id = customer_id_entry.get()
                    mycursor.execute("SELECT * FROM invoice WHERE order_id = %s AND customer_id = %s", (order_id, customer_id))
                    invoice_data = mycursor.fetchall()

                    invoice_window = Toplevel(newWindow)
                    invoice_window.geometry('800x500')
                    invoice_window.title('Invoice')

                    invoice_window.iconbitmap('icon.ico')

                    item_id = Label(invoice_window, text='ITEM ID')
                    item_id.grid(row=0, column=0)

                    or_id = Label(invoice_window, text='ORDER ID')
                    or_id.grid(row=0, column=1)

                    cust_id = Label(invoice_window, text='CUSTOMER ID')
                    cust_id.grid(row=0, column=2)

                    inv_date = Label(invoice_window, text='INVOICE DATE')
                    inv_date.grid(row=0, column=3)

                    t_amt = Label(invoice_window, text='TOTAL AMOUNT')
                    t_amt.grid(row=0, column=4)

                    i = 1
                    for x in invoice_data:
                        for j in range(len(x)):
                            e = Entry(invoice_window, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, x[j])
                        i = i + 1

                order_id_label = Label(view_order_window, text='Enter Order ID:')
                order_id_label.grid(row=0, column=0)
                order_id_entry = Entry(view_order_window)
                order_id_entry.grid(row=0, column=1)

                customer_id_label = Label(view_order_window, text='Enter Customer ID:')
                customer_id_label.grid(row=1, column=0)
                customer_id_entry = Entry(view_order_window)
                customer_id_entry.grid(row=1, column=1)

                bt = Button(view_order_window, text='SHOW PAYMENT', command=payment)
                bt.grid(row=2, column=0, columnspan=2)

                bt = Button(view_order_window, text='SHOW SHIPMENT', command=shipment)
                bt.grid(row=3, column=0, columnspan=3)

                bt = Button(view_order_window, text='SHOW INVOICE', command=invoice)
                bt.grid(row=4, column=0, columnspan=4)

        def add_order_():
            add_order_window = Toplevel(newWindow)
            add_order_window.geometry('800x500')
            add_order_window.title('Add Order')

            add_order_window.iconbitmap('icon.ico')

            l1 = Label(add_order_window, text="Enter Item Id")
            l1.place(x=20, y=20)

            l1 = Label(add_order_window, text="Enter Customer Id")
            l1.place(x=20, y=80)

            l1 = Label(add_order_window, text="Enter Supplier Id")
            l1.place(x=20, y=140)

            l1 = Label(add_order_window, text="Enter Order Date")
            l1.place(x=20, y=200)

            l1 = Label(add_order_window, text="Enter Order Quantity")
            l1.place(x=20, y=260)

            l1 = Label(add_order_window, text="Enter Total Price")
            l1.place(x=20, y=320)

            e1 = Entry(add_order_window)
            e1.place(x=200, y=20)

            e2 = Entry(add_order_window)
            e2.place(x=200, y=80)

            e3 = Entry(add_order_window)
            e3.place(x=200, y=140)

            e4 = Entry(add_order_window)
            e4.place(x=200, y=200)

            e5 = Entry(add_order_window)
            e5.place(x=200, y=260)

            e6 = Entry(add_order_window)
            e6.place(x=200, y=320)

            bt = Button(add_order_window, text='INSERT ORDER', command=lambda: insert_order_(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()))
            bt.place(x=300, y=380)

        def insert_order_(item_id, cust_id, supp_id, or_date, or_quan, t_price):
            mycursor.execute('insert into order_(item_id, customer_id, supplier_id, order_date, order_quantity, total_price) values(%s, %s, %s, %s, %s, %s)', (item_id, cust_id, supp_id, or_date, or_quan, t_price))
            mydb.commit()

        def remove_order_():
            remove_order_window = Toplevel(newWindow)
            remove_order_window.geometry('800x500')
            remove_order_window.title('Remove Order')

            remove_order_window.iconbitmap('icon.ico')

            l1 = Label(remove_order_window, text="Enter Order ID to be deleted: ")
            l1.place(x=20, y=20)

            e1 = Entry(remove_order_window)
            e1.place(x=200, y=20)

            bt = Button(remove_order_window, text='DELETE ORDER', command=lambda: delete_order_(e1.get()))
            bt.place(x=60, y=80)

        def delete_order_(or_id):
            mycursor.execute('delete from order_ where order_id=%s', (or_id,))
            mydb.commit()

        def customer():
            customer_window = Toplevel(newWindow)
            customer_window.geometry('800x500')
            customer_window.title('Customer')

            customer_window.iconbitmap('icon.ico')

            cust_id = Label(customer_window, text='CUSTOMER ID')
            cust_id.grid(row=0, column=0)

            supp_id = Label(customer_window, text='SUPPLIER ID')
            supp_id.grid(row=0, column=1)

            cust_name = Label(customer_window, text='CUSTOMER NAME')
            cust_name.grid(row=0, column=2)

            cust_phone = Label(customer_window, text='CUSTOMER PHONE')
            cust_phone.grid(row=0, column=3)

            cust_email = Label(customer_window, text='CUSTOMER EMAIL')
            cust_email.grid(row=0, column=4)

            cust_add = Label(customer_window, text='CUSTOMER ADDRESS')
            cust_add.grid(row=0, column=5)

            mycursor.execute("SELECT * FROM customer WHERE supplier_id=%s", (supplier_id,))
            i = 1
            for x in mycursor.fetchall():
                for j in range(len(x)):
                    e = Entry(customer_window, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, x[j])
                i = i + 1

            bt = Button(customer_window, text='ADD CUSTOMER', command=lambda: add_customer())
            bt.grid(row=1, column=6)

            bt = Button(customer_window, text='DELETE CUSTOMER', command=lambda: remove_customer())
            bt.grid(row=2, column=6)

        def add_customer():
            add_customer_window = Toplevel(newWindow)
            add_customer_window.geometry('800x500')
            add_customer_window.title('Add Customer')

            add_customer_window.iconbitmap('icon.ico')

            l1 = Label(add_customer_window, text="Enter Supplier Id")
            l1.place(x=20, y=20)

            l1 = Label(add_customer_window, text="Enter Customer Name")
            l1.place(x=20, y=80)

            l1 = Label(add_customer_window, text="Enter Customer PhoneNo.")
            l1.place(x=20, y=140)

            l1 = Label(add_customer_window, text="Enter Customer Email")
            l1.place(x=20, y=200)

            l1 = Label(add_customer_window, text="Enter Customer Address")
            l1.place(x=20, y=260)

            e1 = Entry(add_customer_window)
            e1.place(x=200, y=20)

            e2 = Entry(add_customer_window)
            e2.place(x=200, y=80)

            e3 = Entry(add_customer_window)
            e3.place(x=200, y=140)

            e4 = Entry(add_customer_window)
            e4.place(x=200, y=200)

            e5 = Entry(add_customer_window)
            e5.place(x=200, y=260)

            bt = Button(add_customer_window, text='INSERT CUSTOMER', command=lambda: insert_customer(e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
            bt.place(x=300, y=320)

        def insert_customer(supp_id, cust_name, cust_phone, cust_email, cust_add):
            mycursor.execute('INSERT INTO customer(supplier_id, customer_name, customer_phoneno, customer_email, customer_address) VALUES(%s,%s,%s,%s,%s)', (supp_id, cust_name, cust_phone, cust_email, cust_add))
            mydb.commit()

        def remove_customer():
            remove_customer_window = Toplevel(newWindow)
            remove_customer_window.geometry('800x500')
            remove_customer_window.title('Remove Customer')

            remove_customer_window.iconbitmap('icon.ico')

            l1 = Label(remove_customer_window, text="Enter Customer ID to be deleted: ")
            l1.place(x=20, y=20)

            e1 = Entry(remove_customer_window)
            e1.place(x=200, y=20)

            bt = Button(remove_customer_window, text='DELETE CUSTOMER', command=lambda: delete_customer(e1.get()))
            bt.place(x=60, y=80)

        def delete_customer(cust_id):
            mycursor.execute('delete from customer where customer_id=%s', (cust_id,))
            mydb.commit()

        newWindow = Tk()
        newWindow.geometry('800x500')
        newWindow.title('Show Inventory')

        newWindow.iconbitmap('icon.ico')

        bt = Button(newWindow, text="SHOW PRODUCTS", command=product)
        bt.place(x=20, y=20)

        bt = Button(newWindow, text='SHOW ORDERS', command=order_)
        bt.place(x=150, y=20)

        bt = Button(newWindow, text='SHOW CUSTOMERS', command=customer)
        bt.place(x=280, y=20)

    else:
        print(mycursor.rowcount)
        MessageBox.showwarning('Error', 'Invalid login credentials!')


root = Tk()
root.geometry("600x300")
root.title('Inventory Management System')

root.iconbitmap('icon.ico')

background_image = PhotoImage(file="1st.png")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

supplier_id = Label(root, text="Enter Supplier ID: ")
supplier_id.place(x=20, y=20)

password = Label(root, text="Enter Supplier password: ")
password.place(x=20, y=50)

supplier_id_entry = Entry(root)
supplier_id_entry.place(x=150, y=20)

supplier_password_entry = Entry(root, show='*')
supplier_password_entry.place(x=200, y=50)

login_button = Button(root, text="LOGIN", command=login_user, height=2, width=7)
login_button.place(x=170, y=130)

root.mainloop()