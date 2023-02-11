import pydicom as dicom
from pydicom import dcmread
import mysql.connector
import pymysql
import datetime
import os


'''def convertPixelSpacing2float(tekst):
    poz = tekst.find(',', 0)
    dl = len(tekst)
    X=float(tekst[1:poz])
    Y=float(tekst[poz+1:dl-1])
    return X, Y
'''
# -----------------------------------------------------Pobranie danych z pliku DICOM--------------------------------------------------------------------

#file = dcmread('IM-0001-0010.dcm')

PathDicom = "C:\KarolinaMusial\zdjecia\T1\patient"
lstFilesDCM = list()  # create an empty list
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append((os.path.join(dirName,filename)))

for i in range(len(lstFilesDCM)):
    file = dicom.read_file(lstFilesDCM[i])
    PatientSex = file['PatientSex'].value
    PatientAge = file['PatientAge'].value
    Modality = file['Modality'].value
    BodyPart = file['BodyPartExamined'].value
    Rows = file['Rows'].value
    Columns = file['Columns'].value
    PixelSpacing = file['PixelSpacing'].value
#    X, Y = convertPixelSpacing2float(PixelSpacing)
    SliceThickness = file['SliceThickness'].value
    BitsAllocated = file['BitsAllocated'].value
    BitsStored = file['BitsStored'].value
    HighBit = file['HighBit'].value
    LargestPixelValue = file['LargestImagePixelValue'].value
    InstanceCreationDate = file['InstanceCreationDate'].value
    print('Skan nr:', i+1, "Pateint's Sex", PatientSex, "Pateint's Age", PatientAge, "Modality", Modality,
          "Body Part", BodyPart, 'Rows', Rows, "Columns", Columns, "Pixel Spacing", PixelSpacing, "Slice Thickness",
          SliceThickness, "Bits Allocated", BitsAllocated, "Bits Storred", BitsStored, "High Bit", HighBit,
          "Largest Image Pixel Value", LargestPixelValue)



#Przekształcenie daty
year = InstanceCreationDate[:4]
month = InstanceCreationDate[4:6]
day = InstanceCreationDate[6:8]
date = year+'-'+month+'-'+day
print(date)


# -----------------------------------------------------Połączenie z mySQL---------------------------------------------------------------------------------

mydatabase = mysql.connector.connect(
  host="xxxx",
  user="xxxx",
  password="xxxx",
  database="xxxx" #connecting with a specific database
)

print("Connecting:", mydatabase)

# --------------------------------------------------Wczytanie danych do mySQL------------------------------------------------------------------------------

#set the cursor
mycursor = mydatabase.cursor()

#check existing database
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print("Show database:", x)

#check existing tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print("Show TABLES:", x)

#check existing columns
mycursor.execute("SHOW columns FROM Tomografia")

for x in mycursor:
    print("Show columns:", x)

#insert a record in the table
sql = "INSERT INTO Tomografia (InstanceCreationDate, PatientSex, PatientAge, Modality, BodyPartExamined, Rows, Columns, PixelSpacing, SliceThickness, BitsAllocated, BitsStored, HighBit, LargestPixelValue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (InstanceCreationDate, PatientSex, PatientAge, Modality, BodyPart, Rows, Columns, PixelSpacing, SliceThickness, BitsAllocated, BitsStored, HighBit, LargestPixelValue)
#val = ("2016-03-18", "F", "23", "MR", "BRAIN", "256", "256", "[1,1]", "1", "16", "12", "11", "100")
mycursor.executemany(sql, val)

mydatabase.commit()

print(mycursor.rowcount, "record inserted")