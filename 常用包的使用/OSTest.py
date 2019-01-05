import os
import os.path as op
if __name__ == '__main__':
    mydir=os.getcwd()
    print(mydir)
    os.chdir('E:\jupyter\pythonTest')
    # 切换
    mydir2=os.getcwd()
    print(mydir2)
    #返回某一路径的全部目录和文件列表
    ld=os.listdir(mydir2)
    print(ld)
    # makedirs递归创建文件夹
    # mk=os.makedirs("test")
    # print(mk)
    #system()运行系统的shell命令
    #格式：os.system(系统命令)
    # os.system("ls")
    # os.system("dir")
    #getenv()获取指定的系统环境变量名
    #putenv
    rst=os.getenv("PATH")
    print(rst)
    #exit()退出当前程序


    #值部分
    # os.curdir 当前目录
    # os.pardir 父目录
    # os.sep 当前路径的特定分隔符 windows:"\"  linux：“/”
    # os.linesep 当前系统的换行符号
    # os.name 当前系统名称
    #print(os.name)
    print(os.curdir)
    print(os.pardir)
    print(os.sep)


    #os.path模块，根路径相关的模块
    #abspath() 将路径转换为绝对路径
    # .代表当前目录  ..代表父目录
    absp=op.abspath(".")
    print(absp)
    #basename() 获取路径中的文件名部分
    #join() 将多个路径拼合成一个路径
    #格式：os.path.join(path1,path2)
    bb="E:\jupyter\pythonTest"
    bb2="hehe.dad"
    print(op.join(bb,bb2))
    #split() 将路径切割为文件夹部分和当前文件部分
    #isdir() 检测是否为目录
    # exists() 检测文件或者目录是否存在
    