def is_prime(num):
    i,r=1,2
    if num==2:
        return True
    if 1<num:
        while i<r:
            i+=1
            r=num/i
            if r%1==0:
                return False
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
