from config import config

class OrderInjection:
    
    def __init__(self, VN, doctor_name, medication_input, location_injection, side):
        self._VN = VN
        self._doctor_name = doctor_name
        self._medication_input = medication_input
        self._location_injection = location_injection
        self._side = side
       
            
    def _order(self, config):
         for k in config.keys():
            if k == self._doctor_name:
                for k2 in config[k].keys():
                    if k2 == self._medication_input:
                        for k3,v3 in config[k][k2].items():
                            if k3 == 'locations':
                                for i in v3:
                                    for k4, v4 in i.items():
                                        if k4 == self._location_injection:
                                            return [needle, xylocaine, syringe, v4]
                            elif k3 == 'needle':
                                needle = v3
                            elif k3 == 'syringe':
                                syringe = v3
                            elif k3 == 'xylocaine':
                                xylocaine = v3
                 
  
                                
    def message(self, config, note=None):
        order = self._order(config)
        if order is not None:
            return f"\nคนไข้ VN {self._VN}\
                     \nนพ.{self._doctor_name} ฉีดยา {self._medication_input} และ {order[1]}\
                     \nตำแหน่ง {self._location_injection} ข้าง{self._side} จัดท่า {order[3]}\
                     \nใช้เข็ม {order[0]} และ {order[2]} {note}"
        else:
            return 'ไม่มีข้อมูล'



        
        
