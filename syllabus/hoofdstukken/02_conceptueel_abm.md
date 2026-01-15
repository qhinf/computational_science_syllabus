(hoofdstukken/02_conceptueel_abm)=
# Van fenomeen naar regels (conceptueel ABM)

Je hebt in hoofdstuk 1 geleerd wat emergent gedrag is en hoe agents met simpele regels tot verrassende patronen kunnen leiden. Maar hoe vertaal je een fenomeen uit de echte wereld – zoals een Mexican wave, mieren die voedsel zoeken, of mensen die evacueren – naar een werkend model? In dit hoofdstuk leer je systematisch nadenken over agents, omgeving en interacties. Je ontwerpt regels zonder code te schrijven, bepaalt wat je kunt instellen (parameters) en wat je gaat meten (outputs). Aan het eind kun je een compleet **conceptueel model** opzetten, klaar om in hoofdstuk 3 te programmeren in NetLogo.

**Leerdoel:** Na dit hoofdstuk kun je een fenomeen ontleden in agents en regels, parameters en outputs bepalen, en een conceptueel model-canvas invullen voor je eigen onderzoeksvraag.

## Inhoud

In dit hoofdstuk behandelen we:

- Casus ontleden: agents / omgeving / interacties
- Regels ontwerpen: als-dan regels en drempels
- Parameters vs outputs: wat kun je instellen, wat ga je meten?
- Meetplan: monitors en plots (conceptueel, nog zonder NetLogo)
- Conceptueel model-canvas invullen

---

## Casus ontleden: agents / omgeving / interacties

Voordat je begint met programmeren, moet je helder hebben **wat** je gaat modelleren. De eerste stap is je fenomeen ontleden in drie componenten:

1. **Agents** – Wie of wat zijn de actieve spelers?
2. **Omgeving** – Waar spelen ze? Wat is de ruimte/wereld?
3. **Interacties** – Hoe reageren agents op elkaar en op de omgeving?

### Stap 1: Bepaal de agents

Een agent is een entiteit met eigen eigenschappen en gedrag. Vraag jezelf af: *Wat beweegt, handelt of beslist?*

**Voorbeeld: Mexican wave in een stadion**

- **Agent:** Een persoon in het stadion
- **Eigenschappen:** positie (rijnummer, stoelnummer), status (zit/staat)
- **Gedrag:** Kijk naar je buurman; als die staat, sta dan zelf ook op (na korte vertraging)

**Voorbeeld: Mieren zoeken voedsel**

- **Agent:** Een individuele mier
- **Eigenschappen:** positie (x, y), energie, draagt-voedsel? (ja/nee)
- **Gedrag:** Beweeg willekeurig; als je voedsel ziet, pak het; leg geurspoor achter als je voedsel draagt; volg geursporen

:::{tip}
**Hoe weet je of iets een agent is?**  
Stel de vraag: "Kan dit ding acties uitvoeren of beslissingen nemen?" Zo ja → agent. Zo nee → waarschijnlijk onderdeel van de omgeving.
:::

### Stap 2: Bepaal de omgeving

De omgeving is de ruimte waarin agents bewegen en interacteren. Dit kan een 2D-grid zijn, een continu vlak, een netwerk, of iets abstracts.

**Veel voorkomende omgevingstypen:**

- **Grid (raster):** De wereld is verdeeld in vierkante cellen (zoals een schaakbord). Agents staan op cellen en bewegen van cel naar cel.
- **Continu vlak:** Agents kunnen overal staan met precieze coördinaten (x=3.14, y=7.89), niet alleen op vaste posities.
- **Netwerk:** Agents zijn verbonden via lijnen (denk aan sociale netwerken: personen als knooppunten, vriendschappen als verbindingen).

**Omgevingseigenschappen** zijn dingen die niet bewegen, maar wel van invloed zijn:

- Muren of obstakels (in een evacuatiemodel)
- Geursporen op de grond (in een mierenmodel)
- Voedsel of hulpbronnen (in een foeragemodel)

**Voorbeeld: Mexican wave**

- **Omgeving:** Een rij stoelen (1D-grid: 100 personen naast elkaar)
- **Omgevingseigenschappen:** Geen; de omgeving is statisch

**Voorbeeld: Mieren zoeken voedsel**

