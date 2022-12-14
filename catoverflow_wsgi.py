from json import dumps
from os import path
from pprint import pformat
from urllib import parse

def application(environ, start_response):
  status = '200 OK'

  # show the environment:
  output = [b'<pre>']
  output.append(pformat(environ).encode('utf-8'))

  output.append(b'\n\nPATH_INFO: ' + environ['PATH_INFO'].encode('utf-8'))
  filepath, filename = path.split(environ['PATH_INFO'])
  filebase, fileext = path.splitext(filename)
  output.append(b'\nPath = ' + filepath.encode('utf-8'))
  output.append(b'\nFile = ' + filename.encode('utf-8'))
  output.append(b'\nFile Base = ' + filebase.encode('utf-8'))
  output.append(b'\nFile Ext = ' + fileext.encode('utf-8'))

  output.append(b'\n\nQUERY_STRING is\n' + environ['QUERY_STRING'].encode('utf-8'))
  queryDict = parse.parse_qs(environ['QUERY_STRING'])
  output.append(b'\n\nQUERY_STRING as a dict:\n')
  output.append(dumps(queryDict, sort_keys=True, indent=2).encode('utf-8'))

  output.append(b'</pre>')

  #create a simple form:
  output.append(b'\n\n<form method="post">')
  output.append(b'<input type="text" name="test">')
  output.append(b'<input type="submit">')
  output.append(b'</form>')

  if environ['REQUEST_METHOD'] == 'POST':
    # show form data as received by POST:
    output.append(b'\n\n<h1>FORM DATA</h1>')
    output.append(b'\n<pre>')
    output.append(pformat(environ['wsgi.input'].read()).encode('utf-8'))
    output.append(b'</pre>')

  # send results
  output_len = sum(len(line) for line in output)

  response_headers = [('Content-type', 'text/html'),
                      ('Content-Length', str(output_len)),
                      ('X-Clacks-Overhead', 'GNU Terry Pratchett')]

  start_response(status, response_headers)

  return output


app = application
