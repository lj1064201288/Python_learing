import random
import tkinter


class RandomBall:
    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas

        self.xpos = random.randint(10, int(scrnwidth))
        self.ypos = random.randint(10, int(scrnheight))

        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)

        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        self.radius = random.randint(20,120)

        c = lambda : random.randint(0,255)
        self.color = '#%02x%02x%02x'%(c(),c(),c())

    def create_ball(self):

        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius

        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        self.item = self.canvas.create_oval(x1,y1,x2,y2, fill=self.color, outline=self.color)

    def move_ball(self):
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        if self.ypos >= self.scrnheight - self.radius:
           self.yvelocity = - self.yvelocity

        if self.ypos <= self.radius:
            self.yvelocity = abs(self.yvelocity)

        if self.xpos >= self.scrnwidth - self.radius or self.xpos <= self.radius:
            self.xvelocity = - self.xvelocity

        self.canvas.move(self.item, self.xvelocity, self.yvelocity)

class ScreenSaver:
    balls = []

    def __init__(self,num_balls):
        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)
        # 任何鼠标移动
        self.root.bind('<Motion>', self.myquit)

        w,h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.canvas = tkinter.Canvas(self.root, width=w, height=h )
        self.canvas.pack()

        for i in range(num_balls ):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(200, self.run_screen_saver)

    def myquit(self,event):
        self.root.destroy()

if __name__ == "__main__":
    ScreenSaver(12)