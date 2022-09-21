import random, base64, sys, io, json, time
while True:
    try:
        import PySimpleGUI as psg
        import PIL.Image
        break
    except:
        os.system("install.bat")
    
c = json.load(open("d.json", "r"))
correct_answer = None
streak = 0
icon = base64.b64encode(open("assets/guesstheflag.gif", "rb").read())
country_codes = {
    "Afghanistan": "AF",
    "Albania": "AL",
    "Algeria": "DZ",
    "American Samoa": "AS",
    "Andorra": "AD",
    "Angola": "AO",
    "Anguilla": "AI",
    "Antarctica": "AQ",
    "Antigua and Barbuda": "AG",
    "Argentina": "AR",
    "Armenia": "AM",
    "Aruba": "AW",
    "Australia": "AU",
    "Austria": "AT",
    "Azerbaijan": "AZ",
    "Bahamas (the)": "BS",
    "Bahrain": "BH",
    "Bangladesh": "BD",
    "Barbados": "BB",
    "Belarus": "BY",
    "Belgium": "BE",
    "Belize": "BZ",
    "Benin": "BJ",
    "Bermuda": "BM",
    "Bhutan": "BT",
    "Bolivia (Plurinational State of)": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Bosnia and Herzegovina": "BA",
    "Botswana": "BW",
    "Bouvet Island": "BV",
    "Brazil": "BR",
    "British Indian Ocean Territory (the)": "IO",
    "Brunei Darussalam": "BN",
    "Bulgaria": "BG",
    "Burkina Faso": "BF",
    "Burundi": "BI",
    "Cabo Verde": "CV",
    "Cambodia": "KH",
    "Cameroon": "CM",
    "Canada": "CA",
    "Cayman Islands (the)": "KY",
    "Central African Republic (the)": "CF",
    "Chad": "TD",
    "Chile": "CL",
    "China": "CN",
    "Christmas Island": "CX",
    "Cocos (Keeling) Islands (the)": "CC",
    "Colombia": "CO",
    "Comoros (the)": "KM",
    "Congo (the Democratic Republic of the)": "CD",
    "Congo (the)": "CG",
    "Cook Islands (the)": "CK",
    "Costa Rica": "CR",
    "Croatia": "HR",
    "Cuba": "CU",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Denmark": "DK",
    "Djibouti": "DJ",
    "Dominica": "DM",
    "Dominican Republic (the)": "DO",
    "Ecuador": "EC",
    "Egypt": "EG",
    "El Salvador": "SV",
    "Equatorial Guinea": "GQ",
    "Eritrea": "ER",
    "Estonia": "EE",
    "Eswatini": "SZ",
    "Ethiopia": "ET",
    "Falkland Islands (the) [Malvinas]": "FK",
    "Faroe Islands (the)": "FO",
    "Fiji": "FJ",
    "Finland": "FI",
    "France": "FR",
    "French Guiana": "GF",
    "French Polynesia": "PF",
    "French Southern Territories (the)": "TF",
    "Gabon": "GA",
    "Gambia (the)": "GM",
    "Georgia": "GE",
    "Germany": "DE",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greece": "GR",
    "Greenland": "GL",
    "Grenada": "GD",
    "Guadeloupe": "GP",
    "Guam": "GU",
    "Guatemala": "GT",
    "Guernsey": "GG",
    "Guinea": "GN",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Haiti": "HT",
    "Heard Island and McDonald Islands": "HM",
    "Holy See (the)": "VA",
    "Honduras": "HN",
    "Hong Kong": "HK",
    "Hungary": "HU",
    "Iceland": "IS",
    "India": "IN",
    "Indonesia": "ID",
    "Iran (Islamic Republic of)": "IR",
    "Iraq": "IQ",
    "Ireland": "IE",
    "Isle of Man": "IM",
    "Israel": "IL",
    "Italy": "IT",
    "Jamaica": "JM",
    "Japan": "JP",
    "Jersey": "JE",
    "Jordan": "JO",
    "Kazakhstan": "KZ",
    "Kenya": "KE",
    "Kiribati": "KI",
    "Korea (DPRK)": "KP",
    "Korea (KOR)": "KR",
    "Kuwait": "KW",
    "Kyrgyzstan": "KG",
    "Lao People's Democratic Republic (the)": "LA",
    "Latvia": "LV",
    "Lebanon": "LB",
    "Lesotho": "LS",
    "Liberia": "LR",
    "Libya": "LY",
    "Liechtenstein": "LI",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Macao": "MO",
    "Republic of North Macedonia": "MK",
    "Madagascar": "MG",
    "Malawi": "MW",
    "Malaysia": "MY",
    "Maldives": "MV",
    "Mali": "ML",
    "Malta": "MT",
    "Marshall Islands (the)": "MH",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Mauritius": "MU",
    "Mayotte": "YT",
    "Mexico": "MX",
    "Micronesia (Federated States of)": "FM",
    "Moldova (the Republic of)": "MD",
    "Monaco": "MC",
    "Mongolia": "MN",
    "Montenegro": "ME",
    "Montserrat": "MS",
    "Morocco": "MA",
    "Mozambique": "MZ",
    "Myanmar": "MM",
    "Namibia": "NA",
    "Nauru": "NR",
    "Nepal": "NP",
    "Netherlands (the)": "NL",
    "New Caledonia": "NC",
    "New Zealand": "NZ",
    "Nicaragua": "NI",
    "Niger (the)": "NE",
    "Nigeria": "NG",
    "Niue": "NU",
    "Norfolk Island": "NF",
    "Northern Mariana Islands (the)": "MP",
    "Norway": "NO",
    "Oman": "OM",
    "Pakistan": "PK",
    "Palau": "PW",
    "Palestine": "PS",
    "Panama": "PA",
    "Papua New Guinea": "PG",
    "Paraguay": "PY",
    "Peru": "PE",
    "Philippines (the)": "PH",
    "Pitcairn": "PN",
    "Poland": "PL",
    "Portugal": "PT",
    "Puerto Rico": "PR",
    "Qatar": "QA",
    "Romania": "RO",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Saint Kitts and Nevis": "KN",
    "Saint Lucia": "LC",
    "Saint Martin (French part)": "MF",
    "Saint Pierre and Miquelon": "PM",
    "Saint Vincent and the Grenadines": "VC",
    "Samoa": "WS",
    "San Marino": "SM",
    "Sao Tome and Principe": "ST",
    "Saudi Arabia": "SA",
    "Senegal": "SN",
    "Serbia": "RS",
    "Seychelles": "SC",
    "Sierra Leone": "SL",
    "Singapore": "SG",
    "Sint Maarten (Dutch part)": "SX",
    "Slovakia": "SK",
    "Slovenia": "SI",
    "Solomon Islands": "SB",
    "Somalia": "SO",
    "South Africa": "ZA",
    "South Georgia and the South Sandwich Islands": "GS",
    "South Sudan": "SS",
    "Spain": "ES",
    "Sri Lanka": "LK",
    "Sudan": "SD",
    "Suriname": "SR",
    "Sweden": "SE",
    "Switzerland": "CH",
    "Syrian Arab Republic": "SY",
    "Taiwan (Province of China)": "TW",
    "Tajikistan": "TJ",
    "Tanzania": "TZ",
    "Thailand": "TH",
    "Timor-Leste": "TL",
    "Togo": "TG",
    "Tokelau": "TK",
    "Tonga": "TO",
    "Trinidad and Tobago": "TT",
    "Tunisia": "TN",
    "Turkey": "TR",
    "Turkmenistan": "TM",
    "Turks and Caicos Islands (the)": "TC",
    "Tuvalu": "TV",
    "Uganda": "UG",
    "Ukraine": "UA",
    "United Arab Emirates (the)": "AE",
    "United Kingdom": "GB",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Vanuatu": "VU",
    "Venezuela (Bolivarian Republic of)": "VE",
    "Viet Nam": "VN",
    "Virgin Islands (British)": "VG",
    "Virgin Islands (U.S.)": "VI",
    "Wallis and Futuna": "WF",
    "Western Sahara": "EH",
    "Yemen": "YE",
    "Zambia": "ZM",
    "Zimbabwe": "ZW"
}

