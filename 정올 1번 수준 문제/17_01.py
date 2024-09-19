# 4011 생년월일 출력
n=input()
year = n[0:2]
month=n[2:4]
day=n[4:6]

if int(n[7])==1:
    year = 1900+int(year)
    print(year,month,day+" M",sep="/")
elif int(n[7])==2:
    year = 1900+int(year)
    print(year,month,day+" F",sep="/")
elif int(n[7])==3:
    year = 2000+int(year)
    print(year,month,day+" M",sep="/")
elif int(n[7])==4:
    year = 2000+int(year)
    print(year,month,day+" F",sep="/")