import os


file = r'\\MYCLOUDEX2ULTRA\oO\oO\JOPORN_NET_36250_720p.mp4'
file_info = os.stat(file)
print(file_info)

from moviepy.editor import VideoFileClip


def get_video_info(filename):
    video = VideoFileClip(filename)
    print(video.filename)
    print(video.duration)
    # print(video.)
    for i in video.iteritems():
        print(i)
    # duration = video.duration
    # genre = video.metadata.get('genre')
    # title = video.metadata.get('title')
    #
    # video.close()

    return video


# Пример использования

a = get_video_info(file)

# print('Продолжительность: ', duration)
# print('Жанр: ', genre)
# print('Название: ', title)