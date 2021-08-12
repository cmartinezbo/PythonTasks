# Variables Declaration

bmi = int(input())
ip = int(2 * bmi + 4)
r = int((bmi + ip) / 5)

# If Dev

if 0 <= r <= 20:
    category = "uno"
elif 21 <= r <= 30:
    category = "dos"
elif 31 <= r <= 50:
    category = "tres"
else:
    category = "cuatro"

# Print values & category

print(bmi, ip, r, "\n" + category)
