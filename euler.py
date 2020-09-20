def amicable(n):
	d ={}
	for i in range(1 , n+1):
		d[str(i)] = 0
	count = 0
	maxa = n
	for i in range(2 ,n +1):
		if d[str(i)] == 0:
			isum = 0
			for j in range(1 , int((i+2)/2)):
				if i %j == 0:
					isum = isum + j
			d[str(i)] = isum
			if isum > maxa:
				for k in range(maxa , isum+1):
					d[str(k)] = 0
				maxa = isum
			if d[str(isum)] == 0:
				newsuma = 0
				for l in range(1 , int((isum+2)/2)):
					if isum%l ==0:
						newsuma = newsuma + l
				d[str(isum)] = newsuma
				if newsuma == i and i != isum:
					count = count + i + isum
			else:
				if d[str(isum)] == i and i != isum:
					count = count + i + isum
		else:
			isum = d[str(i)]
			if isum > maxa:
				for k in range(maxa , isum+1):
					d[str(k)] = 0
			if d[str(isum)] == 0:
				newsuma = 0
				for l in range(1 , int((isum+2)/2)):
					if isum%l ==0:
						newsuma = newsuma + l
				d[str(isum)] = newsuma
				if newsuma == i and i != isum:
					count = count + i + isum
			else:
				if d[str(isum)] == i and i != isum:
					count = count + i + isum
	return(count/2)

def new(n):
	count = 0
	for i in range(3, n):
		
		suma = 0
		for j in range(1 , int((i+2)/2)):
			if i%j ==0:
				suma = suma + j
		if suma == i:
			pass
		else:
			newsuma = 0
			for j in range(1 , int((suma+2)/2)):
				if suma%j ==0:
					newsuma = newsuma + j
			if newsuma == i:
				print(i , suma)
				count = count + i + suma
	return(count/2)


