(eindopdracht)=
# Eindopdracht

Deze eindopdracht vormt de logische afsluiting van de zes hoofdstukken die je hebt doorlopen. Tijdens de hoofdstukken heb je stap voor stap gewerkt aan het begrijpen van agent-based modelling, het ontwerpen van modellen, het implementeren in NetLogo, het systematisch experimenteren en het valideren van je resultaten. In deze eindopdracht breng je al deze elementen samen in één compleet onderzoeksproject.

## Overzicht: Van theorie naar praktijk

De eindopdracht volgt dezelfde structuur als de zes hoofdstukken:

| Hoofdstuk | Onderwerp | Onderdeel eindopdracht |
|-----------|-----------|------------------------|
| {ref}`hoofdstukken/01_modellen_emergent` | Modellen en emergent gedrag | Casus kiezen en onderzoeksvraag formuleren |
| {ref}`hoofdstukken/02_conceptueel_abm` | Conceptueel model maken | Conceptueel model ontwerpen met canvas |
| {ref}`hoofdstukken/03_netlogo_basis` | NetLogo programmeren | Model implementeren in NetLogo |
| {ref}`hoofdstukken/04_emergent_bouwen` | Emergent gedrag bouwen | Verificatie tijdens implementatie |
| {ref}`hoofdstukken/05_experimenteren_data` | Experimenteren en data | Systematisch experimenteren met BehaviorSpace |
| {ref}`hoofdstukken/06_verificatie_validatie_verslag` | Validatie en rapportage | Valideren en IMRAD-verslag schrijven |

## Werkvorm

Je werkt alleen of met z'n tweeën aan deze opdracht. Wanneer je met z'n tweeën werkt, moet je een extra hoofdstuk aan je verslag toevoegen (zie {ref}`samenwerken`). Kies een casus uit {ref}`casussen` of bedenk zelf een onderwerp (overleg dit dan eerst met de docent).

## Deel 1: Casus en onderzoeksvraag

*Zie {ref}`hoofdstukken/01_modellen_emergent` voor de achtergrond bij modellen en emergent gedrag.*

### Wat ga je onderzoeken?

Beschrijf helder wat je gaat modelleren en waarom. Beantwoord de volgende vragen:

a. **Context:** Wat weet je al van dit fenomeen? Voer eventueel literatuuronderzoek uit. Welke factoren spelen een rol?

b. **Afbakening:** Welk deel van het fenomeen wil je modelleren? Wat laat je bewust buiten beschouwing en waarom?

c. **Onderzoeksvraag:** Wat wil je te weten komen met je model? Formuleer een concrete, beantwoordbare onderzoeksvraag.

```{admonition} Voorbeeld onderzoeksvraag
:class: tip
"Hoe beïnvloedt het aantal uitgangen en de breedte van de uitgangen de evacuatietijd van een gebouw met 500 personen?"

Deze vraag is concreet (aantal uitgangen, breedte, evacuatietijd), meetbaar (tijd in seconden) en gericht op een specifiek scenario (gebouw, 500 personen).
```

## Deel 2: Conceptueel model

*Zie {ref}`hoofdstukken/02_conceptueel_abm` voor uitleg over het conceptueel canvas.*

### Het canvas invullen

Ontwerp je model systematisch met behulp van het 9-velden canvas dat je in hoofdstuk 2 hebt leerd kennen:

1. **Agents:** Welke soorten agents zijn er? Wat zijn hun eigenschappen?
2. **Omgeving:** Hoe ziet de wereld eruit? Zijn er omgevingsagents (patches)?
3. **Gedrag:** Wat doen agents op elk moment (elke tick)?
4. **Interacties:** Hoe beïnvloeden agents elkaar en de omgeving?
5. **Parameters:** Welke waarden kun je aanpassen (sliders, switches)?
6. **Initialisatie:** Hoe ziet de beginsituatie eruit?
7. **Inputs:** Welke externe gegevens of instellingen heb je nodig?
8. **Outputs:** Wat meet en visualiseer je?
9. **Tijd:** Wat gebeurt er elke tick en in welke volgorde?

**Belangrijk:** Onderbouw je keuzes! Leg uit *waarom* je bepaalde eigenschappen wel of niet meeneemt.

