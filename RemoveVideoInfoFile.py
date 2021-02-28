# !-*- encoding: utf-8 -*-
#遍历子目录删除特定文件
import os,sys,shutil  # 引入文件操作库
dir_list = []

for root, dirs, files in os.walk(os.getcwd()):
    dir_list.append(root)
    #print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    #print(files)

    for name in files:

        if ("320-10.bif" in name) or ("poster.jpg" in name) :
            print(name)
            os.remove(os.path.join(root, name))

    for name in dirs:

        if ("320-10.bif" in name) or ("poster.jpg" in name):
            print(name)
            #os.removedirs(os.path.join(root, name))
            shutil.rmtree(os.path.join(root, name))