# -*- coding: utf-8 -*-
"""
Created on Sun May  6 23:19:25 2018

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
                                  
                              
def step4stage3v1(message, bot):
    add_m.set_one_button("На этом этапе мы разберем как пользоваться табулатурой, бой \"шестерка\" и простой перебор",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_1_STAGE3.value)
        
        
                
    
def step4_1stage3v1(message, bot):
    
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "В этом уроке разбермся в табулатуре.\nНажми, чтобы посмотреть.", sleep_time, bot, message, 1)     
    s_n.newStep.add(config.Step_bot.STEP4_2_STAGE3.value)
    
    
def step4_1stage3v2(message, bot):
    set_link("Посмотреть видео" ,"https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "Давай посмотрим табулатуру.\nНажми, чтобы посмотреть.",
                    sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
def step4_2stage3v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Теперь можем разобрать бой \"шестерка\". \nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
        
    s_n.newStep.add(config.Step_bot.STEP4_3_STAGE3.value)
    
    
    
def step4_2stage3v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Посморим бой \"шестерка\".\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())



def step4_3stage3v0(message, bot):
    add_m.set_one_button("Куда хочешь вернуться?",
                         "Я хочу посмотреть разборку табулатуры",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S3.value)

    
def step4_3stage3v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
                 "Теперь можем познакомиться с перебором. Давай приступим.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_4_STAGE3.value)


def step4_3stage3v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
             "Давай посмотрим перебор.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    

def step4_4stage3v0(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть разборку табулатуры",
                         "Я хочу посмотреть бой \"шестерка\"",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S3.value)


def step4_4stage3v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Теперь можно изучить еще одну песню.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_5_STAGE3.value)
  

  
def step4_4stage3v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Давай повторим песню\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
def step4_5stage3v0(message, bot):
    add_m.set_three_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть разборку табулатуры",
                         "Я хочу посмотреть бой \"шестерка\"",
                         "Хочу еще раз посмотреть как играть перебором",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S3.value)



def step4_5stage3v1(message, bot):
    add_m.send_message("Вот уже два три позади, это большой успех.\nМожно теперь перейти на четвертый этап.",
                       bot, message)
    add_m.set_two_buttons("Ну что, приступим или хочешь повторить предыдущее?",
                          "Не, я хочу перейти на четвертый этап",
                          "Думаю, что стоит повторить предыдущее", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_6_STAGE3.value)
    
    
def step4_6stage3v1(message, bot):
    p_a_m.step3v4(message, bot)

def step4_6stage3v2(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть разборку табулатуры",
                         "Я хочу посмотреть бой \"шестерка\"",
                         "Хочу еще раз посмотреть как играть перебором",
                         "Хочу посмореть как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    print(s_n.saveID.add(s_n.newStep.get()))
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S3.value)
    
def step4_6stage3_return(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть разборку табулатуры",
                         "Я хочу посмотреть бой \"шестерка\"",
                         "Хочу еще раз посмотреть как играть перебором",
                         "Хочу посмореть как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S3.value)