```{admonition} Voorbeeld onderbouwing
:class: tip
"De schapen kunnen zich voortplanten. Als twee schapen elkaar tegenkomen, dan is er een kans van 20% dat er een nieuw schaap ontstaat. We hebben besloten om het geslacht van de schapen niet te modelleren omdat dat in dit geval niet relevant is voor de populatiedynamiek die we willen onderzoeken."
```

### PO-mijlpaal uit hoofdstuk 2

Gebruik de checklist uit de PO-mijlpaal van {ref}`hoofdstukken/02_conceptueel_abm` om te controleren of je conceptuele model compleet is.

## Deel 3: Implementatie in NetLogo

*Zie {ref}`hoofdstukken/03_netlogo_basis` en {ref}`hoofdstukken/04_emergent_bouwen` voor NetLogo-programmering en verificatie.*

### Van ontwerp naar code

Beschrijf eerst in detail (eventueel met pseudocode) hoe je `setup`- en `go`-procedures eruit komen te zien:

- Welke agents creëer je in `setup`?
- Welke eigenschappen stel je in?
- Wat gebeurt er in `go`, en in welke volgorde?

### Stapsgewijs implementeren

Bouw je model **incrementeel** op:

1. Begin met een minimale versie (bijvoorbeeld: alleen agents plaatsen)
2. Voeg stap voor stap gedrag toe
3. **Test na elke toevoeging** of het werkt zoals verwacht (verificatie!)
4. Gebruik `print`-statements of monitors om gedrag te controleren

```{admonition} Verificatie tijdens implementeren
:class: warning
Ga niet te snel! Als je te veel code in één keer schrijft, is het moeilijk om fouten te vinden. Test regelmatig met kleine experimenten of je code doet wat je verwacht. Dit is **verificatie**: controleren of de code correct is.
```

### PO-mijlpaal uit hoofdstukken 3 en 4

Gebruik de checklists uit {ref}`hoofdstukken/03_netlogo_basis` en {ref}`hoofdstukken/04_emergent_bouwen` om te controleren of je implementatie compleet en correct is.

## Deel 4: Systematisch experimenteren

*Zie {ref}`hoofdstukken/05_experimenteren_data` voor BehaviorSpace en data-analyse.*

### Experiment opzetten

Gebruik **BehaviorSpace** om systematisch te experimenteren:

1. **Bepaal je onafhankelijke variabelen:** Welke parameters ga je variëren? Welke waarden neem je?
2. **Bepaal je afhankelijke variabelen:** Wat ga je meten? Hoe registreer je dit in NetLogo?
3. **Herhalingen:** Hoeveel runs doe je per parameterwaarde? (Meestal minimaal 10-20 voor betrouwbare resultaten)
4. **Stopcriterium:** Wanneer stopt een run? (Na x ticks, of bij een bepaalde conditie?)

```{admonition} Voorbeeld experimentopzet
:class: tip
**Onderzoeksvraag:** Hoe beïnvloedt het aantal predators de stabiliteit van de schaapspopulatie?

**Onafhankelijke variabele:** aantal-predators (variërend van 0 tot 10 in stappen van 2)

**Afhankelijke variabele:** standaarddeviatie van aantal schapen over de laatste 100 ticks

**Herhalingen:** 20 runs per waarde

**Stopcriterium:** 500 ticks
```

### Data analyseren

Verwerk je BehaviorSpace-resultaten:

1. **Importeer data** in een spreadsheet of Python
2. **Maak grafieken** die je resultaten helder tonen
3. **Analyseer patronen:** Wat zie je? Zijn er trends, drempelwaarden, of onverwachte effecten?

### PO-mijlpaal uit hoofdstuk 5

Gebruik de checklist uit {ref}`hoofdstukken/05_experimenteren_data` om te controleren of je experiment en analyse compleet zijn.

## Deel 5: Validatie

*Zie {ref}`hoofdstukken/06_verificatie_validatie_verslag` voor validatietechnieken.*

### Micro- en macrovalidatie

Controleer of je model realistisch is:

a. **Microvalidatie:** Komt het gedrag van individuele agents overeen met de werkelijkheid? 
   - Doen schapen realistisch wat echte schapen doen?
   - Als er verschillen zijn, zijn die relevant voor je onderzoeksvraag?

