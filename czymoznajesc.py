from flask import Flask, request, render_template, jsonify
from fuzzywuzzy import process
import listajedzenia
import czyjestjedzeniem

app = Flask(__name__)

combined_food_list = czyjestjedzeniem.polish_food_list + list(listajedzenia.niejescwciazy_uzasadnienie.keys())

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    print(query)
    if query in combined_food_list:
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
    best_match = process.extractOne(query, combined_food_list)
    if 50 > best_match[1]:
        suggestions = [word for word in combined_food_list if word.startswith(query)]
    else:
        suggestions = [best_match[0]]
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
