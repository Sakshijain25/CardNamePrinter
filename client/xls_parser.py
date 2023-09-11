# import pandas lib as pd
import pandas as pd
import os, sys
from optparse import OptionParser
import json
import time

from name_printer import add_text_to_pdf
from cordinate_extractor import extract_cordinate
from sender import Sender

def Conversion(short_card, big_card, xlsPath, output_folder, contacts_path):
    short_x, short_y = extract_cordinate(short_card, 'To,')
    big_x, big_y = extract_cordinate(big_card, 'To,')

    with open(contacts_path, 'r') as json_file:
        contacts = json.load(json_file)
    # read by default 1st sheet of an excel file
    data_frame = pd.read_excel(xlsPath, 'Sheet3')
    data_frame.fillna('', inplace = True)
    sheet = data_frame.to_dict()
    # sender_obj = Sender()
    time.sleep(2)
    not_found = []
    for inx in range(data_frame.shape[0]):
        content = data_frame.iloc[inx].to_dict()
        if not content['mobile no.']:
            print("No number found : ", content['Name of Family'])
            not_found.append(content['Name of Family'])
            continue
        # name = contacts.get(str(int(content['mobile no.'])),'')
        name = content['mobile no.']
        if name:
            os.mkdir(os.path.join(output_folder,str((content['mobile no.']))))
            if content['Big Card']:
                output_pdf_path = os.path.join(output_folder,str((content['mobile no.'])), 'Choudhary_invitation'+'.pdf')
                add_text_to_pdf(big_card, output_pdf_path, content, big_x, big_y)
            else:
                output_pdf_path = os.path.join(output_folder, str((content['mobile no.'])), 'Choudhary_invitation'+'.pdf')
                add_text_to_pdf(short_card, output_pdf_path, content, short_x, short_y)
            # ret = sender_obj.send(name, output_pdf_path)
            # if ret == False:
            #     not_found.append([name, content['mobile no.']])
        else:
            not_found.append(int(content['mobile no.']))

        with open("contacts_not_found.json", "w") as outfile:
            json.dump(not_found, outfile, indent=4)
