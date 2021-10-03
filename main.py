from PIL import Image
import requests
from progress.bar import Bar

im = Image.open("kittens.jpg")
im.show()
print(im.format, im.size, im.mode)

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
bar = Bar('Processing', max=20)
for i in range(20):
    # Какая-то работа
    bar.next()
bar.finish()

