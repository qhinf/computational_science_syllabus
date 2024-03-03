# Eindopdracht

## De opdracht zelf

In deze praktische opdracht ga je de wetenschappelijke methode toepassen op het modelleren van een fenomeen, zoals beschreven in hoofdstuk 3 van het [lesmateriaal](assets/Module_ABM_lesmateriaal.pdf).

### Groepjes vormen en casus kiezen

Je mag alleen of met z'n tweeën werken. Kies een casus uit de lijst {ref}`de-lijst`. Je gaat een heel nieuw model maken. Je mag ook zelf een casus bedenken. Het is dan wel nodig dat je met de docent overlegt of deze casus voldoende is om deze module mee af te sluiten.

### Casus en onderzoeksvraag

Beschrijf wat je gaat modelleren en met welke doel aan de hand van de volgende vragen:

a.  Wat weet je van dit fenomeen? Voer eventueel het benodigde (literatuur-) onderzoek uit. 

b.  Welke (deel van het) fenomeen wil je modelleren?

c.   Waar hoop je achter te komen met behulp van jouw model?

### Model ontwerpen

Ontwerp je model aan de hand van de onderstaande vragen. Geef steeds aan welke overwegingen en keuzes je hebt gemaakt. 

Voorbeeld:

*De schapen kunnen zich voortplanten. Als twee schapen elkaar tegenkomen, dan is er een kans van 20% dat er een nieuw schaap ontstaat. We hebben besloten om het geslacht van de schapen niet te modelleren omdat dat in dit geval niet relevant is.*

De eerste twee vragen zijn alleen relevant als je een nieuw model ontwerpt.

a.  Wat zijn de voornaamste soorten agents die betrokken zijn bij dit fenomeen?

b.  In wat voor omgeving functioneren deze agents? Zijn er ook omgevingsagents aanwezig?

c.   Welke eigenschappen hebben de agents? (Beschrijf per type agent.)

d.  Welk gedrag vertonen de agents? (Beschrijf per type agent.) 

e.  Welke interacties hebben de agents onderling? En met de omgeving?

f.   Als je dit fenomeen in discrete tijdseenheden zou beschrijven, wat gebeurt er dan in elke tijdseenheid (d.w.z. bij elke tik van de klok) en in welke volgorde?

### Model implementeren

Beschrijf in detail (eventueel met pseudocode) de eigenschappen, het gedrag en de interacties van alle (omgevings-) agents. Beschrijf hoe de tijd verloopt in het model en wat de volgorde van gebeurtenissen is. Met andere woorden: geef aan hoe de *setup*- en *go*-procedures eruit zullen zien.

Implementeer je model in NetLogo. Doe niet te veel tegelijk: schrijf de code stukje voor stukje en blijf testen (verificatie)!

### Model valideren

Valideer je model aan de hand van de volgende vragen:

a.  Microvalidatie: in hoeverre komt het gedrag van de agents overeen met het gedrag dat in werkelijkheid wordt geobserveerd? Als het niet (helemaal) overeenkomt, zijn de verschillen dan relevant voor je onderzoeksvraag?

b.  Macrovalidatie: in hoeverre komt het gedrag van de het systeem als geheel in jouw model overeen met het gedrag dat in werkelijkheid wordt geobserveerd. Als het niet (helemaal) overeenkomt, zijn de verschillen dan relevant voor je onderzoeksvraag?

### Experiment, analyse en conclusie

Gebruik je model om het antwoord op jouw onderzoeksvraag te vinden aan de hand van de volgende punten:

a.  Beschrijf gedetailleerd hoe het experiment eruit ziet. Als je gebruik maakt van *BehaviorSpace*, beschrijf dan hoeveel experimenten er zijn uitgevoerd en met welke parameters.

b.  Vermeld je uitkomsten op een geschikte manier (beschrijvend, m.b.v. een tabel, een grafiek enz.)

c.   Analyseer de uitkomsten. 

d.  Beantwoord jouw onderzoeksvraag.

### Reflectie

Reflecteer op het modeleerproces aan de hand van de volgende vragen:

a.  Wat ging goed? Wat kon beter? 

b.  Heb je aannames gedaan, die je de volgende keer toch anders zou doen? Welke aspecten van het model wil je veranderen?

c.   Heb je in het begin van bepaalde zaken (agents of gedrag) afgezien, terwijl je nu denkt dat je ze toch had moeten meenemen in het model? Maak een *wishlist* van de zaken die je in een volgende versie van het model zou willen toevoegen, verwijderen en / of wijzigen.

## Inleveren: Model en documentatie

·   Een document met uitwerkingen van de hoofdvragen 1 t/m 6 uit de opdracht. Het document maak je in Word met een opmaak met kopteksten, inhoudsopgave. Wanneer je externe bronnen, zoals websites of literatuur gebruikt, dan vermeld je deze ook. Voorzie je document van paginanummering.

·   Het NetLogo-bestand van je model

