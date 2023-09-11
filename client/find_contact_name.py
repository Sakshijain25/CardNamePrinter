import addressbook
import phonenumbers

def get_contact_name_by_number(number):
    contacts = addressbook.AddressBook()
    contacts.load()
    for contact in contacts.people:
        for phone_number in contact.phone_numbers:
            parsed_number = phonenumbers.parse(phone_number.number, None)
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            if formatted_number == number:
                return contact.name
    return None



contact_number = "+919462556397"  # Replace with the desired contact number
contact_name = get_contact_name_by_number(contact_number)
if contact_name:
    print("Contact Name:", contact_name)
else:
    print("Contact not found.")
