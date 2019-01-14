'''
使用多进程编写程序
'''

import time
import multiprocessing


movie_list = ['无双.mp4', '万万没想到.mp4', '斗破苍穹.m3u8', '无问西东.mp4', '仙剑.avi']
music_list = ['三字经.mp3', '去年夏天.mp3', '可不可以.mp3', '火力全开.mp3', '东西.mp3']

movie_foramt = ['mp4', 'm3u8']
music_format = ['mp3']


def play(play_list):
    for i in play_list:
        if i.split('.')[1] in movie_foramt:
            print('你现在观看的视频是:{}'.format(i.split('.')[0]))
            time.sleep(5)
        elif i.split('.')[1] in music_format:
            print('你现在收听的音乐是:{}'.format(i.split('.')[0]))
            time.sleep(3)
        else:
            print('Not Found!')

def multipressing_test():
    p1 = multiprocessing.Process(target=play, args=(movie_list,))
    p2 = multiprocessing.Process(target=play, args=(music_list,))

    p1.start()
    p2.start()

if __name__ == '__main__':
    multipressing_test()