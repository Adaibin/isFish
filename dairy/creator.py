import os
from datetime import date, datetime

from jinja2 import Template
import qrcode

domain = 'http://xn--viqv0at04j.xn--6qq986b3xl'


def folder_():
    """find new folders"""
    files = os.listdir(os.getcwd())
    folders = [f for f in files if os.path.isdir(f)]

    if not os.path.exists('folder.fish'):
        _ = open('folder.fish', 'w')

    with open('folder.fish', 'r') as f_:
        folders_ = f_.readlines()
        folders_new = [f for f in folders if f not in folders_]
    with open('folder.fish', 'w') as f_:
        f_.writelines(folders_new)

    return folders_new


def creator_(folder):
    """create page file"""
    # get content
    path_ = '/'.join((os.getcwd(), folder))
    content_file = '/'.join((path_, 'content.fish'))
    if not os.path.exists(content_file):
        print('there is no content file in this folder.')
        return False
    with open(content_file, 'r') as f_:
        content_ = f_.readlines()
        if len(content_) < 2:
            print('this is not content in content.fish.')
            return False
        title = content_[0].strip()
        context = content_[1:]

    # get image&music files
    files = os.listdir('/'.join((os.getcwd(), folder)))
    files_ = {'.jpg': [], '.png': [], '.mp3': [], '.wma': []}
    [files_[f.lower()[-4:]].append(f) for f in files if f.lower()[-4:] in files_]
    images = files_['.jpg'] + files_['.png']
    musics = files_['.mp3'] + files_['.wma']
    images.sort(), musics.sort()

    # render page
    with open(os.getcwd() + '/template.html', 'r', encoding='utf-8') as f:
        template = Template(f.read())
        text = {'title': title,
                'context': context,
                'images': images,
                'musics': musics,
                'date': datetime.now()}
        html = template.render(text=text)

    with open(path_ + '/' + title + '.html', 'w', encoding='utf-8') as wf:
        wf.write(html)

    qr = qrcode.QRCode(version=7,
                       error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=10,
                       border=30)

    qr.add_data('%s/dairy/%s/%s.html' % (domain, folder, title))
    qr.make()

    img = qr.make_image(fill_color="white", back_color="blue")
    img.save(open('%s/%s.png' % (folder, title), 'wb'))


creator_('20180309')

