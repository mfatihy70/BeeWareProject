from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from toga import *

def comps(mw, box):
    input = TextInput()
    label = Label("Hello World!")
    
    def hello(widget): label.text = f"Hello {input.value}!"
    def greet(widget): mw.info_dialog(f"Hello, {input.value}", "Hi there!")

    widgets = [
        input, 
        label,
        Button("Print Hello!", on_press=hello),
        Button("Greet!", on_press=greet),
        ProgressBar(max=100, value=50),
        NumberInput(min=0, max=100, step=1, value=50),
        PasswordInput(),
        Selection(items=['One', 'Two', 'Three', 'Four', 'Five']),
        DateInput(),
        Divider(),
        Slider(min=0, max=100, value=50),
        Switch(text="On/Off", on_change=None),
        Table(
            style=Pack(flex=1),
            headings=["Name", "Age", "Planet"],
            data=[
                {"name": "Arthur Dent", "age": 42, "planet": "Earth"},
                {"name": "Ford Prefect", "age": 37, "planet": "Betelgeuse Five"},
                {"name": "Tricia McMillan", "age": 38, "planet": "Venus"},
            ]  
        ),
        MultilineTextInput(placeholder="Write your text here..."),
        DetailedList(
            style=Pack(flex=1),
            data=[
                {
                "icon": Icon("../../icons/car"),
                "title": "Arthur Dent",
                "subtitle": "Where's the tea?"
                },
                {
                "icon": Icon("../../icons/castle"),
                "title": "Ford Prefect",
                "subtitle": "Do you know where my towel is?"
                },
                {
                "icon": Icon("../../icons/human"),
                "title": "Tricia McMillan",
                "subtitle": "What planet are you from?"
                },
            ]
        )
    ]

    for widget in widgets:
        widget.style.update(padding=5)
        box.add(widget)    
    

def menu_group(mw, commands):
    action0 = lambda widget: mw.info_dialog('Info', 'Hello World')
    action1 = lambda widget: mw.question_dialog('Option', 'Hello World')
        
    group = Group('Own Menu')
    cmd0 = Command(action0, 'Info Popup', group=group)
    cmd1 = Command(action1, 'Yes or No', group=group)
    commands.add(cmd0, cmd1)
    return group