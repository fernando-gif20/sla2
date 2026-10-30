
from flask import Flask, render_template

# Criar o aplicativo Flask
app = Flask(__name__)

# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    return "Bem-vindo ao Dashboard!"

# Executar servidor
if __name__ == "__main__":
    app.run(debug=True)
