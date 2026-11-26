# Workflows n8n — adoption basset

Deux workflows qui fonctionnent ensemble, avec une boîte mail « lab » comme point d'entrée.

## 1. veille-adoption-basset-male.json

Chaque matin (8h10) :
- lit la page « Basset Hound » de Tailharbor et repère les nouvelles annonces de **mâles adultes** (femelles et chiots exclus) ;
- détecte un changement sur la page adoption de l'association « Un cœur sous l'oreille » ;
- s'il y a du nouveau, envoie un mail dont le sujet commence par `[BASSET]` vers la boîte lab.

## 2. traitement-basset-lab.json

Surveille la boîte lab (IMAP) et ne garde que les mails liés aux bassets : sujets `[BASSET]`, alertes chien.com / Seconde Chance, messages de l'association.
Mistral extrait chaque mâle adulte (âge, lieu, refuge, compatibilité, lien) ; les annonces de Normandie et des départements voisins sont classées en premier.
Un récap HTML est envoyé aux destinataires. **Aucune réponse n'est jamais envoyée à l'association.**

## Installation

1. n8n → **Workflows → Import from file** (les deux fichiers).
2. Dans chaque nœud, choisir les connexions (IMAP, Mistral, SMTP) et remplacer `EXPEDITEUR_A_REMPLIR`, `ADRESSE_LAB_A_REMPLIR`, `DESTINATAIRES_A_REMPLIR`.
3. Activer le workflow 2, puis le workflow 1.
4. Optionnel : filtre Gmail qui transfère les mails de l'association vers la boîte lab.

## Notes

- La mémoire des annonces déjà vues ne fonctionne que si le workflow 1 est **actif**.
- Le workflow 2 ne marque pas les mails comme lus (pour ne pas gêner d'autres workflows qui lisent la même boîte) et ne traite que les mails reçus depuis la date indiquée dans ses règles IMAP.
- Ne jamais versionner un export contenant de vraies adresses mail ou des identifiants de connexion.
