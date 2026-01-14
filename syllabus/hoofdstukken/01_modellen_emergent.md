# Modellen en emergent gedrag

Waarom gedragen mensen zich anders in een volle trein dan in een lege? Hoe kan een file ontstaan zonder dat er een ongeluk is? Waarom ontstaan er Chinese wijken in steden, ook als mensen niet perse bij elkaar willen wonen? Dit soort vragen beantwoorden met de wetenschappelijke methode is lastig: je kunt niet zomaar een pandemie uitbreken, file veroorzaken of een hele stad opnieuw inrichten. Hier komt **computational science** om de hoek kijken. In dit hoofdstuk leer je wat modellen zijn, waarom we ze gebruiken, en hoe simpele regels voor individuen kunnen leiden tot verrassend complex groepsgedrag – dat noemen we **emergent gedrag**. Je maakt kennis met de basisconcepten van Agent-Based Modeling (ABM) en leert hoe je goede onderzoeksvragen formuleert. Dit is de fundering voor alles wat volgt in deze module.

**Leerdoel:** Na dit hoofdstuk begrijp je wat modellen zijn, kun je emergent gedrag herkennen en uitleggen, en weet je hoe je een onderzoeksvraag en hypothese formuleert voor een ABM-project.

## Inhoud

In dit hoofdstuk behandelen we:

- Wat is een model? (waarom we vereenvoudigen)
- Agents en regels
- Emergent gedrag: van lokaal naar globaal
- Ticks, iteraties en tijd in simulaties
- Goede onderzoeksvragen en hypothesen
- Mini-check: begrippen en misvattingen

---

## Wat is een model?

Een **model** is een vereenvoudigde weergave van de werkelijkheid. Denk aan een plattegrond van een gebouw, een weerbericht, of een maquette van een nieuw stadion. Het is nooit compleet – en dat is precies de bedoeling. Een model laat alleen zien wat relevant is voor je vraag.

**Waarom versimpelen we?**

De werkelijkheid is ongelooflijk complex. Elk mens heeft duizenden eigenschappen: lengte, gewicht, stemming, honger, opinies, herinneringen, noem maar op. Als je alle details meeneemt in een model, wordt het even complex als de werkelijkheid zelf. Dan kun je er niets mee. Daarom kiezen we bewust: *welke eigenschappen zijn belangrijk voor mijn vraagstuk, en welke kan ik negeren?*

**Voorbeeld:** Stel je wilt begrijpen hoe mensen evacueren uit een brandend gebouw. Dan is de vraag: wat heb je nodig?

- **Wel belangrijk:** positie van mensen, loopsnelheid, kennis van nooduitgangen, paniek
- **Niet belangrijk:** haarkleur, favoriete muziek, schoenmaat

Door slim te versimpelen krijg je een **bruikbaar** model dat je helpt inzicht te krijgen zonder te verdrinken in details.

**Waarom gebruiken we modellen?**

Modellen worden in de wetenschap en praktijk voor veel doelen gebruikt:

- **Beschrijven:** Hoe ziet het systeem eruit? (bijv. stroomschema van verkeer)
- **Uitleggen:** Waarom gebeurt iets? (bijv. waarom ontstaan files?)
- **Experimenteren:** Wat gebeurt er als…? (bijv. wat als we meer bushaltes plaatsen?)
- **Voorspellen:** Wat gebeurt er in de toekomst? (bijv. hoeveel mensen raken besmet?)
- **Communiceren:** Hoe leg ik iets uit aan anderen? (bijv. animatie van virus-verspreiding)

:::{tip}
**Gouden regel:** Een model is altijd *fout* (het is immers vereenvoudigd), maar het kan wel *nuttig* zijn. De kunst is kiezen welke details je weggooit.
:::

---

## Agents en regels

In **Agent-Based Modeling (ABM)** bouw je een model door individuele entiteiten te simuleren. Die entiteiten noemen we **agents**. Een agent kan van alles zijn: een persoon, een mier, een auto, zelfs een bloedcel.

**Wat maakt iets een agent?**