b. **Macrovalidatie:** Komt het gedrag van het systeem als geheel overeen met de werkelijkheid?
   - Zie je patronen die je ook in de echte wereld ziet?
   - Zijn de uitkomsten in de buurt van bekende waarden of observaties?

```{admonition} Als validatie niet perfect is
:class: note
Een model hoeft niet perfect de werkelijkheid te weerspiegelen. Belangrijk is dat je:
1. Bewust bent van de verschillen
2. Kunt beredeneren of deze verschillen invloed hebben op je onderzoeksvraag
3. Dit expliciet benoemt in je verslag
```

### PO-mijlpaal uit hoofdstuk 6

Gebruik de validatiechecklist uit {ref}`hoofdstukken/06_verificatie_validatie_verslag` om je validatie compleet te maken.

## Deel 6: Conclusie en reflectie

### Onderzoeksvraag beantwoorden

Geef een helder antwoord op je onderzoeksvraag:

- Wat zijn je belangrijkste bevindingen?
- Wat zeggen je data hierover?
- Zijn er verassende resultaten?

### Reflectie op het proces

Reflecteer kritisch op je werk:

a. **Wat ging goed? Wat kon beter?**
   - Waar ben je tevreden over?
   - Waar liep je tegenaan?

b. **Modelaannames heroverwegen**
   - Welke aannames heb je gemaakt?
   - Zou je die nu anders doen?
   - Waarom wel/niet?

c. **Wishlist voor volgende versie**
   - Wat zou je willen toevoegen?
   - Wat zou je willen verwijderen of veranderen?
   - Waarom zou dat het model verbeteren?

(samenwerken)=
## (Optioneel) Deel 7: Voor wanneer je samenwerkt
Je mag bij deze module met z'n tweeën samenwerken. In dat geval moet je in het verslag aangeven:
- Per persoon: een reflectie op wat je geleerd hebt *van* deze module.
- Werkverdeling: wie heeft wat gedaan? Maak dit zo concreet mogelijk. Vage omschrijvingen worden niet nagekeken.

## Het verslag: IMRAD-structuur

Je eindopdracht lever je in als een wetenschappelijk verslag volgens de **IMRAD-structuur** die je in {ref}`hoofdstukken/06_verificatie_validatie_verslag` hebt geleerd:

1. **Introduction:** Casus, context, onderzoeksvraag (Deel 1)
2. **Method:** Conceptueel model, implementatie, experimentopzet (Deel 2, 3, 4)
3. **Results:** Data en grafieken uit je experimenten (Deel 4)
4. **Analysis:** Interpretatie van resultaten (Deel 4)
5. **Discussion:** Validatie, beperkingen, reflectie (Deel 5, 6)
6. **Conclusion:** Antwoord op onderzoeksvraag (Deel 6)

Gebruik de IMRAD-template en checklist uit {ref}`hoofdstukken/06_verificatie_validatie_verslag` om je verslag te structureren.

## Checklist eindopdracht

Controleer voor inleveren of je alles hebt:

### Deel 1: Casus en onderzoeksvraag
- [ ] Context en achtergrondonderzoek beschreven
- [ ] Afbakening: duidelijk wat wel/niet wordt gemodelleerd
- [ ] Concrete, beantwoordbare onderzoeksvraag geformuleerd
- [ ] Bronnen vermeld als je literatuuronderzoek hebt gedaan

### Deel 2: Conceptueel model
- [ ] 9-velden canvas volledig ingevuld
- [ ] Agents en hun eigenschappen beschreven
- [ ] Omgeving beschreven (patches, topologie)
- [ ] Gedrag per agent-type uitgewerkt
- [ ] Interacties tussen agents en omgeving beschreven
- [ ] Parameters en hun waarden benoemd
- [ ] Initialisatie (setup) beschreven
- [ ] Inputs en outputs gespecificeerd
- [ ] Tijdverloop (wat gebeurt elke tick) uitgelegd
- [ ] **Alle keuzes onderbouwd** (waarom wel/niet meenemen?)

