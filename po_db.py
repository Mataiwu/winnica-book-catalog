#do the importing first
import format_cell_data



def make_it_happen():
    wb=openpyxl.load_workbook('data-preparation.xlsx')
    sheet=wb.get_sheet_by_name('Sheet1')
    for r in range(303):
        title=sheet.cell(row=r, column=1).value
        authors=sheet.cell(row=r, column=2).value
        published=sheet.cell(row=r, column=3).value
        publsiher=sheet.cell(row=r, column=4).value
        cathegory=sheet.cell(row=r, column=5).value
        translators=sheet.cell(row=r, column=6).value
        isbn=sheet.cell(row=r, column=7).value
        regal=sheet.cell(row=r, column=8).value
        shelf=sheet.cell(row=r, column=9).value
        language=sheet.cell(row=r, column=10).value


        authors_list=get_names(authors)

        for author in author_list:
            l_name, f_name=get_last_first(author)
            author, created=Author.objects.get_or_create(first_name=f_name,
                                                        last_name=l_name)

        if translator==None:
            continue
        else:

            translators_list=get_names(authors)
            for translator in translator_list:
                l_name, f_name=get_last_first(translator)

                translator, created=Translator.objects.get_or_create(
                                                    first_name=f_name,
                                                    last_name=l_name
                                                    )

        regal, created=Translator.objects.get_or_create(name=regal)
        #remember to add regal object
        book=Book.objects.create(title=title, author=author, published=published,
                    publisher=publisher, translator=translator, isbn=isbn,
                    Language=language, cathegory=cathegory, regal=regal,
                    shelf=shelf)
        book.save()
