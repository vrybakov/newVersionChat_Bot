# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:06:54 2018

@author: 123
"""

import additional_methods as add_m
import config
import StepNumber as s_n


def step1v1(message, bot):
    add_m.send_message("Отлично!\nДля того, чтобы начать обучение, нам необходимо узнать твой навык игры на гитаре.", bot, message)
    add_m.set_two_buttons("Можем устроить проверку или сразу начать обучение с нуля\nЧто выберешь?",
                          "Приступим к обучению с нуля",
                          "Можно проверить мой уровень", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2.value)      
        
def step1v2(message, bot):
    bot.send_message(message.chat.id, "Твое дело.")
    
###   
    

def step2v1(message, bot):
    add_m.set_two_buttons("Давай я тебе расскажу как устроена гитара и как ее настроить, если тебе это интересно", "Интересно", "Я уже знаю", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_1.value)    
        
def step2v2(message, bot):
    bot.send_message(message.chat.id, "Пройдем тесты. (не рабоает)")
###
    
def step2_1v1(message, bot):
#    bot.send_message(message.chat.id, "На этом изображение подробно показано строение гитары")
#    photo = open('image/guitar structure.jpg', 'rb') #открывает изображение
#    bot.send_photo(message.chat.id, photo)    #отправляет сообщение с изображением
#    bot.send_message(message.chat.id, "В этом видо подробно показано строение гитары")
#    video = open('image/VID_20170418_152255.mp4', 'rb')
#    bot.send_video(message.chat.id, video)
    add_m.send_link("Посмореть видео", "https://www.youtube.com/watch?v=G3e_svu8PCQ",
                "Нажми сюда, чтобы посмотреть строение гитары.", bot, message)
    add_m.set_one_button("Скажи, когда разберешься.",
                         "Всё, готово", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_1.value)    
        
def step2_1v2(message, bot):
    add_m.set_two_buttons("Хочешь узнать, как можно настроить гитару?",
                          "Интересно узнать",
                          "Не, я уже знаю как ее настроить", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_2.value)                          
    
###
def step2_2v1(message, bot):
    add_m.send_link("Посмореть видео", "https://www.youtube.com/watch?v=iAZkTAc_2E0",
                    "Нажми сюда, чтобы посмотреть, какие есть методы.", bot, message)
    add_m.set_one_button("Если разобрались, то скажи, что можно идти дальше.",
                         "Можем пойти дальше", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_2.value)    
        
def step2_2v2(message, bot):
    add_m.set_one_button("Тогда далее поэтапно будем учиться играть.\nНаш курс буде разбит на 5 этапов от простого к сложному.",
                         "Хорошо", bot, message)
    s_n.newStep.add(config.Step_bot.STEP3.value)    
    
        
###
def step3v1(message, bot):
    add_m.set_two_buttons("Давай перейдем к первому этапу.",
                          "Давай",
                          "Нет, я все же хочу вернуться назад", bot, message)
    s_n.saveID.add(s_n.newStep.get())
    s_n.newStep.add(config.Step_bot.STEP4_STAGE1.value)    
    
def step3v2(message, bot):
    add_m.send_message("Я рад, что ты уже на втором этапе, дальше буде только интереснее.", bot, message)
    add_m.set_one_button("Нажми далее, чтобы мы смогли приступить.",
                          "Далее",
                          bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_STAGE2.value) 
    
    
def step3v3(message, bot):
    add_m.send_message("Раз ты уже на этом этапе, значит ты уже можешь сыграть простую песню, это хороший результат.", bot, message)
    add_m.set_one_button("Нажми далее, чтобы мы смогли приступить.",
                          "Далее",
                          bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_STAGE3.value)
    
    
    
def step3v4(message, bot):
    add_m.send_message("Поздравляю! Уже четвертый этап начинается.", bot, message)
    add_m.set_one_button("Нажми далее, чтобы мы смогли приступить.",
                          "Далее",
                          bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_STAGE4.value)  
    
def step3v5(message, bot):
    add_m.send_message("Остался последний этап в нашем курсе обучения.", bot, message)
    add_m.set_one_button("Нажми далее, чтобы мы смогли приступить.",
                          "Далее",
                          bot, message)
    s_n.newStep.add(config.Step_bot.STEP4_STAGE5.value) 
    
    
def return_to_previous_stage(message, bot):
    if s_n.saveID.get() == config.Step_bot.STEP_BREAK.value:
        add_m.set_one_button("На какой этап хочешь вернуться?", 
                       "На первый",
                       bot, message)
    if s_n.newStep.get() == config.Step_bot.STEP_BREAK_S2.value:
        add_m.set_two_buttons("На какой этап хочешь вернуться?", 
                       "На первый",
                       "На второй",
                       bot, message)
    if s_n.newStep.get() == config.Step_bot.STEP_BREAK_S3.value:
        add_m.set_three_buttons("На какой этап хочешь вернуться?", 
                       "На первый",
                       "На второй",
                       "На третий",
                       bot, message)
    if s_n.newStep.get() == config.Step_bot.STEP_BREAK_S4.value:
        add_m.set_four_buttons("На какой этап хочешь вернуться?", 
                       "На первый",
                       "На второй",
                       "На третий",
                       "На четвертый",
                       bot, message)
    if s_n.newStep.get() == config.Step_bot.STEP_BREAK_S5.value:
        add_m.set_five_buttons("На какой этап хочешь вернуться?", 
                       "На первый",
                       "На второй",
                       "На третий",
                       "На четвертый",
                       "На пятый",
                       bot, message)                     
    if s_n.newStep.get() == config.Step_bot.STEP4_6_STAGE5.value:
        add_m.set_five_buttons("На какой этап хочешь вернуться?", 
                       "На первый",
                       "На второй",
                       "На третий",
                       "На четвертый",
                       "На пятый",
                       bot, message)
    s_n.newStep.add(config.Step_bot.STEP_RETURN.value)
### 
def unsuitable(message, bot):
    bot.send_message(message.chat.id, "Что-то не то. Попробуй повторить.")