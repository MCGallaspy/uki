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
        for lexeme in session.query(Lexeme):
            print(lexeme)