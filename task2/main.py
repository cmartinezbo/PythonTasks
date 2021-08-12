# Input's Declaration

treatment_natural = input()
treatment_artificial = input()
general = input()

# Counters Declaration

counter_natural = 0
counter_artificial = 0

# For Dev

for letter_gen in general:
    for letter_natural in treatment_natural:
        if letter_natural == letter_gen:
            counter_natural = counter_natural + 1
    for letter_artificial in treatment_artificial:
        if letter_artificial == letter_gen:
            counter_artificial = counter_artificial + 1
    if counter_natural > counter_artificial:
        print("N", end="")
    elif counter_natural < counter_artificial:
        print("A", end="")
    else:
        print("E", end="")
