import time
from time import gmtime, strftime
target_time = ['hour', 'min' , 'sec', 'day' ]#input from bot
while True:
  rawStr = time.strftime("%a %d %b %Y %I %M %S %p", time.gmtime())
  strLst = rawStr.split()
class timer():
  if 




