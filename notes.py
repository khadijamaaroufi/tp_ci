def moyenne(notes):
    if not notes:
        raise ValueError("La liste de notes est vide")
    return sum(notes) / len(notes)


def mention(moy):
    if moy >= 16:
        return "Très bien"
    if moy >= 14:
        return "Bien"
    if moy >= 12:
        return "Assez bien"
    if moy >= 10:
        return "Passable"
    return "Ajourné"


def est_admis(notes):
    return moyenne(notes) >= 10