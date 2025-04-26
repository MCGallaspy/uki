import dearpygui.dearpygui as dpg


def import_from_lift(sender, app_data, user_data):
    app_state, import_callback = user_data
    
    with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=set_selected_lift_filename,
            id="lift_filename_dialog",
            width=700,
            height=400,
        ):
        dpg.add_file_extension(".lift", color=(0, 255, 255, 255))

    with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=set_selected_flextext_filename,
            id="flextext_filename_dialog",
            width=700,
            height=400,
        ):
        dpg.add_file_extension(".flextext", color=(0, 255, 255, 255))

    with dpg.window(
            label="LIFT Import",
            tag="import_from_lift",
            on_close=on_close,
            width=400,
            height=200,
        ):
        with dpg.group(horizontal=True):
            dpg.add_text("LIFT File:")
            dpg.add_text("", tag="lift_filename")
            dpg.add_button(
                label="Choose file",
                callback=lambda: dpg.show_item(item="lift_filename_dialog"),
            )
        with dpg.group(horizontal=True):
            dpg.add_text("Flextext File:")
            dpg.add_text("", tag="flextext_filename")
            dpg.add_button(
                label="Choose file",
                callback=lambda: dpg.show_item(item="flextext_filename_dialog"),
            )
        
        def import_callback_wrapper(sender, app_data, user_data):
            lift_filename = dpg.get_value(item="lift_filename")
            flextext_filename = dpg.get_value(item="flextext_filename")
            on_close()
            return import_callback(app_state, lift_filename, flextext_filename)

        dpg.add_button(
            label="Import",
            callback=import_callback_wrapper,
        )


def on_close():
    dpg.delete_item("import_from_lift")
    dpg.delete_item("lift_filename_dialog")
    dpg.delete_item("flextext_filename_dialog")


def set_selected_lift_filename(sender, app_data, user_data):
    dpg.set_value(item="lift_filename", value=app_data['file_path_name'])


def set_selected_flextext_filename(sender, app_data, user_data):
    dpg.set_value(item="flextext_filename", value=app_data['file_path_name'])