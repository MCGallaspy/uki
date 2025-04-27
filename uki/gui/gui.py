import dearpygui.dearpygui as dpg

from uki.gui.application_state import ApplicationState
from uki.gui.application_controller import load_lift_data
from uki.gui.views.import_from_lift import import_from_lift
from uki.gui.views.lexicon import toggle_show_lexicon


def main():
    APPLICATION_STATE = ApplicationState(
        sql_alchemy_url="sqlite:///test.db"
    )
    dpg.create_context()

    with dpg.window(
            label="Lexicon",
            tag="lexicon-window",
            show=False,
            on_close=lambda: dpg.set_value("lexicon-visible-checkbox", False),
        ):
        pass

    with dpg.window(label="Ukiʔ") as primary_window:
        dpg.set_primary_window(primary_window, True)

        with dpg.viewport_menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="Import from LIFT",
                    callback=import_from_lift,
                    user_data=(APPLICATION_STATE, load_lift_data),
                )
            with dpg.menu(label="View"):
                dpg.add_checkbox(
                    label="Lexicon",
                    tag="lexicon-visible-checkbox",
                    callback=toggle_show_lexicon,
                    user_data=(APPLICATION_STATE, "lexicon-window"),
                )

    dpg.create_viewport(title='Ukiʔ', width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()