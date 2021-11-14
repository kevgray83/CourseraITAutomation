
#!/usr/bin/env python3
import os
import requests


upload_path = "/supplier-data/descriptions/"
url = "http:// /fruits/"

files = os.listdir(upload_path)

for file in files:
        print(file)
        with open(upload_path+file) as f:
                fruit_name = os.path.splitext(file)[0]
                review = f.read().split("\n")
                description = {"name": review[0], "weight":(review[1].strip(" lbs")), "description":review[2], "image_name":fruit_name + ".jpeg"}
                #print(feedback)
        response = requests.post(url,data=description)

        print(response.status)


       
        
        

