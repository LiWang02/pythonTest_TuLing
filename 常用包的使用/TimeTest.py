import time
# 时间戳
# 一个时间表示，根据不同的语言，有整数表示，也有浮点数表示的
# 从1970年1月1日开始到现在经历的秒数
### UTC时间 中国是UTC+8 东八区

### 时间元组
# 一个包含时间内容的时间元组
if __name__ == '__main__':
    print(time.timezone)
    print(time.localtime())
    #localtime可以通过点号得到相关属性
    t = time.localtime()
    print(t.tm_hour)
    # strftime()
    # 它可以将localtime()
    # 中获取的时间元组转换为自定义的日期时间格式进行。如：
    # time.strftime("%Y-%m-%d %H:%M:%S", struct_local_time)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # gmtime()
    # 可以将时间秒转换为日期时间，此时日期和时间表示的是标准时间，北京时间为标准时间加上8个小时。不传入参数代表当前时间即转换time()
    # 函数的结果。如：
    # time.gmtime()
    print(time.gmtime())
    # ctime:获取字符串化的当前时间
    print(time.ctime())
    #


