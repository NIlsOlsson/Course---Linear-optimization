using JuMP     
using Clp      
using Gurobi   

#Build the model and get variables and constraints back (see intro_mod.jl)
include("biodiesel_mod.jl")
m, y, x, diesel_supply, water_limitation, land_limitation = build_diet_model("biodiesel_dat.jl")
print(m) # prints the model instance

set_optimizer(m, Gurobi.Optimizer)
optimize!(m)

# display the optimal solution
println("z =  ", objective_value(m))   		
println("y =  ", value.(y.data)) 
println("x =  ", value.(x.data))  
println("diesel supply dual =  ", shadow_price(diesel_supply))
println("water supply dual =  ", shadow_price(water_limitation))
println("land limit dual =  ", shadow_price(land_limitation))