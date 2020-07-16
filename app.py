import func_module

# func_module.module_show()

nowdate = func_module.data_now()
nowdate.replace(month=12, day=25)
date_today = '{}년 {}월 {}일'.format(nowdate.year, nowdate.month, nowdate.day)
print(date_today)

x_mas = nowdate.replace(month = 12, day = 25)

date_x_mas = '{}년 {}월 {}일'.format(x_mas.year, x_mas.month, x_mas.day)
print(date_x_mas)