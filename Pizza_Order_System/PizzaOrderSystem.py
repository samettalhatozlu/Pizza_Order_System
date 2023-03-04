import csv
import datetime

#Pizza üst sınıfını oluşturuyoruz.
class Pizza:
    def get_description(self): 
        return self.__class__.__name__

    def get_cost(self): 
        return self.__class__.cost

#Pizza alt sınıflarını oluşturuyoruz.
class Klasik(Pizza):
    cost = 70.0

    def __init__(self):
        #Her alt sınıf için özellikler yazılacak.
        self.description = "Klasik Malzemeler: Sucuk, Salam, Kaşar"
        print(self.description +"\n")

class Margarita(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Margarita Malzemeler: Domates, Fesleğen, Mozarella"
        print(self.description +"\n")

class TurkPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Türk Malzemeler: Kıyma, Soğan, Biber, Sarımsak, Kaşar"
        print(self.description +"\n")

class SadePizza(Pizza):
    cost = 80.0


    def __init__(self):
        self.description = "Sade Malzemeler: Salam, Sucuk, Zeytin"
        print(self.description +"\n")


#Decorator üst sınıf oluşturulacak.
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ;' + Pizza.get_description(self)
    
#Decorator alt sınıf oluşturulacak 
class Zeytin(Decorator):
    cost = 2.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 3.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 4.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 10.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 5.0

    def __init__(self, topping):
        Decorator.__init__(self, topping)

#Menüyü ekrana yazmak gibi işlemler için main fonksiyonu oluşturulmuştur.
def main():
    with open("Menu.txt") as cust_menu:
        for i in cust_menu:
            print(i, end="")

    class_dict = {1: Klasik, 
                  2: Margarita, 
                  3: TurkPizza, 
                  4: SadePizza, 
                  5: Zeytin, 
                  6: Mantar, 
                  7: Peynir, 
                  8: Et, 
                  9: Sogan, 
                  10: Misir}
    
    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("Yanlış Tuşlama Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "*":
        code = input("Ek Malzeme Almak İçin Tuşlama Yapınız (Direkt Siparişinizi Onaylamak İçin '*' Tuşuna Basınız): ")
        if code in ["5","6","7","8","9","10"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          "; $" + str(order.get_cost()))
    print("\n")

#Sipariş Bilgi Kartı oluşturuyoruz.
    print("----------Sipariş Bilgileri----------\n")
    name = input("İsminiz: ")
    ID = input("TC Kimlik Numaranız: ")
    kk_no = input("Kredi Kartı Numaranızı Giriniz: ")
    kk_psw = input("Kredi Kartı Şifrenizi Giriniz: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, kk_no, kk_psw, order.get_description(), time_of_order])
    print("Siparişiniz Onaylandı.")







main()




