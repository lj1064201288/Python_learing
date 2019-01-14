'''
使用类方式进行多线程编写代码
'''

import threading, time


movie_list = ['无双.mp4', '万万没想到.mp4', '斗破苍穹.m3u8', '无问西东.mp4', '仙剑.avi']
music_list = ['三字经.mp3', '去年夏天.mp3', '可不可以.mp3', '火力全开.mp3', '东西.mp3']

movie_foramt = ['mp4', 'm3u8']
music_format = ['mp3']


class Thraead_test(threading.Thread):
    def __init__(self, play_list):
        super().__init__()
        self.play_list = play_list

    def play(self):
        for i in self.play_list:
            if i.split('.')[1] in movie_foramt:
                print('你现在观看的视频是:{}'.format(i.split('.')[0]))
                time.sleep(3)

            elif i.split('.')[1] in music_format:
                print('你现在收听的音乐是:{}'.format(i.split('.')[0]))
                time.sleep(2)

            else:
                print('没有找到相应的播放,请查看格式')

    def run(self):
        self.play()

if __name__ == '__main__':

    t1 = Thraead_test(movie_list)
    t2 = Thraead_test(music_list)

    t1.start()
    t2.start()
