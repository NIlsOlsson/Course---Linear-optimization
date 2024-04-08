"""
  Construct and returns the model of this assignment.
"""
function build_diet_model(data_file::String)
  # The diet problem
  include(data_file)
  #I: set of fuels
  #J: set of crops
  #fuels: name of the fuels, i in I
  #crops: name of the crops, j in J
  #diesel_supply: i in I
  #profit: profit per liter sold, i in I
  #water_requirement: water per ha, j in J
  #yield: ton per ha, j in J
  #oil_content: l oil per kg, j in J

  #name the model
  m = Model()

  @variable(m, x[I] >= 0) #amout of fuel i
  @variable(m, y[J] >= 0) #ha of crop j

  #maximize profit
  @objective(m, Max, sum(profit[i]*x[i] for i in I))

  #production constraints
  @constraint(m, total_production, sum(x[i] for i in I) >= 280000)
  @constraint(m, diesel_supply, sum(diesel_content[i]*x[i] for i in I) <= 150000)
  @constraint(m, land_limitation, sum(y[j] for j in J) <= 1600)
  @constraint(m, water_limitation, sum(water_requirement[j]*y[j] for j in J) <= 5000)
  biodiesel_available = @expression(m, sum(y[j]*yield[j]*oil_content[j]*1000*0.9 for j in J))
  @constraint(m, biodiesel_availability, sum(x[i]*(1-diesel_content[i]) for i in I) <= biodiesel_available)


  return m, y, x
end
