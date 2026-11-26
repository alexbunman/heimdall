# Workflows n8n

## veille-adoption-basset-male.json

Veille quotidienne (8h10) des annonces de bassets hound **mâles adultes** à adopter.

- Lit la page « Basset Hound » de Tailharbor et repère les nouvelles annonces de mâles (femelles et chiots exclus).
- Détecte un changement sur la page adoption de l'association « Un cœur sous l'oreille ».
- Envoie un mail récapitulatif **uniquement s'il y a du nouveau**. N'écrit jamais à un tiers.

### Installation

1. n8n → **Workflows → Import from file**.
2. Nœud **« Mail recap »** : choisir la connexion SMTP, remplacer `EXPEDITEUR_A_REMPLIR` et `DESTINATAIRE_A_REMPLIR`.
3. Activer le workflow. Le premier passage envoie un mail « démarrage » listant les annonces déjà en ligne.

### Notes

- La mémoire des annonces déjà vues (`$getWorkflowStaticData`) ne fonctionne que lorsque le workflow est **actif**, pas en test manuel.
- Tailharbor liste aussi des refuges hors de France : vérifier la localisation.
- Ne jamais versionner un export contenant de vraies adresses mail ou des identifiants de connexion.
