import CSV
with open ('us500.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
