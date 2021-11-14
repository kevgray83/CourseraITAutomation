
#!/usr/bin/env python3
import os
import requests


upload_path = "/data/feedback/"
url = "http://34.132.28.237/feedback/"

files = os.listdir(upload_path)

for file in files:
        print(file)
        with open(upload_path+file) as f:
                review = f.read().split("\n")
                feedback = {"title": review[0], "name":review[1], "date":review$
                #print(feedback)
        response = requests.post(url,data=feedback)

        print(response.status)


       
        
        

