#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk

root= tk.Tk() #创建页面
root.title('BMI计算器') #给程序窗口命名

#创建文本信息
tk.Label(root, text="体重(单位：kg)：").grid(row=0)
tk.Label(root, text="身高(单位：m)：").grid(row=1)

#创建输入框
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)

#定义输入过程的变量并设置初值
var_BMI = tk.StringVar()#计算得到的BMI
var_BMI_text = tk.StringVar()#针对BMI给出的文字提示
var_BMI.set('')
var_BMI_text.set('')

def count():
    weight = float(entry1.get())#从输入框得到体重
    height = float(entry2.get())#从输入框获得身高
    temp_BMI = weight/(height**2)#计算得到BMI
    temp_BMI = round(temp_BMI, 2)
    var_BMI.set(str(temp_BMI)) # 控制参数为小数点两位
    #对针对于BMI给出的文字提示进行更改
    if temp_BMI<18.5:
        var_BMI_text.set('您的体重偏轻')
    elif temp_BMI>=18.5 and temp_BMI<=24.9:
        var_BMI_text.set('您的体重正常')
    elif temp_BMI>24.9 and temp_BMI<=30:
        var_BMI_text.set('您的体重偏重')
    elif temp_BMI>=30:
        var_BMI_text.set('您的体重过重了')
    #显示BMI值得文本信息
tk.Label(root, text="BMI值为：").grid(row=2, column=0)
tk.Label(root, textvariable=var_BMI).grid(row=2, column=1)

#针对BMI值显示身体状况的BMI信息
tk.Label(root, text="健康状况：").grid(row=3, column=0)
tk.Label(root, textvariable=var_BMI_text).grid(row=3, column=1)

#计算BMI按钮和推出按钮
tk.Button(root, text="计算BMI", width=10, command=count).grid(row=4, column=0, padx=10, pady=10)

root.mainloop()

