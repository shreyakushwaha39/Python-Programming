s=int(input("Enter no of second :"))
hour=s//(60*60)
min=s%(60*60)
sec=s%60
print("Answer is",hour,"hours",min,"minutes",sec,"seconds")