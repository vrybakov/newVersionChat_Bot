# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:25:36 2018

@author: 123
"""





class StepNumber:
    def __init__(self, f):
        self.f = f
    
    def add(self, name_button):
        file_id = open(self.f, "w")
        file_id.write(name_button)
        file_id.close()
        
    def get(self):
        file_id = open(self.f)
        _get_step = file_id.read()
        file_id.close()
        return _get_step
newStep = StepNumber("file_id.ini")
saveID = StepNumber("save_id.ini")