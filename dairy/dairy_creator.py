import os
from datetime import datetime

from jinja2 import Template

from text import dairy_

with open(os.getcwd() + '/template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

    title = dairy_.split('\n')[0]
    context = dairy_.split('\n')[1:]
    text = {'title': title, 'context': context, 'date': datetime.now()}

    nature = template.render(text=text)

    with open(os.getcwd() + '/' + title + '.html', 'w', encoding='utf-8') as wf:
        wf.write(nature)
