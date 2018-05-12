# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:48:53 2018

@author: 123
"""
import additional_methods as add_m
import processing_all_message as p_a_m

import config
import StepNumber as s_n
from telebot import types  
import time
COPY_CURRENT_STEP = ""
sleep_time = 0

def set_link(name_link, link, answer, sleep_t, bot, message):   
    add_m.send_link(name_link, link, answer, bot, message)
#    bot.send_message(message.chat.id, "A я пока подожду.", reply_markup = types.ReplyKeyboardRemove(selective=False))
    time.sleep(sleep_t)
    add_m.set_two_buttons("Если закончили, то можно приступить дальше или вернуться назад.",
                          "Дальше",
                          "Хочу вернуться назад", bot, message)
 
#        add_m.set_one_button("Если закончили, то можно приступить дальше или вернуться назад.",
#                      "Дальше", bot, message)



def step4stage1v1(message, bot):
    add_m.set_one_button("В первом этапе я буду тебе рассказывать про посадку и обозначение пальцев. Ещё научимся играть правой и левой рукой и сыграем мелодию. В общем приступаем.",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_1_STAGE1.value)
        
        
        
def step4stage1v2(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Хочу посмотреть разбор гитары",
                         "Хочу посмотреть, какими способами можно настроить гитару", bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BEGINING.value)

        
        
def stepBeginningV1(message, bot):

#    bot.send_message(message.chat.id, "На этом изображение подробно показано строение гитары")
#    photo = open('image/guitar structure.jpg', 'rb') #открывает изображение
#    bot.send_photo(message.chat.id, photo)    #отправляет сообщение с изображением
    add_m.send_link("Посмореть видео", "https://www.youtube.com/watch?v=G3e_svu8PCQ",
            "Нажми сюда, чтобы посмотреть строение гитары.", bot, message)
    add_m.set_one_button("Скажи, когда разберешься.",
                         "Всё, готово", bot, message)
    s_n.newStep.add(s_n.saveID.get())           

def stepBeginningV2(message, bot):
    add_m.send_link("Посмореть видео", "https://www.youtube.com/watch?v=iAZkTAc_2E0",
                    "Нажми сюда, чтобы посмотреть, какие есть методы.", bot, message)
    add_m.set_one_button("Если разобрались, то нажмите далее.",
                         "Всё, готово", bot, message)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
    
def step4_1stage1v1(message, bot):
    add_m.send_link("Посмотреть видео" ,"https://www.youtube.com/watch?v=xqaiIoP4UXk",
                    "Давай посмотрим как правильно держать гитару\nНажми, чтобы посмотреть.",
                    bot, message)
    bot.send_message(message.chat.id, "Я в тебя верю.", reply_markup = types.ReplyKeyboardRemove(selective=False))
    time.sleep(sleep_time)
    add_m.set_one_button("Скажи, когда посмотришь видео и сможем продожить дальше.",
                         "Это оказалось достаточно просто, пошли дальше", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_2_STAGE1.value)
    
    
def step4_1stage1v2(message, bot):
    set_link("Посмотреть видео" ,"https://www.youtube.com/watch?v=xqaiIoP4UXk",
                    "Давай посмотрим как правильно держать гитару\nНажми, чтобы посмотреть.",
                    sleep_time, bot, message)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
def step4_2stage1v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=TI7rs5Ov4UA",
                 "Отлично!\nТеперь можем разобраться как правильно играть правой рукой и как пользоваться метрономом.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message)
        
    s_n.newStep.add(config.Step_bot.STEP4_3_STAGE1.value)
    
    
    
def step4_2stage1v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=TI7rs5Ov4UA",
                 "Ну что, давай еще раз посмотрим как правильно играть правой рукой и как пользоваться метрономом",
                 sleep_time, bot, message)
    s_n.newStep.add(s_n.saveID.get())



def step4_3stage1v0(message, bot):
    add_m.set_one_button("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно держать гитару",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK.value)

    
def step4_3stage1v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=yctV3syuPiY",
             "Ну вот, уже скоро будешь знать все принципы. Осталось узнать, что делает правая рука.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_4_STAGE1.value)


def step4_3stage1v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=yctV3syuPiY",
             "Ну давай еще раз глянем как зажимать струны.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message)
    s_n.newStep.add(s_n.saveID.get())
    
    

def step4_4stage1v0(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно держать гитару",
                         "Я хочу посмотреть видео про парвую руку",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK.value)


def step4_4stage1v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=JZy4wX9pTmw",
             "Так как ты уже достаточно знаешь, то можно разобрать \"В траве сидел кузнечик\"\nНажми, чтобы посмотреть.",
             sleep_time, bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_5_STAGE1.value)
  

  
def step4_4stage1v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=JZy4wX9pTmw",
             "Теперь можно разобрать \"В траве сидел кузнечик\"\nНажми, чтобы посмотреть.",
             sleep_time, bot, message)
    s_n.newStep.add(s_n.saveID.get())
    
    
def step4_5stage1v0(message, bot):
    add_m.set_three_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно держать гитару",
                         "Я хочу посмотреть видео про парвую руку",
                         "Хочу еще раз посмотреть как зажимать струны",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK.value)



def step4_5stage1v1(message, bot):
    add_m.send_message("Поздравляю! Вот и закончился перевый этап.\nМожно теперь перейти на второй этап.",
                       bot, message)
    add_m.set_two_buttons("Ну что, приступим или хочешь повторить предыдущее?",
                          "Не, я хочу перейти на второй этап",
                          "Думаю, что стоит повторить предыдущее", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_6_STAGE1.value)
    
    
def step4_6stage1v1(message, bot):
    p_a_m.step3v2(message, bot)

def step4_6stage1v2(message, bot):
    add_m.set_four_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно держать гитару",
                         "Я хочу посмотреть видео про парвую руку",
                         "Хочу еще раз посмотреть как зажимать струны",
                         "Хочу посмореть как играется \"В траве сидел кузнечик\"",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK.value)
    
    
def step4_6stage1_return(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно держать гитару",
                         "Я хочу посмотреть видео про парвую руку",
                         "Хочу еще раз посмотреть как зажимать струны",
                         "Хочу посмореть как играется \"В траве сидел кузнечик\"",
                         "Выбрать другой этап",
                         bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BREAK.value)
