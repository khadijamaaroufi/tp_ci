import pytest
from notes import moyenne, mention, est_admis


def test_moyenne():
    assert moyenne([10, 12, 14]) == 12


def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])


@pytest.mark.parametrize("moy, attendu", [
    (17, "Très bien"),
    (15, "Bien"),
    (12, "Assez bien"),
    (10, "Passable"),
    (7, "Ajourné"),
])
def test_mention(moy, attendu):
    assert mention(moy) == attendu


def test_est_admis():
    assert est_admis([12, 14]) is True
    assert est_admis([5, 8]) is False