from PIL.Image import open as OpenImage
from PIL.ImageFont import load_default
from PIL.ImageDraw import Draw

def add_watermark(image_path : str, text: str = 'Example', size: int = 30, margin: int = 5, padding: int = 10,show: bool = True, save_path: str | None = None):
    im = OpenImage(image_path)
    img_width, img_height = im.size
    draw = Draw(im)
    police = load_default(size=size)

    text_width, text_height = police.getbbox(text)[2], size
    x = img_width - text_width - 10
    y = img_height - text_height - 10
    largeur_rectangle = text_width + padding
    hauteur_rectangle = text_height + padding

    draw.rectangle((x-margin, y-margin, x + largeur_rectangle - margin, y + hauteur_rectangle - margin), fill="black")
    draw.text((x - margin, y - margin), text, font=police, fill="white")

    (im.show() if show else None)
    (im.save(save_path) if save_path else None)

if __name__ == '__main__':
    add_watermark(
        '/Users/kali/Desktop/test.png',
        text='Salut',
        show=True,
        #save_path='/Users/kali/Desktop/t.jpg',
        margin=30,
        padding=10,
        size=35)
