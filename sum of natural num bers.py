num=int(input("enter a number"))
if num<0:
  print("enter a number")
else:
    sumnumbers=0
    count = 1
    while count<=num:
      sumnumbers +=count
      count+=1
      print("the sum of natural numbers :",sumnumbers)
