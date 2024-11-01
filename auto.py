class Automobilis:
    def __init__(self,marka,modelis, year):
        self.marka=marka
        self.modelis=modelis
        self.year=year

    def info(self):
        print(f'Auto marka ir {self.marka}, modelis:{self.modelis}, gadas:{self.year}')

    def apmaksa(self):
        self.dienas=int(input('ievadiet cik dienas jūs izmantosiet'))
        if self.year>2020:
            print('auto apmaksa ir 50eiro par dienu')
            self.cena_par_dienu=50
            cena=self.cena_par_dienu*self.dienas
            print(f"auto ires maksa par {self.dienas} ir {cena}")
        else:
            print('Auto apmaksa ir 30 eiro dienā')
            self.cena_par_dienu=30
            cena=self.cena_par_dienu*self.dienas
            print(f"auto ires maksa par {self.dienas} ir {cena}")

auto1=Automobilis('Audi','A5',2008)
auto1.info
()
auto1.apmaksa()
auto2=Automobilis('BMW','X5',2021)
auto2.info
()
auto2.apmaksa() 