#!-*- encoding: utf-8 -*-
import os,sys  # 引入文件操作库


def deldir(path):
    """
    清理空文件夹和空文件
    param path: 文件路径，检查此文件路径下的子文件
    """
    print ('*'*30)
    try:
        files = os.listdir(path)  # 获取路径下的子文件(夹)列表
        #print (files)
        for file in files:
            #print (u'遍历路径：'+os.fspath(path +'/'+ file))
            if os.path.isdir(os.fspath(path+'/'+file)):  # 如果是文件夹
                #print (file+u'是文件夹')
                if not os.listdir(os.fspath(path+'/'+file)):  # 如果子文件为空
                    print (file+u'是空文件夹,不执行删除操作')
                    # no delete on empty folder
                    #os.rmdir(os.fspath(path+'/'+file))  # 删除这个空文件夹
                else:
                    #print (file+u'不是空文件夹')
                    deldir(os.fspath(path+'/'+file)) # 遍历子文件
                    if not os.listdir(os.fspath(path+'/'+file)):  # 如果子文件为空
                        print (file+u'是空文件夹,不执行删除操作')
                        # no delete on empty folder
                        #os.rmdir(os.fspath(path+'/'+file))  # 删除这个空文件夹
            elif os.path.isfile(os.fspath(path+'/'+file)):  # 如果是文件
                #print(file+u'是文件')
                if os.path.getsize(os.fspath(path+'/'+file)) == 0:  # 文件大小为0
                    print (file+u'是空文件，即将执行删除操作！')
                    os.remove(os.fspath(path+'/'+file))  # 删除这个文件
        return
    except FileNotFoundError:
        print (u"文件夹路径错误")

if __name__ == "__main__":
    path = input("Please input the files path:")  # 输入路径
    deldir(path)
