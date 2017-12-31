f = open('tmpfile2.csv','w')

for i in range(1000):
    for j in range(1000):
        f.write(str(i) + ',' + str(j) + '\n')

f.close()
