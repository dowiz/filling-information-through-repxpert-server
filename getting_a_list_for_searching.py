import openpyxl


def getting_list():
    wb = openpyxl.load_workbook(
        r"Y:\Temp.Документи\EXPORT AGIS\import goods from agis.xlsx")

    sheet = wb["for export to prom"]

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] and row[18] and row[24]:
            data.append([row[24], row[0], row[18]])

    return data
