import os

index=0
for filename in os.listdir("."):
    if filename.endswith(".jpg"):
        os.rename(filename,str(index)+".jpg")
        backgrounds=open("backgrounds.json","r").read()
        backgrounds=backgrounds.replace(filename,str(index) + ".jpg")
        with open("backgrounds.json","w") as file:
            file.write(backgrounds)
        index+=1
