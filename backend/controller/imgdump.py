import os

def imglista ():
    palautettava = ""

    for img in os.listdir("../frontend/Image_dump"):
        palautettava += f'<img src="{os.path.join("/Image_dump", img)}" alt "random ass img">'
    return palautettava