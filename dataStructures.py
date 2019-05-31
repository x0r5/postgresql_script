#data_structures

class Database:

  """ Constructor with an array of data and structure """
  def __init__(self, array):
    self.adattar = []
    i = 0
    #map structure inside
    for itemName, item in zip(array["structure"], array["data"][0]):
      self.adattar.append({itemName : item})
