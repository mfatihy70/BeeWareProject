from toga.style import Pack
from toga import *
from helloworld.order import Order
# import mysql.connector

def connect():
    pass
    # con = mysql.connector.connect(
    #     host="localhost",
    #     user="admin",
    #     password="1234",
    #     database="BeeWareDB"
    # )
    # return con


def send(mw, box):
    def send_order(inputs):
        pass
        # con = connect()
        # cursor = con.cursor()
        # values = ', '.join("'" + str(input.value) + "'" for input in inputs)
        # query = "insert into orders(name, address, number, milk, eggs, other) values(" + values + ")"
        # cursor.execute(query) 
        # con.commit() 
        # mw.info_dialog("Info", "Data is sent!")
        # cursor.close() 
        # con.close()

    def send_form():
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
            box.add(widget)


    send_form()

def get(mw,box):
    def get_orders(widget):
        pass
        # con = connect()
        # cursor = con.cursor()
        # query = "select * from orders"    
        # cursor.execute(query) 
        # table = cursor.fetchall() 
        # cursor.close() 
        # con.close()
        # return table

    def update_table(orders, table, search_text):

        orders = [
            Order(1, "John Doe", "123 Main St", "1234567890", 2, 3, "Bread"),
            Order(2, "Jane Doe", "456 Maple St", "0987654321", 1, 0, "Butter"),
            Order(3, "Jim Smith", "789 Oak St", "1122334455", 0, 2, "Cheese"),
            Order(4, "Jill Smith", "321 Pine St", "5566778899", 3, 1, "Yogurt"),
            Order(5, "Joe Johnson", "654 Elm St", "9988776655", 2, 2, "Milk")
        ]

        # if search_text:
        #     column_index = table.headings.index(selected_column)
        #     filtered_orders = [order for order in orders if search_text in order[column_index]]
        # else:
        #     filtered_orders = orders

        # table.data.clear()
        # for order in filtered_orders:
        #     table.data.append(order)

        if search_text:
            #column_index = table.headings.index(selected_column)
            filtered_orders = [order for order in orders if search_text in str(getattr(order, selected_column.lower()))]
        else:
            filtered_orders = orders

        table.data.clear()
        for order in filtered_orders:
            table.data.append(list(vars(order).values()))
            
    def show_orders():
        orders = get_orders(mw)
        search = TextInput(placeholder="Input the search keyword, leave blank for all orders")
        #col_sel_label = Label("Search by:")
        #col_selection = Selection(items=["Name", "Address", "Phone Number", "Milk", "Eggs", "Other"])
        table = Table(headings=["ID", "Name", "Address", "Phone Number", "Milk", "Eggs", "Other"], style=Pack(flex=1))
        
        on_show_press = lambda widget: update_table(orders, table, search.value)
        #on_delete_press = lambda widget: delete_order(mw, table)
        show_button = Button("Show Orders", on_press=on_show_press)
        #delete_button = Button("Delete Order", on_press=on_delete_press)
        #update_button = Button("Update Order", on_press=update_order)

        widgets = [
            search,
            #col_sel_label,
            #col_selection, 
            show_button, 
            #delete_button,
            #update_button,
            table]

        for widget in widgets:
            widget.style.update(padding=5)
            box.add(widget)

    def delete_order(widget, table):
        if table.selection:
            selected_order = table.data[table.selection[0]]
            order_id = selected_order.id

            pass
            # con = connect()
            # cursor = con.cursor()
            # query = "delete from orders where id = " + str(order_id)
            # cursor.execute(query)
            # con.commit()
            # cursor.close()
            # con.close()

            table.data.remove(selected_order)

    def update_order(widget):
        pass
        

    show_orders()