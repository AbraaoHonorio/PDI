def mediana(vector):  
	vectorOrder=sorted(vector)
    
	n = len(vectorOrder)/2
	middle= n/2

	if n %2==0:
		mediana=(int(vectorOrder[middle+1]) + int(vectorOrder[middle+2])) / 2
	else:
		mediana=vectorOrder[middle+1]*1

	return(mediana)