### Deel 3: Implementatie
- [ ] Pseudocode of gedetailleerde beschrijving van `setup` en `go`
- [ ] NetLogo-code geschreven en werkend
- [ ] Code is overzichtelijk en voorzien van commentaar
- [ ] Verificatiestappen beschreven in verslag
- [ ] Model doet wat het zou moeten doen (geen bugs)

### Deel 4: Experimenteren
- [ ] BehaviorSpace-experiment opgezet
- [ ] Onafhankelijke variabelen benoemd met bereik en stapgrootte
- [ ] Afhankelijke variabelen benoemd (wat wordt gemeten?)
- [ ] Voldoende herhalingen uitgevoerd (≥10-20 runs)
- [ ] Stopcriterium vastgesteld
- [ ] Data geëxporteerd en geanalyseerd
- [ ] Grafieken gemaakt die resultaten helder tonen
- [ ] Patronen in data beschreven en geïnterpreteerd

### Deel 5: Validatie
- [ ] Microvalidatie: gedrag agents vergeleken met werkelijkheid
- [ ] Macrovalidatie: systeemgedrag vergeleken met werkelijkheid
- [ ] Verschillen benoemd en besproken
- [ ] Relevantie van verschillen voor onderzoeksvraag beargumenteerd
- [ ] Beperkingen van model expliciet genoemd

### Deel 6: Conclusie en reflectie
- [ ] Onderzoeksvraag beantwoord met onderbouwing uit resultaten
- [ ] Belangrijkste bevindingen samengevat
- [ ] Reflectie op proces: wat ging goed/beter?
- [ ] Modelaannames heroverwogen
- [ ] Wishlist voor volgende versie gemaakt

### (Optioneel) Deel 7: Samenwerking
- [ ] Per persoon een reflectie
- [ ] Werkverdeling

### Verslag (IMRAD)
- [ ] Introduction: context, onderzoeksvraag, relevantie
- [ ] Method: conceptueel model, implementatie, experiment
- [ ] Results: data en grafieken
- [ ] Analysis: interpretatie van resultaten
- [ ] Discussion: validatie, beperkingen, reflectie
- [ ] Conclusion: antwoord op onderzoeksvraag
- [ ] Bronnen vermeld (websites, literatuur, externe data)
- [ ] Inhoudsopgave aanwezig
- [ ] Paginanummering aanwezig
- [ ] Kopteksten gebruikt voor structuur

### Inleveren
- [ ] Verslag als Word- of PDF-document
- [ ] NetLogo-bestand (.nlogo) van je model
- [ ] Eventuele aanvullende bestanden (databestanden, grafieken)

## Inleveren

Lever de volgende bestanden in:

1. **Verslag** in Word of PDF met:
   - IMRAD-structuur
   - Inhoudsopgave
   - Paginanummering
   - Bronvermelding
   
2. **NetLogo-bestand** (.nlogo) van je werkende model

3. **Eventuele aanvullende bestanden** zoals:
   - Ruwe data uit BehaviorSpace (CSV)
   - Grafieken als losse bestanden
   - Andere relevante documenten

## Beoordeling

Deze eindopdracht wordt beoordeeld aan de hand van een rubric. Een rubric is een manier om een grotere, praktische opdracht te beoordelen aan de hand van criteria. 

Je kunt maximaal **40 punten** scoren, wat overeenkomt met een 10. Met een score van **20 punten** heb je een 5,5.

De rubric beoordeelt onder andere:

- **Onderzoeksvraag en afbakening** (is de vraag concreet en beantwoordbaar?)
- **Conceptueel model** (is het canvas volledig en zijn keuzes onderbouwd?)
- **Implementatie** (werkt de code, is deze overzichtelijk?)
- **Experimenteren** (is het experiment systematisch opgezet?)
- **Data-analyse** (zijn grafieken helder en is de interpretatie correct?)
- **Validatie** (is kritisch gekeken naar realisme van het model?)
- **Verslag** (is de structuur helder en de taal wetenschappelijk?)
- **Reflectie** (is kritisch nagedacht over proces en model?)

Heb je vragen over de beoordeling? Vraag de docent naar het volledige beoordelingsmodel.

## Tot slot

Deze eindopdracht is het moment waarop je laat zien dat je agent-based modelling beheerst: van onderzoeksvraag tot werkend model, van experiment tot wetenschappelijk verslag. Veel succes!