from class_function import OrderInjection as OI
from config import config



order1 = OI(VN="1234", doctor_name="เติมพงศ์", medication_input="Kenacort 40 mg", 
               location_injection="knee", side="ขวา")
message = order1.message(config)
print(message)