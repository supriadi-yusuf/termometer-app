#!/usr/local/bin/python3

from termometer import Termometer
from termometer_gui import TermometerInterface
from tkinter import messagebox

def do_conversion(termometer, termometer_interface):
  current_term = termometer_interface.get_current_termo()
  convert_to_term = termometer_interface.get_convert_to_termo()
  temperature = termometer_interface.get_temperature()

  # convert temperature from string to number
  try:
    temperature = float(temperature)
  except:
    messagebox.showerror('Error', 'Please type a correct number!')
  else:
    result = termometer.convert_temperature( current_term, convert_to_term, temperature)
    result = "%.2f" % (result)
    termometer_interface.set_result(result)

if __name__ == '__main__':
  termometer = Termometer()
  termometer_interface = TermometerInterface()

  termometer_interface.set_do_conversion(lambda:do_conversion(termometer, termometer_interface))

  termometer_interface.mainloop()
