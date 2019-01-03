# 1、模块
- 一个模块就是一个包含了python代码的文件
# 2、模块的搜索路径和存储
- 已有的路径是个列表形式，可以添加
- 模块加载顺序：搜索内存中已经加载好的、搜索python的内置模块、搜索sys.path的路径
# 3、包
- 相当于是一个文件夹，里边包含了多个python文件
- 包的导入操作
    - import package_name 
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式是： 
            - package_name.func_name   
            - package_name.class_name.func_name
        import packageTest 相当于只导入__init__.py内容
    - import package_name.moddule 导入包中某一个具体的模块
        - 使用方法  
            - package_name.module.func   
            - package.module.class.fun  
            - package.module.class.var
    - import package.module as p
 - from ... import 
    - from package import module1,module2.....
    - 此种导入方法不执行__init__.py中的内容
    -from package import *  全部导入
        - 导入当前包__init__.py中所有的函数和类
        - 使用方法
            - func_name
            - class_name
            - class_name.var
- __all__的用法：
  - 在使用from package import *时，*可以导入的内容
  - 一般是导入了__init__.py中的内容 ，若为空，__all__也为空
  - 如果设置了__all__的值，则会按照__all__中的模块或者子包进行载入，则不会执行__init__的内容
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