## De beoordeling
Deze eindopdracht wordt beoordeeld aan de hand van een rubric. Een rubric is een manier om een grotere, praktische opdracht te beoordelen aan de hand van criteria. Met de [tabellen in dit document](assets/Computational_Science_nakijkmodel.pdf) kun je zelf al een inschatting maken hoe je eindopdracht gewaardeerd wordt. Heb je ergens twijfel of vragen over, aarzel niet ze te stellen aan de docent.

Je kunt maximaal 40 punten scoren. Je hebt dan een 10. Met een score van 20 punten heb je een 5,5.

(de-lijst)=
## De casussen

### Verkeersplein

Bij een kruispunt met stoplichten ontstaan er regelmatig files tijden het spitsuur. De gemeente overweegt om het kruispunt te vervangen door een verkeersplein.

 Zou dat de doorstroming van het verkeer ten goede komen?

### Leven op Mars

Kunnen mensen echt op Mars leven? 

NASA [^Nasa]
en SpaceX[^SpaceX]
denken van wel. Het idee is dat mensen op den duur zelfvoorzienend op Mars zouden kunnen leven, zonder afhankelijk te zijn van bevoorrading vanaf de Aarde.


Stel dat er geschikt onderdak geregeld is. Wat is er dan nodig om voldoende water, lucht en voedsel te produceren om te overleven? Is het mogelijk om zelfvoorzienend te worden?

### Wachtrij

Een bank wil een nieuwe filiaal openen. Met het oog op de klantenvriendelijkheid wil men de service in het filiaal zo organiseren dat de wachttijd voor de klanten zo klein mogelijk is.
 Bij een balie kan men verschillende soorten zaken doen. Sommige daarvan zijn vrij snel klaar (bijvoorbeeld saldo opvragen, geld storten) en duren maximaal 5 minuten. Andere zaken duren wat langer (bijvoorbeeld een rekening openen of opheffen) en dat duurt tussen de 3 en 10 minuten. Ten slotte zijn er zaken die lang duren en waarvoor men twee keer moet komen (bijvoorbeeld het regelen van een lening of hypotheek). In dat geval duurt elke bezoek tussen de 5 en 20 minuten.

Hoe kunnen de diensten het beste over de balies worden verdeeld? En wat betekent dit voor de wachtrijen van de klanten?

### Kaaspakhuis

Kaas wordt na de productie opgeslagen in kaaspakhuizen om te rijpen en in afwachting van verkoop. Hoe ouder de kaas, des te hoger de opbrengt, maar opslag in een pakhuis brengt ook kosten met zich mee.

Een kleine kaasproducent wil zijn verkoopstrategie optimaliseren, ofwel zijn winst maximaliseren. Op zijn boerderij worden elke maand 25 boerenkazen geproduceerd en in zijn pakhuis heeft hij ruimte voor 400 kazen. Als het pakhuis vol is, kan hij kiezen: hij zet de productie stop, of hij geeft een aantal kazen aan een goed doel. Hij kan kiezen uit een aantal verkoopkanalen. Hij kan leveren aan een biologische winkel waar hij langlopende contracten mee kan sluiten, of aan een streekmarkt met maandelijkse contracten waar hij hogere prijzen kan rekenen.

Hoe zit een optimale verkoopstrategie eruit?

### Aardappels

Een biologische aardappelteler wil zijn winst maximaliseren. Daartoe moet hij rekening houden met kosten die hij maakt voor pootgoed, mest, het verwijderen van aangetaste planten etc., maar ook met plagen en ziektes die zich makkelijk verspreiden als aardappels te dicht bij elkaar zijn geplant. Hij kan alleen aardappels van goede kwaliteit verkopen. De rest gooit hij weg.

Wat is de optimale strategie voor het planten en telen van aardappels?

### Brand op school

Bij brand in een school of een ander gebouw waar zich veel mensen bevinden, is het belangrijk dat mensen tijdig gealarmeerd kunnen worden om snel het gebouw te kunnen verlaten. Mensen die niet op tijd naar buiten kunnen komen lopen gevaar om dit niet te overleven.

De leiding van jouw school heeft advies nodig over het aantal alarmen en de positie van alarmen en nooduitgangen om de begane grond goed te kunnen evacueren. Idealiter wordt er ook rekening gehouden met het evacueren van mensen in een rolstoel.

Wat is op basis van jouw model het advies?

### Weerstand

Maak een model van elektrische weerstand. Controleer of de volgende natuurkundige wetten kloppen:

1. Wet van Ohm voor serieschakeling:

$$
R_v = \sum^n_{i=1}R_i
$$

2. Wet van Ohm voor parallelschakeling: 

$$
\frac{1}{R}=\sum^n_{i=1}\frac{1}{R_i}
$$

------

[^Nasa]: https://www.nasa.gov/image-article/nasas-journey-mars/

[^SpaceX]: http://www.spacex.com/mars