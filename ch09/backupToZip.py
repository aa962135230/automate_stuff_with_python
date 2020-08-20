import zipfile, os

def backup_to_zip(folder):
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    print("Creating %s..." % (zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    for folder_name, sub_folder_name, filenames in os.walk(folder):
        sub_folder_name
        print('Adding file in %s...' % (folder_name))
        backup_zip.write(folder_name)

    
    for filename in filenames:
        new_base = os.path.basename(folder) + "_"
        if filename.startswith(new_base) and filename.endswith('.zip'):
            continue
        backup_zip.write(os.path.join(folder_name, filename))
    
    backup_zip.close()
    print("Done")

backup_to_zip("/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch09")