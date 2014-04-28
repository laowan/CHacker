import os

def code_count(path):
    print path
    file_count = 0
    line_count = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            ext = file[file.find('.'):]
            if ext in ['.cpp', '.c', '.hpp', '.h']:
                file_count += 1
                file_path = root + '\\' + file
                fp = open(file_path)
                line_count += len(fp.readlines())
                fp.close()

    print file_count
    print line_count