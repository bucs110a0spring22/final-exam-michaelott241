import requests 

class CovidUSAApi: 

  def __init__(self): 
    self.api_url = "https://covid19.mathdro.id/api/countries/USA"

  def get(self): 
    r = requests.get(self.api_url)
    data = r.json()
    return data 

  def totaldeaths(self): 
    data = self.get()
    return data['deaths']['value']

  def statedeaths(self, state): 
    total = 0
    r = requests.get(self.get()['deaths']['detail'])
    data = r.json()
    for d in data:
      if d["provinceState"] == state:
        total += d["deaths"]
    return total
