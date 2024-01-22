import os

parent_dir = "D:/BACKUP_FIXED LATER/IT Carreer/02_PYTHON"


def current_path():
    print("Current working path: ")
    print(os.getcwd())
    print()


# joint two directory
def create_folder(num, name):
    for i in range(num):
        new_dir = f"{name}_{i}"
        path = os.path.join(parent_dir, new_dir)
        os.mkdir(path)


def remove_dir(num, name):
    for i in range(num):
        new_dir = f"{name}_{i}"
        path = os.path.join(parent_dir, new_dir)
        os.removedirs(path)


def creat_file(file_name):
    path = os.path.join(os.getcwd(), file_name)
    # create a new file
    f = open(path, "x")
    f.close()
