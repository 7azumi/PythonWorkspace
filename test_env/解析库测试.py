import lxml
import bs4
import pyquery
import tesserocr
from lxml import etree
from PIL import Image

image = Image.open('verycode.png')
print(tesserocr.image_to_text(image))
