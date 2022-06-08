#!/usr/bin/python3


def main():
	x_displacement = 0
	y_displacement = 0
	finalArea = 0
	sanityCheck = 0
	with open("input.txt", "r") as fp:
		for line in fp:
			direction = line.split()[0]
			absolute_displacement = int(line.strip().split()[1])
			if (direction == "forward"):
				x_displacement+=absolute_displacement
			elif (direction == "down"):
				y_displacement+=absolute_displacement
			elif (direction == "up"):
				y_displacement+=(absolute_displacement*-1)
			else: #future case for -x direction if requested
				pass
			sanityCheck+=absolute_displacement
		finalArea = x_displacement*y_displacement
		print(f"x:{x_displacement}; y:{y_displacement}")
		print(f"Final area: {finalArea} squared units")
		print(f"sanityCheck: {sanityCheck}")

if __name__ == '__main__':
	main()