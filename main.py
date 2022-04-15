# IMAGE: manipula a imagem
# IMAGEFONT: manipula a fonte
# IMAGEDRAW: desenha na imagem

import time
from datetime import date
from PIL import ImageFont, ImageDraw, Image

v = 30
h = 1000
coord_data = (h+200,v)
data = date.today().strftime('%d/%m/%Y')

with open(r'textos.txt', 'r') as f:

	textos = f.read()

	for texto in textos.split('\t'):

		coord_texto = (h,v+30)

		imagem = Image.open(r'5w2h.jpg')
		caminho_fonte = r"font/allstar.ttf"
		font = ImageFont.truetype(caminho_fonte, 24)
		rgb_preto = (255,255,255)
		desenho = ImageDraw.Draw(imagem)
		desenho.text(coord_texto, texto, font=font, fill=rgb_preto)

desenho.text(coord_data, data, font=font, fill=rgb_preto)
imagem.save(f"/home/kromodoro/Imagens/Wallpapers/5w2h.jpg")


