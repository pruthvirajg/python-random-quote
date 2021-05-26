def primary():
    # print("Keep it logically awesome.")
    
  last = 13
  rnd = random.randint(0, last)

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  f = open("quotes.txt","a")
  f.write("Failures are steping stones of success")
  f.close()
  

  print(quotes[rnd],end="")
  print(quotes[rnd +1],end="")
  print(quotes[rnd-1],end="")

if __name__== "__main__":
  import random
  primary()
