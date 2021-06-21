class Country(object):
    name = 'Country Name'
    population = 'Population'
    capital = 'Capital'

    def show(self):
        print('Country Class Method')


class Korea(Country):

    def show_name(self):
        print(f'Country Name is {self.name}')


def main():
    k = Korea()
    k.name = 'KOREA'
    k.show_name()


main()
