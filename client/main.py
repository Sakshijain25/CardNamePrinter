from xls_parser import Conversion

def main():
    short_card = "D:\Sakshi\weddinginvitation\input\Wedding Invitation Short.pdf"    # Replace with the actual path of the input PDF
    big_card = "D:\Sakshi\weddinginvitation\input\Wedding Invitation Full.pdf"
    dataset_path = "D:\Sakshi\weddinginvitation\input\Cards List.xlsx"  # Replace with the desired output path
    output_folder = "D:\Sakshi\weddinginvitation\output"
    contacts = "D:\Sakshi\weddinginvitation\input\contacts.json"
    Conversion(short_card, big_card, dataset_path, output_folder, contacts)


if __name__ == "__main__":
    main()
