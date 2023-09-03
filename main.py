from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
# you should write csv file outside of function, so it only load once
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/def/v1/<word>")
def definition(word):
    word_def = df.loc[df["word"] == word]["definition"].squeeze()
    return {"word": word,
            "definition": word_def}


if __name__ == "__main__":
    app.run(debug=True)
