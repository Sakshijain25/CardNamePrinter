import pandas as pd
import json

def simplify_contacts(contact_file):
    data_frame = pd.read_excel(contact_file, 'in')
    data_frame.fillna('', inplace = True)
    sheet = data_frame.to_dict()
    # import pdb; pdb.set_trace()
    data = {}
    for inx in range(data_frame.shape[0]):
        content = data_frame.iloc[inx].to_dict()
        name = str(content['First Name']).strip() + ' ' + str(content['Middle Name']).strip() + ' ' + str(content['Last Name']).strip()
        name = name.strip()
        number = str(content['Mobile Phone'])
        number = clean_number(number)
        if len(number) == 10:
            if number in data:
                print(name)
            data[number] = name
        else:
            print("Incorrect Number "+ number)

        number = str(content['Home Phone'])
        number = clean_number(number)
        if len(number) == 10:
            if number in data:
                print(name)
            data[number] = name
        number = str(content['Home Phone 2'])
        number = clean_number(number)
        if len(number) == 10:
            if number in data:
                print(name)
            data[number] = name

    with open("contacts.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

def clean_number(number):
    number = number.split('.')[0]
    number = number.replace(' ','')
    number = number.replace('-','')
    number = number.replace('+','')
    if len(number) > 10:
        number = number[2:]
    return number


contacts = "D:\Sakshi\weddinginvitation\input\contacts.xlsx"
simplify_contacts(contacts)