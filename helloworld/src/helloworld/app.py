from toga import *
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.constants import Direction

from helloworld.widgets import comps, menu_group
from helloworld.orderform import send_form
from helloworld.orderform import show_orders


from toga import OptionContainer, OptionItem

class HelloWorld(App):
    def startup(self):
        send_box = Box(style=Pack(direction=COLUMN, padding_top=10, padding_left=10, padding_right=10, padding_bottom=10))
        get_box = Box(style=Pack(direction=COLUMN, padding_top=10, padding_left=10, padding_right=10, padding_bottom=10))
        delete_box = Box(style=Pack(direction=COLUMN, padding_top=10, padding_left=10, padding_right=10, padding_bottom=10))

        option_container = OptionContainer(
            content=[
                OptionItem('Send Order', send_box),
                OptionItem('Show Orders', get_box),
                OptionItem('Delete Order', delete_box),
            ]
        )

        self.main_window = MainWindow(title=self.formal_name)
        self.main_window.content = option_container
        self.main_window.show()

        send_form(self.main_window, send_box)
        show_orders(self.main_window, get_box)
        # Add other components to right_inner_box here

def main():
    return HelloWorld()

def main():
    return HelloWorld()
def main():
    return HelloWorld()