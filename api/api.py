import time
import requests
import json

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
headers = {'User-Agent': 'CommanderSearch/0.0.1', 
           'Accept': 'application/json'
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/getCard")
def get_card():
    r = requests.get("https://api.scryfall.com/cards/random", headers=headers)
    if r.status_code == 200:
        print("Card data fetched successfully")
        data = r.json()
        return jsonify(data)
    return jsonify({'error': 'Failed to fetch card data'}), r.status_code

@app.route("/api/search", methods=['POST'])
def search_cards():
    colors = []
    selected_colors = []
    colors = request.json['colors']
    searchTerms = request.json['searchTerms']
    effects = []
    print(searchTerms)
        
    for color in colors['colors']:
        #print(color)
        if 'checked' in color and color['checked']:
            if color['name'] == 'White':
                selected_colors.append('W')
            elif color['name'] == 'Blue':
                selected_colors.append('U')
            elif color['name'] == 'Black':
                selected_colors.append('B')
            elif color['name'] == 'Red':
                selected_colors.append('R') 
            elif color['name'] == 'Green':
                selected_colors.append('G')

    q="?q=is%3Acommander+legal%3Acommander+%28game%3Apaper%29"
    if selected_colors != []:
        q += "+id%3D" + ''.join(selected_colors)
    if searchTerms != []:
        for term in searchTerms['searchTerms']:
            if term['type'] == 'Oracle Text':
                if ' ' in term['value']:
                    effects = term['value'].split()
                    for effect in effects:
                        if '+' in effect:
                            effect = effect.replace('+', '%2B')
                        q+= "+o%3A" + effect
                else:
                    effects = term['value']
                    if '+' in effects:
                        effects = effects.replace('+', '%2B')
                    q+= "+o%3A" + effects
            elif term['type'] == 'CMC':
                q+= "+cmc%3D" + term['value']
            elif term['type'] == 'Power':
                q+= "+pow%3D" + term['value']
            elif term['type'] == 'Toughness':
                q+= "+tou%3D" + term['value']
            elif term['type'] == 'Artist':
                if ' ' in term['value']:
                    effects = term['value'].split()
                    q+= '+artist%3A"'
                    for effect in effects:
                        if ' ' in effect:
                            effect = effect.replace(' ', '+')
                        q+= effect
                    q+= '"'
                else:
                    effects = term['value']
                    q+= "+artist%3A" + effects
            elif term['type'] == 'Rarity':
                q+="rarity%3A"
                match term['value']:
                    case "Common":
                        q+="c"
                    case "Uncommon":
                        q+="u"
                    case "Rare":
                        q+="r"
                    case "Mythic":
                        q+="m"
    print(q)
    r = requests.get("https://api.scryfall.com/cards/random" + q, headers=headers)
    if r.status_code == 200:
        print("Card data fetched successfully")
        #card_data = r.json()
        #return render_template('card.html', card=card_data)
        data = r.json()
        return jsonify(data)
    return jsonify({'error': 'Failed to fetch card data'}), r.status_code