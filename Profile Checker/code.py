print("=" * 40)
print("   PERSONAL PROFILE CHECKER")
print("=" * 40)

# String
name = input("Enter your name: ")
city = input("Enter your city: ")

# Integer
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid whole number for age.")
    raise SystemExit

if age < 0 or age > 120:
    print("Please enter an age between 0 and 120.")
    raise SystemExit

# Boolean
newsletter_input = input(
    "Subscribe to newsletter? (yes/no): "
).lower()

if newsletter_input not in ("yes", "no"):
    print("Please enter yes or no.")
    raise SystemExit

newsletter = newsletter_input == "yes"

# List
hobbies_input = input(
    "Enter your hobbies separated by commas: "
)

hobbies = [
    hobby.strip()
    for hobby in hobbies_input.split(",")
    if hobby.strip()
]

# Tuple
location = (city, age)

# Set
unique_hobbies = set(hobbies)

# Dictionary
profile = {
    "name": name,
    "age": age,
    "city": city,
    "newsletter": newsletter,
    "hobbies": hobbies
}

# Eligibility checks
adult = age >= 18
driving_age_eligible = age >= 18

print("\n" + "=" * 40)
print("         PROFILE SUMMARY")
print("=" * 40)

print("Name:", profile["name"])
print("Age:", profile["age"])
print("City:", profile["city"])
print("Adult:", adult)
print("Driving age eligible:", driving_age_eligible)
print("Newsletter:", profile["newsletter"])
print("Hobbies:", profile["hobbies"])
print("Unique hobbies:", unique_hobbies)
print("Location tuple:", location)

print("\n--- Data Types ---")

for key, value in profile.items():
    print(key, ":", type(value).__name__)

print("\nProfile created successfully!")