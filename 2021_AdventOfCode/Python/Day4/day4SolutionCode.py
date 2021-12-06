#each row is just a set of five of sequential numbers
#	ex. row1 = 0->4
#		row2 = 5->9
#		etc.
#each column is just the set of five numbers where y = 5x + i, where {i,x}={0,1,2,3,4}
#	ex. 
#		i=0     i=1     i=2     i=3     i=4
#	x=0 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i    
#	x=1 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=2 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=3 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  
#	x=4 y=5x+i  y=5x+i  y=5x+i  y=5x+i  y=5x+i  


#>Boards are hardcoded in size, so each board will have ten possible win conditions that can be stored in two(?) lists.
#>When number is called, search the board strings for the number, identify its position number, and then find its row and col using math for each matching board
#	>replace the called index with an "X" and check that row and column (ex. row 2 and col 3) for all X's. 