def random_flag(choices=4):
    if choices < 2: choices = 2
    while True:
        try:
            countries = random.sample(country_codes.keys(), k=choices)
            correct_answer = random.choice(countries)
            correct_flag_fp = f"flags/{country_codes[correct_answer].lower()}.png"
            return {
                "countries": countries, 
                "correct_answer": correct_answer, 
                "correct_flag_fp": correct_flag_fp
            }
            break
        except:
            pass

def resize(image, resize):
    img = image.copy()
    cur_width, cur_height = img.size
    new_width, new_height = resize
    scale = min(new_height/cur_height, new_width/cur_width)
    img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)    
    ImgBytes = io.BytesIO()
    img.save(ImgBytes, format="PNG")
    del img
    return base64.b64encode(ImgBytes.getvalue())

def wipe_data():
    o = {
        "data": {
            "color_before": "grey", 
            "correct_flags": 0, 
            "flags_displayed": 0, 
            "highest_streak": 0, 
            "first_time_user": True
        }, 
        "settings": {
            "choices": 4
        }
    }
    json.dump(o, open("d.json", "w"), indent=4)
    sys.exit(0)

layout = [
    [
        psg.Button("_", key=";_", visible=False)
    ], 
    [
        psg.Column([
            [
                psg.Text("Correct Flags: ", font=("sans-serif", 10, "bold"), text_color="white", background_color="#131517"), psg.Text(f"""{c["data"]["correct_flags"]}/{c["data"]["flags_displayed"]}""", font=("sans-serif", 10), text_color=c["data"]["color_before"], key=";CORRECT", background_color="#131517", auto_size_text=True)
            ]
        ], background_color="#131517", element_justification="center", expand_x=True), 
        psg.Column([
            [
                psg.Text("Previous Correct Answer: ", font=("sans-serif", 10, "bold"), text_color="white", background_color="#131517"), psg.Text("None", font=("sans-serif", 10), text_color="white", key=";CORRECT_ANS_PREV", background_color="#131517", auto_size_text=True)
            ]
        ], background_color="#131517", element_justification="center")
    ], 
    [
        psg.Column([
            [
                psg.Text("Streak: ", font=("sans-serif", 10, "bold"), text_color="white", background_color="#131517"), psg.Text("0", font=("sans-serif", 10), text_color="white", key=";STREAK", background_color="#131517", auto_size_text=True)
            ]
        ], background_color="#131517", element_justification="center", expand_x=True), 
        psg.Column([
            [
                psg.Text("Highest Streak: ", font=("sans-serif", 10, "bold"), text_color="white", background_color="#131517"), psg.Text(str(c["data"]["highest_streak"]), font=("sans-serif", 10), text_color="white", key=";HIGHEST_STREAK", background_color="#131517", auto_size_text=True)
            ]
        ], background_color="#131517", element_justification="center", expand_x=True)
    ], 
    [
        psg.Column([
            [
                psg.Text("Guess The Flag", font=("sans-serif", 15, "bold"), text_color="#00ffff", background_color="#131517")
            ], 
            [
                psg.Text("Made By FloppaSec;", font=("sans-serif", 9), text_color="white", background_color="#131517")
            ], 
            [
                psg.Text("Choices: ", font=("sans-serif", 11, "bold"), text_color="white", background_color="#131517"), psg.Spin([x for x in range(2, 11)], initial_value=c["settings"]["choices"], background_color="#131517", text_color="white", key=";CHOICES", expand_x=True, enable_events=True)
            ], 
            [
                psg.Button("Library", key=";LIB", button_color=("black", "grey"), expand_x=True)
            ], 
            [
                psg.Button("Wipe Data", key=";CLS", button_color=("black", "grey"), expand_x=True)
            ]
        ], expand_x=True, expand_y=True, background_color="#131517", element_justification="center"), 
        psg.Column([
            [
                psg.Image(data=None, background_color="#131517", key=";FLAG", visible=False)
            ], 
            [
                psg.Listbox(values=["Empty_flag", "Empty_flag", "Empty_flag", "Empty_flag"], select_mode="extended", background_color="#131517", key=";ANSWER", text_color="white", size=(30, c["settings"]["choices"]))
            ], 
            [
                psg.Button("Submit", key=";SUBMIT", button_color=("white", "green"))
            ], 
        ], expand_x=True, expand_y=True, background_color="#131517")
    ]
]

