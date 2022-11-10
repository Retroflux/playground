#!/usr/bin/python3


def main():
	x_displacement = 0
	aimAngle = 0
	depth = 0
	with open("input.txt", "r") as fp:
		for line in fp:
			direction = line.split()[0]
			absolute_displacement = int(line.strip().split()[1])
			if (direction == "forward"):
				x_displacement+=absolute_displacement
				depth += (absolute_displacement * aimAngle)
			elif (direction == "down"):
				aimAngle+=absolute_displacement
			elif (direction == "up"):
				aimAngle+=(absolute_displacement*-1)
			else: #future case for -x direction if requested
				pass
		print(f"Final depth: {depth} units")
		resultant_distance = depth * x_displacement
		print(f"Final distance: {resultant_distance} units")


if __name__ == '__main__':
	main()