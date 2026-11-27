import os
import shutil

while True:
    userdir = input('Enter absolute path of folder to organize: ')
    directory = userdir.strip().strip("'").strip('"')
    if os.path.isdir(directory):
        print("Directory found")
        break
    else:
        print("Directory not found")

extensions = {
    ".svg":"Images",
    ".jpeg":"Images",
    ".jpg":"Images",
    ".png":"Images",
    ".gif":"Images",
    ".mp4":"Videos",
    ".mp3":"Audios",
    ".docx":"Documents",
    ".csv":"Documents",
    ".txt":"Documents",
    ".pdf":"Documents",
    ".xlsx":"Documents",
    ".pptx":"Documents",
    ".py":"Code",
    ".java":"Code",
    ".c":"Code",
    ".html":"Webfiles",
    ".css":"Webfiles",
    ".js":"Webfiles",
    }

for filename in os.listdir(directory):
    filepath = os.path.join(directory,filename)

    if os.path.isfile(filepath):
        extension = os.path.splitext(filepath)[1].lower()  #splitext returns (root,ext)

        if extension in extensions:
            foldername = extensions[extension]
            folderpath = os.path.join(directory,foldername)
            os.makedirs(folderpath,exist_ok = True)  #if already exists, returns none and no error

            destpath = os.path.join(folderpath,filename)
            shutil.move(filepath,destpath)

            print(f"Moved {filename} to {foldername} folder")
        else:
            print(f"Skipped {filename}. Unknown file extension")
    else:
        print(f"Skipped {filename}. Not a file")

print('File organization completed')
         