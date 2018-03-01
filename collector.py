import os
from datetime import datetime

from jinja2 import Template

from text import dairy


with open(os.getcwd() + '/template.html', 'r') as f:
    template = Template(f.read())

    title = dairy.split('\n')[0]
    context = dairy.split('\n')[1:]
    text = {'title': title, 'context': context, 'date': datetime.now()}

    nature = template.render(text=text)

    with open(os.getcwd() + '/' + title + '.html', 'w', encoding='utf-8') as wf:
        wf.write(nature)