1. **Agents hebben eigenschappen** (ook wel *attributen* of *variabelen* genoemd).  
   Voorbeeld: een persoon-agent heeft `leeftijd`, `besmet?` (waar/onwaar), `energie-level`
   
2. **Agents hebben gedrag** (ze kunnen acties uitvoeren).  
   Voorbeeld: `beweeg-naar-doel`, `besmet-anderen`, `zoek-voedsel`
   
3. **Agents reageren op hun omgeving en andere agents**.  
   Voorbeeld: een persoon gaat naar rechts als de uitgang daar is; een mier legt een spoor achter dat andere mieren volgen

**Standaardvragen voor een conceptueel model:**

Wanneer je een fenomeen wilt modelleren, stel je deze vragen:

1. Wat zijn de **agents** in het model?
2. Welke **eigenschappen** hebben de agents?
3. Welk **gedrag** kunnen de agents vertonen?
4. In welke **omgeving** opereren de agents? (bijv. een grid, een gebouw, een landschap)
5. Hoe **reageren** agents op hun omgeving en op elkaar?

**Voorbeeld: Virus-verspreiding**

- **Agents:** Individuele mensen
- **Eigenschappen:** `besmet?` (ja/nee), `immuun?` (ja/nee), `positie-x`, `positie-y`
- **Gedrag:** Beweeg willekeurig rond; als je besmet bent, besmet je je buren; na 5 dagen word je immuun
- **Omgeving:** Een 2D-wereld (vierkant vlak) waar mensen rondlopen
- **Interactie:** Als een besmette persoon naast een niet-besmette persoon staat, kan besmetting plaatsvinden

:::{admonition} Let op
:class: warning
Agents zijn *autonoom*: ze beslissen zelf wat ze doen op basis van hun regels en omgeving. Er is geen centrale "regisseur" die alles aanstuurt. Dat is het verschil met traditionele modellen waar je één grote formule hebt.
:::

```{exercise} Oefening (Oefenen)
:label: oef-1-1

Match de begrippen met de juiste definitie:

| Begrip | Definitie |
|--------|-----------|
| 1. Eigenschappen | A. De handelingen die een agent kan uitvoeren |
| 2. Gedrag | B. De ruimte waarin agents opereren en bewegen |
| 3. Omgeving | C. Kenmerken of attributen die een agent beschrijven |
| 4. Autonoom | D. Agents beslissen zelf wat ze doen zonder centrale sturing |

Schrijf je antwoord op als: 1-C, 2-A, enz.
```

---

## Emergent gedrag: van lokaal naar globaal

Hier wordt het écht interessant. **Emergent gedrag** is het groepsgedrag dat ontstaat uit simpele individuele regels, zonder dat iemand het groepsgedrag heeft geprogrammeerd.

**Definitie:** Emergent gedrag is het gedrag van een systeem als geheel dat *niet* expliciet is geprogrammeerd, maar *ontstaat* door de interacties tussen individuele agents die simpele regels volgen.

Dat klinkt abstract. Laten we twee concrete voorbeelden bekijken.

### Voorbeeld 1: Mieren zoeken voedsel

Individuele mieren zijn niet slim. Ze hebben geen kaart, geen meesterplan. Toch kunnen duizenden mieren efficiënt voedsel vinden en naar hun nest brengen. Hoe?

**Simpele regels per mier:**
1. Beweeg willekeurig rond
2. Als je voedsel vindt, pak het op en loop terug naar het nest
3. Terwijl je terugloopt, laat je een **geurspoor** (feromoon) achter
4. Als je een geurspoor ruikt, loop je liever in die richting

**Emergent resultaat:**  
Zodra één mier voedsel vindt en een spoor legt, gaan andere mieren dat spoor volgen. Zij versterken het spoor. Na een tijdje ontstaat er een *snelweg* tussen nest en voedsel, zonder dat er een "baas-mier" is die het heeft bedacht. Het pad ontstaat vanzelf uit de simpele regels.

[Screenshot: NetLogo ants model – mieren vormen paden naar voedselbronnen]

