
while True:
    dollars_owed = float(input("Change owed: "))
    cents_owed = (dollars_owed * 100)

    if cents_owed > 0:
        break

quarters = cents_owed // 25
dimes = (cents_owed % 25) // 10
nickels = ((cents_owed % 25) % 10) // 5
pennies = ((cents_owed % 25) % 10) % 5

print(f"{quarters + dimes + nickels + pennies}")
