try:
	import statistics
except:
	print("Could not import statistics module")
print("Histogram Standard Deviation Calculator")
print("")
print("Mode selection: ")
print("1. Histogram")
print("2. Standard list")
try:
	mode = int(input("Enter choice [1-2]: "))
	print()
	listNumbers = []
	if(mode == 1):
		while True:
			try:
				entered = input("Enter format [number],[frequency]: ").split(',')
				if(len(entered)<2):
					break
				for i in range(int(entered[1])):
					listNumbers.append(float(entered[0]))
			except:
				break
	elif(mode ==2):
		while True:
			try:
				listNumbers.append(float(input("Enter number: ")))
			except:
				break
	else:
		raise ValueError('Fault Between Keyboard And Chair Detected')
	print()
	print()
	if(len(listNumbers)>0):
		print()
		print("n (count) = "+str(len(listNumbers)))
		print("x (mean) = "+str(statistics.mean(listNumbers)))
		print("σx (Population standard deviation) = "+str(statistics.pstdev(listNumbers)))
		print("Σx (Sum) = "+str(statistics.fsum(listNumbers)))
		t = statistics.quantiles(listNumbers)
		print("minX (Minimum) = "+str(min(listNumbers)))
		print("Q1 (Lower quartile) = "+str(t[0]))
		print("Med (Median) = "+str(t[1]))
		print("Q3 (Upper quartile) = "+str(t[2]))
		print("maxX (Maximum) = "+str(max(listNumbers)))
		
	else:
		print("No numbers were entered")
except:
	print()
	print("Invalid input")
