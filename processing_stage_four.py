# -*- coding: utf-8 -*-
"""
Created on Tue May  8 08:50:33 2018

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
                                  
                              
def step4stage4v1(message, bot):
    add_m.set_one_button("На этом этапе будем изучать перебор: \"Восьмерка\", сложносокращенный, \"Щипок\". А в конце как обычно сыграем песню.",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_1_STAGE4.value)
        
        
                
    
def step4_1stage4v1(message, bot):
    
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "Сейчас мы разберем перебор \"Восьмерка\".\nНажми, чтобы посмотреть.", sleep_time, bot, message, 1)     
    s_n.newStep.add(config.Step_bot.STEP4_2_STAGE4.value)
    
    
def step4_1stage4v2(message, bot):
    set_link("Посмотреть видео" ,"https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "Давай повторим перебор \"Восьмерка\".\nНажми, чтобы посмотреть.",
                    sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
def step4_2stage4v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Раз уже усвоили тот перебор, то можно научиться играть сложносокращенный. \nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
        
    s_n.newStep.add(config.Step_bot.STEP4_3_STAGE4.value)
    
    
    
def step4_2stage4v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Хорошо, повторим сложносокращенный перебор.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())



def step4_3stage4v0(message, bot):
    add_m.set_one_button("Куда хочешь вернуться?",
                         "Я хочу посмотреть перебор \"Восьмерка\"",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S4.value)

    
def step4_3stage4v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
                 "Последний перебор на этом этапе, это \"Щипок\".\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_4_STAGE4.value)


def step4_3stage4v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
             "Давай посмотрим перебор \"Щипок\".\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    

def step4_4stage4v0(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть перебор \"Восьмерка\"",
                         "Я хочу посмотреть сложносокращенный перебор",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S4.value)


def step4_4stage4v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Для закрепления изучим еще одну песню.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_5_STAGE4.value)
  

  
def step4_4stage4v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Давай повторим песню\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
def step4_5stage4v0(message, bot):
    add_m.set_three_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть перебор \"Восьмерка\"",
                         "Я хочу посмотреть сложносокращенный перебор",
                         "Я хочу посмотреть перебор \"Щипок\"",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S4.value)



def step4_5stage4v1(message, bot):
    add_m.send_message("Поздравляю! Уже проделан большой путь.\nМожно теперь перейти на пятый этап.",
                       bot, message)
    add_m.set_two_buttons("Ну что, приступим или хочешь повторить предыдущее?",
                          "Не, я хочу перейти на пятый этап",
                          "Думаю, что стоит повторить предыдущее", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_6_STAGE4.value)
    
    
def step4_6stage4v1(message, bot):
    p_a_m.step3v5(message, bot)

def step4_6stage4v2(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть перебор \"Восьмерка\"",
                         "Я хочу посмотреть сложносокращенный перебор",
                         "Я хочу посмотреть перебор \"Щипок\"",
                         "Я хочу повторить как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S4.value)
    
    
def step4_6stage4_return(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу посмотреть перебор \"Восьмерка\"",
                         "Я хочу посмотреть сложносокращенный перебор",
                         "Я хочу посмотреть перебор \"Щипок\"",
                         "Я хочу повторить как играется песня",
                         "Выбрать другой этап",
                         bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S4.value)