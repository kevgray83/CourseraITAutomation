#!/usr/bin/env python3

import os
import datetime
import reports


if __name__ == "__main__":
    upload_path = "/supplier-data/descriptions/"
    files = os.listdir(upload_path)
    pdf_data = ""
    for file in files:
            print(file)
            with open(upload_path+file) as f:
                data = f.read().split("\n")
                name = data[0]
                weight = data[1]
                pdf_data = "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    title = "Processed Update on " + current_date
    reports.generate_report(("/tmp/processed.pdf", title, pdf_data)#
    
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)
            
            
