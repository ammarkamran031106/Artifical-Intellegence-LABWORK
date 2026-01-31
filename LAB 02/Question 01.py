#This task demonstrates OOP in AI automation:
#● Classes organize devices logically.
#● Objects represent individual lights.
#● Methods automate actions like turning ON/OFF.
#Expected Output
#Living Room light turned ON.
#Bedroom light turned OFF.
#Living Room light is ON.
#Bedroom light is OFF.
class Lights:
  def __init__(self,name,status):
    self.name=name
    self.status=status
  
  def light_on(self):
    self.status="ON"
  
  def light_off(self):
    self.status="OFF"
 
  def get_status(self):
    return self.status
  
  def get_name(self):
    return self.name
 
  def display(self):
    print(self.name," Light Turned ",self.status)



l1=Lights("kitchen", "OFF")
l2=Lights("living room", "ON")
l3=Lights("bedroom", "OFF")
l1.display()
l2.display()
l3.display()
l1.light_on()
l2.light_off()
l3.light_on()
print("AFTER CHANGING STATUS OF LIGHTS")
l1.display()
l2.display()
l3.display()

