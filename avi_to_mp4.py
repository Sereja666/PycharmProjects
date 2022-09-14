import os

def convert_avi_to_mp4(avi_file_path, output_name):
    # os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    os.popen(f'ffmpeg -i {avi_file_path} -strict -2 {output_name}')
    return



dirname = r"C:\test"
os.chdir(dirname)
files = os.listdir(dirname)
for file in files:
    if '.avi' in file:
        file_mp4 = file.replace('.avi', '.mp4')
        convert_avi_to_mp4(file, file_mp4)