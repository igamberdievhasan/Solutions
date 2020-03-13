def extra_end(str):
  temp = ""
  if len(str) == 2:
    for x in range(0, 3):
      temp += str
    return temp
  l = len(str) - 2
  temp1 = ""
  temp = str[l:]
  for x in range(0, 3):
      temp1 += temp
  return temp1
  
