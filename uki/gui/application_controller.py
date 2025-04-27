import xml.etree.ElementTree as ET

from sqlalchemy.orm.session import Session
from typing import List

from uki.gui.application_state import ApplicationState
from uki.orm.lexeme import Lexeme
from uki.orm.surface_form import SurfaceForm
from uki.orm.sense import Sense


def load_lift_data(
        app_state: ApplicationState,
        lift_filename: str,
        flextext_filename: str = None,
    ):
    
    tree = ET.parse(lift_filename)
    root = tree.getroot()
    with Session(app_state.engine) as session, session.begin():
        for entry in root.findall('entry'):
            lexeme_form = entry.find('./lexical-unit/form')
            lemma = lexeme_form.find('text').text
            morpheme_type = entry.find('./trait[@name="morph-type"]').attrib['value']

            lexeme = Lexeme(
                lemma=lemma,
                morpheme_type=morpheme_type,
            )
            session.add(lexeme)
            
            session.add(SurfaceForm(form=lemma, lexeme=lexeme))
            for variant_form in entry.findall('./variant/form/text'):
                session.add(SurfaceForm(form=variant_form.text, lexeme=lexeme))

            for sense in entry.findall('sense'):
                gloss = sense.find('./gloss/text').text
                grammatical_info = sense.find('grammatical-info')
                part_of_speech = "NULL"
                if grammatical_info is not None:
                    part_of_speech = grammatical_info.attrib['value']
                    part_of_speech = f"'{part_of_speech}'"
                session.add(Sense(gloss=gloss, lexeme=lexeme))
                for trait in sense.findall('./grammatical-info/trait'):
                    name = trait.attrib['name']
                    value = trait.attrib['value']
        
        session.commit()
        
        if flextext_filename:
            print(f"flextext_filename: {flextext_filename}")
    


'''
tree = ET.parse(texts_file)
root = tree.getroot()
for text in root.findall('interlinear-text'):
    title = root.find(".//item[@type='title']").text
    
    word_values = []
    for narrative_order, word in enumerate(text.findall('.//word')):
        word_values.append([title, narrative_order, word.find('./item').text])
    cur.executemany(f"INSERT INTO texts VALUES (NULL, ?, ?, ?)", word_values)
    con.commit()

    morpheme_values = []
    for narrative_order, word in enumerate(text.findall('.//word')):
        query = f"SELECT rowid FROM texts WHERE text_name='{title}' AND narrative_order={narrative_order}"
        textid = cur.execute(query).fetchone()[0]
        for morpheme_order, morph in enumerate(word.findall('.//morph')):
            gloss = morph.find("./item[@type='gls']")
            spelling = morph.find("./item[@type='txt']")
            if (gloss is None) or (spelling is None):
                continue
            gloss = gloss.text
            gloss = gloss.replace("=", "")
            gloss = gloss.replace("*", "")
            gloss = gloss.replace("-", "")
            spelling = spelling.text
            query = f"""SELECT spellings.rowid AS spellingid
                        FROM spellings, senses
                        WHERE spellings.lexeme=senses.lexeme
                          AND senses.gloss='{gloss}' AND spellings.form='{spelling}'"""
            try:
                spellingid = cur.execute(query).fetchone()[0]
                morpheme_values.append([spellingid, textid, morpheme_order])
            except Exception as e:
                print(query)
                print(e)
    cur.executemany(f"INSERT INTO text_morphemes VALUES (NULL, ?, ?, ?)", morpheme_values)
    con.commit()
'''