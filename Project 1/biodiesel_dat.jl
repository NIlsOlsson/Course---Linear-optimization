# Sets
I = 1:3 # 3 different fuels
J = 1:3 # 3 different crops

#Labels
fuels = ["B5", "B30", "B100"] # for i in I
crops  = ["soybeans", "sunflower seeds", "cotton seeds"]

#Parameters
diesel_content = [0.95, 0.7, 0] 
tax = [0.2, 0.05, 0]
diesel_price = 1
biodiesel_price = 1/3
cost = diesel_content.*diesel_price.+([1,1,1].-diesel_content).*biodiesel_price
price = [1.43, 1.29, 1.16]
profit = price.*([1,1,1].-tax).-cost
rain = 0
water_requirement = [5.0, 4.2, 1.0] .- rain #Ml per ha
yield = [2.6, 1.4, 0.9] #ton per ha
oil_content = [0.178, 0.216, 0.433] #l per kg

print(profit)