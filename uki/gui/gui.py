import dearpygui.dearpygui as dpg

from sqlalchemy.engine import Engine

from uki.gui.application_state import ApplicationState
from uki.gui.application_controller import initialize_database_engine

APPLICATION_STATE = ApplicationState()
engine: Engine = initialize_database_engine(APPLICATION_STATE)

dpg.create_context()

with dpg.window(label="Tutorial"):

    # configuration set when button is created
    dpg.add_button(label="Apply", width=300)

    # user data and callback set any time after button has been created
    btn = dpg.add_button(label="Apply 2")
    dpg.set_item_label(btn, "Button 57")
    dpg.set_item_width(btn, 200)

dpg.show_item_registry()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()