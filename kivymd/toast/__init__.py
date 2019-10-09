# -*- coding: utf-8 -*-

''' 
Разработано специально для проекта VKGroups -
https://github.com/HeaTTheatR/VKGroups

Copyright © 2010-2018 HeaTTheatR

Для предложений и вопросов:
<kivydevelopment@gmail.com>

Данный файл распространяется по услолвиям той же лицензии,
что и фреймворк Kivy.

'''
print("inside toast init method.......")
from kivy import platform


if platform == 'android': 
    print("befor toast module import........")
    from . androidtoast import toast
    print("after toast module import........")
else:
    from . kivytoast import toast
