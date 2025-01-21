# # Zadanie 1

# Pamiętasz zadanie z listą zakupów?
# Załóżmy, że mamy do zrobienia zakupy spożywcze, potrzebujemy pójść do piekarni, w której kupujemy chleb, bułki oraz pączka. Poza tym po drodze wstąpimy też do warzywniaka, gdzie kupimy marchew, seler i rukolę.
# W pliku, który właśnie utworzyliśmy:

#     zdefiniuj słownik zawierający listę zakupów, gdzie kluczem jest nazwa sklepu, a wartością lista przedmiotów, które chcesz kupić w danym sklepie.
#     Następnie za pomocą pętli for, przeiteruj po tym słowniku i wyświetl napis w postaci: Idę do <sklep> i kupuję tam <rzeczy>.
#     Dodatkowo, używając wbudowanych metod operacji na napisach, spowoduj, aby nazwy sklepów i towarów były wypisane wielką literą (sięgnij do oficjalnej dokumentacji, by odnaleźć taką funkcjonalność).
#     Na koniec, w ostatniej linii wypisz W sumie kupuję <X> produktów.. X to sumaryczna liczba towarów, które są na listach.

# Twój program po uruchomieniu, powinien wyświetlić następujące informacje:

# Lista zakupów
# Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
# Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
# W sumie kupuję 6 produktów.

lista_zakupów = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

x = 0
print("Lista zakupów")
print("")

for sklep, produkty in lista_zakupów.items():  
    produkty_duza_litera = [produkt.title() for produkt in produkty]  # Tworzenie listy z produktami z wielkimi literami
    print(f"Idę do {sklep.title()}, kupuję tu następujące rzeczy: {produkty_duza_litera}") # metoda title zmienia pierwsza literę na duza
    x = x + len(lista_zakupów.get(sklep))


print(f"W sumie kupuję {x} produktów")

print("pierwszy tekst")

print("dodatkowy tekst piosenki tralalalala")
print("To kolejne zadanie na GITHUB z KOdilla")
