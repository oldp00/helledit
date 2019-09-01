import sys

lineCount = 1
tmpTexts = []

try: 
  while True: 
    text = input("%s ~ " % str(lineCount))
    tmpTexts.append(text)
    lineCount += 1
    
except KeyboardInterrupt:
  print("\nCommand Mode")
  while True:
    command = input("$ ~ ")
    
    if command == "exit":
      sys.exit()
    
    if command == "showtmp":
      for index in range(0, len(tmpTxts)):
        print(tmpTxts[index])
