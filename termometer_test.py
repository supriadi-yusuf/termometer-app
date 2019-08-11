#!/usr/local/bin/python3
"""""""""""""""""""""""""""""""""""""""""""""""
for more informaton about testing :
https://docs.python.org/3/library/unittest.html

    if src_term == my_termo.celcius_termo:
      result = temperature 
    elif src_term == my_termo.fahreinheit_termo:
      result = self.fahreinheit_to_celcius(temperature)
    elif src_term == my_termo.riomer_termo:
      result = self.riomer_to_celcius(temperature)
    elif src_term == my_termo.kelvin_termo: 

"""""""""""""""""""""""""""""""""""""""""""""""

import unittest
from termometer import Termometer

my_termo = Termometer()

class TermometerTest(unittest.TestCase): # class must inherit unittest.TestCase

  def test_celcius_celcius(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.celcius_termo, my_termo.celcius_termo, 100), 100) 

  def test_celcius_fahreinheit(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.celcius_termo, my_termo.fahreinheit_termo, 100), 212) 

  def test_celcius_riomer(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.celcius_termo, my_termo.riomer_termo, 100), 80) 

  def test_celcius_kelvin(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.celcius_termo, my_termo.kelvin_termo, 100), 373) 

  def test_fahreinheit_fahreinheit(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.fahreinheit_termo, my_termo.fahreinheit_termo, 212), 212) 

  def test_fahreinheit_celcius(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.fahreinheit_termo, my_termo.celcius_termo, 212), 100) 

  def test_fahreinheit_riomer(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.fahreinheit_termo, my_termo.riomer_termo, 212), 80) 

  def test_fahreinheit_kelvin(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.fahreinheit_termo, my_termo.kelvin_termo, 212), 373) 

  def test_riomer_riomer(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.riomer_termo, my_termo.riomer_termo, 80), 80) 

  def test_riomer_celcius(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.riomer_termo, my_termo.celcius_termo, 80), 100) 

  def test_riomer_fahreinheit(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.riomer_termo, my_termo.fahreinheit_termo, 80), 212) 

  def test_riomer_kelvin(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.riomer_termo, my_termo.kelvin_termo, 80), 373) 

  def test_kelvin_kelvin(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.kelvin_termo, my_termo.kelvin_termo, 373), 373) 

  def test_kelvin_celcius(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.kelvin_termo, my_termo.celcius_termo, 373), 100) 

  def test_kelvin_fahreinheit(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.kelvin_termo, my_termo.fahreinheit_termo, 373), 212) 

  def test_kelvin_riomer(self): # name of method begins with 'test'
    self.assertEqual(my_termo.convert_temperature(my_termo.kelvin_termo, my_termo.riomer_termo, 373), 80) 

if __name__ == '__main__':
  unittest.main()

# python -m unittest module1 module2 module3
# python -m unittest module1.Class1
# python -m unittest module1.Class1.method1

# python -m unittest -v termometer_test.py
