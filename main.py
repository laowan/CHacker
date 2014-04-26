import os

source_path = './data/'
database = {}

def parse_line(line):
    if line.find('OmMethodSet') < 0:
        return
    left_bracket_idx = line.find('(')
    right_bracket_idx = line.find(')')
    line = line[left_bracket_idx+1:right_bracket_idx]
    data = line.split(',')
    list = [data[1].strip(), data[2].strip()]
    if len(data) == 3:
        if not database.has_key(data[0].strip()):
            database[data[0].strip()] = []
        database[data[0].strip()].append(list)

def parse_file(filename):
    fp = open(filename)

    lines = fp.readlines()

    line_is_valid = True
    init_func_is_found = False

    for line in lines:
        line = line.strip()

        # ignore the comments
        if line[:2] == '//':
            continue
        if line[:2] == '/*':
            line_is_valid = False
            continue
        if line[len(line)-2:] == '*/':
            line_is_valid = True
            continue

        if line_is_valid:
            if line.find('void') >= 0 and line.find('init'):
                init_func_is_found = True
                continue

            if init_func_is_found:
                if line[:1] == '}':
                    init_func_is_found = False
                    continue

                # now parse the OmMethodSet function
                if init_func_is_found:
                    parse_line(line);
    fp.close()

if __name__ == "__main__":
    for name in  os.listdir(source_path):
        filename = source_path + name
        if os.path.isfile(filename):
            parse_file(filename)
            
    print database