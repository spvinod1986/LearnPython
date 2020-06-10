import sys
# option 1
from module1 import calculate_tax, calculate_shipping
# option 2
import module1

# no performance or any difference between option 1 and 2. Just personal preference.


# option 1
calculate_shipping()
calculate_tax()

# option 2
module1.calculate_tax()
module1.calculate_shipping()

print(sys.path)
