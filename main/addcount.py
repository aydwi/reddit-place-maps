import csv

tmplist = []
endlist = []

tmpdict = {}

with open('tmpfile1.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
    for rows in readcsv:
        tmplist.append(tuple(list(map(int, rows))))

for r in tmplist:
    if r in tmpdict:
        tmpdict[r] = tmpdict[r] + 1
    else:
        tmpdict[r] = 1

fin = tuple(tmpdict.items())

for i in fin:
    i = i[0] + (i[1],)
    endlist.append(i)

endtup = tuple(endlist)

with open("tmpfile4.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(endtup)
