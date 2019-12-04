
def compute_fuel_requirement_helper(mass):
    return (mass // 3) - 2

def compute_fuel_requirement(mass):
	total_fuel_requirement = 0
	new_fuel_requirement = compute_fuel_requirement_helper(mass)
	while (new_fuel_requirement > 0):
		total_fuel_requirement += new_fuel_requirement
		new_fuel_requirement = compute_fuel_requirement_helper(new_fuel_requirement)
	return total_fuel_requirement

def main():
	print("check: {}".format(compute_fuel_requirement(1969)))
	print("check: {}".format(compute_fuel_requirement(100756)))
	with open('input.txt', 'r') as f:
		print(sum(compute_fuel_requirement(int(l)) for l in f.readlines()))

if __name__ == '__main__':
    main()
