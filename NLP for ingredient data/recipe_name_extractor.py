import csv


to_file = 'NLP for ingredient data/testset.csv'

fp = open('../datasets/testrecipes.csv', 'r')
fx = open(to_file, 'w', newline='')

reader = csv.reader(fp)
writer = csv.writer(fx)

for row in reader:
    dish_name = row[0].split('/')[-1].replace('-', ' ')
    dish_name = dish_name.split('.')[0]
    writer.writerow([row[0],dish_name, row[1]])


fp.close()
fx.close()