### Voorbeeld 2: Mexican wave in een stadion

Je hebt het vast wel eens gezien: duizenden mensen in een stadion maken samen een golf die rondgaat. Niemand is de regisseur. Hoe ontstaat dit?

**Simpele regels per persoon:**
1. Als de persoon naast je opstaat, wacht dan 1 seconde en sta dan ook op
2. Blijf 2 seconden staan
3. Ga weer zitten

**Emergent resultaat:**  
De "golf" loopt door het stadion zonder dat iemand het stuurt. Als je van bovenaf kijkt, zie je een prachtig patroon. Maar elke persoon deed alleen maar: kijk naar je buurman, sta op, ga zitten. Dat is emergent gedrag: het *geheel* is meer dan de som der *delen*.

[Screenshot: Simulatie van Mexican wave – mensen staan op in een golfpatroon]

### Nog een krachtig voorbeeld: Segregatie

Econoom Thomas Schelling deed in de jaren '70 een beroemd experiment. Hij simuleerde mensen in een stad met twee groepen (bijv. groep A en groep B). Elke persoon wilde dat *minstens 60%* van zijn buren dezelfde groep was. Dat lijkt redelijk tolerant, toch?

**Verrassend resultaat:** Zelfs met deze lage eis ontstond er **sterke segregatie** in de stad. Groep A ging in één wijk wonen, groep B in een andere. Niemand wilde dat, maar het gebeurde toch door de lokale beslissingen van individuen. De lokale beslissing van een mens is dus dat die persoon minstens 60% van zijn buren uit zijn eigen groep wil hebben. Is minder dan 60% van je buren van jouw groep? Dan ga je verhuizen.

Dit is het krachtige van ABM: je ziet patronen ontstaan die je *niet* had verwacht. En je kunt experimenteren: wat gebeurt er als we de tolerantie verhogen naar 80%? Of verlagen naar 40%?

:::{tip}
**Herken emergent gedrag:**  
Vraag jezelf af: "Staat dit gedrag in de regels van één agent?" Als het antwoord "nee" is, maar je ziet het wel gebeuren in het systeem, dan is het emergent.

Voorbeelden:
- Mieren vormen een pad → emergent (geen enkele mier "weet" dat er een pad komt)
- Een mier beweegt willekeurig → niet emergent (dit staat in de regel van die mier)
- Files ontstaan op de snelweg → emergent (geen automobilist "wil" een file, maar het gebeurt toch)
:::

```{exercise} Oefening (Toepassen)
:label: oef-1-2

Analyseer de Mexican wave en beantwoord:

a) Wie/wat zijn de agents?  
b) Noem minimaal 2 regels die een agent volgt.  
c) Wat is het emergente gedrag?  
d) Welke meetbare output zou je kunnen gebruiken? (bijv. snelheid van de golf, hoe vaak de golf rondgaat voordat hij stopt)

Schrijf je antwoorden in volledige zinnen.
```

---

## Ticks, iteraties en tijd in simulaties

In de echte wereld loopt tijd continu. In een simulatie werken we met **discrete tijdstappen**, ook wel **ticks** genoemd.

**Wat is een tick?**

Een **tick** is één tijdstap in je model. Je kunt het zien als een moment waarin het systeem "één stap verder" zet. Tijdens elke tick gebeurt het volgende:

1. Alle agents voeren hun acties uit (in een bepaalde volgorde)
2. De omgeving wordt bijgewerkt
3. De tijdsteller gaat één omhoog
4. De cyclus begint opnieuw

**Voorbeeld: één tick in een virus-model**

Stel je een model voor waar mensen rondlopen en elkaar kunnen besmetten:

- **Tick 0 (startsituatie):** 100 mensen, 1 persoon besmet
- **Tick 1:** Alle mensen bewegen → besmette personen besmetten hun buren → nu 3 mensen besmet
- **Tick 2:** Alle mensen bewegen → besmette personen besmetten hun buren → nu 8 mensen besmet
- **Tick 3:** Alle mensen bewegen → besmette personen besmetten hun buren → nu 18 mensen besmet
- *... enzovoort ...*

