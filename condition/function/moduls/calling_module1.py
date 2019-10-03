#here I am calling module one. which is in same folder
#3 ways we can call our module

# 1. import module as namespace. when we call funtion that time need to say the module name also. 
import module1
module1.print_time('hello world')

#2. import every thing from the module
from module1 import *
print_time('everything imported from module')

#3 single funtion import from a module

from module1 import print_time
print_time('single funtion called from a module ')