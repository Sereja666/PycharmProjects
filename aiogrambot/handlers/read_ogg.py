# -*- coding: utf-8 -*-


import speech_recognition as speech_recog
import subprocess, os
import subprocess
import time

from aiogram import executor, Bot, Dispatcher, types
import schedule
import transliterate
from aiogram import types
import re
import datetime
import asyncio
from contextlib import suppress
# from aiogrambot.handlers.skills import goroskop
# from badwords import *
from pathlib import Path
from aiogram.types import ContentType, File, Message
from aiogrambot.handlers.read_ogg import *

global txt_for_bot

class BotListen:
    file = 'C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\1.ogg'
    cmds = 'C:\\Users\\Sereja\\PycharmProjects\\ffmpeg\\bin\\ffmpeg.exe'
    cmds_probe = 'C:\\Users\\Sereja\\PycharmProjects\\ffmpeg\\bin\\ffprobe.exe'

    def init(self, file_in):
        self.file_name = 'C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\1.ogg'
        self.file_in = file_in
        self.text_out = ''

    def mp3_wav(self, file):
        try:
            os.remove('C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\ready.wav')
        except FileNotFoundError:
            pass
        if file.endswith('ogg'):
            self.file_wav = "ready.wav"
            p = subprocess.Popen(BotListen.cmds + " -i " + file + " -acodec pcm_s16le -ac 1 -ar 16000 " + self.file_wav)
            p.communicate()
            return self.file_wav
        else:
            return self.file_wav

    def noize_to_txt(self):
        sample_audio = speech_recog.AudioFile(self.file_wav)
        recog = speech_recog.Recognizer()

        with sample_audio as audio_file:
            audio_content = recog.record(audio_file, duration=100)

        self.text_out = recog.recognize_google(audio_content, language = "ru-RU")
        # txt_for_bot = self.text_out
        return self.text_out

    # def create_text(self):
    #     with open('text.txt', "w", encoding="utf-8") as file_good:
    #         file_good.write(self.text_out)



    def act(self, file):
        self.mp3_wav(file)
        self.noize_to_txt()
        # self.create_text()

# botListen = BotListen()
# botListen.act(file='C:\\Users\\Sereja\\PycharmProjects\\aiogrambot\\converter\\1.ogg')