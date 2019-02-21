import streetview
from PIL import Image


# streetview.download_panorama('drE6CR_cgPs2lyQJvG_eCw', 'ls', tile_dir='gg')
#
# #panorama = Image.new('RGB', (26 * 512, 13 * 512))

# streetview.panoids(34.0689, -118.445)


import json
import subprocess

id = 'DsK88fpAYl9NpNsM2yKMMA'
file_name = 'loop.json'
final_pano_name = id +'.jpg'
if subprocess.call(['node', 'panodata.js', id, file_name]) == 0:
    with open(file_name) as data_file:
        data = json.load(data_file)
    width_num = int(int(data['Data']['image_width']) / 512)
    height_num = int(int(data['Data']['image_height']) / 512)
    print(width_num)
    streetview.download_panorama('DsK88fpAYl9NpNsM2yKMMA', 'hhh', width_num, height_num, final_pano_name, cb=None)

#panorama.save('ls/hhu.jpg')