- **Omgeving:** Een 2D-grid van 50x50 cellen
- **Omgevingseigenschappen:** Voedselstukken op bepaalde locaties, geursporen die vervagen over tijd

### Stap 3: Bepaal de interacties

Hoe beïnvloeden agents elkaar en de omgeving? Dit is waar het interessant wordt!

**Soorten interacties:**

1. **Agent ↔ Agent:** Mieren botsen op elkaar, mensen besmetten elkaar, auto's remmen voor de auto ervoor
2. **Agent → Omgeving:** Mieren leggen geursporen, mensen bouwen obstakels
3. **Omgeving → Agent:** Mieren ruiken geursporen, mensen zien voedsel of obstakels

**Voorbeeld: Mexican wave**

- **Interactie:** Persoon A kijkt naar persoon B (zijn buurman). Als B staat, wacht A 1 seconde en staat dan ook op.

**Voorbeeld: Mieren**

- **Agent → Omgeving:** Mier legt geurspoor achter op de grond
- **Omgeving → Agent:** Mier ruikt geurspoor en loopt liever in die richting
- **Agent ↔ Agent:** Mieren botsen (niet direct interactie, maar wel effect: ze gaan om elkaar heen)

:::{admonition} Let op
:class: warning
Verwar **properties** (eigenschappen) niet met **interacties**! Een agent heeft `energie` (eigenschap), maar *verliest* energie door te bewegen (interactie met de omgeving/tijd).
:::

```{exercise} Oefening (Oefenen)
:label: oef-2-1

Kies één van deze fenomenen: **een file op de snelweg** of **mensen die in paniek evacueren uit een gebouw**.

Vul de volgende tabel in:

| Component | Jouw antwoord |
|-----------|---------------|
| **Agent** (wie/wat?) | |
| **Agent-eigenschappen** (minimaal 3) | |
| **Omgeving** (waar?) | |
| **Omgevingseigenschappen** (minimaal 2) | |
| **Interacties** (minimaal 2) | |

Probeer zo concreet mogelijk te zijn. Bijvoorbeeld: niet "auto's", maar "auto met snelheid, positie, agressiviteit-van-bestuurder".
```

---

## Regels ontwerpen: als-dan regels en drempels

Je hebt nu agents, omgeving en interacties. De volgende stap: **wat doen agents precies?** Hier ontwerp je de **gedragsregels**.

### Als-dan logica

Agents volgen simpele **als-dan regels** (ook wel *if-then* of *conditionele regels*):

**Formaat:** Als [situatie], dan [actie].

**Voorbeelden:**

- Als `buurman staat`, dan `wacht 1 seconde en sta zelf ook op`
- Als `energie < 10`, dan `zoek voedsel`
- Als `afstand tot uitgang < 5 meter`, dan `versnel naar uitgang`
- Als `besmet? = ja` EN `buurman besmet? = nee`, dan `besmet buurman met kans 20%`

### Drempels en kansen

Veel regels bevatten **drempels** (grenswaardes) of **kansen** (probabiliteit):

**Drempels:** Een actie gebeurt alleen als een waarde boven/onder een grens komt.

- Als `energie < 20`, dan zoek voedsel
- Als `afstand tot buurman < 2 meter`, dan rem
- Als `aantal staande buren >= 1`, dan sta op

**Kansen:** Een actie gebeurt met een bepaalde waarschijnlijkheid.

- Met kans 30%: beweeg willekeurig
- Met kans 10%: besmet je buur
- Met kans 5%: verlaat de groep

:::{tip}
**Waarom kansen?**  
De echte wereld is vol onzekerheid. Niet iedereen besmet altijd zijn buren, niet iedere mier vindt meteen voedsel. Kansen maken je model realistischer én interessanter (elke run is anders!).
:::

### Goede regels zijn simpel en specifiek

Vermijd vage regels zoals:

- "Agents gedragen zich logisch" ❌
- "Mensen proberen te overleven" ❌

Gebruik concrete, programmeerbare regels:

- "Als paniek > 0.7, beweeg met 2x snelheid in willekeurige richting" ✅
- "Als geen voedsel in zicht, draai 15 graden en beweeg 1 stap vooruit" ✅

### Voorbeeld: Volledige regelset Mexican wave

Laten we de Mexican wave volledig uitwerken:

**Agent:** Persoon in stadion  
**Eigenschappen:** `status` (zit/staat), `positie` (nummer 1-100), `timer` (teller voor vertraging)

