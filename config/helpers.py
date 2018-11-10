import os, shutil
from sample import app


def create_new_default_image(name):
    path = app.config['UPLOAD_PATH']
    shutil.copy(os.path.join(path, 'default_pic.jpg'), os.path.join(path, name))

def recover_image(id):
    for file_name in os.listdir(app.config['UPLOAD_PATH']):
        if f'pic{id}' in file_name:
            return file_name

def delete_file(id):
    file = recover_image(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], file))
