
# Demendencies
# pip3 install polib google_trans_new googletrans requests


##############################################################
# There is a but in the google_trans_new package 
# inside google_trans_new.py file in translate method. 
#
# Need to change line number 151 as following
# 
# response = (decoded_line + ']') -> response = decoded_line
##############################################################


import polib
from google_trans_new import google_translator
from googletrans import Translator
import io


def read_lines(file: str) -> list:
    """ Read lines into memory. """
    return polib.pofile(file)

def translate(source: str, arguments) -> str:
    """ Translates a single string into target language. """
    translator = google_translator()
    return translator.translate(source, lang_tgt=arguments['to'], lang_src=arguments['fro'])

def save_lines(file: str, lines: list):
    """ 
    Save lines from memory into a file.
    :parameter file:
    :parameter lines:
    """
    with io.open(file, 'w', encoding='utf8') as infile:
        infile.write("""msgid "" msgstr """"")
        for keys, values in lines.metadata.items():
            infile.write(f'"{keys}:{values}"\n')
        infile.write('\n')
        for line in lines:
            infile.write(line.__unicode__())

lines = read_lines('/opt/odoo/odoo15/MIC/bista_repair_extended/i18n/fr_CA.po')
arguments = {
    'dest': '/home/gm/',
    'fro': 'en',
    'src': '/opt/odoo/odoo15/MIC/bista_repair_extended/i18n/',
    'to': 'fr_CA'
}
list = []
for line in lines:

    try:
        line.msgstr = polib.unescape(translate(polib.escape(line.msgid), arguments))
        print(f"Translated {lines.percent_translated()}% of the lines.")
    except:
        list.append(line.msgid_with_context)
        continue

save_lines('/home/gm/fr_CA.po', lines)
