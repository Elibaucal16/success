from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello():
return "Hello world"


if name == "main":
    app.run(debug=True)

def hello_world():
  head = '<h1>REGISTRESE</h1>'
  email = '<br><input type="email" id="email" name="email" required><br>'
  password = '<br><input type="text" id="nombre" name="nombre" required><br>'
  enviar = '<br><input type="submit" value="Enviar">'
  return head + 'Correo:' + email + 'Contraseña:' + password + enviar

