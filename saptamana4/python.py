file = open("data.txt", "w")
# r - doar citire (read) default dar da eroare daca fisierul nu exista
# w - cu drept sciere (write)
# a - cu drept de adaugare ( append)
# r+ - deshidem cu drept de citire si scriere
file.write("hello")
file.close()