import cv2
import os

src = str(input("Podaj lokalizacje plików: "))
name = str(input("Podaj nazwe pliku (taka jak nazwa folderu + spacja): "))


# Funkcja obliczająca wartość średnią z danej grupy próbek
def srednia(var):
    sum_var = sum(var)
    return sum_var / float(len(var))


# załadowanie zdjęć z folderu
imgs = []
n = int(input("Ile zaladowac zdjec: "))
count = 1

for i in range(n):
    plik = src + '\\' + name + str(count).zfill(4) + '.png'
    imgs.append(cv2.imread(plik, 0))
    count += 1


# Odczytanie wartości pixeli ze wszystkich załadowanych zdjęć
pixel = []
for i in range(n):
    img = imgs[i]
    pixel.append(img[:][:])

split_pixel = list()
split_num = int(input("Ile razy chcesz pomniejszyc zbior zdjec: "))

# Tworzenie grup ze skanów w osi Z, których wartość pikseli jest uśredniana
for i in range(0, len(pixel), split_num):
    split_pixel.append(pixel[i:i + split_num])

new_pixel = []
for i in split_pixel:
    new_pixel.append(srednia(i))

# Zmiana rozmiaru zdjęcia w osi X i Y
x = int(input("Podaj wymiar po zmniejszeniu: "))
dim = (x, x)
resized_photo = []
for i in range(len(new_pixel)):
    resized_photo.append(cv2.resize(new_pixel[i], dim, interpolation=cv2.INTER_NEAREST))

# Utworzenie nowego katalogu i zapisanie zredukowanych zdjęć
new_src = "D:\Praktyki-Inzynierka\zdjecia\\"
directory = str(input("Podaj nazwe folderu ze zmniejszonym zdjeciami:  " ))
path = os.path.join(new_src, directory)
os.mkdir(path)

for i in range(len(resized_photo)):
    cv2.imwrite(path + '\\' + name + str(count).zfill(4) + '.png', resized_photo[i])
    count += 1
