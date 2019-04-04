def weight_on_planets():
	prompt=input('What do you weigh on earth? ')
	
	w_mars=.38*int(prompt)
	w_jupit=w_mars/.38*2.34
	
	print ("\nOn Mars you would weigh " , w_mars , " pounds." , "\nOn Jupiter you would weigh " , w_jupit , " pounds.")

   
if __name__ == '__main__':
   weight_on_planets()