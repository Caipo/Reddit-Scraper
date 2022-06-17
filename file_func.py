import os
import csv
import shutil

'''Writes an array to a csv file'''
def csv_write(data, file_name):


    for fields in data:

        with open(file_name, 'a', encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(fields.values())
    f.close()

        
'''Will use to store data '''
def make_file(file_name):
    
    
    if os.path.exists(file_name):
        append_write = 'w' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    file = open(file_name, append_write)
    file.close()

    return(file_name)


def make_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
            
    else:
        shutil.rmtree(path)
        os.makedirs(path)

