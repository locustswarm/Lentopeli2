import os

def imglista ():
    palautettava = []

    for img in os.listdir("../frontend/Image_dump"):
        img_path = os.path.join("../frontend/Image_dump", img)
        palautettava.append(img_path)

    return palautettava