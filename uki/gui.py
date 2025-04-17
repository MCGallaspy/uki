import dearpygui.dearpygui as dpg

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from uki.flex_utils import import_lift_lexicon
from uki.orm import UkiʔBase

dpg.create_context()
dpg.create_viewport(title='Ukiʔ', width=800, height=600)

engine = create_engine("sqlite:///:memory:", echo=True)
UkiʔBase.metadata.create_all(engine)

with dpg.window(label="Ukiʔ"):
    with Session(engine) as session, session.begin():
        lexemes = import_lift_lexicon("xml/xml.lift")
        session.add_all(lexemes)
        session.flush()
        for lexeme in lexemes:
            print(lexeme)
            print(lexeme.surface_forms)
    
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()