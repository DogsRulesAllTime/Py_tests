import time
print(time.ctime())
later = time.time() + 60
print(time.ctime(later))

def transfer_to_sec(sec=0,min=0,hour=0,days=0,**month):


	total_secs = sec + (min*60) + (hour*60)*60 + (days*24*60*60)
	return total_secs

z = time.time()+transfer_to_sec(min=2,hour=2)
print(z)

print(time.ctime(z))
