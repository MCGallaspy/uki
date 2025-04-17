import xml.etree.ElementTree as ET

from typing import Optional

from uki.orm import Lexeme, Sense, SurfaceForm


def import_lift_lexicon(
    filename: str,
    flextexts_filename: Optional[str] = None,
):
    with open(filename, "rb") as f:
        tree = ET.parse(f)
    
    lexemes = []
    root = tree.getroot()
    for entry in root.findall('entry'):
        lexeme_form = entry.find('./lexical-unit/form')
        lemma = lexeme_form.find('text').text
        morpheme_type = entry.find('./trait[@name="morph-type"]').attrib['value']
        lexemes.append(Lexeme(lemma=lemma, morpheme_type=morpheme_type))
        lexeme = lexemes[-1]
        lexeme.surface_forms.add(SurfaceForm(form=lemma))
        for variant_form in entry.findall('./variant/form/text'):
            lexeme.surface_forms.add(SurfaceForm(form=variant_form.text))
        
        '''
        for sense in entry.findall('sense'):
            gloss = sense.find('./gloss/text').text
            grammatical_info = sense.find('grammatical-info')
            part_of_speech = "NULL"
            if grammatical_info is not None:
                part_of_speech = grammatical_info.attrib['value']
                part_of_speech = f"'{part_of_speech}'"
            cur.execute(f"INSERT INTO senses VALUES (NULL, '{gloss}', {lexeme_id}, {part_of_speech})")
            con.commit()
            sense_id = cur.lastrowid
            for trait in sense.findall('./grammatical-info/trait'):
                name = trait.attrib['name']
                value = trait.attrib['value']
                cur.execute(f"INSERT INTO sense_grammatical_info VALUES ('{name}', '{value}', {lexeme_id})")
            con.commit()

    if texts_file:
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
    return lexemes
