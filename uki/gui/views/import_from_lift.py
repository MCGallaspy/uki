import dearpygui.dearpygui as dpg


def import_from_lift(sender, app_data, user_data):
    def on_close():
        dpg.delete_item("import_from_lift")
        dpg.delete_item("lift_file_dialog")
        dpg.delete_item("flextext_file_dialog")

    with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=set_selected_lift_file,
            id="lift_file_dialog",
            width=700,
            height=400,
        ):
        dpg.add_file_extension(".*")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension("Source files (*.cpp *.h *.hpp){.cpp,.h,.hpp}", color=(0, 255, 255, 255))
        dpg.add_file_extension(".h", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".py", color=(0, 255, 0, 255), custom_text="[Python]")
    dpg.add_file_dialog(
        directory_selector=False,
        show=False,
        callback=set_selected_lift_file,
        tag="flextext_file_dialog",
        width=700,
        height=400,
    )

    with dpg.window(
            label="LIFT Import",
            tag="import_from_lift",
            on_close=on_close,
            width=400,
            height=200,
        ):
        with dpg.group(horizontal=True):
            dpg.add_text("LIFT File:")
            dpg.add_text("", tag="lift_file")
            dpg.add_button(
                label="Choose file",
                callback=lambda: dpg.show_item(item="lift_file_dialog"),
            )


def set_selected_lift_file(sender, app_data, user_data):
    print(app_data)
    dpg.set_value(item="lift_file", value="Foo")