**Volgorde is belangrijk!**

De volgorde van acties binnen een tick maakt uit voor het resultaat. Vergelijk:

- **Volgorde A:** Eerst bewegen, dan besmetten → mensen besmetten op hun nieuwe positie
- **Volgorde B:** Eerst besmetten, dan bewegen → mensen besmetten op hun oude positie

Dit geeft verschillende uitkomsten! Bij het ontwerpen van je model moet je dus goed nadenken over de logische volgorde.

**Tijdschaal koppelen aan werkelijkheid**

Je beslist zelf wat één tick betekent in termen van echte tijd. Dit noem je de **tijdschaal** van je model. Voorbeelden:

- In een virus-model: 1 tick = 1 dag
- In een verkeer-model: 1 tick = 1 seconde  
- In een evolutie-model: 1 tick = 1 generatie
- In een evacuatie-model: 1 tick = 0.1 seconde

De keuze hangt af van je onderzoeksvraag en de snelheid van de processen die je modelleert.

**Initialisatie en reset**

Voordat je een simulatie start, moet je de beginsituatie instellen:

- Hoeveel agents zijn er?
- Waar bevinden ze zich?
- Wat zijn hun beginwaarden (bijv. welke persoon is besmet)?
- Zet de tijdsteller op 0

Dit noem je de **initialisatie** of **setup** van je model.

:::{tip}
**Reproduceerbare resultaten**  
Door steeds met dezelfde beginsituatie te starten, kun je experimenten herhalen. Dit is belangrijk voor wetenschappelijk onderzoek: anderen moeten je resultaten kunnen reproduceren.
:::

**Iteratie en simulatie-runs**

Een **iteratie** is één cyclus door alle stappen (één tick). Je model doorloopt vaak honderden of duizenden iteraties. Het geheel van alle iteraties vanaf de start tot het einde noem je een **simulatie-run** of kortweg **run**.

Bijvoorbeeld: je start je virus-model en laat het 100 ticks lopen. Dat is 1 run van 100 iteraties.

---

## Goede onderzoeksvragen en hypothesen

Een model is pas nuttig als je er een goede **onderzoeksvraag** mee beantwoordt. Zonder vraag is het alleen maar een leuk speeltje.

### Wat is een goede onderzoeksvraag?

Een goede onderzoeksvraag is:

1. **Specifiek:** Niet "Hoe werkt een virus?" maar "Hoe ontwikkelt de besmettingsgraad zich in de tijd bij verschillende besmettingspercentages?"
2. **Meetbaar:** Je moet kunnen zien in je model of je de vraag beantwoordt (bijv. via een grafiek of tabel)
3. **Interessant:** De vraag moet iets nieuws onthullen of een probleem oplossen

**Voorbeelden van goede onderzoeksvragen:**

- "Hoe hangt de gemiddelde wachttijd bij de bushalte af van de frequentie van bussen?"
- "Bij welke tolerantiewaarde ontstaat er geen segregatie meer in de stad?"
- "Hoe snel bereikt een virus 50% van de populatie bij een besmettingskans van 10% vs. 50%?"

**Voorbeelden van slechte onderzoeksvragen:**

- "Is dit model realistisch?" (te vaag)
- "Wat gebeurt er als ik op go druk?" (niet specifiek, geen richting)
- "Hoeveel mensen zijn er?" (triviaal, staat al in je model)

### Hypotheses opstellen

Voordat je je model uitvoert, stel je een **hypothese** op. Dat is een voorspelling van wat je denkt dat er gaat gebeuren.

**Voorbeeld:**

- **Onderzoeksvraag:** "Hoe ontwikkelt de besmettingsgraad zich in de tijd?"
- **Hypothese:** "Ik verwacht dat de besmettingsgraad eerst langzaam stijgt, dan exponentieel groeit, en uiteindelijk afvlakt wanneer bijna iedereen besmet of immuun is (S-curve)."

