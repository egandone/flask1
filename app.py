import os
from io import StringIO
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
def index():
  out = StringIO()
  out.write('<html><body>')
  out.write('<h1>Hello, World!</h1>\n')
  out.write('<pre>')
  for param in os.environ.keys():
    out.write("%40s %s\n" % (param,os.environ[param]))
  out.write('</pre>')
  out.write('</body></html>')
  return out.getvalue()

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
