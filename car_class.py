#!/usr/bin/env/ python

class Car(object):
  '''
     Car class made from tests description
  '''
  def __init__(self, name = 'General', model = 'GM', car_type = 'saloon'):
    '''
      initializer method
    '''
    self.model = model
    self.name = name
    self.car_type = car_type

    if self.name == 'Porshe' or self.name == 'Koenigsegg':
      self.num_of_doors = 2
    else:
      self.num_of_doors = 4

    if self.car_type == 'trailer':
      self.num_of_wheels = 8
    else:
      self.num_of_wheels = 4
    self.speed = 0

  def is_saloon(self):
    '''
    boolean method
    '''
    if self.car_type == 'saloon':
      return True
    else:
      return False

  def drive(self, num):
    '''
      drive method
    '''
    if self.num_of_wheels > 4:
      self.speed = num * 11
    else:
       self.speed = 10 ** num
    return self