Na het experimenteren ga je kijken: *klopt mijn hypothese?* Zo niet, waarom niet? Dit is de wetenschappelijke methode.

### De modelleercyclus

Bij computational science volg je deze cyclus:

1. **Definiëren** – Wat is het probleem? Wat wil je weten?
2. **Conceptualiseren** – Vertaal het probleem naar een conceptueel model (agents, regels, omgeving)
3. **Formaliseren** – Programmeer het model in NetLogo (volgende hoofdstukken!)
4. **Experimenteren** – Voer het model uit, varieer parameters, verzamel data
5. **Analyseren** – Interpreteer resultaten, trek conclusies, beantwoord je vraag

Je doorloopt deze cyclus vaak meerdere keren: je ontdekt iets, past je model aan, en experimenteert opnieuw.

:::{tip}
**"One run is no run!"**  
Veel modellen bevatten random elementen (zoals willekeurige beweging). Als je het model maar één keer uitvoert, kan het toeval een grote rol spelen. Voer je experiment daarom *meerdere keren* uit (bijv. 10 of 20 runs) en neem het gemiddelde. Zo krijg je betrouwbare resultaten.
:::

```{exercise} Oefening (Reflecteren)
:label: oef-1-3

Bedenk twee fenomenen die je zou willen modelleren met ABM. Formuleer per fenomeen:

a) Een korte omschrijving (2-3 zinnen): wat is het fenomeen?  
b) Een onderzoeksvraag (specifiek en meetbaar)  
c) Een hypothese: wat verwacht je dat er gebeurt?  
d) Een meetbare uitkomstmaat (bijv. "gemiddelde snelheid", "percentage besmette personen")

**Reflecteer ook:** Welke aspecten van de werkelijkheid ga je *weglaten* in je model? Wat verlies je daardoor aan realisme? Geef 2 concrete voorbeelden.
```

---

## Mini-check: begrippen en misvattingen

Laten we checken of de belangrijkste concepten helder zijn.

**Centrale begrippen samengevat:**

| Begrip | Betekenis | Voorbeeld |
|--------|-----------|-----------|
| **Model** | Vereenvoudigde weergave van werkelijkheid | Plattegrond, weerbericht, ABM van virus |
| **Agent** | Individuele entiteit met eigenschappen en gedrag | Persoon, mier, auto |
| **Emergent gedrag** | Groepspatroon dat ontstaat uit individuele regels | Mierenpad, Mexican wave, segregatie |
| **Tick** | Discrete tijdstap in simulatie | 1 tick = 1 dag in virus-model |
| **Hypothese** | Voorspelling van uitkomst vóór je experimenteert | "Ik verwacht een S-curve van besmettingen" |
| **Iteratie** | Eén keer door de `go` procedure | Model draait 100 iteraties = 100 ticks |

**Veelgemaakte misvattingen:**

1. **"Een agent weet wat er in het hele systeem gebeurt"**  
   → Nee! Agents zijn lokaal. Een mier weet niet waar het nest is, alleen of ze een spoor ruikt.

2. **"Emergent gedrag is hetzelfde als het gedrag van één agent"**  
   → Nee! Emergent gedrag ontstaat op *systeemniveau* en staat niet in de regels van één agent.

3. **"Een model moet zo gedetailleerd mogelijk zijn"**  
   → Nee! Een goed model is zo *eenvoudig als mogelijk* voor de vraag die je wilt beantwoorden.

4. **"Eén run is genoeg om conclusies te trekken"**  
   → Nee! Bij random modellen heb je meerdere runs nodig voor betrouwbare gemiddeldes.

:::{admonition} Check jezelf
:class: tip
Kun je deze vragen beantwoorden zonder terug te bladeren?

- Wat is het verschil tussen een agent en een model?
- Noem een voorbeeld van emergent gedrag uit je eigen leven.
- Waarom is een hypothese belangrijk?

Zo ja? Top! Zo nee? Blader even terug en lees de sectie opnieuw.
:::

---

## Verdiepende opgaven

