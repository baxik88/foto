import os
from PIL import Image



for fn in os.listdir('.\\'):



	name = fn.split('.')
	img_name = name[0] + ".jpg"
	print(img_name)

	# foreground = Image.open("V.png").convert('RGBA')
	newfoto = Image.open(fn)
	# area = (458, 0, 1500, 1118)
	# crop_img = background.crop(area)
	
	background = newfoto.resize((1920, 1080),Image.ANTIALIAS)
	# back = background.resize((1658, 1118),Image.ANTIALIAS)

	# background.paste(foreground, (0, 0), foreground)

	# background.save(f"{save_path}\\{img_name}")
	background.save(f"C:\\Users\\bax\\Desktop\\foto\\png\\{img_name}", quality=90)