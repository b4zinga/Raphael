# author: myc

import os


def get_files(path, isabs=True):
    files = []
    if os.path.isfile(path):
        if isabs:
            files.append(path)
        else:
            files.append(os.path.basename(path))
    elif os.path.isdir(path):
        file_list = os.listdir(path)
        for i in range(len(file_list)):
            _path = os.path.join(path, file_list[i])
            files.extend(get_files(_path, isabs))
    return files


def read_file(path, mode='r'):
    if not os.path.isfile(path):
        return ""
    file = open(path, mode)
    content = file.read()
    file.close()
    return content


def write_file(path, content, mode='w'):
    file = open(path, mode)
    file.write(content)
    file.close()


def read_dict(path, sep="\n", strict=False):
    content = read_file(path)
    if content:
        return list(set([d.strip() for d in content.split(sep)[:-1]]))
    else:
        return [] if strict else [path]