**Regels:**

1. **Als** `status = zit` EN `linker-buurman staat`, **dan** zet `timer = 1 seconde`
2. **Als** `timer = 0` EN `status = zit`, **dan** `status = staat`
3. **Als** `status = staat`, **dan** wacht 2 seconden en zet `status = zit`
4. **Als** `positie = 1` (eerste persoon), **dan** sta spontaan op (start de wave)

Dit zijn slechts 4 simpele regels, maar ze produceren het emergente gedrag van een prachtige golf door het stadion!

[Screenshot: Simulatie van Mexican wave met regels visueel weergegeven]

```{exercise} Oefening (Toepassen)
:label: oef-2-2

Kies **Mexican wave** of **mieren zoeken voedsel**.

Ontwerp minimaal **5 concrete als-dan regels** voor de agents in dit model. Gebruik het formaat:

**Als** [situatie], **dan** [actie].

Zorg dat minimaal:
- 1 regel een drempel bevat (bijv. "energie < 10")
- 1 regel een kans bevat (bijv. "met kans 20%")
- Alle regels specifiek en programmeerbaar zijn

*Tip:* Denk na over: Wat doet een agent als er niets speciaals aan de hand is? Wat doet een agent in een bijzondere situatie?
```

---

## Parameters vs outputs: wat kun je instellen, wat ga je meten?

Je hebt agents en regels. Nu komt een cruciaal onderscheid: **parameters** vs **outputs**.

### Parameters (inputs)

**Parameters** zijn waarden die je *instelt* voordat je het model start. Ze bepalen het gedrag van het systeem. Je kunt ze vaak *variëren* om te experimenteren.

**Voorbeelden:**

- Aantal agents (bijv. 100 mieren)
- Besmettingskans (bijv. 20%)
- Startsnelheid (bijv. 5 meter/seconde)
- Grootte van de wereld (bijv. 50x50 grid)
- Hoeveelheid voedsel (bijv. 10 stukken)

**Goede parameternamen zijn duidelijk:**

- `aantal-mensen` ✅ (beter dan `n`)
- `besmettingskans` ✅ (beter dan `prob`)
- `initiele-energie` ✅ (beter dan `e0`)

### Outputs (metingen)

**Outputs** zijn waarden die je *meet* tijdens of na de simulatie. Ze beantwoorden je onderzoeksvraag.

**Voorbeelden:**

- Percentage besmette personen na 100 ticks
- Gemiddelde tijd tot evacuatie
- Aantal mieren dat voedsel heeft gevonden
- Maximale lengte van de file

**Output kan zijn:**

- Een enkel getal (bijv. "na 50 ticks waren 73% besmet")
- Een grafiek (bijv. besmettingsgraad over tijd)
- Een telling (bijv. "hoeveel mieren hebben voedsel?")

### Het verschil onthouden

| Aspect | Parameter | Output |
|--------|-----------|--------|
| **Wanneer?** | Vooraf instellen | Tijdens/na meten |
| **Jij bepaalt?** | Ja, jij kiest de waarde | Nee, het model bepaalt het |
| **Doel?** | Experimenteren ("wat als?") | Resultaten analyseren |
| **Voorbeeld** | "Besmettingskans = 30%" | "Na 50 ticks: 80% besmet" |

:::{tip}
**Experimenteer met parameters!**  
De kracht van ABM zit in het variëren van parameters. Begin met een basiswaarde, verander dan één parameter en kijk wat er gebeurt. Zo ontdek je hoe het systeem werkt.
:::

### Voorbeeld: Virus-model

**Parameters:**
- `aantal-mensen` = 100
- `besmettingskans` = 20%
- `herstel-tijd` = 10 ticks
- `start-besmetten` = 5 mensen

**Outputs:**
- `percentage-besmet` (grafiek over tijd)
- `piek-besmetting` (hoogste aantal besmetten tegelijk)
- `tijd-tot-einde` (wanneer is iedereen hersteld of immuun?)

**Onderzoeksvraag:** Hoe beïnvloedt de besmettingskans de piek-besmetting?

**Experiment:** Voer model uit met besmettingskans = 10%, 20%, 30%, 40%, 50% en vergelijk de piek-besmetting.

