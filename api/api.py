import time
import requests
import json

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
headers = {'User-Agent': 'CommanderSearch/0.0.1', 
           'Accept': 'application/json'
}

UBSets = {
    "Marvel: Darkhold Destiny": "mdd",
    "Darkhold Destiny Commander": "mdc",
    "Star Trek": "trk",
    "Star Dates": "sds",
    "Star Trek Commander": "trc",
    "The Hobbit": "hob",
    "The Hobbit Eternal": "hoc",
    "Marvel Super Heros": "msh",
    "Marvel Super Heroes Commander": "msc",
    "Teenage Mutant Ninja Turtles": "tmt",
    "Teenage Mutant Ninja Turtles Eternal": "tmc",
    "Avatar: The Last Airbender": "tla",
    "Avatar: The Last Airbender Eternal": "tle",
    "Marvel's Spiderman": "spm",
    "Marvel's Spiderman Eternal": "spe",
    "Marvel Universe": "mar",
    "Final Fantasy": "fin",
    "Final Fantasy Commander": "fic",
    "Assassin's Creed": "acr",
    "Fallout": "pip",
    "Doctor Who": "who",
    "The Lord of the Rings: Tales of Middle-earth": "ltr",
    "Tales of Middle-earth Commander": "ltc",
    "Transformers": "bot",
    "Warhammer 40,000 Commander": "40k"
}

