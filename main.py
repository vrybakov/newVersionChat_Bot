# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:06:28 2018

@author: 123
"""

import telebot
import processing_all_message as p_a_m
import processing_stage_one as p_a_o
import processing_stage_two as p_a_2
import processing_stage_three as p_a_3
import processing_stage_four as p_a_4
import processing_stage_five as p_a_5
import test_class
import additional_methods as add_m
import config
import StepNumber
#
#from flask import Flask, request
#import logging
#import os
#
##






bot = telebot.TeleBot(config.token)






#
#@bot.message_handler(commands = ['start'])
#def start_bot(message):
#    bot.send_message(message.chat.id, "Привет")



#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message.chat.id, message.text)




@bot.message_handler(commands = ['start'])
def start_bot(message):
    add_m.set_two_buttons("Привет!\nХочешь научиться играть на гитаре или проверить свои знания?", "Да, хочу научиться играть", "Хочу проверить свои знания", bot, message)
    
    StepNumber.newStep.add(config.Step_bot.STEP2.value) 



@bot.message_handler(commands = ['return'])
def return_bot(message):
    add_m.set_five_buttons("На какой этап хочешь вернуться?", 
                           "На первый",
                           "На второй",
                           "На третий",
                           "На четвертый",
                           "На пятый",
                           bot, message)
    StepNumber.saveID.add(StepNumber.newStep.get())
    StepNumber.newStep.add(config.Step_bot.STEP_RETURN.value)              



@bot.message_handler(content_types = ['text'])
def test(message):
    
    obj = test_class.TestProcessingStage(message, StepNumber.newStep.get(), bot, "", False)


    obj.answer_person("Да, хочу научиться играть", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v1)
    obj.answer_person("Хочу проверить свои знания", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v2)

    obj.answer_person("Интересно", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v1)
    obj.answer_person("Я уже знаю", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
    obj.answer_person("Всё, готово", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
    

    obj.answer_person("Интересно узнать", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v1)
    obj.answer_person("Не, я уже знаю как ее настроить", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)
    obj.answer_person("Можем пойти дальше", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)



#####################   ПЕРЕХОД НА ПЕРВЫЙ ЭТАП   ######################
    obj.answer_person("Хорошо", config.Step_bot.STEP3.value).set_work_step(p_a_m.step3v1)
    
    
    obj.answer_person("Давай", config.Step_bot.STEP4_STAGE1.value).set_work_step(p_a_o.step4stage1v1)
    obj.answer_person("Нет, я все же хочу вернуться назад", config.Step_bot.STEP4_STAGE1.value).set_work_step(p_a_o.step4stage1v2)
    
    obj.answer_person("Хочу посмотреть разбор гитары", config.Step_bot.STEP_BEGINING.value).set_work_step(p_a_o.stepBeginningV1)
    obj.answer_person("Хочу посмотреть, какими способами можно настроить гитару", config.Step_bot.STEP_BEGINING.value).set_work_step(p_a_o.stepBeginningV2)

    obj.answer_person("Всё, готово", config.Step_bot.STEP3.value).set_work_step(p_a_m.step3v1)


    obj.answer_person("Хорошо", config.Step_bot.STEP4_1_STAGE1.value).set_work_step(p_a_o.step4_1stage1v1)
    
    
    obj.answer_person("Это оказалось достаточно просто, пошли дальше", config.Step_bot.STEP4_2_STAGE1.value).set_work_step(p_a_o.step4_2stage1v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_3_STAGE1.value).set_work_step(p_a_o.step4_3stage1v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_3_STAGE1.value).set_work_step(p_a_o.step4_3stage1v0)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_4_STAGE1.value).set_work_step(p_a_o.step4_4stage1v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_4_STAGE1.value).set_work_step(p_a_o.step4_4stage1v0)
    
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_5_STAGE1.value).set_work_step(p_a_o.step4_5stage1v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_5_STAGE1.value).set_work_step(p_a_o.step4_5stage1v0)
    
    
    obj.answer_person("Не, я хочу перейти на второй этап", config.Step_bot.STEP4_6_STAGE1.value).set_work_step(p_a_o.step4_6stage1v1)
    
    obj.answer_person("Думаю, что стоит повторить предыдущее", config.Step_bot.STEP4_6_STAGE1.value).set_work_step(p_a_o.step4_6stage1v2)

    
    obj.answer_person("Я хочу посмотреть видео о том, как правильно держать гитару", config.Step_bot.STEP_BREAK.value).set_work_step(p_a_o.step4_1stage1v2)
    obj.answer_person("Я хочу посмотреть видео про парвую руку", config.Step_bot.STEP_BREAK.value).set_work_step(p_a_o.step4_2stage1v2)
    obj.answer_person("Хочу еще раз посмотреть как зажимать струны", config.Step_bot.STEP_BREAK.value).set_work_step(p_a_o.step4_3stage1v2)
    obj.answer_person("Хочу посмореть как играется \"В траве сидел кузнечик\"", config.Step_bot.STEP_BREAK.value).set_work_step(p_a_o.step4_4stage1v2)
    obj.answer_person("Хочу перейти на второй этап", config.Step_bot.STEP_BREAK.value).set_work_step(p_a_o.step4_6stage1v1)
    
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_6_STAGE1.value).set_work_step(p_a_o.step4_6stage1v2)

    obj.answer_person("Дальше", config.Step_bot.STEP4_6_STAGE1.value).set_work_step(p_a_m.step3v2)
#####################   КОНЕЦ ПЕРВОГО ЭТАПА   ######################

    
  
    
#####################   ПЕРЕХОД НА ВТОРОЙ ЭТАП   ######################
    

    
    
    obj.answer_person("Далее", config.Step_bot.STEP4_STAGE2.value).set_work_step(p_a_2.step4stage2v1)


    obj.answer_person("Хорошо", config.Step_bot.STEP4_1_STAGE2.value).set_work_step(p_a_2.step4_2stage2v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_2_STAGE2.value).set_work_step(p_a_2.step4_2stage2v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_3_STAGE2.value).set_work_step(p_a_2.step4_3stage2v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_3_STAGE2.value).set_work_step(p_a_2.step4_3stage2v0)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_4_STAGE2.value).set_work_step(p_a_2.step4_4stage2v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_4_STAGE2.value).set_work_step(p_a_2.step4_4stage2v0)
    
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_5_STAGE2.value).set_work_step(p_a_2.step4_5stage2v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_5_STAGE2.value).set_work_step(p_a_2.step4_5stage2v0)
    
    
    obj.answer_person("Не, я хочу перейти на третий этап", config.Step_bot.STEP4_6_STAGE2.value).set_work_step(p_a_2.step4_6stage2v1)
    
    obj.answer_person("Думаю, что стоит повторить предыдущее", config.Step_bot.STEP4_6_STAGE2.value).set_work_step(p_a_2.step4_6stage2v2)

    
    obj.answer_person("Я хочу посмотреть видео о том, как правильно играть бой", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_2.step4_1stage2v2)
    obj.answer_person("Я хочу посмотреть видео как ставяться аккорды", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_2.step4_2stage2v2)
    obj.answer_person("Хочу еще раз посмотреть, что такое аппликатура", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_2.step4_3stage2v2)
    obj.answer_person("Хочу посмореть как играется песня", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_2.step4_4stage2v2)
    obj.answer_person("Хочу перейти на третий этап", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_2.step4_6stage2v1)
    obj.answer_person("Выбрать другой этап", config.Step_bot.STEP_BREAK_S2.value).set_work_step(p_a_m.return_to_previous_stage)
    
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_6_STAGE2.value).set_work_step(p_a_2.step4_6stage2v2)

    obj.answer_person("Дальше", config.Step_bot.STEP4_6_STAGE2.value).set_work_step(p_a_m.step3v3)
    
#####################   КОНЕЦ ВТОРОГО ЭТАПА   ######################   
    
    
    
    
#####################   ПЕРЕХОД НА ТРЕТИЙ ЭТАП   ######################
    

    
    
    obj.answer_person("Далее", config.Step_bot.STEP4_STAGE3.value).set_work_step(p_a_3.step4stage3v1)


    obj.answer_person("Хорошо", config.Step_bot.STEP4_1_STAGE3.value).set_work_step(p_a_3.step4_2stage3v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_2_STAGE3.value).set_work_step(p_a_3.step4_2stage3v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_3_STAGE3.value).set_work_step(p_a_3.step4_3stage3v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_3_STAGE3.value).set_work_step(p_a_3.step4_3stage3v0)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_4_STAGE3.value).set_work_step(p_a_3.step4_4stage3v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_4_STAGE3.value).set_work_step(p_a_3.step4_4stage3v0)
    
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_5_STAGE3.value).set_work_step(p_a_3.step4_5stage3v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_5_STAGE3.value).set_work_step(p_a_3.step4_5stage3v0)
    
    
    obj.answer_person("Не, я хочу перейти на четвертый этап", config.Step_bot.STEP4_6_STAGE3.value).set_work_step(p_a_3.step4_6stage3v1)
    
    obj.answer_person("Думаю, что стоит повторить предыдущее", config.Step_bot.STEP4_6_STAGE3.value).set_work_step(p_a_3.step4_6stage3v2)

    
    obj.answer_person("Я хочу посмотреть разборку табулатуры", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_3.step4_1stage3v2)
    obj.answer_person("Я хочу посмотреть бой \"шестерка\"", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_3.step4_2stage3v2)
    obj.answer_person("Хочу еще раз посмотреть как играть перебором", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_3.step4_3stage3v2)
    obj.answer_person("Хочу посмореть как играется песня", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_3.step4_4stage3v2)
    obj.answer_person("Хочу перейти на четвертый этап", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_3.step4_6stage3v1)
    obj.answer_person("Выбрать другой этап", config.Step_bot.STEP_BREAK_S3.value).set_work_step(p_a_m.return_to_previous_stage)
    
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_6_STAGE3.value).set_work_step(p_a_3.step4_6stage3v2)
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_6_STAGE3.value).set_work_step(p_a_m.step3v4)

    
    
#####################   КОНЕЦ ТРЕТЬЕГО ЭТАПА   ######################    
    
    
#####################   ПЕРЕХОД НА ЧЕТВЕРТЫЙ ЭТАП   ######################
    
    
    
    obj.answer_person("Далее", config.Step_bot.STEP4_STAGE4.value).set_work_step(p_a_4.step4stage4v1)


    obj.answer_person("Хорошо", config.Step_bot.STEP4_1_STAGE4.value).set_work_step(p_a_4.step4_2stage4v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_2_STAGE4.value).set_work_step(p_a_4.step4_2stage4v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_3_STAGE4.value).set_work_step(p_a_4.step4_3stage4v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_3_STAGE4.value).set_work_step(p_a_4.step4_3stage4v0)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_4_STAGE4.value).set_work_step(p_a_4.step4_4stage4v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_4_STAGE4.value).set_work_step(p_a_4.step4_4stage4v0)
    
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_5_STAGE4.value).set_work_step(p_a_4.step4_5stage4v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_5_STAGE4.value).set_work_step(p_a_4.step4_5stage4v0)
    
    
    obj.answer_person("Не, я хочу перейти на пятый этап", config.Step_bot.STEP4_6_STAGE4.value).set_work_step(p_a_4.step4_6stage4v1)
    
    obj.answer_person("Думаю, что стоит повторить предыдущее", config.Step_bot.STEP4_6_STAGE4.value).set_work_step(p_a_4.step4_6stage4v2)

    
    obj.answer_person("Я хочу посмотреть перебор \"Восьмерка\"", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_4.step4_1stage4v2)
    obj.answer_person("Я хочу посмотреть сложносокращенный перебор", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_4.step4_2stage4v2)
    obj.answer_person("Я хочу посмотреть перебор \"Щипок\"", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_4.step4_3stage4v2)
    obj.answer_person("Я хочу повторить как играется песня", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_4.step4_4stage4v2)
    obj.answer_person("Хочу перейти на четвертый этап", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_4.step4_6stage4v1)
    obj.answer_person("Выбрать другой этап", config.Step_bot.STEP_BREAK_S4.value).set_work_step(p_a_m.return_to_previous_stage)
    
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_6_STAGE4.value).set_work_step(p_a_4.step4_6stage4v2)

    obj.answer_person("Дальше", config.Step_bot.STEP4_6_STAGE4.value).set_work_step(p_a_m.step3v5)
    
    
#####################   КОНЕЦ ЧЕТВЕРТОГО ЭТАПА   ######################  
    
    
#####################   ПЕРЕХОД НА ПЯТЫЙ ЭТАП   ######################
    
    obj.answer_person("Далее", config.Step_bot.STEP4_STAGE5.value).set_work_step(p_a_5.step4stage5v1)


    obj.answer_person("Хорошо", config.Step_bot.STEP4_1_STAGE5.value).set_work_step(p_a_5.step4_2stage5v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_2_STAGE5.value).set_work_step(p_a_5.step4_2stage5v1)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_3_STAGE5.value).set_work_step(p_a_5.step4_3stage5v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_3_STAGE5.value).set_work_step(p_a_5.step4_3stage5v0)
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_4_STAGE5.value).set_work_step(p_a_5.step4_4stage5v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_4_STAGE5.value).set_work_step(p_a_5.step4_4stage5v0)
    
    
    
    obj.answer_person("Дальше", config.Step_bot.STEP4_5_STAGE5.value).set_work_step(p_a_5.step4_5stage5v1)
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_5_STAGE5.value).set_work_step(p_a_5.step4_5stage5v0)
    
    
    obj.answer_person("Не, я хочу перейти на четвертый этап", config.Step_bot.STEP4_6_STAGE5.value).set_work_step(p_a_5.step4_6stage5v1)
    
    obj.answer_person("Думаю, что стоит повторить предыдущее", config.Step_bot.STEP4_6_STAGE5.value).set_work_step(p_a_5.step4_6stage5v2)

    
    obj.answer_person("Я хочу повторить урок с баррэ", config.Step_bot.STEP_BREAK_S5.value).set_work_step(p_a_5.step4_1stage5v2)
    obj.answer_person("Я хочу посмотреть песню с баррэ", config.Step_bot.STEP_BREAK_S5.value).set_work_step(p_a_5.step4_2stage5v2)
    obj.answer_person("Я хочу посмотреть как ставть баррэ в разных позициях", config.Step_bot.STEP_BREAK_S5.value).set_work_step(p_a_5.step4_3stage5v2)
    obj.answer_person("Я хочу повторить сложную песню", config.Step_bot.STEP_BREAK_S5.value).set_work_step(p_a_5.step4_4stage5v2)
    obj.answer_person("Выбрать другой этап", config.Step_bot.STEP_BREAK_S5.value).set_work_step(p_a_m.return_to_previous_stage)
    
    obj.answer_person("Хочу вернуться назад", config.Step_bot.STEP4_6_STAGE5.value).set_work_step(p_a_5.step4_6stage5v2)
    
    obj.answer_person("Повторить урок", config.Step_bot.STEP4_6_STAGE5.value).set_work_step(p_a_5.step4_6stage5v2)

    obj.answer_person("Дальше", config.Step_bot.STEP4_6_STAGE5.value).set_work_step(p_a_m.return_to_previous_stage)
    
    
    
#####################   КОНЕЦ ПЯТОГО ЭТАПА   ######################  
    
    
    
    
    
    
#####################   ВОЗВРАЩЕНИЕ   ######################
    
    obj.answer_person("На первый", config.Step_bot.STEP_RETURN.value).set_work_step(p_a_o.step4_6stage1_return)
    obj.answer_person("На второй", config.Step_bot.STEP_RETURN.value).set_work_step(p_a_2.step4_6stage2_return)
    obj.answer_person("На третий", config.Step_bot.STEP_RETURN.value).set_work_step(p_a_3.step4_6stage3_return)
    obj.answer_person("На четвертый", config.Step_bot.STEP_RETURN.value).set_work_step(p_a_4.step4_6stage4_return)
    obj.answer_person("На пятый", config.Step_bot.STEP_RETURN.value).set_work_step(p_a_5.step4_6stage5_return)
    
#####################   ВОЗВРАЩЕНИЕ   ######################  

    
    obj.unsuitable()

    

## Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
#if "HEROKU" in list(os.environ.keys()):
#    logger = telebot.logger
#    telebot.logger.setLevel(logging.INFO)
#
#    server = Flask(__name__)
#    @server.route("/bot", methods=['POST'])
#    def getMessage():
#        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#        return "!", 200
#    @server.route("/")
#    def webhook():
#        bot.remove_webhook()
#        bot.set_webhook(url="https://calm-ravine-51322.herokuapp.com") # этот url нужно заменить на url вашего Хероку приложения
#        return "?", 200
#    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
#else:
#    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
#    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
#    bot.remove_webhook()
#    bot.polling(none_stop=True)

#
#
if __name__ == '__main__':
    bot.polling(none_stop = True) 