```{exercise} Oefening (Oefenen)
:label: oef-2-3

Gebruik je eigen gekozen fenomeen (uit de vorige oefeningen) of kies een nieuw fenomeen.

Maak twee lijsten:

**A. Parameters** (wat stel je in? minimaal 4)  
Geef per parameter een **plausibele beginwaarde**. Bijvoorbeeld:
- aantal-auto's = 50
- max-snelheid = 120 km/u

**B. Outputs** (wat meet je? minimaal 3)  
Geef per output aan **hoe** je het zou meten. Bijvoorbeeld:
- gemiddelde-snelheid = som van alle snelheden / aantal auto's
- aantal-stilstaande-auto's = tel auto's met snelheid = 0

Denk na: Welke output helpt je om je onderzoeksvraag te beantwoorden?
```

---

## Meetplan: monitors en plots (conceptueel)

Je weet nu wat je wilt meten (outputs). Maar *hoe* visualiseer je dat tijdens je simulatie? In ABM gebruiken we twee hoofdmethoden: **monitors** en **plots**.

### Monitors: huidige waarde

Een **monitor** toont één getal: de huidige waarde van een variabele op dit moment in de simulatie.

**Voorbeelden:**

- `percentage-besmet` → toont "42%" (nu op dit moment)
- `aantal-mieren-met-voedsel` → toont "7" (actueel)
- `huidige-tick` → toont "125" (welke tijdstap zijn we?)

**Wanneer gebruik je monitors?**

- Voor een quick check: "Hoeveel agents zijn er nog?"
- Voor waarden die niet snel veranderen
- Voor het debuggen: "Klopt mijn model? Zijn er 100 agents zoals ik dacht?"

### Plots: verloop over tijd

Een **plot** (grafiek) toont hoe een waarde verandert tijdens de simulatie. De x-as is meestal de tijd (ticks), de y-as de gemeten waarde.

**Voorbeelden:**

- **Lijnplot:** Percentage besmetten over tijd (x=ticks, y=percentage)
- **Multi-line plot:** Vergelijk meerdere groepen (bijv. besmet/immuun/gezond in één grafiek)
- **Histogram:** Verdeling van snelheden van auto's

**Waarom plots?**

Plots laten patronen zien die je anders mist:

- Exponentiële groei van besmettingen
- Een stabiel evenwicht (plateau)
- Oscillaties (op-en-neer patroon)
- Chaos (onvoorspelbaar)

[Screenshot: Voorbeeld plot met besmettingscurve: langzaam starten, exponentiële groei, afvlakken]

:::{admonition} Let op
:class: warning
Een plot alleen is niet genoeg! Je moet de grafiek ook **interpreteren**. Bijvoorbeeld: "De grafiek toont een S-curve: eerst langzame groei, dan snelle verspreiding, daarna afvlakking omdat er geen nieuwe mensen meer besmet kunnen worden."
:::

### Meetplan opstellen

Een **meetplan** is een overzicht van wat je gaat meten en hoe.

**Formaat:**

| Output | Type | Eenheid | Verwachting |
|--------|------|---------|-------------|
| percentage-besmet | Plot | % | Stijgt eerst snel, dan afvlakken |
| aantal-mieren-met-voedsel | Monitor | aantal | Groeit langzaam, plateau op ~50 |
| gemiddelde-snelheid | Plot | km/u | Daalt bij file, stijgt als file oplost |

**Waarom een meetplan?**

- Het dwingt je na te denken: *wat verwacht ik?*
- Je kunt achteraf checken: *klopte mijn verwachting?*
- Het voorkomt dat je achteraf denkt: "Oh, ik had eigenlijk X moeten meten..."

```{exercise} Oefening (Reflecteren)
:label: oef-2-4

Beantwoord de volgende vragen in 3-5 zinnen per vraag:

**a)** Je modelleert een evacuatie. Je meet "gemiddelde tijd tot evacuatie". Na 10 runs varieert dit tussen 30 en 90 seconden. Wat betekent deze variatie? Is dat een probleem? Waarom wel/niet?

**b)** Je ziet in je plot dat het percentage besmetten eerst stijgt, dan daalt, dan weer stijgt, dan weer daalt (zigzag-patroon). Dit had je niet verwacht. Wat zou je doen? (Hint: denk aan regels, parameters, bugs)

**c)** Noem twee voorbeelden van regels in je model die "vals realistisch" zijn: ze lijken logisch, maar zijn eigenlijk te simpel of niet kloppend met de werkelijkheid. Leg uit waarom ze vals zijn.
```

