
# 🧮 BMI Calculator with Ideal Weight Recommendation
# Hashtags: #Python #BMICalculator #IdealWeight #PythonProjects

def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def recommend_weight(height):
    # Approximate healthy adult BMI range: 18.5 to 24.9
    minimum_weight = 18.5 * (height ** 2)
    maximum_weight = 24.9 * (height ** 2)
    return minimum_weight, maximum_weight


def main():
    print("=" * 40)
    print("      BMI & IDEAL WEIGHT CALCULATOR")
    print("=" * 40)

    try:
        weight = float(input("Enter your weight in kg: "))
        height_cm = float(input("Enter your height in cm: "))

        if weight <= 0 or height_cm <= 0:
            print("Error: Weight and height must be positive.")
            return

        height = height_cm / 100

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)
        min_weight, max_weight = recommend_weight(height)

        print("\n--------- YOUR RESULTS ---------")
        print(f"Your weight       : {weight:.1f} kg")
        print(f"Your height       : {height_cm:.1f} cm")
        print(f"Your BMI          : {bmi:.2f}")
        print(f"BMI category      : {category}")

        print("\n--- ESTIMATED HEALTHY WEIGHT RANGE ---")
        print(f"Lower end         : {min_weight:.1f} kg")
        print(f"Upper end         : {max_weight:.1f} kg")
        print(
            f"Estimated range   : "
            f"{min_weight:.1f} - {max_weight:.1f} kg"
        )

        if weight < min_weight:
            print("\nYour weight is below the general adult BMI range.")
        elif weight > max_weight:
            print("\nYour weight is above the general adult BMI range.")
        else:
            print("\nYour weight is within the general adult BMI range.")

        print("\nNote: BMI is a screening tool, not a diagnosis.")
        print("This estimate is intended for adults.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


if __name__ == "__main__":
    main()
