# SarakaFund

Prototype de plateforme de financement participatif pour la diaspora africaine.
Les donateurs peuvent venir de n'importe quel pays ; les projets concernent l'Afrique.

**État : maquette de démonstration.** Aucun paiement réel, pas de serveur. Les comptes,
contributions et collectes restent dans le navigateur (`localStorage`).

## Fonctionnalités

- Deux types de collecte : projets avec contreparties (tout ou rien ou flexible) et cagnottes solidaires
- Interface en 9 langues : français, anglais, néerlandais, allemand, espagnol, portugais, italien, russe, chinois (simplifié)
- Pays de résidence (25 entrées) et pays d'origine sur chaque projet
- Moyens de paiement selon le pays du contributeur, plus mobile money par opérateur du pays de la collecte
- Conversion indicative dans la devise du contributeur (taux de démonstration)
- Comptes (démo locale), suivi des contreparties, budget détaillé et nouvelles du porteur réservés aux membres
- Application installable (PWA) : `manifest.webmanifest`, `sw.js`, `icon.svg`
- 9 projets d'exemple **fictifs**, signalés « Exemple »

## Structure

| Fichier | Rôle |
|---|---|
| `app.html` | Source unique (HTML, CSS, JS) |
| `build.py` | Génère `index.html` autonome à partir de `app.html` |
| `index.html` | Version générée à héberger |
| `manifest.webmanifest`, `sw.js`, `icon.svg` | Installation comme application |

## Lancer

```bash
python3 build.py
python3 -m http.server 8000   # puis ouvrir http://localhost:8000
```

Pour l'installer comme application, héberger les quatre fichiers (`index.html`,
`manifest.webmanifest`, `sw.js`, `icon.svg`) en HTTPS.

## Avant un vrai lancement

- Serveur sécurisé : comptes, e-mails de confirmation, récupération de mot de passe, statuts de livraison mis à jour par les porteurs
- Prestataire de paiement multi-pays et agrégateur de mobile money, avec vérification d'identité des porteurs
- Conditions générales, politique de confidentialité (RGPD), vérification des moyens de paiement et des opérateurs par pays
- Relecture des traductions par des locuteurs natifs, surtout les textes sur les frais
- Vérification du nom (marques EUIPO / BOIP, noms de domaine) et du sens de « saraka »
- Retirer ou remplacer les projets d'exemple avant toute présentation publique
