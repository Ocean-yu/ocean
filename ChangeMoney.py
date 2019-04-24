"""
    汇率转换器
"""
# 1.获取需要转换的数据
usb = float(input("请输入要转换的美元："))

# 2.进行逻辑运算
rmb = usb * 6.6935

# 3.输出结果
result = str(rmb)
print("对应的人民币数目为：" + result)