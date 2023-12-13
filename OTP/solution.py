ciphertext = open('ciphertext_bytes', 'rb').read()
var_key = ""
dico = {}

# On test pour des tailles de clef allant de 1 a 10
for LEN_KEY in range(1,10):
    for k in range(0, LEN_KEY):
        # Deux lettres espacées de LEN_KEY sont xorées avec la même lettre de la clef
        for i in range(k, len(ciphertext), LEN_KEY):
            if ciphertext[i] in dico:
                dico[ciphertext[i]] += 1
            else:
                dico[ciphertext[i]] = 1
        # L'espace a des chances d'être le caractère le plus fréquent
        var_key += chr((max(dico, key=dico.get))^ord(' '))
        dico.clear()
    print(var_key)
    var_key = ""
