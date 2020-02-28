from tabula import read_pdf



def parse(pdf_file):
    df = read_pdf(pdf_file, encoding='big5', pages='all')
    print(df)


if __name__ == "__main__":
    test_pdf_file = "./data/building_list_chi.pdf"
    parse(test_pdf_file)