import os
# print(os.getcwd())
# os.chdir("rpa_basic")
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("c:/")
# print(os.getcwd())

# file_path = os.path.join(os.getcwd(),"my_file.txt")
# print(file_path)

# print(os.path.dirname(r"C:\Users\samsung\AppData\Local\Programs\Python\Python39\Lib\site-packages\pip\rpa_basic\2_desktop\my_file.txt"))

# import time
# import datetime

# ctime = os.path.getctime("num_btn.png")
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M%S"))

# mtime = os.path.getmtime("num_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M%S"))

# atime = os.path.getatime("num_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M%S"))

# size = os.path.getsize("num_btn.png")
# print(size)

# print(os.listdir())
# print(os.listdir("rpa_basic"))

# result = os.walk("rpa_basic")#"."모든파일
# # print(result)

# for root,dirs,files in result:
#     print(root,dirs,files)

# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# import fnmatch
# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name,pattern):
#             result.append(os.path.join(root,name))
# print(result)

# print(os.path.isdir("rpa_basic"))
# print (os.path.isfile("rpa_basic"))
# print(os.path.isdir("num_btn.png"))
# print (os.path.isfile("num_btn.png"))

# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다")
# else:
#     print("존재하지 않습니다")

# open("new_file.txt","a").close()

# os.rename("new_file.txt","new_file_rename.txt")

# os.remove("new_file_rename.txt")

# os.mkdir("new_folder")

# os.makedirs("new_folders/a/b/c")

# os.rename("new_folder","new_folder_rename")

# os.rmdir("new_folder_rename")

import shutil

# shutil.rmtree("new_folders")#하위 모든폴더 같이 지우기

# shutil.copy("num_btn.png","test_folder")
#어떤파일을 다른이름으로 저장
# shutil.copy("num_btn.png","test_folder/copied_run_btn.png")

# shutil.copyfile("num_btn.png","test_folder/copied_run_btn_2.png")

# shutil.copy2("num_btn.png","test_folder/copy2.png")

# shutil.copytree("test_folder","test_folder2")
# shutil.copytree("test_folder","test_folder3")

# shutil.move("test_folder","test_folder3")
# shutil.move("test_folder3","test_folder_rename")