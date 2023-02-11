import pydicom as dicom
import os
import cv2

folder_path = str(input("Podaj lokalizacje plików: "))

directory = str(input("Podaj nazwe folderu dla PNG: "))
save_folder_path = os.path.join("D:\\Praktyki-Inzynierka\\zdjecia", directory)
os.mkdir(save_folder_path)

images_path = os.listdir(folder_path)

for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(save_folder_path, image), pixel_array_numpy)

    if n % 50 == 0:
        print('{} image converted'.format(n))

# _____________________________________________________________________________________
# ZMIANA NAZWY PLIKOW
save_folder_path = r"D:\Praktyki-Inzynierka\zdjecia" + "\\" + directory + "\\"
name = str(input("Podaj nową nazwe pliku: "))
count = 1

for file_name in os.listdir(save_folder_path):
    source = save_folder_path + file_name
    destination = save_folder_path + "\\" + name + str(count).zfill(4) + ".png"
    os.rename(source, destination)
    count += 1
