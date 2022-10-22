# ! encoding=utf-8

import os
import zipfile


def file2zip(zip_file_name, file_names):
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for fn in file_names:
            parent_path, name = os.path.split(fn)
            zf.write(fn, arcname=name)


if __name__ == '__main__':
    zip_name = "/Program/PycharmProjects/python_Paramiko/testRotate.zip"
    files = ['/Program/PycharmProjects/python_Paramiko/testRotate.log', '/Program/PycharmProjects/python_Paramiko/testRotate1.log']
    file2zip(zip_name, files)
