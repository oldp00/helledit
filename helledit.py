lineCount = 1
fileContents = []

while True:
  text = input("%s ~ " % str(lineCount))
  fileContents.append(text + "\n")
  lineCount += 1
