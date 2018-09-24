#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = """\n""".join(['Created by : ','Markus Paramahasti <markus@volantis.io>'])

import logging

__all__ = ["test"]



logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
logger.addHandler(handler)



def test(a : float, b : float) -> float:
  
  return a+b


class Testing(object):
  
  __distance__ = 10.
  
  def __init__(self, name : str, address : str):
    self.name = name
    self.address = address
    self.email = name+"@company.com"
  
  def _getName(self):
    logger.info("Get the name... --> %s", self.name)
    return self.name
  
  def _getAddress(self):
    logger.info("Get the address... --> %s", self.address)
    return self.address
  
  def getEmail(self):
    return self.name+" has an email adress "+self.email
    
  
  

    





if __name__ == "__main__":
  
  a = Testing("Thomas", "Depok")
  
  a._getName()
  a._getAddress()
  a.getEmail()
  
  
  t = test(23, 34)
  u = test(90, 23)
  
  print ("ini t --> ", t)
  print ("ini u --> ", u)
  
  
  
