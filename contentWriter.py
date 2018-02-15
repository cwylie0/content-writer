""" Device Service Page Content Generator INPUT: user input device name, contentTemplate.py OUTPUT: .csv version of a set of unique service cateogory pages for a specific device, in the following template: optional video, h2 
title, optional disclaimer, intro paragraph, diagnostic paragraph, shipping paragraph, warranty paragraph """ import random import csv from contentTemplate import * services = {
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
print("") print("Device Service Page Content Generator ver 3.0") print("---------------------------------------------") print("") device = input("ENTER DEVICE: ") row = ['Active', 'Name', 'Categories', 'Retail price', 'Tax 
rule', 'Short description', 'Description',
       'Tags', 'Meta title', 'Meta description', 'URL rewritten', 'Available for order', 'Show price'] a = [] a.append(row) for service in services:
    serviceName = device + " " + service
    category = device + " Repair Services"
    cost = services[service]
    taxRule = 9
    tags = serviceName
    metaTitle = serviceName
    outputFileName = device + " " + service + ".html"
    outputFileName = outputFileName.replace(" ", "-")
    title = "<h2>" + serviceName + "</h2>"
    shortDescription = "<strong><h4>CALL 888-494-4349 for latest pricing</h4></strong><br/><ul><li>90-day warranty</li><li>Excellent customer service</li><li>Expert technicians</li></ul>"
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
    l.append(random.choice(intro))
    if service == "Diagnostic Service" or service == "Water Damage Repair":
        l.append(disclaimer)
    if service == "Water Damage Repair":
        l.append(" Water Damage repair is what you need if you have splashed or submerged your DEVICE in water or any other liquid. iFixYouri has a high success rate restoring devices that have lost power or function after 
coming in contact with liquid.")
    if service == "Diagnostic Service":
        l.append(" This is the service you need if you aren't quite sure what the problem with your DEVICE is. We'll find out what is going on, and contact you with a repair quote.")
    if service == "Glass Repair":
        l.append(" Those who have both cracked glass and a broken LCD should opt for our DEVICE Glass & LCD Repair. This service is for glass breakage only.")
    if service == "Glass & LCD Repair":
        l.append(" Those who have only cracked glass, NOT a broken LCD, should opt for our DEVICE Glass Repair. This service is for both cracked glass and a broken LCD.")
    if service == "Battery Replacement":
       l.append(" Old or bad batteries can really be frustrating. You might need SERVICE if your battery does not hold charge well or charges very slowly or barely at all.")
    if service == "Charging Port Repair":
       l.append(" Charging port repair may be what you need if your device is charging slowly or not at all. Sometimes the battery needs replacement. Whatever the case, the professional technicians at iFixYouri can help.")
    l.append(random.choice(diagnostic))
    l.append(random.choice(shipping))
    l.append(random.choice(warranty))
    longDescription = ''.join(l)
    longDescription = longDescription.replace("SERVICE", service)
    longDescription = longDescription.replace("DEVICE", device)
    row = ['1', serviceName, category, cost, taxRule, shortDescription,
           longDescription, tags, metaTitle, metaDescription, urlRewritten, '1', '1']
    a.append(row) device = device.replace(" ", "-") outputFileName = device + '.csv' myFile = open(outputFileName, 'w') with myFile:
    writer = csv.writer(myFile)
    writer.writerows(a) print('\n') print('Create a category called ' + device + '.') print('Upload the file below into that product category.') print("FILE CREATED: " + outputFileName) print('\n')
