import dearpygui.dearpygui as dpg

from sqlalchemy.orm.session import Session

from uki.gui.application_state import ApplicationState
from uki.orm.lexeme import Lexeme


def toggle_show_lexicon(sender, app_data, user_data):
    app_state, container_tag = user_data
    if dpg.is_item_shown(container_tag):
        dpg.hide_item(container_tag)
    else:
        make_lexicon(app_state, container_tag)
        dpg.show_item(container_tag)


def make_lexicon(app_state: ApplicationState, container_tag: str):

    with Session(app_state.engine) as session:
        with dpg.table(header_row=True, label="lexicon_view", sortable=True, parent=container_tag):
            dpg.add_table_column(label="Lexeme")
            dpg.add_table_column(label="Senses")
            dpg.add_table_column(label="Surface Forms")
            for lexeme in session.query(Lexeme):
                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_text(lexeme.lemma)
                    with dpg.table_cell():
                        dpg.add_text("; ".join([s.gloss for s in lexeme.senses]))
                    with dpg.table_cell():
                        dpg.add_text("; ".join([s.form for s in lexeme.surface_forms]))