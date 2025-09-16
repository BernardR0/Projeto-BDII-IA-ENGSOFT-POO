from flask import Flask, url_for
from logica_fuzzy import calculo_fuzzy
from configuration import configure_all


app = Flask(__name__)

configure_all(app)

app.run(debug=True)



