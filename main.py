import covid_api
import covidusaapi 

def main():
  covidGlobal = covid_api.CovidApi()
  covidUSA = covidusaapi.CovidUSAApi()

  print("Global Covid Deaths: " + str(covidGlobal.deaths()) + "/n")
  print("USA COVID Deaths: " + str(covidUSA.totaldeaths()) + "/n")
  print("New York COVID Deaths: " + str(covidUSA.statedeaths("New York")))

main()

      