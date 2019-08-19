import csv
# Import CSV data
def getCSVData(fileName):
    rows = []
    # open the CSV file
    datafile = open(fileName, "r")
    # create a CSV reader from the file
    reader = csv.reader(datafile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows