class Customer:
    def init(self):
        """Initialize customer details."""
        self.cars = 0
        self.R_basis = None
        self.R_time = None

    def request_car(self):
        """Request car rental."""
        cars = int(input('Enter required number of cars : '))
        self.cars = cars
        '''basis = input('Enter on which basis cars to be rented (hourly / daily / weekly : ').lower()
        self.R_basis = basis
        time = int(input('Enter the time for which car is required : '))
        self.R_time = time'''
        return self.cars

    def return_car(self):
        """Return rented car."""
        if self.R_time and self.R_basis and self.cars:
            return self.R_time, self.R_basis, self.cars
        else:
            return 0, 0, 0