Wil je verder? Probeer deze uitdagingen. Hiervoer is het handig wanneer je NetLogo al op je computer hebt staan.

```{exercise} Opdracht (Emergent gedrag in de natuur)
:label: verd-1

Zoek online naar het fenomeen **"starling murmuration"** (spreeuwen zwermen). Bekijk een video en beantwoord:

a) Wat zijn de agents?  
b) Welke simpele regels denk je dat een spreeuw volgt? (hint: kijk naar afstand tot buren, richting van buren)  
c) Wat is het emergente gedrag?  
d) Waarom zou dit nuttig zijn voor de vogels (evolutionair voordeel)?

Schrijf 200-300 woorden.
```

```{exercise} Opdracht (Schelling segregatie-model)
:label: verd-2

Lees over het **Schelling segregation model** (zoek op Wikipedia of bekijk het model in NetLogo Library: Social Science → Segregation). 

a) Experimenteer met de "%-similar-wanted" slider. Wat is het minimale percentage waarbij sterke segregatie ontstaat?  
b) Is dit verrassend? Leg uit waarom wel/niet.  
c) Bedenk een maatschappelijke context waar dit relevant is (bijv. schoolsegregatie, woonsegregatie). Formuleer een onderzoeksvraag die je met dit model zou kunnen onderzoeken.
```

```{exercise} Opdracht (File-dynamiek)
:label: verd-3

Bestudeer het fenomeen "phantom traffic jams" (spookfiles). Dit zijn files die ontstaan zonder aanleiding (geen ongeluk, geen verkeerslicht).

a) Zoek een animatie/uitleg van dit fenomeen online.  
b) Schets een conceptueel ABM-model voor dit fenomeen:  
   - Agents: …  
   - Eigenschappen per agent: …  
   - Regels per agent: …  
   - Meetbare uitkomst: …  
c) Wat is hier het emergente gedrag?

Schrijf 300-400 woorden.
```

---

## PO-mijlpaal

Na dit hoofdstuk ben je klaar om te starten met je eindopdracht. Dit is je eerste mijlpaal:

### Wat lever je op na deze fase?

Als het je helpt, zet de volgende punten in een document. Dit is alvast je opzet voor je eindopdracht.

1. **Gekozen fenomeen:** Welk fenomeen met emergent gedrag ga je modelleren? (2-3 zinnen beschrijving)
2. **Onderzoeksvragen:** Formuleer 2 concrete, meetbare onderzoeksvragen over dit fenomeen
3. **Hypothese:** Formuleer 1 hypothese voor één van je onderzoeksvragen (wat verwacht je dat er gebeurt?)
4. **Meetbare uitkomstmaat:** Welke variabele(n) ga je bijhouden? (bijv. "percentage besmette personen na 50 ticks", "gemiddelde tijd tot evacuatie")

### Checklist: je bent klaar als…

- [ ] Je fenomeen heeft duidelijk emergent gedrag (niet: één agent doet iets ingewikkelds)
- [ ] Je onderzoeksvragen zijn specifiek en meetbaar (niet vaag zoals "hoe werkt dit?")
- [ ] Je hypothese is toetsbaar (je kunt straks zeggen: klopt / klopt niet)
- [ ] Je uitkomstmaat is concreet (een getal, grafiek of percentage)
- [ ] Je hebt nagedacht over: welke versimpelingen ga ik maken? (je hoeft niet alles mee te nemen!)

### Waar komt dit terug in je eindproject?

Dit document wordt de basis van:

- Je **inleiding** in het verslag (probleemstelling, onderzoeksvraag)
- Je **methode** sectie (conceptueel model, hypothese)
- Je **resultaten** sectie (meetbare uitkomsten)

Bewaar het goed! Je gaat dit uitwerken in de komende weken tot een compleet model en verslag.

---

**Volgende stap:** In hoofdstuk 2 ga je je fenomeen vertalen naar een conceptueel model: wie zijn de agents precies, welke regels volgen ze, in welke omgeving leven ze? Dan komen we dichterbij het echte programmeerwerk in NetLogo. Veel succes!