dump = lambda c: json.dump(c, open("d.json", "w"), indent=4)
window = psg.Window(f"Guess The Flag", [[psg.Column(layout, expand_x=True, expand_y=True, background_color="#23272A")]], finalize=True, icon=icon, background_color="#23272A", resizable=False)
window.Element(";_").click()

while True:
    event, values = window.read()
    if event == ";_":
        if c["data"]["first_time_user"] is True:
            pl = [
                [
                    psg.Button("_", key=";_", visible=False)
                ], 
                [
                    psg.Text("Welcome to Guess The Flag, \nYou can start guessing flags now or memorize flags with the library!", text_color="white", background_color="#23272A")
                ], 
                [
                    psg.Button("Ok", button_color=("black", "grey"))
                ]
            ]
            pw = psg.Window("Welcome", pl, modal=True, icon=icon, background_color="#23272A", resizable=False)
            pw.read()
            pw.close()
            c["data"]["first_time_user"] = False
            dump(c)
        flagobj = random_flag(choices=c["settings"]["choices"])
        window.Element(";FLAG").update(data=resize(PIL.Image.open(flagobj["correct_flag_fp"]), resize=(240, 135)), visible=True, size=(240, 135))
        window.Element(";ANSWER").update(flagobj["countries"])
        correct_answer = flagobj["correct_answer"]
        c["data"]["flags_displayed"] += 1
        dump(c)
    if event == ";SUBMIT":
        if len(values[";ANSWER"]) != 0: 
            if values[";ANSWER"][0] == correct_answer:
                c["data"]["correct_flags"] += 1
                streak += 1
                if streak >= c["data"]["highest_streak"]:
                    c["data"]["highest_streak"] += 1
                    window.Element(";HIGHEST_STREAK").update(str(streak))
                c["data"]["color_before"] = "green"
                window.Element(";CORRECT").update(text_color="green")
                window.Element(";STREAK").update(str(streak))
            else:
                streak = 0
                c["data"]["color_before"] = "red"
                window.Element(";CORRECT").update(text_color="red")
                window.Element(";STREAK").update(str(streak))
            dump(c)
            window.Element(";CORRECT_ANS_PREV").update(correct_answer)
            window.Element(";CORRECT").update(f"""{c["data"]["correct_flags"]}/{c["data"]["flags_displayed"]}""")
            window.Element(";_").click()
    if event == ";CHOICES":
        c["settings"]["choices"] = values[";CHOICES"]
        window.Element(";ANSWER").set_size((30, values[";CHOICES"]))
        window.Element(";_").click()
        c["data"]["flags_displayed"] -= 1
        dump(c)
    if event == ";LIB":
        lib_layout = [
            [
                psg.Column([
                    [
                        psg.Button("_", key=";_", visible=False)
                    ], 
                    [
                        psg.Image(data=resize(PIL.Image.open("flags/af.png"), resize=(160, 90)), size=(160, 90), background_color="#131517", key=";LIB_FLAG")
                    ], 
                    [
                        psg.Text("Afghanistan", font=("sans-serif", 11, "bold"), text_color="white", background_color="#131517", key=";LIB_FLAG_LABEL")
                    ], 
                    [
                        psg.Listbox(values=list(country_codes.keys()), select_mode="extended", background_color="#131517", key=";COUNTRYLIST", text_color="white", size=(30, 15), enable_events=True)
                    ]
                 ], element_justification="center", expand_x=True, expand_y=True, background_color="#131517")
            ]
        ]
        tw = psg.Window("Library", lib_layout, modal=True, icon=icon, background_color="#23272A", resizable=False)
        while True:
            e, v = tw.read()
            if e == ";COUNTRYLIST":
                tw.Element(";LIB_FLAG").update(data=resize(PIL.Image.open(f"""flags/{country_codes[v[";COUNTRYLIST"][0]].lower()}.png"""), resize=(160, 90)))
                tw.Element(";LIB_FLAG_LABEL").update(v[";COUNTRYLIST"][0])
            if e == psg.WIN_CLOSED:
                break
    if event == ";CLS":
        cls_layout = [
            [
                [
                    psg.Text("Are you sure you want to wipe all data? this cannot be undone.", text_color="white", background_color="#23272A")
                ], 
                [
                    psg.Button("No", button_color=("white", "green"), key=";N"), psg.Button("Yes", button_color=("white", "red"), key=";Y")
                ]
            ]  
        ]
        clsw = psg.Window("Wipe data", cls_layout, modal=True, icon=icon, background_color="#23272A", resizable=False)
        while True:
            e, v = clsw.read()
            if e == ";Y":
                wipe_data()
            if e == ";N":
                clsw.close()
            if e == psg.WIN_CLOSED:
                break
    if event == psg.WIN_CLOSED:
        sys.exit(0)