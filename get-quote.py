def primary():
    # print("Keep it logically awesome.")
    
  last = 13
  rnd = random.randint(0, last)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])
  print(quotes[rnd +1])
  print(quotes[rnd-1])

if __name__== "__main__":
  import random
  primary()
