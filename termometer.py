#!/usr/local/bin/python3

from termo_type import TermoType

class Termometer(TermoType):

  @staticmethod
  def celcius_to_riomer(temperature):
    return 4 * temperature / 5

  @staticmethod
  def celcius_to_fahreinheit(temperature):
    return 9 * temperature / 5 + 32

  @staticmethod
  def celcius_to_kelvin(temperature):
    return temperature + 273

  @staticmethod
  def riomer_to_celcius(temperature):
    return 5 * temperature / 4

  @staticmethod
  def fahreinheit_to_celcius(temperature):
    return ( temperature - 32) * 5 / 9 

  @staticmethod
  def kelvin_to_celcius(temperature):
    return temperature - 273

  def convert_temperature(self, src_term, dst_term, temperature):
    # convert temperature to celcius degree
    if src_term == self.celcius_termo:
      result = temperature 
    elif src_term == self.fahreinheit_termo:
      result = self.fahreinheit_to_celcius(temperature)
    elif src_term == self.riomer_termo:
      result = self.riomer_to_celcius(temperature)
    elif src_term == self.kelvin_termo: 
      result = self.kelvin_to_celcius(temperature) 
    else:
      raise Exception('Unsupported termometer!')

    # convert celcius degree to ...
    if dst_term == self.celcius_termo:
      pass
    elif dst_term == self.fahreinheit_termo:
      result = self.celcius_to_fahreinheit(result)
    elif dst_term == self.riomer_termo:
      result = self.celcius_to_riomer(result)
    elif dst_term == self.kelvin_termo: 
      result = self.celcius_to_kelvin(result)
    else:
      raise Exception('Unsupported termometer!')

    return result   

if __name__ == '__main__':
  my_termo = Termometer()

  answers = [my_termo.celcius_termo, my_termo.fahreinheit_termo, my_termo.riomer_termo, my_termo.kelvin_termo]
  answers2 = [int(answers[0]), int(answers[1]), int(answers[2]), int(answers[3])]

  print("you can convert termometer from / to : ")
  print("1. Celcius")
  print("2. Fahreinheit")
  print("3. Riomer")
  print("4. Kelvin") 
  print("which termometer do you want to convert ?")
  src_term = input("your answer " + str(tuple(answers2)) + " : ") 
  while src_term not in answers:
    src_term = input("Wrong answer. Please choose " + str(tuple(answers2)) + " : ")

  answers.remove(src_term)
  answers2.remove(int(src_term))
  
  print("which termometer do you want to convert to ?")
  dst_term = input("your answer " + str(tuple(answers2)) + " : ") 
  while dst_term not in answers:
    dst_term = input("Wrong answer. Please choose " + str(tuple(answers2)) + " : ")  

  temperature = input("temperatur ? ( please type number ) : ")
  while 1:
    correct_temp = True
    try:
      temperature = float(temperature)
    except :
      correct_temp = False

    if correct_temp :
       break
    
    temperature = input("wrong answer ! ( please type number ) : ")

  result = my_termo.convert_temperature( src_term, dst_term, temperature)

  print('Result : %8.2f' % (result))

