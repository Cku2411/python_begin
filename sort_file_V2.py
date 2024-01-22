import os, shutil

# ================
path = input("Enter Path: ")


def main(path):
    files = os.listdir(path)

    for file in files:
        fileName, extention = os.path.splitext(file)
        # take extention name
        extention = extention[1:]

        folder_path = os.path.join(path, extention)
        source_path = os.path.join(path, file)
        des_path = os.path.join(path, extention, file)

        if os.path.exists(folder_path):
            shutil.move(source_path, des_path)
        else:
            os.makedirs(folder_path)
            shutil.move(source_path, des_path)


main(path)
# =========
print("done")
