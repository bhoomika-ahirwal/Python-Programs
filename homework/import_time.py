import time
x=int(input("enter the value:"))
start_time = time.time_ns()
fact=1
for i in range (1,x+1):
	fact = fact*i
print("factorial of {}={}".format(x,fact))
end_time = time.time_ns()
total_time=end_time - start_time
print("total_time",total_time)