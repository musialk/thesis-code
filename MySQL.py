import mysql.connector
import os
import pydicom as dicom


def connectMySQL(host, database):
    if host == 'xxxx' and database == 'xxxx':
        mydb = mysql.connector.connect(
            host="xxxx",
            user="xxxx",
            password="xxxx",
            database="xxxx"
        )
    return mydb


def getDatabases(mydb):
    data = mydb.cursor()
    query = "SHOW DATABASES"
    data.execute(query)
    out = []
    for x in data:
        out.append(x[0])
    return out


def getTables(mydb):
    data = mydb.cursor()
    query = "SHOW TABLES"
    data.execute(query)
    out = []
    for x in data:
        out.append(x[0])
    return out


def getColumnNameFromTable(mydb, table):
    data = mydb.cursor()
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + table + "';"
    data.execute(query)
    result = data.fetchall()
    out = []
    for x in result:
        out.append(x[0])
    return out


def getLimitRecords(mydb, table, limit):
    data = mydb.cursor()
    query = "select * from " + table
    query += ' limit ' + str(limit)
    query += ";"
    data.execute(query)
    result = data.fetchall()
    out = []
    for record in result:
        rec = []
        for field in record:
            rec.append(field)
        out.append(rec)
    return out


def createTable(mydb):
    data = mydb.cursor()
    query = "CREATE TABLE Metadata (id INT AUTO_INCREMENT PRIMARY KEY, creation_date VARCHAR, description VARCHAR(255))"
    data.execute(query)
    out = []
    for x in data:
        out.append(x[0])
    return out


def deleteTable(mydb, name):
    data = mydb.cursor()
    query = "DROP TABLE " + name + ""
    data.execute(query)
    result = data.fetchall()
    out = []
    for x in result:
        out.append(x[0])
    return out


mydb = connectMySQL(host='xxxx', database='xxxx')
mycursor = mydb.cursor()


PathDicom = "D:\\Praktyki-Inzynierka\\zdjecia\\torso3"
lstFilesDCM = list()
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():
            lstFilesDCM.append((os.path.join(dirName, filename)))

# print(lstFilesDCM[:])

for i in range(len(lstFilesDCM)):
    file = dicom.read_file(lstFilesDCM[i])
    PatientSex = file['PatientSex'].value
    #PatientAge = file['PatientAge'].value
    Modality = file['Modality'].value
    BodyPart = file['BodyPartExamined'].value
    SliceThickness = file['SliceThickness'].value
    # InstanceCreationDate = file['InstanceCreationDate'].value

    print('Skan nr:', i+1, "Pateint's Sex", PatientSex, "Modality", Modality,
          "Body Part", BodyPart, "Slice size", SliceThickness)


# #insert a record in the table
# sql = "insert into Metadata (creation_date, patient_sex, modality, body_part, slice_size) values (1, 20160318, 0, 23, MR, BRAIN, 256)"
# # val = Modality
# mycursor.execute(sql)
# mydb.commit()


#insert a record in the table
sql = "insert into Processed_data (json_data, description) values (json, opis)"
# val = Modality
mycursor.execute(sql)
mydb.commit()

print('')
print('DATABASES:')
out1 = getDatabases(mydb)
print(out1)
print('')
print('TABLES:')
out2 = getTables(mydb)
print(out2)
print('')
print('COLUMN_Names:')
out3 = getColumnNameFromTable(mydb, "Metadata")
out4 = getColumnNameFromTable(mydb, "Processed_data")
print("Metadata", out3, "\n", "Processed_data", out4)
print('')
print('Records:')
result = getLimitRecords(mydb, table=out2[0], limit=10)
print(result)


