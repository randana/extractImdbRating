mport xlsxwriter

# Create a workbook and add a worksheet.

        workbook = xlsxwriter.Workbook('MovieDatabase.xlsx')
        worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
# Start from the first cell. Rows and columns are zero indexed.

# Iterate over the data and write it out row by row.

worksheet.write(foo.row, 0, "Movie RAting"   )
worksheet.write(foo.row, 1, rating)
foo.row += 1
print foo.row

workbook.close()
