# Fonction pour convertir une règle donnée en un dictionnaire
def parse_rule(rule):
    if rule.startswith('"'):
        # La règle est un caractère unique
        return rule.strip('"')
    else:
        # La règle est une liste de numéros de règle séparés par des espaces ou des barres verticales
        subrules = rule.split("|")
        subrules = [[int(x) for x in subrule.strip().split(" ")] for subrule in subrules]
        return subrules

# Fonction pour générer toutes les chaînes de caractères possibles qui peuvent être générées par une règle donnée
def generate_strings(rule_num, rules):
    rule = rules[rule_num]
    if isinstance(rule, str):
        # La règle est un caractère unique
        return [rule]
    else:
        # La règle est une liste de numéros de règle
        result = []
        for subrule in rule:
            subresult = [""]
            for subrule_num in subrule:
                subsubresult = generate_strings(subrule_num, rules)
                subresult = [s + r for s in subresult for r in subsubresult]
            result += subresult
        return result

# Lire les règles de grammaire et les chaînes de caractères de l'entrée
with open("input.txt") as f:
    lines = f.readlines()

rules = {}
strings = []
for line in lines:
    if ":" in line:
        rule_num, rule = line.strip().split(": ")
        rules[int(rule_num)] = parse_rule(rule)
    elif line.strip():
        strings.append(line.strip())

# Générer toutes les chaînes de caractères possibles qui peuvent être générées par la règle numéro 0
strings_0 = generate_strings(0, rules)

# Compter le nombre de chaînes de caractères générées qui correspondent au format de chaîne de caractères donné dans l'entrée du puzzle
count = sum(1 for string in strings if string in strings_0)
print("Partie 1:", count)

# Modification des règles pour la partie 2
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

# Générer toutes les chaînes de caractères possibles qui peuvent être générées par la règle numéro 0
strings_0 = generate_strings(0, rules)

# Compter le nombre de chaînes de caractères générées qui correspondent au format de chaîne de caractères donné dans l'entrée du puzzle
count = sum(1 for string in strings if string in strings_0)
print("Partie 2:", count)
