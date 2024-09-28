from car import RentalCars
from customer import Customer


def main():
    rental_shop = RentalCars(100)  # Initial car inventory
    customer = Customer()

    while True:
        print("""
        ====== Car Rental Shop ======
        1. Display available cars
        2. Rent a car on hourly basis
        3. Rent a car on daily basis
        4. Rent a car on weekly basis
        5. Return a car
        6. Exit
        """)

        choice = input("Enter choice: ")

        if choice == '1':
            rental_shop.inventory()

        elif choice == '2':
            customer.R_time = rental_shop.hourly(customer.request_car())
            customer.R_basis = 'hourly'

        elif choice == '3':
            customer.R_time = rental_shop.daily(customer.request_car())
            customer.R_basis = 'daily'

        elif choice == '4':
            customer.R_time = rental_shop.weekly(customer.request_car())
            customer.R_basis = 'weekly'

        elif choice == '5':
            request = customer.return_car()
            rental_shop.return_car(request)

        elif choice == '6':
            break

        else:
            print("Invalid input. Please choose a valid option.")


if __name__ == "__main__":
    main()
