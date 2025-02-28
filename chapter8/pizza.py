def pizza_oven(*toppings):
    print(f"Here is your pizza with {', '.join(toppings)}.")
    print("Toppings:")
    for topping in toppings:
        print(f"- {topping}")

pizza_oven("Ham", "Cheese", "Pepper")
