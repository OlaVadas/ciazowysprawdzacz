from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import process
import listajedzenia
import czyjestjedzeniem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form["query"]
    print(query)
    if query in czyjestjedzeniem.polish_food_list:
        if query in listajedzenia.niejescwciazy_uzasadnienie:
            rationale = listajedzenia.niejescwciazy_uzasadnienie[query]
            return render_template('niejedz.html', rationale=rationale, query=query)
        else:
            return render_template('jedz.html', query=query)
    else:
        return render_template('nieznaleziono.html', query=query)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query')
    best_match = process.extractOne(query, listajedzenia.niejescwciazy_uzasadnienie.keys())
    if 50 > best_match[1]:
        suggestions = [word for word in listajedzenia.niejescwciazy_uzasadnienie if word.startswith(query)]
    else:
        suggestions = [best_match[0]]
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(host='0.0.0.0')