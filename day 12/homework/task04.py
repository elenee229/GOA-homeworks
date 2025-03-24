#read_pages=22
#free_time=true

read_pages=int(input("how many pages did you read?"))
didnt_read=34
free_time=(input("did u have free time?"))
productive=read_pages<25 and free_time
productive1=read_pages==22 and not free_time
productive2=read_pages>didnt_read or free_time

print(productive)#true
print(productive1)#false
print(productive2)#true