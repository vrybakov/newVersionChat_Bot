# -*- coding: utf-8 -*-
"""
Created on Sun May  6 15:48:35 2018

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

def set_link(name_link, link, answer, sleep_t, bot, message, count_answer):   
    add_m.send_link(name_link, link, answer, bot, message)
#    bot.send_message(message.chat.id, "A я пока подожду.", reply_markup = types.ReplyKeyboardRemove(selective=False))
    time.sleep(sleep_t)
    if count_answer == 1:
        add_m.set_one_button("Если закончили, то можно приступить дальше или вернуться назад.",
                              "Дальше", bot, message)
    elif count_answer == 2:
        add_m.set_two_buttons("Если закончили, то можно приступить дальше или вернуться назад.",
                              "Дальше",
                              "Хочу вернуться назад", bot, message)
                                  
                              
def step4stage2v1(message, bot):
    add_m.set_one_button("Во втором этапе мы изучим бой \"четверка\", простые аккорды, аппликатуру и песню",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_1_STAGE2.value)
        
        
                
    
def step4_1stage2v1(message, bot):
    
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=816&v=BoKaijCssGM",
                    "В этом уроке научимся играть простой бой.\nНажми, чтобы посмотреть.", sleep_time, bot, message, 1)     
    s_n.newStep.add(config.Step_bot.STEP4_2_STAGE2.value)
    
    
def step4_1stage2v2(message, bot):
    set_link("Посмотреть видео" ,"https://www.youtube.com/watch?time_continue=816&v=BoKaijCssGM",
                    "Давай посмотрим как играть бой\nНажми, чтобы посмотреть.",
                    sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
def step4_2stage2v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=TI7rs5Ov4UA",
                 "Прекрасно, что теперь умеешь играть бой. Теперь будем изучать аккорды. \nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
        
    s_n.newStep.add(config.Step_bot.STEP4_3_STAGE2.value)
    
    
    
def step4_2stage2v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=TI7rs5Ov4UA",
                 "Аккорды сразу сложно запомнить.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())



def step4_3stage2v0(message, bot):
    add_m.set_one_button("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно играть бой",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S2.value)

    
def step4_3stage2v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=jM9XE9RNmI8",
                 "Теперь ты знаешь несколько простых аккордов, но тебе может захочется другие узнать, тогда давай разберем что такое аппликатура",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_4_STAGE2.value)


def step4_3stage2v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=jM9XE9RNmI8",
             "Ну давай еще раз глянем, что такое аппликатура\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    

def step4_4stage2v0(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно играть бой",
                         "Я хочу посмотреть видео как ставяться аккорды",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S2.value)


def step4_4stage2v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=ixTYVIoXvVw",
             "Отлично! Раз ты здесь, значит уже готов изучить первую песню\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_5_STAGE2.value)
  

  
def step4_4stage2v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=ixTYVIoXvVw",
             "Давай повторим песню\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
def step4_5stage2v0(message, bot):
    add_m.set_three_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно играть бой",
                         "Я хочу посмотреть видео как ставяться аккорды",
                         "Хочу еще раз посмотреть, что такое аппликатура",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S2.value)



def step4_5stage2v1(message, bot):
    add_m.send_message("Вот уже два этапа позади, это большой успех.\nМожно теперь перейти на третий этап.",
                       bot, message)
    add_m.set_two_buttons("Ну что, приступим или хочешь повторить предыдущее?",
                          "Не, я хочу перейти на третий этап",
                          "Думаю, что стоит повторить предыдущее", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_6_STAGE2.value)
    
    
def step4_6stage2v1(message, bot):
    p_a_m.step3v3(message, bot)

def step4_6stage2v2(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно играть бой",
                         "Я хочу посмотреть видео как ставяться аккорды",
                         "Хочу еще раз посмотреть, что такое аппликатура",
                         "Хочу посмореть как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S2.value)


def step4_6stage2_return(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть видео о том, как правильно играть бой",
                         "Я хочу посмотреть видео как ставяться аккорды",
                         "Хочу еще раз посмотреть, что такое аппликатура",
                         "Хочу посмореть как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S2.value)                             
                              
                              
