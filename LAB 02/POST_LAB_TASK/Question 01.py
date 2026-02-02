class Vehicle:
  
  def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id= vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day


  def cal_rent(self, days):
        rent= self.rent_per_day* days
        return rent

  def display_details(self, rent):
       print("Vehicle ID:", self.vehicle_id)
       print("Brand:", self.brand)
       print("Rent per day:", self.rent_per_day)
       print("Rent:", rent)

# Creating objects
civic= Vehicle(2345, "Honda", 7000)
prius= Vehicle(7894, "Toyota",6000)

rent1=civic.cal_rent(5)
civic.display_details(rent1)
print()
rent2=prius.cal_rent(3)
prius.display_details(rent2)