---

## Conceptueel model-canvas invullen

Je hebt alle bouwstenen: agents, regels, parameters, outputs, meetplan. Nu zet je het in één overzicht: het **conceptueel model-canvas**. Dit is je ontwerp-document voordat je gaat programmeren.

### Het canvas: structuur

Een conceptueel model-canvas bevat deze onderdelen:

1. **Fenomeen/onderzoeksvraag**  
   *Wat modelleer je? Welke vraag wil je beantwoorden?*

2. **Agents**  
   *Wie/wat zijn de agents? Welke eigenschappen hebben ze?*

3. **Omgeving**  
   *Waar speelt het? Grid/continu/netwerk? Welke omgevingseigenschappen?*

4. **Interacties**  
   *Hoe beïnvloeden agents elkaar en de omgeving?*

5. **Regels (gedrag)**  
   *Wat doen agents? (als-dan regels)*

6. **Parameters**  
   *Wat kun je instellen? (met beginwaarden)*

7. **Outputs/metingen**  
   *Wat ga je meten? Monitors/plots?*

8. **Hypothese**  
   *Wat verwacht je dat er gebeurt?*

9. **Vereenvoudigingen/aannames**  
   *Wat laat je bewust weg? Welke aannames maak je?*

### Voorbeeld: Conceptueel canvas Mexican wave

**1. Fenomeen/onderzoeksvraag**  
Mexican wave in stadion. *Vraag:* Bij welke reactiesnelheid houdt de wave op met rondgaan?

**2. Agents**  
Personen (100 stuks). Eigenschappen: `status` (zit/staat), `positie` (1-100), `reactietijd` (in seconden).

**3. Omgeving**  
1D-rij van 100 stoelen naast elkaar. Geen obstakels.

**4. Interacties**  
Agent → Agent: Persoon ziet linker-buurman staan en reageert daarop.

**5. Regels**
- Als `linker-buurman staat` EN `status = zit`, wacht `reactietijd` seconden, dan `status = staat`
- Als `status = staat`, wacht 2 seconden, dan `status = zit`
- Als `positie = 1`, start spontaan (sta na 1 seconde op)

**6. Parameters**
- `aantal-personen` = 100
- `reactietijd` = 0.5 seconden (variabel in experiment!)

**7. Outputs**
- Monitor: `aantal-staande-personen`
- Plot: `golf-snelheid` (hoeveel personen per seconde staat de golf)
- Telling: `aantal-rondes` (hoe vaak gaat de golf rond voordat hij stopt?)

**8. Hypothese**  
Als reactietijd < 1 seconde, blijft de wave rondgaan (minimaal 3 rondes). Als reactietijd > 2 seconden, sterft de wave na 1 ronde.

**9. Vereenvoudigingen**
- Alle personen hebben dezelfde reactietijd (in werkelijkheid varieert dit)
- Personen zijn altijd attent (kijken altijd naar hun buur, niet afgeleid door telefoon)
- Geen "domino-effect" van beide kanten (alleen linker buur telt)

:::{tip}
**Canvas = ontwerp, code = uitvoering**  
Het canvas is je blauwdruk. Als je het goed invult, is programmeren daarna veel makkelijker. Je hoeft niet meer na te denken over *wat* je moet bouwen, alleen over *hoe* je het programmeert.
:::

```{exercise} Oefening (Toepassen)
:label: oef-2-5

Vul een compleet **conceptueel model-canvas** in voor je eigen gekozen fenomeen (of kies: mieren zoeken voedsel).

Gebruik de 9 onderdelen:
1. Fenomeen/onderzoeksvraag
2. Agents (met eigenschappen)
3. Omgeving
4. Interacties
5. Regels (minimaal 5 als-dan regels)
6. Parameters (minimaal 4, met beginwaarden)
7. Outputs (minimaal 3: monitors en/of plots)
8. Hypothese (wat verwacht je?)
9. Vereenvoudigingen (wat laat je weg? minimaal 2)

Je mag dit in een tabel of met koppen en opsommingen. Doel: een ander moet jouw model kunnen begrijpen en nabouwen zonder jou te vragen om uitleg.
```

---

## Verdiepende opgaven

Klaar voor meer uitdaging? Deze opgaven helpen je dieper nadenken over modelontwerp.

