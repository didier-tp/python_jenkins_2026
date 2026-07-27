def mensualite(montant,nb_mois,taux_interet_pct):
    taux_mensuel = (taux_interet_pct / 100) / 12
    return ( montant * taux_mensuel)  / (1 - (1+taux_mensuel)** (- nb_mois)) + 2
