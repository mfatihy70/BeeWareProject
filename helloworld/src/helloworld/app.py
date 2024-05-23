from toga import *
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga.constants import Direction

from helloworld.widgets import comps, menu_group
from helloworld.orders import send, get


from toga import OptionContainer, OptionItem

class HelloWorld(App):
    def startup(self):
        send_box = Box(style=Pack(direction=COLUMN, padding_top=10, padding_left=10, padding_right=10, padding_bottom=10))
        get_box = Box(style=Pack(direction=COLUMN, padding_top=10, padding_left=10, padding_right=10, padding_bottom=10))

        option_container = OptionContainer(
            content=[
                OptionItem('Send Order', send_box),
                OptionItem('Show Orders', get_box),
            ]
        )

        self.main_window = MainWindow(title=self.formal_name)
        self.main_window.content = option_container
        self.main_window.show()

        send(self.main_window, send_box)
        get(self.main_window, get_box)

def main():
    return HelloWorld()