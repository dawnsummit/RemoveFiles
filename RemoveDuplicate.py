# /usr/bin/env python
# -*- coding:utf-8 -*-
# 运行的代码文件要放到删除重复的文件或图片所包含的目录中
import Lib.os as os
import Lib.hashlib as hashlib

#定义全局变量
dirpath = "F:\Photos\EVA-CL00\\"


def filecount():
    #filecount = int(os.popen('dir /B |find /V /C ""').read())

    filecount=len([lists for lists in os.listdir(dirpath)])
    return (filecount)


def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())


def delfile():
    all_md5 = {}
    #filedir = os.walk(os.getcwd())

    filedir = os.walk(dirpath)
    for i in filedir:
        for tlie in i[2]:
            fullfilename=dirpath+tlie
            #print(filepath)
            if md5sum(fullfilename) in all_md5.values():
                os.remove(fullfilename)
            else:
                all_md5[tlie] = md5sum(fullfilename)


if __name__ == '__main__':
    oldf = filecount()
    print('去重前有', oldf, '个文件\n\n\n请稍等正在删除重复文件...')
    delfile()
    print('\n\n去重后剩', filecount(), '个文件')
    print('\n\n一共删除了', oldf - filecount(), '个文件\n\n')