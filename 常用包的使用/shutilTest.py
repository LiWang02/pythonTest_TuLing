import shutil as st
if __name__ == '__main__':
    # copy拷贝，拷贝的同时可以重命名
    rst=st.copy("E:\jupyter\pythonTest\OOP\note.md","E:/jupyter")
    # copy2()
    #copyfile()讲一个文件的内容复制到另一个文件中
    #move()移动文件、文件夹


    #归档和压缩
    #归档：把多个文件或者文件夹合并到一个文件中
    #压缩：用算法把多个文件或者文件夹无损或者有损的合并到一个文件当中
    #make_archive()归档操作
    #语法：shutil.make_archive(归档之后的目录和文件名，后缀，需要归档的文件夹)
    #

    #unpack_archive() 解包操作

    #zip压缩包
    #，模块名称zipfile
