#wap that create a dictionary of radius of circle and its circumference
r=input('data:').split(',') #input list of radius
r=list(map(int,r))
c=[map((lambda x:(2*3.14*x)),r)]
dic=dict(zip(r,c))
print(dic)
