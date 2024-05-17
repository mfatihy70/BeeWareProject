from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga import *

import mysql.connector

def connect():
    con = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="1234",
        database="BeeWareDB"
    )
    return con
     

def get_orders(widget):
    con = connect()
    cursor = con.cursor()
    query = "select * from orders"    
    cursor.execute(query) 
    table = cursor.fetchall() 
    cursor.close() 
    con.close()
    return table


def send_order(mw, inputs):
    con = connect()
    cursor = con.cursor()
    values = ', '.join("'" + str(input.value) + "'" for input in inputs)
    query = "insert into orders(name, address, number, milk, eggs, other) values(" + values + ")"
    cursor.execute(query) 
    con.commit() 
    mw.info_dialog("Info", "Data is sent!")
    cursor.close() 
    con.close()


def delete_order():
    con = connect()
    cursor = con.cursor()
    query = "delete from orders where name"    
    cursor.execute(query) 
    con.commit() 
    cursor.close() 
    con.close()


def send_form(mw, box):
    inputs = [
        TextInput(),  
        TextInput(),  
        NumberInput(),
        NumberInput(),
        NumberInput(),
        TextInput()  
    ]

    labels = [
        Label("Name"), # TODO save locally for auto fill
        Label("Address"), # TODO save locally for auto fill
        Label("Number"), # TODO save locally for auto fill
        Label("Milk"),
        Label("Egg"),
        Label("Other")
    ]


    widgets = []
    for label, input in zip(labels, inputs):
        widgets.append(label)
        widgets.append(input)

    widgets.append(Button("Send", on_press=lambda widget: send_order(mw, inputs)))
    
    for widget in widgets:
        widget.style.update(padding=5)
        widget.style.update(flex=1)
        box.add(widget)


def update_table(orders, table, search_text):
    if search_text:
        filtered_orders = [order for order in orders if search_text in order]
    else:
        filtered_orders = orders

    table.data.clear()
    for order in filtered_orders:
        table.data.append(order)


def show_orders(mw, box):
    orders = get_orders(widget=None)
    search = TextInput(style=Pack(padding=5))

    # Create a table with column names corresponding to your order data
    table = Table(headings=["ID", "Name", "Address", "Phone Number", "Milk", "Eggs", "Other"], style=Pack(padding=5))

    update_table(orders, table, search.value)

    def on_show_button_press(widget):
        update_table(orders, table, search.value)

    show_button = Button("Show Orders", on_press=on_show_button_press)

    box.add(search)
    box.add(show_button)
    box.add(table)
