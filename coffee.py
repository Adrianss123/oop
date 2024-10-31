from datetime import*
class dog:
    list_name=[]
    list_cena=[]

    def __init__(self,name=str,age=int,breed="unknown",weight=float,gender=str,cena=float,color="melns"):
      self.name=name
      self.age=age
      self.breed=breed
      self.weight=weight
      self.gender=gender
      self.cena=cena
      self.color=color
      dog.list_name.append(self.name)
      dog.list_cena.append(self.cena)
    def print_info(self):
      print(f"suna vards {self.name},vecums {self.age},cena {self.cena} kg, suna krasa {self.color}" )
    def registration(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y/%M/%S")
        print(f"suns ir reg {dt_string}")


    def sacensibas(self,vieta,pilseta):
      self.vieta=vieta
      self.pilseta=pilseta
      print(f"suns{self.name}, piedalijas {self.pilseta}, un ieguva {self.vieta} vietu")
   
    def svars(self,svars1):
        self.svars1=svars1
        a=input('Vai svars palielinājās? (samazinājās, palielinājās, nemainījās)')
        if a=='samazinājās':
           self.weight-=self.svars1
        if a=='palielinājās':
            self.weight+=self.svars1
        if a=='nemainījās':
            print(f'Svars palika nemainīgs {self.weight} kg') 

         

    def vitamini(self,doze):
            self.doze=doze
            vitamins=self.weight/self.doze
            print(f"vitaminu doze ir {vitamins}")
            print( f'suņa deva ir {round(daudzums,0)}') 



suns1=dog("Tobiks",12,"Dog",32,"v",250.00)
suns1.print_info()
suns2=dog("vens",10,"Dog",50,"v",250.00, 'balts')
suns2.print_info()
suns1.registration()
suns1.sacensibas(1,'Riga')
suns1.svars(5)
suns1.print_info()
suns1.vitamini(10)


