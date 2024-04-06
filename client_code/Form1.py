from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.message_label.text = "Hello "  + self.name_box.text + "!"
    anvil.server.call('say_hello', self.name_box.text)
    # Replace 'NewPage' with the name of the page you want to navigate to
    self.open_form('ItemTemplate1')

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
