from mensualite import mensualite
def test_mensualite():
    # montant=10000 euros, nb_mois=60 = 5*12 = 5 ans , taux_interet_pct = 2%
    nb_mois=60
    res_mensualite=mensualite(10000, nb_mois , 2)
    print(f'res_mensualite={res_mensualite} pour nb_mois={nb_mois} ')
    assert (res_mensualite - 175 ) < 1
    
# nb: lancement du test via la commande:
#     pytest test_mensualite.py 
#  ou pytest -s test_mensualite.py  
# ---------
# sous windows ou autre , installation de pytest via 
#     pip install pytest
#-----------
# sous python3 et debian , installation de pytest via
#     sudo apt install python3-pytest 
    
    