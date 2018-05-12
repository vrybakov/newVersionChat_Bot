# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:35:45 2018

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
                                  
                              
def step4stage5v1(message, bot):
    add_m.set_one_button("В пятом этапе рассмотрим сложные аккорды и сыграем пару песен.",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_1_STAGE5.value)
        
        
                
    
def step4_1stage5v1(message, bot):
    
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "Сейчас покажу как ставить баррэ. Это не так просто, но я уверен, что справишься.\nНажми, чтобы посмотреть.", sleep_time, bot, message, 1)     
    s_n.newStep.add(config.Step_bot.STEP4_2_STAGE5.value)
    
    
def step4_1stage5v2(message, bot):
    set_link("Посмотреть видео" ,"https://www.youtube.com/watch?v=P1ChNaohBAI",
                    "Хорошо, повторим как ставить баррэ.\nНажми, чтобы посмотреть.",
                    sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
    
def step4_2stage5v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Теперь закрепим песней. \nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
        
    s_n.newStep.add(config.Step_bot.STEP4_3_STAGE5.value)
    
    
    
def step4_2stage5v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=13zkSFsGbOc",
                 "Давай повторим песню.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())



def step4_3stage5v0(message, bot):
    add_m.set_one_button("Куда хочешь вернуться?",
                         "Я хочу повторить урок с баррэ",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S5.value)

    
def step4_3stage5v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
                 "Теперь научимся ставить баррэ в разных позициях.\nНажми, чтобы посмотреть.",
                 sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_4_STAGE5.value)


def step4_3stage5v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?v=SgZ92DnJy8M",
             "Повторим урок.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    

def step4_4stage5v0(message, bot):
    add_m.set_two_buttons("Куда хочешь вернуться?",
                         "Я хочу повторить урок с баррэ",
                         "Я хочу посмотреть песню с баррэ",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S5.value)


def step4_4stage5v1(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Теперь сыграем сложную песню для закрепления навыков.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(config.Step_bot.STEP4_5_STAGE5.value)
  

  
def step4_4stage5v2(message, bot):
    set_link("Посмотреть видео", "https://www.youtube.com/watch?time_continue=1&v=FfH6FpPK4lY",
             "Давай повторим песню.\nНажми, чтобы посмотреть.",
             sleep_time, bot, message, 2)
    s_n.newStep.add(s_n.saveID.get())
    
    
def step4_5stage5v0(message, bot):
    add_m.set_three_buttons("Куда хочешь вернуться?",
                         "Я хочу повторить урок с баррэ",
                         "Я хочу посмотреть песню с баррэ",
                         "Я хочу посмотреть как ставть баррэ в разных позициях",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S5.value)



def step4_5stage5v1(message, bot):
    add_m.send_message("Поздравляю! Теперь ты достаточно знаешь и умеешь, чтобы впечатлить своих друзей и знакомых, теперь ты можешь сыграть в компании или себе для души. И еще ты теперь всегда можешь найти песню и выучить, которая тебе нравится",
                       bot, message)
    add_m.send_message("Спасибо, что прошел этот курс. В дальнейшем рассматривается разбор песен на гитаре.", bot, message)
    add_m.set_one_button("Можешь повторить урок.",
                          "Повторить урок", bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_6_STAGE5.value)
    
    
def step4_6stage5v1(message, bot):
    p_a_m.step3v5(message, bot)

def step4_6stage5v2(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу повторить урок с баррэ",
                         "Я хочу посмотреть песню с баррэ",
                         "Я хочу посмотреть как ставть баррэ в разных позициях",
                         "Я хочу повторить сложную песню",
                         "Выбрать другой этап",
                         bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S5.value)
    
    
def step4_6stage5_return(message, bot):
    add_m.set_five_buttons("Куда хочешь вернуться?",
                         "Я хочу повторить урок с баррэ",
                         "Я хочу посмотреть песню с баррэ",
                         "Я хочу посмотреть как ставть баррэ в разных позициях",
                         "Я хочу повторить сложную песню",
                         "Выбрать другой этап",
                         bot, message)
    s_n.newStep.add(config.Step_bot.STEP_BREAK_S5.value)