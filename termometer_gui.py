#!/usr/local/bin/python3

from tkinter import Tk, Frame, LabelFrame, Button, Label, LEFT, CENTER, Radiobutton, W, X, StringVar, Entry, DISABLED
from termo_type import TermoType

class TermometerInterface(Tk):
  """ """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  this class defines how termometer application interface looks
  like. this class is for collecting application input and 
  output to user.
  """""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
  
  def __init__(self, *args, **kwargs):
    super(TermometerInterface, self).__init__(*args, **kwargs)
    self.title('Termometer Conversion') 
    width = 500
    height = 300
    x = ( self.winfo_screenwidth() - width ) / 2
    y = 100 #( layar.winfo_screenheight() - height ) / 2
    self.geometry('%dx%d+%d+%d' % (width, height, x, y))

    fr_main_term = Frame(self)

    lbfr_current_term = LabelFrame( fr_main_term, text='Current Termometer') 
  
    lb_termometer_type1 = Label( lbfr_current_term, text='Termometer Type :')

    termo_type = TermoType()

    self.__current_termo = StringVar()
    self.__current_termo.set('1')
    rd_celcius1 = Radiobutton( lbfr_current_term, value=termo_type.celcius_termo, variable=self.__current_termo, text='Celcius')
    rd_fahreinheit1 = Radiobutton( lbfr_current_term, value=termo_type.fahreinheit_termo, variable=self.__current_termo, text='Fahreinheit')
    rd_riomer1 = Radiobutton( lbfr_current_term, value=termo_type.riomer_termo, variable=self.__current_termo, text='Riomer')
    rd_kelvin1 = Radiobutton( lbfr_current_term, value=termo_type.kelvin_termo, variable=self.__current_termo, text='Kelvin')

    self.__temperature = StringVar()
    self.__temperature.set('0')
    lb_temperature = Label( lbfr_current_term, text='Termperature Value :')
    ent_temperature = Entry( lbfr_current_term, textvariable=self.__temperature, width=18, justify=CENTER)
    
    
    lb_termometer_type1.pack(anchor=W, padx=(10, 30), pady=(10,5))
    rd_celcius1.pack(anchor=W)
    rd_fahreinheit1.pack(anchor=W)
    rd_riomer1.pack(anchor=W)
    rd_kelvin1.pack(anchor=W)
    lb_temperature.pack(pady=(10,0))
    ent_temperature.pack(pady=(0,10))


    lbfr_choosen_term = LabelFrame( fr_main_term, text='Converting to')

    lb_termometer_type2 = Label( lbfr_choosen_term, text='Termometer Type :')

    self.__convert_to_termo = StringVar()
    self.__convert_to_termo.set('3')
    rd_celcius2 = Radiobutton( lbfr_choosen_term, value=termo_type.celcius_termo, variable=self.__convert_to_termo, text='Celcius')
    rd_fahreinheit2 = Radiobutton( lbfr_choosen_term, value=termo_type.fahreinheit_termo, variable=self.__convert_to_termo, text='Fahreinheit')
    rd_riomer2 = Radiobutton( lbfr_choosen_term, value=termo_type.riomer_termo, variable=self.__convert_to_termo, text='Riomer')
    rd_kelvin2 = Radiobutton( lbfr_choosen_term, value=termo_type.kelvin_termo, variable=self.__convert_to_termo, text='Kelvin')

    self.__result = StringVar()
    self.__result.set('0')
    lb_result = Label( lbfr_choosen_term, text='Converstion Result :')
    ent_result = Entry( lbfr_choosen_term, textvariable=self.__result, width=18, justify=CENTER, state=DISABLED)
        
    lb_termometer_type2.pack(anchor=W, padx=(10, 30), pady=(10,5))
    rd_celcius2.pack(anchor=W)
    rd_fahreinheit2.pack(anchor=W)
    rd_riomer2.pack(anchor=W)
    rd_kelvin2.pack(anchor=W)
    lb_result.pack(pady=(10,0))
    ent_result.pack(pady=(0,10))

    lbfr_current_term.pack(side=LEFT, padx=(0,20)) 
    lbfr_choosen_term.pack(side=LEFT)

    fr_conversion = Frame(self)
    bt_convert = Button( fr_conversion, text='Convert', command= self.__convert)
    bt_convert.pack()          

    fr_main_term.pack(pady=(30,10))
    fr_conversion.pack()

    self.__do_conversion = lambda : print('conversion from termometer_gui')

  def __convert(self):
    self.__do_conversion()

  def get_current_termo(self):
    return self.__current_termo.get()

  def get_convert_to_termo(self):
    return self.__convert_to_termo.get()

  def get_temperature(self):
    return self.__temperature.get()

  def set_result(self, result):
    self.__result.set(result)

  def set_do_conversion(self, do_conversion): 
    self.__do_conversion = do_conversion 

if __name__ == '__main__':
  layar = TermometerInterface()

  layar.mainloop()  
