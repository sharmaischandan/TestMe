def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
temp_convert("xyz");


def functionName( level ):
    if level < 1:
      raise "Invalid level!", level

try:
    functionName(-1)
except BaseException , e:
    print "Exception is: ", e.args


class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg

try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args