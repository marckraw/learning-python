import sys
from mymodule import divide
# import mymodule - importing the whole file not only function

print(divide(10,2))

print(__name__)


print()
print()
###

print(sys.path)
print(sys.modules)