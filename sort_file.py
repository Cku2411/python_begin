import os, shutil

path = os.path.join(os.getcwd(), "Test")

# check file => return the array
files = os.listdir(path)
print(files)


def check_file_in_folder(filename, folder_name):
    file_path = os.path.join(path, folder_name, filename)
    return os.path.exists(file_path)


# check if path exist
folders_names = ["png_files", "image_file", "psd_files"]


for folders_name in folders_names:
    folder_path = os.path.join(path, folders_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# lopp through file to sort
for file in files:
    file_path = os.path.join(path, file)
    if ".png" in file and not check_file_in_folder(file, "png_files"):
        shutil.move(file_path, os.path.join(path, "png_files", file))

    elif ".psd" in file and not check_file_in_folder(file, "psd_files"):
        shutil.move(file_path, os.path.join(path, "psd_files", file))
    else:
        print("DONE, EVERYTHING WORKS WELL")
# =========
print("done")
