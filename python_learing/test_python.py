# import _thread as thread
# import time
#
# movie_list = ['无双.mp4', '万能图书馆.mp4', '万万没想到.m3u8', '复仇者联盟.avi', '等风来.rmvb']
# music_list = ['三字经.mp3', '火力全开.mp3', '五月天.mp3', 'we are never every getting to together.mp3', 'my love.mp3']
#
# movie_format = ['mp4', 'm3u8']
# music_format = ['mp3']
#
#
# def Thread_test(play_list):
#     for play in play_list:
#         print(play)
#         if play.split('.')[1] in movie_format:
#             print('你现在观看的是{}'.format(play.split('.')[0]))
#             time.sleep(3)
#         elif play.split('.')[1] in music_format:
#             print("你现在收听的是{}".format(play.split('.')[0]))
#             time.sleep(2)
#         else:
#             print('未找到')
#
# def thread_run():
#     thread.start_new_thread(Thread_test, (movie_list,))
#     thread.start_new_thread(Thread_test, (music_list,))
#
#     while True:
#         time.sleep(10)
#
# if __name__ == "__main__":
#     thread_run()

import tkinter
import random


class RandomBall():
    """
    定义运动的球的内
    """

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        canvas: 画布, 所有的内容都应该在画布上呈现出来, 此处通过此变量传入
        scrnwidth/scrnheight:屏幕宽高
        '''
        self.canvas = canvas
        # 球出现的初始位置要随机
        # xpos表示位置的x坐标
        self.xpos = random.randint(10, int(scrnwidth) - 20)
        # ypos表示位置y坐标
        self.ypos = random.randint(10, int(scrnheight) - 20)

        # 定义球运动的速度
        # 模拟运动: 不断的擦掉原来画, 然后在一个新的地方重新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        # yvelocity模拟y轴方向运动
        self.yvelocity = random.randint(4, 20)
        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # 球的大小随机
        # 此处球的大小用半径来表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法:三个数字每个数字的值是0-255之间, 表示红绿蓝三个颜色的大小
        # 在某些系统中, 之间用英文单词表示也可以, 比如red, green等等
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

    def create_ball(self):
        '''
        用构造函数定义的变量值, 在canvas上画一个球
        '''
        # tkinter没有画圆形的函数
        # 只有一个画椭圆函数, 画椭圆需要定义两个坐标
        # 在一个长方形内画椭圆, 我们只需要定义长方形左上角
        # 求两个坐标的方法是, 已知圆心的坐标, 则圆心坐标减去半径能求出
        # 左上角左坐标, 加上半径能求出右下角坐标
        x1 = self.xpos - self.radius
        x2 = self.xpos + self.radius
        y1 = self.ypos - self.radius
        y2 = self.ypos + self.radius

        # 再有两个对角坐标的前提下, 可以进行画圆
        # fill代表颜色
        # outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候, 需要控制球的方向
        # 每次球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        # 以下判断是否撞墙
        # 撞了南墙就回头
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.scrnwidth:
            # 撞到右边的墙了
            self.xvelocity = -self.xvelocity
            # 或者以下
            # self.xvelocity *= -1
        if self.xpos - self.radius <= 0:
            self.xvelocity = -self.xvelocity
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = self.yvelocity * (-1)
        if self.ypos - self.radius <= 0:
            self.ycelocity = self.yvelocity * (-1)

        # 在画布上面挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
    定义屏保的类
    是一个画布
    '''
    # 如何装随机产生球
    balls = list()

    def __init__(self):
        # 每次启动球的数量是随机的
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind("<Motion>", self.myquit)
        # 同理, 按动任何键盘都需要退出屏保
        self.root.bind("<Any-KeyPress> ", self.myquit)
        # 得到屏幕的规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        # after是200韩淼之后启动一个函数, 需要启动的函数是第二个函数
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件类型
        self.root.destroy()


if __name__ == "__main__":
    # 启动程序
    ScreenSaver()
