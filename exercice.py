#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    resultat = True
    liste_non_ordonne = []
    while len(liste_non_ordonne) < 10:
        liste_non_ordonne = liste_non_ordonne.append(int(input("Veuillez entrer un nombre: ")))

    index = 0
    while index < len(liste_non_ordonne):
        if liste_non_ordonne(index) < liste_non_ordonne(index + 1):
            continue
        else:
        print("Houston, nous avons un probleme")
            break
        index += 1
    print(resultat)

    return

    # print(ma_liste==sorted(ma_liste))


def anagrams(words: list = None) -> bool:
    
    mot1 = ALEVIN
    mot2 = NIVELA

    mot1 = list(mot1)
    mot2 = list(mot2)


    if len(mot1) == len(mot2):
        for lettre in mot1:
            if lettre in mot2:
                mot2.remove(lettre)
        if len(mot2) == 0:
            print("Annagramme")
        else:
            print("Il y a un probleme")

    return


def contains_doubles(items: list) -> bool:
    liste = [2, 3, 4, 1, 6, 7, 4, 6, 1, 6, 3, 4, 6, 1, 1, 1, 1]
    print(len(liste) == len(set(liste)))
    return 


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def histogram(sentence: str) -> tuple:
    phrase = "Je suis le roi du monde."

    phrase_set = set(phrase)
    resultat = {}
    for lettre in phrase_set:
        resultat[lettre] = phrase.count(lettre)
    
    print(resultat)

    return 


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    name, result = best_grades(grades)
    print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
