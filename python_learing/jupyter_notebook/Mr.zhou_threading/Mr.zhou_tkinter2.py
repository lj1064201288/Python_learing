# 做一个输入密码的小程序, 我们自己设定一个密码, 如果用户输入正确则显示正确,否则显示不正确

# enoding:utf-8

import tkinter as tk

window = tk.Tk()
window.wm_title('密码验证')

def check_password():
    password = '123456'
    entered_password = passwordEntry.get()
    if password == entered_password:
        confirmLabel.config(text='正确')
    else:
        confirmLabel.config(text='密码错误')


passwordLabel = tk.Label(window, text='Password:')
passwordEntry = tk.Entry(window, show='*')
button = tk.Button(window, text='校验', command=check_password)
confirmLabel = tk.Label(window)

passwordEntry.pack()
passwordLabel.pack()
button.pack()
confirmLabel.pack()

window.mainloop()
