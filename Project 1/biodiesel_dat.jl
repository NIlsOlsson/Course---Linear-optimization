# Sets
I = 1:3 # 3 different fuels
J = 1:3 # 3 different crops

#Labels
fuels = ["B5", "B30", "B100"] # for i in I
crops  = ["soybeans", "sunflower seeds", "cotton seeds"]

#Parameters
diesel_content = [0.95, 0.7, 0.0] 
profit = [133/750, 0.4255, 62/75] #Profit per liter of fuel
water_requirement = [5.0, 4.2, 1.0] #Ml per ha
yieldd = [2.6, 1.4, 0.9] #ton per ha
oil_content = [0.178, 0.216, 0.433] #l per kg