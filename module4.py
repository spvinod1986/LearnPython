# option 1
from package1.module3 import calculate_order, calculate_invoice
# option 2
from package1 import module3
from package1.subpackage1 import module5

# option 1
calculate_invoice()
calculate_order()

# option 2
module3.calculate_invoice()
module3.calculate_order()
module5.calculate_deliveryfee()
module5.calculate_servicefee()

print(dir(module3))
