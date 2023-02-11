import pydicom
import json

filename = "IM-0001-0010.dcm"
ds = pydicom.dcmread(filename)
print(ds.to_json())
dict1 = ds.to_json()

out_file = open("myfile.json", "w")
json.dump(dict1, out_file, indent=6)
out_file.close()