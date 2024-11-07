from datetime import*

class Sacen:
    def __init__(self, vards,uzvards,vecums,pilseta):
        self.vards=vards
        self.uzvards=uzvards
        self.vecums=vecums
        self.pilseta=pilseta
    def print_info(self):
        print(f"Skolena vards: {self.vards}, Skolena uzvards: {self.uzvards}, skolena vecums: {self.vecums}, skolena pilseta: {self.pilseta}")


    def iegut_punktus_un_aprekinat_skaitu(self,punktiviss,punkti):
        self.punktiviss=punktiviss
        self.punkti=punkti
        punkti1=int(input("ievadiet cik sanema  punktus"))
        punkti2=int(input("ievadiet cik sanema  punktus"))
        punkti3=int(input("ievadiet cik sanema  punktus"))
        punkti4=int(input("ievadiet cik sanema  punktus"))
        punkti5=int(input("ievadiet cik sanema  punktus"))

        self.punktiviss=punkti1+punkti2+punkti3+punkti4+punkti5
        print(f"{self.vards} {self.uzvards} kopējais punktu skaits ir: {self.punkti}")


    def piešķirt_diplomu(self):
        
        if self.punkti >= 45:
            diploms = "1. kartas diploms"
        elif self.punkti >= 40:
            diploms = "2. kartas diploms"
        elif self.punkti >= 35:
            diploms = "3.kartas diploms"
        else:
            diploms = "Diploms netiek piešķirts"

dal1=Sacen("Peters","Dziks","13","Riga")
dal1.print_info()
#dal1.iegut_punktus_un_aprekinat_skaitu()


dal2=Sacen("Vadims","Dodson","13","Jekabpils")
dal2.print_info()
#dal2.iegut_punktus_un_aprekinat_skaitu()


dal3=Sacen("Olga","Duarte","13","Riga")
dal3.print_info()
#dal3.iegut_punktus_un_aprekinat_skaitu()


dal4=Sacen("Vasena","Ayala","13","Rezekne")
dal4.print_info()
#dal4.iegut_punktus_un_aprekinat_skaitu()


dal5=Sacen("Antons","Chavez","13","Riga")
dal5.print_info()
#dal5.iegut_punktus_un_aprekinat_skaitu()







