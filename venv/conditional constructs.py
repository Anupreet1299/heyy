#conditional constructs

total = 500
discount = 40
"""
if total>= 500:
    print("flat 40% off")  #pep
else:
    print("sorry no discount")


if total>=100 and total<200:
    print("flat 20% off")
elif total>=200 and total<500:
    print("flat40%")
"""
#else:
    #print("flat50%")
   """
 elif total>= 500:
      print("flat50%")
else:
print("add more items")

"""

#nested if/else

isInternetConnected = True
if isInternetConnected:
    print("you can browse google maps")

else:
    print("please connect to internet)
