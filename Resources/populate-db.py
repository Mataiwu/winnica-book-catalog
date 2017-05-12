





def assign_values():
    wb=openpyxl.load_workbook('data-preparation.xlsx')
    sheet=wb.get_sheet_by_name('Sheet1')
    for r in range(304):
        title=sheet.cell(row=r, column=1).value
        author=sheet.cell(row=r, column=2).value
        published=sheet.cell(row=r, column=3).value
        publsiher=sheet.cell(row=r, column=4).value
        cathegory=sheet.cell(row=r, column=5).value
        translators=sheet.cell(row=r, column=6).value
        isbn=sheet.cell(row=r, column=7).value
        regal=sheet.cell(row=r, column=8).value
        shelf=sheet.cell(row=r, column=9).value
        language=sheet.cell(row=r, column=10).value
