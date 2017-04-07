from flask import Flask
from flask import render_template
from flask import request
from lxml import etree


app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def index():
    xml = ''
    xmlInput = ''
    if request.method == 'POST':
        xmlInput = request.form.get('xml')
        xml = transform(xmlInput)
    return show_form(xml,xmlInput)


def show_form(xml=None,xmlInput=None):
    return render_template('index.html', xml=xml, xmlInput=xmlInput);


def transform(xml):
    xslt_xml = etree.parse(open("xslt/transcription.xsl"))
    transform = etree.XSLT(xslt_xml)
    tree = etree.fromstring(xml)
    return etree.tostring(transform(tree))


if __name__ == "__main__":
    app.run(port=8002)
