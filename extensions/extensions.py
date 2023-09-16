fname = input("File name: ").strip().lower()
gif = fname.endswith(".gif")
jpg = fname.endswith(".jpg")
jpeg = fname.endswith(".jpeg")
png = fname.endswith(".png")
pdf = fname.endswith(".pdf")
txt = fname.endswith(".txt")
zip = fname.endswith(".zip")

if gif == True:
    print('image/gif')
elif jpg == True or jpeg == True:
    print('image/jpeg')
elif png == True:
    print ('image/png')
elif pdf == True:
    print('application/pdf')
elif txt == True:
    print('text/plain')
elif zip == True:
    print('application/zip')
else:
    print('application/octet-stream')
