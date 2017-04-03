import quandl

#Get US GDP data
quandl.get("FRED/GDP")

#Get WTI Crude Oil price from the US Department of Energy
#(Crude Oil in Dollars per Barrel, Products in Dollars per Gallon)
quandl.get("EIA/PET_RWTC_D")

