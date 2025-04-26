import dearpygui.dearpygui as dpg

from sqlalchemy.engine import Engine

from uki.gui.application_state import ApplicationState
from uki.gui.application_controller import initialize_database_engine
from uki.gui.views.import_from_lift import import_from_lift


def main():
    APPLICATION_STATE = ApplicationState()
    engine: Engine = initialize_database_engine(APPLICATION_STATE)
    dpg.create_context()

    with dpg.window(label="Ukiʔ") as primary_window:
        dpg.set_primary_window(primary_window, True)

        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="Import from LIFT",
                    callback=import_from_lift,
                )

    dpg.create_viewport(title='Ukiʔ', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()