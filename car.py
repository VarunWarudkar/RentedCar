from datetime import datetime

class RentalCars:
    def __init__(self, stock=0):
        ''' Initialize the car rental with available stock. '''
        self.stock = stock

    def inventory(self):
        ''' Displays the available car stock. '''
        print(f'We have currently {self.stock} cars available for rent.')
        return self.stock

    def hourly(self, C_num):
        ''' Rent cars on an hourly basis. '''
        if self.stock <= 0:
            print(f'We have no cars available for rent.')
            return None
        elif C_num > self.stock:
            print(f'We have currently {self.stock} cars available for hourly rent.')
            return None
        else:
            now = datetime.now()
            print(f"Rented {C_num} car(s) on hourly basis at {now.day}/{now.month}/{now.year} :: {now.hour}:{now.minute}.")
            self.stock -= C_num
            return now

    def daily(self, C_num):
        ''' Rent cars on an daily basis. '''
        if self.stock <= 0:
            print(f'We have no cars available for rent.')
            return None
        elif C_num > self.stock:
            print(f'We have currently {self.stock} cars available for daily rent.')
            return None
        else:
            now = datetime.now()
            print(f"Rented {C_num} car(s) on daily basis at {now.day}/{now.month}/{now.year}.")
            self.stock -= C_num
            return now

    def weekly(self, C_num):
        ''' Rent cars on an weekly basis. '''
        if self.stock <= 0:
            print(f'We have no cars available for rent.')
            return None
        elif C_num > self.stock:
            print(f'We have currently {self.stock} cars available for weekly rent.')
            return None
        else:
            now = datetime.now()
            print(f"Rented {C_num} car(s) on weekly basis at {now.day}/{now.month}/{now.year}.")
            self.stock -= C_num
            return now

    def return_car(self, request):
        R_time, R_basis, C_num = request
        if R_time and R_basis and C_num:
            self.stock += C_num
            now = datetime.now()
            R_period = now - R_time
            bill = 0
            match R_basis:
                case 'hourly':
                    bill = R_period.seconds // 3600 * 5 * C_num
                case 'daily':
                    bill = R_period.days * 20 * C_num
                case 'weekly':
                    bill = R_period.days // 7 * 60 * C_num
            print(f'Total bill : $ {bill}.')
            return bill
        else:
            print(f"You haven't rented any car")