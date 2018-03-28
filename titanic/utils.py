import time

BASE_PATH = '/home/liuziyuan/Workspace/tensorflow/titanic/'

def get_file_name(folder, file_name):
    timestamp = int(time.time())
    file_name = "%s/%s/%s_%s.csv" % (BASE_PATH, folder, file_name, timestamp)
    return file_name
    