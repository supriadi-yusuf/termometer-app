#!/usr/local/bin/python3

######################################################################################
# this script shows how to get inputs from termometer GUI and pass the inputs into
# Termometer class for further processing until result is returned. Then the result
# is passed it into termometer GUI to be displayed to user
######################################################################################

from termometer import Termometer
from termometer_gui import TermometerInterface

def do_conversion(termometer, termometer_interface):
  current_term = termometer_interface.get_current_termo()
  convert_to_term = termometer_interface.get_convert_to_termo()
  temperature = termometer_interface.get_temperature()

  # convert temperature from string to number
  try:
    temperature = float(temperature)
  except:
    termometer_interface.show_error() # it should not be allowed. fix this!
  else:
    result = termometer.convert_temperature( current_term, convert_to_term, temperature)
    result = "%.2f" % (result)
    termometer_interface.set_result(result)

if __name__ == '__main__':
  termometer = Termometer()
  termometer_interface = TermometerInterface()

  # assign routine to do conversion
  termometer_interface.set_do_conversion(lambda:do_conversion(termometer, termometer_interface))

  termometer_interface.mainloop()
