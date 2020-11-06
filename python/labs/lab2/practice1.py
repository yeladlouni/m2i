# Ecrire un script python afin de:
# Créer une liste composée des noms de pays
# Trier la liste selon un ordre alphabétique décroissant
# Afficher le nombre de caractères de chaque pays
# Afficher la liste des pays comme chaîne de caractères séparés par une virgule et un espace
# Afficher les 3 derniers caractère de chaque pays en majuscules
# Convertir la liste en tuple

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'AntiguaandBarbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'BosniaandHerzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'BurkinaFaso', 'Burundi', 'Côted''Ivoire', 'CaboVerde', 'Cambodia', 'Cameroon', 'Canada', 'CentralAfricanRepublic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo(Congo-Brazzaville)', 'CostaRica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia(CzechRepublic)', 'DemocraticRepublicoftheCongo', 'Denmark', 'Djibouti', 'Dominica', 'DominicanRepublic', 'Ecuador', 'Egypt', 'ElSalvador', 'EquatorialGuinea', 'Eritrea', 'Estonia', 'Eswatini(fmr.', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'HolySee', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'MarshallIslands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar(formerlyBurma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'NewZealand', 'Nicaragua', 'Niger', 'Nigeria', 'NorthKorea', 'NorthMacedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'PalestineState', 'Panama', 'PapuaNewGuinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'SaintKittsandNevis', 'SaintLucia', 'SaintVincentandtheGrenadines', 'Samoa', 'SanMarino', 'SaoTomeandPrincipe', 'SaudiArabia', 'Senegal', 'Serbia', 'Seychelles', 'SierraLeone', 'Singapore', 'Slovakia', 'Slovenia', 'SolomonIslands', 'Somalia', 'SouthAfrica', 'SouthKorea', 'SouthSudan', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'TrinidadandTobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'UnitedArabEmirates', 'UnitedKingdom', 'UnitedStatesofAmerica', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

countries.sort(reverse=True)

print(countries)

# Solution: loops

for country in countries:
    print(country, len(country))

# Solution: Comprehension list permet de générer une liste à partir d'une liste => one-liner

countries_len = [len(country) for country in countries]

print(countries_len)

# Les 3 derniers caractères en majuscules

countries_last_caracters = [country[-3:].upper() for country in countries]

print(countries_last_caracters)

# Afficher sous forme de texte la liste des pays séparés par des virgules

# Solution à base de concaténation

chaine_countries =""
for country in countries:
    chaine_countries += ', ' + (str(country))
print(chaine_countries)

# En utilisant join

countries_text = ', '.join(countries)

print(countries_text)