```{exercise} Opdracht (Validatie van regels)
:label: verd-2-1

Kies een ABM-fenomeen (bijv. virus, file, evacuatie, mieren, segregatie).

Ontwerp 3 regels die **te simpel** zijn (vals realistisch) en verbeter ze. Gebruik deze tabel:

| Te simpele regel | Waarom is dit te simpel? | Verbeterde regel |
|------------------|---------------------------|-------------------|
| Als `besmet`, besmet altijd je buur | In werkelijkheid besmet je niet altijd | Als `besmet` EN `afstand < 2m`, besmet buur met kans 20% |
| ... | ... | ... |

Reflecteer: Wat win je door de verbeterde regel? Wat verlies je (complexiteit, rekentijd)?
```

```{exercise} Opdracht (Parameter-gevoeligheidsanalyse)
:label: verd-2-2

Neem je conceptuele model. Identificeer de 3 belangrijkste parameters (degene waarvan je denkt dat ze het grootste effect hebben).

Ontwerp een **experiment** om te testen welke parameter het meest invloedrijk is:

a) Omschrijf het experiment: welke waarden test je? (bijv. besmettingskans: 10%, 20%, 30%, 40%, 50%)  
b) Wat is je afhankelijke variabele (output die je meet)?  
c) Wat houd je constant?  
d) Welke parameter verwacht je het meest invloedrijk? Waarom?

Schrijf 200-300 woorden.
```

```{exercise} Opdracht (Van klein naar groot: schaaleffecten)
:label: verd-2-3

Veel modellen gedragen zich anders bij verschillende schalen. Bijvoorbeeld: 10 mieren vs 1000 mieren, of 50x50 grid vs 200x200 grid.

Beantwoord voor jouw model:

a) Wat gebeurt er als je het aantal agents **verdubbelt**? Welke outputs veranderen? Welke blijven hetzelfde?  
b) Wat gebeurt er als je de omgeving **2x groter** maakt, maar hetzelfde aantal agents houdt? (Dus lagere dichtheid)  
c) Zijn er parameters die je moet **aanpassen** als je schaalt? Bijvoorbeeld: moet de besmettingskans hoger als je meer mensen hebt?

Denk kritisch en onderbouw met logica. 250-350 woorden.
```

---

## PO-mijlpaal

Na dit hoofdstuk ben je klaar voor de tweede mijlpaal: het conceptuele ontwerp van je eindproject.

### Wat lever je op na deze fase?

Als het je helpt, zet de volgende punten in een document. Dit is alvast je opzet voor je eindopdracht. Het is een **conceptueel model-canvas** met alle 9 onderdelen.

### Checklist: je bent klaar met je conceptuele model als…

- [ ] Je regels zijn concreet en programmeerbaar (geen vage taal zoals "agents gedragen zich logisch")
- [ ] Je hebt minimaal 1 regel met een drempel (bijv. "energie < 10")
- [ ] Je hebt minimaal 1 regel met een kans (bijv. "met 20% kans")
- [ ] Je parameters zijn duidelijk benoemd en hebben realistische beginwaarden
- [ ] Je outputs zijn **meetbaar** en helpen je onderzoeksvraag beantwoorden
- [ ] Je hypothese is **toetsbaar**: je kunt straks zeggen "klopt" of "klopt niet"
- [ ] Je hebt nagedacht over vereenvoudigingen en kunt uitleggen **waarom** je ze maakt
- [ ] Een klasgenoot kan jouw canvas lezen en het model nabouwen zonder jou te vragen om uitleg

### Waar komt dit terug in je eindproject?

Dit canvas is de **kern van je methodesectie** in het eindverslag:

- **Inleiding:** Je onderzoeksvraag en hypothese komen uit je canvas
- **Methode:** Agents, regels, parameters en omgeving worden hier uitgelegd
- **Resultaten:** Je outputs zijn de grafieken/tabellen die je laat zien
- **Discussie:** Je vereenvoudigingen zijn beperkingen die je bespreekt

Bewaar het canvas goed! In hoofdstuk 3 ga je het implementeren in NetLogo. Met een helder canvas is programmeren véél makkelijker.

---

**Volgende stap:** In hoofdstuk 3 ga je NetLogo leren. Je bouwt je eerste simpele model, leert de syntax, en zet je conceptuele canvas om in werkende code. Je agents gaan écht bewegen! Tot dan!
