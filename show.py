import csv
filename = "encounter.csv"
fields = []
rows = []
 
with open(filename, 'r') as csvfil:
    csvreader = csv.reader(csvfil)
    with open("output12.csv", "w") as result:
        writer = csv.writer(result)
        for r in csvreader:
            #extracting necessary rows alone, and taking it as a separate csv. Rows like Encounter_ID, Member_ID,SOAP , etc are not needed for our cluster model
            writer.writerow((r[10], r[11], r[15], r[16], r[17],r[18],r[19],r[20],r[21],r[22],r[23],r[24])) 
            

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of rows: %d"%(csvreader.line_num))
print('Field names are:' + ', '.join(field for field in fields))

#checking whether unwanted rows are removed
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
    
