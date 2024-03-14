import os
# это работает, открывает в фоне новые процессы, однако не видно момент окончания

def convert_avi_to_mp4(avi_file_path, output_name):
    # os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    aa = os.popen(fr'"C:\Python\PycharmProjects\ffmpeg\bin\ffmpeg.exe" -i "{avi_file_path}" -strict -2 "{output_name}"')
    return aa.line_buffering


# C:\Python\PycharmProjects\ffmpeg\bin\ffmpeg.exe -i C:\Python\work_tests\123.avi -strict -2 C:\Python\work_tests\123.mkv
dirname = r"C:\Python\work_tests"
os.chdir(dirname)
files = os.listdir(dirname)

for file in files:
    if '.avi'  in file :
        print(file)
        file_mp4 = file.replace('.avi', '.mp4')
        convert_avi_to_mp4(file, file_mp4)
    if '.wmv' in file:
        print(file)
        file_mp4 = file.replace('.wmv', '.mp4')
        convert_avi_to_mp4(file, file_mp4)

