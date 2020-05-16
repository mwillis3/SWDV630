class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self, member):
    return member in self.__myTeam

  def __iter__(self):
    for member in self.__myTeam:
      try:
        print(member)
      except:
        raise StopIteration
    return self
    

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print("Number of Teammates:")
  print(len(classmates))
  print("Is Tim a teammate?")
  print("Tim" in classmates)
  print("Is Sam a teammate?")
  print("Sam" in classmates)
  print("List of Teammates:")
  iter(classmates)
  print("Check that length works:")
  print(len(classmates))


main()