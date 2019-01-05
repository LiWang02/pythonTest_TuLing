import calendar

if __name__ == '__main__':
    calendar.setfirstweekday(firstweekday=6)
    # 返回一周的第一天，0是周一
    print(calendar.firstweekday())
    print(calendar.isleap(2008))#是否为闰年
    #leapdays(y1, y2)：返回y1与y2年份之间的闰年数量，y1与y2皆为年份。包括启示年，不包括结束年
    print(calendar.leapdays(2000, 2020))
    #weekday(year, month, day)：获取指定日期为星期几
    print(calendar.weekday(2018, 8, 23))
    #weekheader(n)：返回包含星期的英文缩写，n表示英文缩写所占的宽度
    print(calendar.weekheader(4))
    #monthrange(year, month)：返回一个由一个月第一个天的星期与当前月的天数组成的元组


