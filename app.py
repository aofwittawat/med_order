from config import config

class Order:
    
    def __init__(self, VN, doctor_name, medication_input, location_injection, side):
        self._VN = VN
        self._doctor_name = doctor_name
        self._medication_input = medication_input
        self._location_injection = location_injection
        self._side = side
       
            
    def order(self, config):
        for k in config.keys():
            if k == self._doctor_name:
                for k2 in config[k].keys():
                    if k2 == self._medication_input:
                        for k3,v3 in config[k][k2].items():
                            if k3 == 'locations':
                                for i in v3:
                                    for k4, v4 in i.items():
                                        if k4 == self._location_injection and v4 == self._side:
                                            return [needle, xylocaine, syringe, v4]
                            elif k3 == 'needle':
                                needle = v3
                            elif k3 == 'syringe':
                                syringe = v3
                            elif k3 == 'xylocaine':
                                xylocaine = v3
  
                                
    def message(self, config, note=None):
        order = self.order(config)
        a = "\nคนไข้ VN " + self._VN
        b = f"นพ.{self._doctor_name} ฉีดยา {self._medication_input} และ {order[1]}"
        c = f"ตำแหน่ง {self._side} {self._location_injection} จัดท่า {order[4]}"
        d = f"ใช้เข็ม {order[0]} และ {order[2]}"
        e = a +"\n" + b + "\n" + c + "\n" + d + "\n *** " + note
        if self._medication_input == "Synvisc":
            e = "**น่าจะไม่ถูกต้อง ให้ไปถามแพทย์อีกครั้ง**"
        return e



        
        
order1 = Order(VN="1234", doctor_name="เติมพงศ์", medication_input="Kenacort 40 mg", 
               location_injection="knee", side="ขวา")
message = order1.message(config)
print(message)