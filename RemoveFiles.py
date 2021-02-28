# !-*- encoding: utf-8 -*-

#Date: 2021/2/13
#Changes: 
# add more file extensions for checking
# check filenames containing "()"
#Details: remove all duplicate files ending with _1,_2 etc.
#遍历子目录删除特定文件
import os,sys,shutil  # 引入文件操作库
#photo_path = "F:\\Photos\\iPhone8\\Downloads\\2018"
photo_path="F:\\Moments\\Mobile"
os.chdir(photo_path)


dir_list = []
extensions=['.jpg','.JPG','.png','.PNG','.mov','.MOV','.mp4','.MP4']

for root, dirs, files in os.walk(os.getcwd()):
    dir_list.append(root)
    #print(root) #当前目录路径
    #print(dirs) #当前路径下所有子目录
    #print(files) #当前路径下所有非目录子文件
    #print(files)

    for name in files:
        if "video_" in name or "Video_" in name or "video" in name or "Video" in name:
            continue
        
            
        for num in range(1,20):
            #print(num)
            num=str(num)
            #if ("_"+num+".JPG" in name) or ("_"+num+".jpg" in name) or ("_"+num+".PNG" in name) or ("_"+num+".png" in name) or ("_"+num+".MOV" in name) or ("_"+num+".mp4" in name):
            for ext in extensions: 
                if "_"+num+ext in name or "("+num+")" in name or "Edited" in name or "已编辑" in name:
                    
                    if len(sys.argv)>1:
                        
                        if sys.argv[1]=="d":
                            if os.path.exists(os.path.join(root, name)):
                                os.remove(os.path.join(root, name))
                                print(os.path.join(root, name)+" is already removed.")
                    else:
                        print(os.path.join(root, name)+" is found to be duplicate.")
                            

    for name in dirs:
        if "video_" in name or "Video_" in name or "video" in name or "Video" in name:
            continue
        
        for num in range(1,20):
            #print(num)
            num=str(num)
            for ext in extensions: 
                if "_"+num+ext in name or "("+num+")" in name or "Edited" in name or "已编辑" in name:
                    print(name)
                    if len(sys.argv)>1:
                        if sys.argv[1]=="d":
                            #os.removedirs(os.path.join(root, name))
                            shutil.rmtree(os.path.join(root, name)+" is already removed.")
                    else:
                        print(os.path.join(root, name)+" is found to be duplicate.")
