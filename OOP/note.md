# 1、类的基本实现
- 类的命名
    - 遵守变量命名的规范
    - 大驼峰（由一个或者多个单词实现，每个单词首字母大写）
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    -必须使用关键字class
    - 由属性和方法构成，其它不允许出现
    - 成员属性定义可以直接使用变量属性
- 实例化类
- 访问对象成员
- 对象所有成员检查
    - dict 前后两个下挂线
    - obj.__dict__
- 类的所有成员
# 2、anaconda的基本使用
- 主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list：显示anaconda的安装的包
- conda env list：显示anaconda的虚拟环境列表
- 仅仅为OOP练习创建一个虚拟环境：conda create -n xxx python=3.6
- 激活虚拟环境 activate oop
- 想让自己的代码在虚拟环境oop中运行
# 3、类和对象的成员分析
-  类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员时是存储当前对象中
- 对象访问一个成员时，如果对象中没有该成员，尝试访问
  类中的同名成员，如果对象中有次成员，一定使用对象中的成员
- 通过对象对类中成员重新赋值，或者通过对象添加成员时，对应成员会保存在对象中，而不会修改
类成员

# 4、关于self
- self在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象
会自动传入到当前方法的第一个参数中。
- self并不是关键字，只是一个用于接受对象的普通参数，理论上上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问
    def sayAgain():
        print(__class__.name)
        print("必须用类名进行调用")
        return None
# 5、面向对象的三大特征
- 封装：就是对对象的成员进行访问限制
    - 三个级别：
        - public
        - 受保护的 protected
        - 私有的 private
        - public protected private不是关键字
    - 判别对象的位置
        - 对象内部
        - 对象外部
        - 子类中
    - 私有
        - 私有成员是最高级别的封装，只能在当前类或者对象中访问
        - 在成员前面添加两个下划线即可,例如： __sex="girl"
        - Python中的私有不是真的私有，是一种成为name mangling的改名策略，可以使用对象._classname_attribution
        _PythonStudent__sex
    - 受保护的封装protected
        - 在本类和子类中可以被访问，但是在外部不能进行访问 ，写一个下划线即可
    - 公开的 public
        - 在任何地方都可以被访问
   
- 继承
    - 
- 多态
# 类的常用魔术方法
- 就是不需要人为的去调用，基本上是特定的时刻自发触动
- 方法名被前后两个下划线包裹
- 操作类：
    - __init__构造函数： 
    - __new__对象实例化方法 
    - __call__对象当函数使用的时候触发： 
    - __str__当对象被当做字符串使用的时候调用：
    - __repr__返回字符串
- 描述符：
    - __set __
    - __get __
    - __delete __
- 属性操作相关
    - __getattr __:访问一个不存在的属性时触发
    - 





