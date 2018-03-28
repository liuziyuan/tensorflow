import time

def get_file_name(folder, file_name):
    timestamp = int(time.time())
    file_name = "%s/%s-%s.csv" % (folder, file_name, timestamp)
    return file_name
    