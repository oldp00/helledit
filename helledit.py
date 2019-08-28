lineCount = 1
tmpTexts = []

try: 
  while True: 
    text = input("%s ~ " % str(lineCount))
    fileContents.append(text + "\n")
    lineCount += 1
    
except KeyboardInterrupt:
  print("\nCommand Mode")
  while True:
    command = input("$ ~ ")
