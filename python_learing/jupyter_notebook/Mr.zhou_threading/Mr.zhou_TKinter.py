# 使用tkinter写一个小游戏, 来随机生成我们需要的名字

import tkinter
import random

window = tkinter.Tk()
window.wm_title('随机生成名字')

def random_1():
    s1 = ['cat', 'hippos', 'cakes']
    s = random.choice(s1)
    return s

def random_2():
    s2 = ['eats', 'likes', 'hates', 'has']
    s = random.choice(s2)
    return s

def button_click():
    name = nameEntry.get()
    verb = random_1()
    noun = random_2()
    sentence = name + verb + noun

    result.delete(0, tkinter.END)
    result.insert(0, sentence)

nameLabel = tkinter.Label(window, text='Name:')
nameEntry = tkinter.Entry(window)
button = tkinter.Button(window, text='生成随机名称', command=button_click)
result = tkinter.Entry(window)

nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()


window.mainloop()