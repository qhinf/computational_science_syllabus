# Syllabus Template

Deze syllabus maakt gebruik van Jupyter Book. Alle inhoudelijke bestanden staan in de map *syllabus*:

- *_config.yml* is de configuratie van dit "boek". Je moet daar in elk geval de titel aanpassen! Verder zijn in de meeste gevallen geen wijzigingen nodig, maar lees de comments vooral even door.
- *_toc.yml* is de inhoudsopgave, waarin alle bestanden waaruit de syllabus bestaat op een rijtje worden gezet. Dit bestand bepaalt de volgorde van de hoofdstukken en elk bestand dat niet in de lijst voorkomt, wordt ook geen onderdeel van de syllabus.
- *index.md* is de "homepagina" van deze syllabus (want die staat bij `root` in *_toc.yml*) met de gebruikelijke introductiedingen en een aantal belangrijke zaken.
- De rest van de bestanden vormen de inhoud van de syllabus.

## Benodigdheden

- Een recente versie van Python

## De syllabus bouwen

Zorg eerst dat je alle vereiste dependencies geïnstalleerd hebt:

```sh
pip install --user -r requirements.txt
```

Vervolgens kun je de syllabus bouwen met:

```sh
jupyter-book build syllabus
```

De homepagina staat dan in *syllabus\\_build\html\index.html*.





# Tabel die ik nog mogelijk nodig heb

:::{list-table} **Onderzoek: weging 1**
:header-rows: 1
* - Criterium
  - 0p
  - 1p
  - 2p
  - 3p
  - 4p
* - Wat weet je van dit fenomeen? Voer eventueel het benodigde onderzoek uit. 
  - Niets  of een veel te simpele voorstelling van het fenomeen<br>Geen onderzoek gedaan
  - Enkele beschrijvende algemene opmerkingen<br>geenonderzoek gedaan of alleen onderzoek naar enkele aspecten van het fenomeen.
  - Enig onderzoek gedaan<br>samenhangend beeld van het fenomeen<br>Wel meer relevante aspecten van een fenomeen kunnen benoemen die van belang zijn, maar geen zicht hebben onderlinge relaties.
  - Onderzoek gedaan<br>samenhangend en compleet beeld van het fenomeen<br>relevante aspecten van een fenomeen kunnen benoemen, die van belang zijn. Zicht hebben op de onderlinge relaties.
  - Alles van 3p. En bovendien, relatie van dit fenomeen tot andere fenomenen in de wereld beschreven en/of dit fenomeen zodanig geconceptualiseerd dat het toe te passen is in andere contexten en zijn relevantie uitgelegd. Relevantie voor andere fenomenen uitgelegd.
:::
