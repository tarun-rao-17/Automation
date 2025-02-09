from PIL import Image, ImageFilter,ImageOps,ImageEnhance

import os
file="img.jpeg"
img = Image.open(file)
edit1=img.rotate(270).save("rotated_hopper_270.jpg")
edit2=img.rotate(180).save("rotated_hopper_180.jpg")
edit3=img.rotate(90).save("rotated_hopper_90.jpg")

filename=[

    "img.jpeg",
    "rotated_hopper_270.jpg",
    "rotated_hopper_180.jpg",
    "rotated_hopper_90.jpg",
]
images=[Image.open(x) for x in filename]
images[0].save(
    'animated.gif',
    save_all=True,
    append_images=images[1:],
    duration=1000,
    loop=0
)
os.system("animated.gif")


 



 