allSets = {
    'Stardates': 'sds',
    'Reality Fracture': 'fra',
    'Reality Fracture Commander': 'frc',
    'Reality Fracture Promos': 'pfra',
    'The Zeta Set': 'slz',
    'The Hobbit Eternal': 'hoc',
    'The Hobbit': 'hob',
    'Marvel Super Heroes Commander': 'msc',
    'Marvel Super Heroes': 'msh',
    'Secrets of Strixhaven Promos': 'psos',
    'Secrets of Strixhaven': 'sos',
    'Secrets of Strixhaven Commander': 'soc',
    'Teenage Mutant Ninja Turtles': 'tmt',
    'Teenage Mutant Ninja Turtles Source Material': 'pza',
    'Teenage Mutant Ninja Turtles Eternal': 'tmc',
    'Year of the Horse 2026': 'pl26',
    'Lorwyn Eclipsed Promos': 'pecl',
    'Lorwyn Eclipsed Commander': 'ecc',
    'Lorwyn Eclipsed': 'ecl',
    'MagicFest 2026': 'pf26',
    'Wizards Play Network 2026': 'pw26',
    'Avatar: The Last Airbender Promos': 'ptla',
    'Avatar: The Last Airbender': 'tla',
    'Avatar: The Last Airbender Eternal': 'tle',
    'Marvel Legends Series Inserts': 'lmar',
    "Marvel's Spider-Man Promos": 'pspm',
    "Marvel's Spider-Man Eternal": 'spe',
    "Marvel's Spider-Man": 'spm',
    'Marvel Universe': 'mar',
    'Arena Anthology 4': 'aa4',
    'Arena Anthology 3': 'aa3',
    'Through the Omenpaths Bonus Sheet': 'omb',
    'Through the Omenpaths': 'om1',
    'Arena Anthology 2': 'aa2',
    'Edge of Eternities Promos': 'peoe',
    'Edge of Eternities Commander': 'eoc',
    'The Big Score Promos': 'pbig',
    'Edge of Eternities': 'eoe',
    'Final Fantasy Promos': 'pfin',
    'Final Fantasy: Through the Ages': 'fca',
    'Final Fantasy Commander': 'fic',
    'Final Fantasy': 'fin',
    'FIN Standard Showdown': 'pss5',
    'Pioneer Anthology 1': 'pa1',
    'Tarkir: Dragonstorm Promos': 'ptdm',
    'Tarkir: Dragonstorm Commander': 'tdc',
    'Tarkir: Dragonstorm': 'tdm',
    'Aetherdrift Promos': 'pdft',
    'Aetherdrift': 'dft',
    'Aetherdrift Commander': 'drc',
    'Year of the Snake 2025': 'pl25',
    'Innistrad Remastered': 'inr',
    'Spotlight Series': 'pspl',
    'Wizards Play Network 2025': 'pw25',
    'MagicFest 2025': 'pf25',
    'Pioneer Masters': 'pio',
    'Foundations Promos': 'pfdn',
    'Foundations Commander': 'fdc',
    'Foundations Jumpstart': 'j25',
    'Foundations': 'fdn',
    'Tales of Middle-earth Deluxe Commander Kit': 'pltc',
    'Duskmourn: House of Horror': 'dsk',
    'Duskmourn: House of Horror Commander': 'dsc',
    'Duskmourn: House of Horror Promos': 'pdsk',
    'Bloomburrow Promos': 'pblb',
    'Bloomburrow Commander': 'blc',
    'Mystery Booster 2': 'mb2',
    'Bloomburrow': 'blb',
    "Assassin's Creed": 'acr',
    'Modern Horizons 3 Promos': 'pmh3',
    'Modern Horizons 3 Commander': 'm3c',
    'Modern Horizons 3': 'mh3',
    'Modern Horizons 2 Timeshifts': 'h2r',
    'Outlaws of Thunder Junction Promos': 'potj',
    'Outlaws of Thunder Junction Commander': 'otc',
    'The Big Score': 'big',
    'Outlaws of Thunder Junction': 'otj',
    'Fallout': 'pip',
    'Ravnica: Clue Edition': 'clu',
    'Murders at Karlov Manor Promos': 'pmkm',
    'Murders at Karlov Manor': 'mkm',
    'Murders at Karlov Manor Commander': 'mkc',
    'Year of the Dragon 2024': 'pl24',
    'Ravnica Remastered': 'rvr',
    'Special Guests': 'spg',
    'The Lost Caverns of Ixalan Promos': 'plci',
    'March of the Machine: The Aftermath Promos': 'pmat',
    'The Lost Caverns of Ixalan': 'lci',
    'The Lost Caverns of Ixalan Commander': 'lcc',
    'Jurassic World Collection': 'rex',
    'Doctor Who': 'who',
    'Wilds of Eldraine Promos': 'pwoe',
    'Wilds of Eldraine Commander': 'woc',
    'Magic × Duel Masters Promos': 'pmda',
    'Wilds of Eldraine': 'woe',
    'Commander Masters': 'cmm',
    'Explorer Anthology 3': 'ea3',
    'Historic Anthology 7': 'ha7',
    'MagicFest 2023': 'pf23',
    'Tales of Middle-earth Promos': 'pltr',
    'Tales of Middle-earth Commander': 'ltc',
    'The Lord of the Rings: Tales of Middle-earth': 'ltr',
    'March of the Machine: The Aftermath': 'mat',
    'March of the Machine Commander': 'moc',
    'Multiverse Legends': 'mul',
    'March of the Machine': 'mom',
    'March of the Machine Promos': 'pmom',
    'Shadows of the Past': 'sis',
    'Shadows over Innistrad Remastered': 'sir',
    'Secret Lair Promo': 'slp',
    'Year of the Rabbit 2023': 'pl23',
    'Phyrexia: All Will Be One Promos': 'pone',
    'Phyrexia: All Will Be One': 'one',
    'Phyrexia: All Will Be One Commander': 'onc',
    'Dominaria Remastered': 'dmr',
    'Wizards Play Network 2023': 'pw23',
    'Explorer Anthology 2': 'ea2',
    'Starter Commander Decks': 'scd',
    'Jumpstart 2022': 'j22',
    "The Brothers' War Commander": 'brc',
    "The Brothers' War Retro Artifacts": 'brr',
    "The Brothers' War Promos": 'pbro',
    'Transformers': 'bot',
    "The Brothers' War": 'bro',
    'Secret Lair Countdown': 'slc',
    'Game Night: Free-for-All': 'gn3',
    'Unfinity': 'unf',
    'Warhammer 40,000 Commander': '40k',
    'Dominaria United Promos': 'pdmu',
    'Dominaria United': 'dmu',
    'Dominaria United Commander': 'dmc',
    '30th Anniversary Play Promos': 'p30a',
    'Explorer Anthology 1': 'ea1',
    'Historic Anthology 6': 'ha6',
    'Store Championships': 'sch',
    'Double Masters 2022': '2x2',
    "Alchemy Horizons: Baldur's Gate": 'hbg',
    "Battle for Baldur's Gate Promos": 'pclb',
    "Commander Legends: Battle for Baldur's Gate": 'clb',
    'New Capenna Commander Promos': 'pncc',
    'Streets of New Capenna': 'snc',
    'New Capenna Commander': 'ncc',
    'Streets of New Capenna Promos': 'psnc',
    'Game Day Promos': 'gdy',
    'Wizards Play Network 2022': 'pw22',
    'Universes Within': 'slx',
    'Year of the Tiger 2022': 'pl22',
    'Kamigawa: Neon Dynasty Promos': 'pneo',
    'Kamigawa: Neon Dynasty': 'neo',
    'Neon Dynasty Commander': 'nec',
    'Commander Collection: Black': 'cc2',
    'Innistrad: Double Feature': 'dbl',
    'Judge Gift Cards 2022': 'p22',
    'Innistrad: Crimson Vow Promos': 'pvow',
    'Innistrad: Crimson Vow': 'vow',
    'Crimson Vow Commander': 'voc',
    'Pioneer Challenger Decks 2021': 'q06',
    'Innistrad: Midnight Hunt Promos': 'pmid',
    'Midnight Hunt Commander': 'mic',
    'Innistrad: Midnight Hunt': 'mid',
    'Jumpstart: Historic Horizons': 'j21',
    'Adventures in the Forgotten Realms Promos': 'pafr',
    'Forgotten Realms Commander': 'afc',
    'Adventures in the Forgotten Realms': 'afr',
    'Love Your LGS 2021': 'plg21',
    'Modern Horizons 2 Promos': 'pmh2',
    'Modern Horizons 2': 'mh2',
    'Modern Horizons 1 Timeshifts': 'h1r',
    'Historic Anthology 5': 'ha5',
    'Strixhaven: School of Mages Promos': 'pstx',
    'Strixhaven: School of Mages': 'stx',
    'Commander 2021': 'c21',
    'Time Spiral Remastered': 'tsr',
    'Historic Anthology 4': 'ha4',
    'Kaldheim Promos': 'pkhm',
    'Kaldheim': 'khm',
    'Kaldheim Commander': 'khc',
    'Year of the Ox 2021': 'pl21',
    'Judge Gift Cards 2021': 'pj21',
    'Commander Collection: Green': 'cc1',
    'Commander Legends': 'cmr',
    'Kaladesh Remastered': 'klr',
    'The List': 'plst',
    'Zendikar Rising Promos': 'pznr',
    'Zendikar Rising': 'znr',
    'Zendikar Rising Commander': 'znc',
    'Amonkhet Remastered': 'akr',
    'Double Masters': '2xm',
    'Jumpstart Arena Exclusives': 'ajmp',
    'Jumpstart': 'jmp',
    'Core Set 2021 Promos': 'pm21',
    'Core Set 2021': 'm21',
    'Historic Anthology 3': 'ha3',
    'Ikoria: Lair of Behemoths Promos': 'piko',
    'Ikoria: Lair of Behemoths': 'iko',
    'Commander 2020': 'c20',
    'Historic Anthology 2': 'ha2',
    'Theros Beyond Death Promos': 'pthb',
    'Theros Beyond Death': 'thb',
    'Secret Lair Drop': 'sld',
    'Historic Anthology 1': 'ha1',
    'Game Night 2019': 'gn2',
    'Throne of Eldraine Promos': 'peld',
    'Throne of Eldraine': 'eld',
    'Planeswalker Championship Promos': 'pwcs',
    'Commander 2019': 'c19',
    'San Diego Comic-Con 2019': 'ps19',
    'Core Set 2020 Promos': 'pm20',
    'Core Set 2020': 'm20',
    'Modern Horizons Promos': 'pmh1',
    'Modern Horizons': 'mh1',
    'War of the Spark Promos': 'pwar',
    'War of the Spark': 'war',
    'Judge Gift Cards 2019': 'j19',
    'RNA Guild Kit': 'gk2',
    'Ravnica Allegiance Promos': 'prna',
    'Ravnica Allegiance': 'rna',
    'Ultimate Box Topper': 'puma',
    'Ultimate Masters': 'uma',
    'Game Night': 'gnt',
    'GRN Guild Kit': 'gk1',
    'Guilds of Ravnica Promos': 'pgrn',
    'Guilds of Ravnica': 'grn',
    'Commander 2018': 'c18',
    'MTG Arena Promos': 'pana',
    'Core Set 2019 Promos': 'pm19',
    'Core Set 2019': 'm19',
    'Battlebond Promos': 'pbbd',
    'Commander Anthology Volume II': 'cm2',
    'Battlebond': 'bbd',
    'Dominaria Promos': 'pdom',
    'Dominaria': 'dom',
    'Duel Decks: Elves vs. Inventors': 'ddu',
    'Masters 25': 'a25',
    'Rivals of Ixalan Promos': 'prix',
    'Rivals of Ixalan': 'rix',
    'Judge Gift Cards 2018': 'j18',
    'From the Vault: Transform': 'v17',
    'Iconic Masters': 'ima',
    'Duel Decks: Merfolk vs. Goblins': 'ddt',
    'Ixalan Promos': 'pxln',
    'Ixalan': 'xln',
    'Commander 2017': 'c17',
    'Hour of Devastation Promos': 'phou',
    'Hour of Devastation': 'hou',
    'Archenemy: Nicol Bolas': 'e01',
    'Commander Anthology': 'cma',
    'Amonkhet Promos': 'pakh',
    'Amonkhet Invocations': 'mp2',
    'Amonkhet': 'akh',
    'Duel Decks: Mind vs. Might': 'dds',
    'Modern Masters 2017': 'mm3',
    'Aether Revolt Promos': 'paer',
    'Aether Revolt': 'aer',
    'Judge Gift Cards 2017': 'j17',
    'Planechase Anthology': 'pca',
    'Treasure Chest': 'pz2',
    'Commander 2016': 'c16',
    'Kaladesh Promos': 'pkld',
    'Kaladesh': 'kld',
    'Conspiracy: Take the Crown': 'cn2',
    'From the Vault: Lore': 'v16',
    'Eldritch Moon Promos': 'pemn',
    'Eldritch Moon': 'emn',
    'Eternal Masters': 'ema',
    'Shadows over Innistrad Promos': 'psoi',
    'Shadows over Innistrad': 'soi',
    'Duel Decks: Blessed vs. Cursed': 'ddq',
    'Oath of the Gatewatch Promos': 'pogw',
    'Oath of the Gatewatch': 'ogw',
    'Judge Gift Cards 2016': 'j16',
    'Legendary Cube Prize Pack': 'pz1',
    'Commander 2015': 'c15',
    'Battle for Zendikar Promos': 'pbfz',
    'Battle for Zendikar': 'bfz',
    'From the Vault: Angels': 'v15',
    'Magic Origins Clash Pack': 'cp3',
    'Magic Origins Promos': 'pori',
    'Magic Origins': 'ori',
    'San Diego Comic-Con 2015': 'ps15',
    'Modern Masters 2015': 'mm2',
    'Tempest Remastered': 'tpr',
    'Dragons of Tarkir Promos': 'pdtk',
    'Dragons of Tarkir': 'dtk',
    'Fate Reforged Promos': 'pfrf',
    'Fate Reforged': 'frf',
    'Judge Gift Cards 2015': 'j15',
    'Duel Decks Anthology: Elves vs. Goblins': 'evg',
    'Duel Decks Anthology: Divine vs. Demonic': 'dvd',
    'Commander 2014': 'c14',
    'Khans of Tarkir Promos': 'pktk',
    'Khans of Tarkir': 'ktk',
    'Duel Decks: Speed vs. Cunning': 'ddn',
    'From the Vault: Annihilation': 'v14',
    'Magic 2015': 'm15',
    'Magic 2015 Promos': 'pm15',
    'Vintage Masters': 'vma',
    'Conspiracy': 'cns',
    'Modern Event Deck 2014': 'md1',
    'Journey into Nyx': 'jou',
    'Born of the Gods': 'bng',
    'Born of the Gods Promos': 'pbng',
    'Judge Gift Cards 2014': 'j14',
    'Commander 2013': 'c13',
    'Theros': 'ths',
    'Theros Promos': 'pths',
    'Duel Decks: Heroes vs. Monsters': 'ddl',
    'From the Vault: Twenty': 'v13',
    'Modern Masters': 'mma',
    "Dragon's Maze": 'dgm',
    "Dragon's Maze Promos": 'pdgm',
    'World Magic Cup Qualifiers': 'wmc',
    'Gatecrash': 'gtc',
    "Commander's Arsenal": 'cm1',
    'Return to Ravnica': 'rtr',
    'Duel Decks: Izzet vs. Golgari': 'ddj',
    'Magic 2013': 'm13',
    'Planechase 2012': 'pc2',
    'Avacyn Restored': 'avr',
    'Dark Ascension': 'dka',
    'Judge Gift Cards 2012': 'j12',
    'Premium Deck Series: Graveborn': 'pd3',
    'Innistrad': 'isd',
    'From the Vault: Legends': 'v11',
    'Commander 2011': 'cmd',
    'New Phyrexia': 'nph',
    'New Phyrexia Promos': 'pnph',
    'Mirrodin Besieged': 'mbs',
    'Mirrodin Besieged Promos': 'pmbs',
    'Judge Gift Cards 2011': 'g11',
    'Salvat 2011': 'ps11',
    'Magic Player Rewards 2011': 'p11',
    'Premium Deck Series: Fire and Lightning': 'pd2',
    'Magic Online Theme Decks': 'td0',
    'Scars of Mirrodin': 'som',
    'From the Vault: Relics': 'v10',
    'Archenemy': 'arc',
    'Duels of the Planeswalkers': 'dpa',
    'Rise of the Eldrazi': 'roe',
    'Duel Decks: Phyrexia vs. the Coalition': 'dde',
    'Worldwake': 'wwk',
    'Premium Deck Series: Slivers': 'h09',
    'Zendikar': 'zen',
    'Masters Edition III': 'me3',
    'Planechase': 'hop',
    'Alara Reborn': 'arb',
    'Duel Decks: Divine vs. Demonic': 'ddc',
    'URL/Convention Promos': 'purl',
    'Conflux Promos': 'pcon',
    'Conflux': 'con',
    'Shards of Alara': 'ala',
    'Masters Edition II': 'me2',
    'From the Vault: Dragons': 'drb',
    'Eventide': 'eve',
    'Shadowmoor': 'shm',
    '15th Anniversary Cards': 'p15a',
    'Morningtide': 'mor',
    'Magic Premiere Shop 2008': 'pmps08',
    'Duel Decks: Elves vs. Goblins': 'dd1',
    'Lorwyn Promos': 'plrw',
    'Lorwyn': 'lrw',
    'Masters Edition': 'me1',
    'Tenth Edition': '10e',
    'Tenth Edition Promos': 'p10e',
    'Future Sight Promos': 'pfut',
    'Future Sight': 'fut',
    'Grand Prix Promos': 'pgpx',
    'Pro Tour Promos': 'ppro',
    'Planar Chaos Promos': 'pplc',
    'Planar Chaos': 'plc',
    'Time Spiral Promos': 'ptsp',
    'Time Spiral': 'tsp',
    'Time Spiral Timeshifted': 'tsb',
    'Coldsnap': 'csp',
    'Dissension': 'dis',
    'Champs and States': 'pcmp',
    'Guildpact': 'gpt',
    'Hachette UK': 'phuk',
    'Ravnica: City of Guilds': 'rav',
    'Salvat 2005': 'psal',
    'Saviors of Kamigawa Promos': 'psok',
    'Saviors of Kamigawa': 'sok',
    'Betrayers of Kamigawa Promos': 'pbok',
    'Betrayers of Kamigawa': 'bok',
    'Champions of Kamigawa Promos': 'pchk',
    'Champions of Kamigawa': 'chk',
    'Fifth Dawn': '5dn',
    'Darksteel': 'dst',
    'Mirrodin': 'mrd',
    'Scourge': 'scg',
    'Legions': 'lgn',
    'Onslaught': 'ons',
    'Hobby Japan Promos': 'jp1',
    'Magic Online Promos': 'prm',
    'Judgment': 'jud',
    'Torment': 'tor',
    'Odyssey': 'ody',
    'Apocalypse': 'apc',
    'Planeshift': 'pls',
    'Invasion': 'inv',
    'Prophecy': 'pcy',
    'Nemesis': 'nem',
    'Mercadian Masques': 'mmq',
    "Urza's Destiny": 'uds',
    'Portal Three Kingdoms Promos': 'pptk',
    'Portal Three Kingdoms': 'ptk',
    "Urza's Legacy": 'ulg',
    'Arena League 1999': 'pal99',
    'Anthologies': 'ath',
    "Urza's Saga": 'usg',
    'Exodus': 'exo',
    'Stronghold': 'sth',
    'Tempest': 'tmp',
    'Weatherlight': 'wth',
    'Mirage': 'mir',
    'Alliances': 'all',
    'Homelands': 'hml',
    'Chronicles Foreign Black Border': 'bchr',
    'Chronicles': 'chr',
    'Ice Age': 'ice',
    'Media and Collaboration Promos': 'pmei',
    'Legends': 'leg'
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/getCard")
def get_card():
    r = requests.get("https://api.scryfall.com/cards/random?q=is%3Acommander+legal%3Acommander+%28game%3Apaper", headers=headers)
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
    idType = ''
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
        for term in searchTerms['searchTerms']:
            if term['type'] == 'ID Type':
                idType = term['value']
        if idType == '=':
            q += "+id%3D" + ''.join(selected_colors)
        elif idType == '<':
            q += "+id%3C" + ''.join(selected_colors)
        elif idType == '>':
            q += "+id%3E" + ''.join(selected_colors)
        else:
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
            elif term['type'] == 'Type Line':
                if ' ' in term['value']:
                    effects = term['value'].split()
                    for effect in effects:
                        if ' ' in effect:
                            effect = effect.replace(' ', '+')
                        q+= "+t%3A" + effect
                else:
                    effects = term['value']
                    q+= "+t%3A" + effects
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