#Random number array
New_Array=[1, 4, -1, 20, 9, 50, 82, 1, 3]
#First thing to set avalue for the variable to avoid probles with the division later
max = New_Array[0]
#loop from first item (index 0) to the last item (length of the array)
for i in range (0,len(New_Array)):
	#Check if it is the maximum yet
	if (max < New_Array[i]):
		max = New_Array[i]
		
print (max)
