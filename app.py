from flask import Flask, render_template
import pandas as pd

import Italian_Real_Estate_Web_Scraper as irews

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

df = pd.read_csv("ImmobiliareWebScraperDataset.csv")
df.to_csv("ImmobiliareWebScraperDataset.csv", index=None)

@app.route("/")
def index():
    data = pd.read_csv("ImmobiliareWebScraperDataset.csv")
    return render_template("index.html", tables=[data.to_html()], titles=[''])

#-----Button Click Action-----
@app.route("/update", methods=["POST"])
def update():
    irews.check_price()
    data = pd.read_csv("ImmobiliareWebScraperDataset.csv")
    return render_template("index.html", tables=[data.to_html()], titles=[''])

if __name__ == "__main__":
    app.run()