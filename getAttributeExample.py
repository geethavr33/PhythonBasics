class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Main program to demonstrate getattr
car = Car("Toyota", "Corolla", 2020)

# Using getattr to access attributes
brand = getattr(car, 'brand')
model = getattr(car, 'model')
year = getattr(car, 'year')

print(f"Brand: {brand}")   # Outputs: Brand: Toyota
print(f"Model: {model}")   # Outputs: Model: Corolla
print(f"Year: {year}")     # Outputs: Year: 2020
