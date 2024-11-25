class Employee:

    def __init__(self, info):
        self.name = info['name']
        self.id = info['id']

    def print_info(self):
        print(f'{self.name}: {self.id}')

    def calculate_monthly_pay(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, info):
        super().__init__(info)
        self.monthly_salary = info['monthly_salary']

    def calculate_monthly_pay(self):
        print(f'{self.name} is available to calculate the monthly pay')
        print(f'{self.name}[{self.id}] monthly pay is {str(self.monthly_salary)}')


class PartTimeEmployee(Employee):

    def __init__(self, info):
        super().__init__(info)
        self.daily_salary = info['daily_salary']

    def calculate_monthly_pay(self):
        print(f'{self.name} is still need to get their manager to calculate the monthly pay')
        _monthly_salary = self.daily_salary * 21
        print(f'OK, {self.name}[{self.id}] monthly pay is {_monthly_salary}')


if __name__ == '__main__':
    zs_info = {'name': 'Zhang San', 'id': 43843433, 'monthly_salary': 10000, 'daily_salary': ''}
    ls_info = {'name': 'Li Si', 'id': 45499595, 'monthly_salary': '', 'daily_salary': 400}
    zs = FullTimeEmployee(zs_info)
    ls = PartTimeEmployee(ls_info)

    zs.print_info()
    zs.calculate_monthly_pay()
    ls.print_info()
    ls.calculate_monthly_pay()
