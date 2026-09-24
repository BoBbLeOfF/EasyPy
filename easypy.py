''' 
                                      
██████  ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ █████▄ ▄▄ ▄▄ 
██▄▄   ██▀██ ███▄▄ ▀███▀ ██▄▄█▀ ▀███▀ 
██▄▄▄▄ ██▀██ ▄▄██▀   █   ██       █   
             by BoBbLeOfF                        '''


''' 
    like print but quicker to type 
       ''' 


def p(x):

  print(x)







'''
    date and time tools

        '''

import datetime
import time 

def year_():

  current_year = datetime.datetime.now()
  print(current_year.year)
  

def day_name_():

  dayname = datetime.datetime.now()
  print(dayname.strftime("%A"))

def month_num_():

  month_number = datetime.datetime.now()
  print(month_number.month)

def month_str_():

  month_string = datetime.datetime.now()
  print(month_string.strftime("%B"))

def dmy_(s):

  x = datetime.datetime.now()

  d = str(x.day)
  m = str(x.month)
  y = str(x.year)

  print(d + s + m + s + y)


def mdy_(s):

  x = datetime.datetime.now()

  m = str(x.month)
  d = str(x.day)
  y = str(x.year)

  print(m + s + d + s + y)

def time_stamp_():

  now = datetime.datetime.now()
  print(now.strftime("%H:%M:%S"))

def time_live_():##

  

  while True:
    print (time.strftime("%H:%M:%S"), end="", flush=True)
    print("\r", end="", flush=True)
    time.sleep(1)



