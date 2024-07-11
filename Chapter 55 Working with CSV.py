import csv

with open('test.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=';', lineterminator='\n')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([5423, 'bogdan', 1300])
    writer.writerow([5425, 'alice', 830])
    writer.writerow([7245, 'alex', 970])


with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)