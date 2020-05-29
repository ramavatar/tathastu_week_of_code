from collections import OrderedDict
def Duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
print(Duplicate(input("ENTER string:")))   
