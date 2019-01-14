'''
使用协程的方式进行编译
'''
movie_list = ['无双.mp4', '万万没想到.mp4', '斗破苍穹.m3u8', '无问西东.mp4', '仙剑.avi']
music_list = ['三字经.mp3', '去年夏天.mp3', '可不可以.mp3', '火力全开.mp3', '东西.mp3']

movie_foramt = ['mp4', 'm3u8']
music_format = ['mp3']

import asyncio, time

# @asyncio.coroutine
async def play(playlist):
    for i in playlist:
        if i.split('.')[1] in movie_foramt:
            print("你正在观看的视频是{}".format(i.split('.')[0]))
            #yield time.sleep(3)
            await asyncio.sleep(3)

        if i.split('.')[1] in music_format:
            print('你现在收听的音乐是{}'.format(i.split('.')[0]))
            #yield time.sleep(2)
            await asyncio.sleep(2)
        else:
            print('没有找到相应的格式')

loop = asyncio.get_event_loop()
task = [play(movie_list), play(music_list)]
loop.run_until_complete(asyncio.wait(task))
loop.close()