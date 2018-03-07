import os
from datetime import datetime

from jinja2 import Template
import qrcode

from text import dairy_

with open(os.getcwd() + '/template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

    title = dairy_.split('\n')[0]
    context = dairy_.split('\n')[1:]
    text = {'title': title, 'context': context, 'date': datetime.now()}

    nature = template.render(text=text)

    with open(os.getcwd() + '/' + title + '.html', 'w', encoding='utf-8') as wf:
        wf.write(nature)

qr = qrcode.QRCode(version=7,
                   error_correction=qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=30)

qr.add_data('http://xn--viqv0at04j.xn--6qq986b3xl/dairy/%s.html' % title)
qr.make()

img = qr.make_image(fill_color="white", back_color="blue")
img.save(open('%s.png' % title, 'wb'))
