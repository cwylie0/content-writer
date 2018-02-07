""" Device Service Page Content Generator INPUT: user input device name, contentTemplate.py OUTPUT: .csv version 
of a set of unique service cateogory pages for a specific device, in the following template: optional video, h2 
title, optional disclaimer, intro paragraph, diagnostic paragraph, shipping paragraph, warranty paragraph """ 
import random import csv from contentTemplate import * services = {
    'Diagnostic Service': 0.00,
    'Glass Repair': 199.99,
    'Glass & LCD Repair': 189.99,
    'Battery Replacement': 69.99,
    'Charging Port Repair': 69.99,
    'Front Camera Repair': 69.99,
    'Headphone Jack Repair': 69.99,
    'Home Button Repair': 69.99,
    'Loud Speaker Repair': 69.99,
    'Microphone Repair': 69.99,
    'Power Button Repair': 69.99,
    'Rear Camera Repair': 69.99,
    'Volume Button Repair': 69.99,
    'Water Damage Repair': 0.00,
    'Ear Speaker Repair': 69.99,
    'Vibrate Switch Repair': 69.99
}
print("") print("Device Service Page Content Generator ver 3.0") 
print("---------------------------------------------") print("") device = input("ENTER DEVICE: ") row = 
['Active', 'Name', 'Categories', 'Retail price', 'Tax rule', 'Short description', 'Description',
       'Tags', 'Meta title', 'Meta description', 'URL rewritten', 'Available for order', 'Show price'] a = [] 
a.append(row) for service in services:
    serviceName = device + " " + service
    category = device + "Repair Services"
    cost = services[service]
    taxRule = 9
    tags = serviceName
    metaTitle = serviceName
    outputFileName = device + " " + service + ".html"
    outputFileName = outputFileName.replace(" ", "-")
    title = "<h2>" + serviceName + "</h2>"
    shortDescription = "<strong><h4>CALL 888-494-4349 for latest pricing</h4></strong><br/><ul><li>90-day 
warranty</li><li>Excellent customer service</li><li>Expert technicians</li></ul>"
    urlRewritten = serviceName.replace(" ", "-")
    metaDescription = serviceName + \
        " performed by repair experts iFixYouri. Warranty included. Call today 888-494-4349."
    l = []
    if service == "Water Damage Repair":
        l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/GfawakMoM9E?rel=0"))
    if service == "Diagnostic Service":
        l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/9z61L7QyDVo"))
    if service == "Glass Repair":
        l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/1vrnuazxPIo"))
    if service == "Glass & LCD Repair":
        l.append(videoDiv.replace("YOUTUBEURL",
                                  "https://www.youtube.com/embed/tF_zuMX4ixI"))
    l.append(title)
    if service == "Diagnostic Service" or service == "Water Damage Repair":
        l.append(disclaimer)
    l.append(random.choice(intro))
    l.append(random.choice(diagnostic))
    l.append(random.choice(shipping))
    l.append(random.choice(warranty))
    longDescription = ''.join(l)
    longDescription = longDescription.replace("SERVICE", service)
    longDescription = longDescription.replace("DEVICE", device)
    row = ['1', serviceName, category, cost, taxRule, shortDescription,
           longDescription, tags, metaTitle, metaDescription, urlRewritten, '1', '1']
    a.append(row) device = device.replace(" ", "-") outputFileName = device + '.csv' myFile = 
open(outputFileName, 'w') with myFile:
    writer = csv.writer(myFile)
    writer.writerows(a) print('\n') print('Create a category called ' + device + '.') print('Upload the file 
below into that product category.') print("FILE CREATED: " + outputFileName) print('\n')
