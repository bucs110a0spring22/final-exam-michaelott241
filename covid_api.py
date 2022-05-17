import requests 

class CovidApi: 

  def __init__(self):
    self.api_url = "https://api.covid19api.com/summary"

  def get(self): 
    r = requests.get(self.api_url)
    data = r.json()
    return data

  def deaths(self):
    data = self.get()
    return data['Global']['TotalDeaths']