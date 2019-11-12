from PIL import Image

if __name__ == '__main__':
    img = Image.open('GUIUtils\\pic\\pic_1.gif')
    w,h = img.size
    img = img.resize((int(w/4),int(h/4)))
    img.save('1.gif')