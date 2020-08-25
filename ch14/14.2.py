import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue
    print('Removing header from ' + csv_filename + '...')

    csv_rows = []
    csv_fileobj = open(csv_filename)
    reader_obj = csv.reader(csv_filename)
    for row in reader_obj:
        if reader_obj.line_num == 1:
            continue
        csv_rows.append(row)
    csv_fileobj.close()


    csv_fileobj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
    csv_writer = csv.writer(csv_fileobj)
    for row in csv_rows:
        csv_writer.writerow(row)
    csv_fileobj.close()
