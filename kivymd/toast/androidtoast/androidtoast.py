# -*- coding: utf-8 -*-

'''
VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по услолвиям той же лицензии,
что и фреймворк Kivy.

'''
print("inside androidtoast file....................")
from kivy.logger import Logger
print("check error.......................................1")
from jnius import autoclass, PythonJavaClass, java_method, cast
print("check error.......................................2")
from android import activity
print("check error.......................................3")
from android.runnable import run_on_ui_thread
print("check error.......................................4")

Toast = autoclass('android.widget.Toast')
print("check error.......................................5")
context = autoclass('org.kivy.android.PythonActivity').mActivity
print("check error.......................................6")

@run_on_ui_thread
def toast(text, length_long=False):
    print("check error.......................................7")
    duration = Toast.LENGTH_LONG if length_long else Toast.LENGTH_SHORT
    print("check error.......................................8")
    String = autoclass('java.lang.String')
    print("check error.......................................9")
    c = cast('java.lang.CharSequence', String(text))
    print("check error.......................................10")
    t = Toast.makeText(context, c, duration)
    print("check error.......................................11")
    t.show()
    print("check error.......................................12")
