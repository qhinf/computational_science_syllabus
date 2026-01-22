<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #3498db, #ffffff)" -->

# Computational Science

Q-highschool / Bijeenkomst 1

Notes:
Welkom bij Computational Science! Deze module gaat over het begrijpen van complexe systemen door ze na te bouwen met computers.

Voorstellen / wie heeft er al eens een simulatie gemaakt of gezien? / Wie heeft wel eens nagedacht over waarom mensen zich anders gedragen in een groep?

---

## Vandaag

- Wat zijn modellen en waarom gebruiken we ze?
- Agents en regels
- Emergent gedrag: van simpel naar complex
- Eerste kennismaking met NetLogo

---

## Wat ga je leren?

<div class="columns">
<div class="fragment">

**Begrijpen**
- Emergent gedrag herkennen
- Van fenomeen naar model

**Bouwen**
- Werken met NetLogo
- Je eigen ABM maken

</div>
<div class="fragment">

**Onderzoeken**
- Experimenteren met parameters
- Data verzamelen en analyseren

**Rapporteren**
- Wetenschappelijk verslag
- Verificatie & validatie

</div>
</div>

Notes:
In 7 weken ga je van nul naar een compleet werkend model. Je leert modelleren, programmeren in NetLogo, experimenteren en rapporteren. En het mooie: je kiest zelf een fenomeen dat jou interesseert!

---

## Deze module

Veel zelfstandig aan het werk!

<!-- .element: class="fragment" -->

Met een beetje begeleiding, natuurlijk

<!-- .element: class="fragment" -->

Aan het eind: jouw eigen werkend model!

<!-- .element: class="fragment" -->

***

## Openingsquiz

Wat hebben deze situaties gemeen?

---

Een file ontstaat op de snelweg, zonder ongeluk

_Wat veroorzaakt dit?_

- Iedereen rijdt te snel
- Eén auto remt even
- De weg is te smal
- Pech van de weggebruikers

<!-- .element: class="mc" -->

Notes:
Het antwoord is: één auto remt even. Door de reactietijd van alle volgende auto's ontstaat er een schokgolf die kan uitgroeien tot een file. Elk individu doet iets simpels (afstand houden, remmen als de voorganger remt), maar het collectieve gedrag is een file.

---

Vogels vliegen in perfecte formatie

_Hoe doen ze dat?_

- Een leider geeft commando's
- Ze volgen simpele regels (afstand, richting)
- Ze communiceren via geluiden
- Ze hebben een ingebouwde GPS

<!-- .element: class="mc" -->

Notes:
Vogels volgen simpele regels: blijf bij je buren, vlieg in dezelfde richting, botst niet. Geen leider, geen GPS. Toch ontstaat er een prachtige formatie. Dit is emergent gedrag!

---

## Gemeenschappelijkheid

**Complex groepsgedrag ontstaat uit simpele individuele regels**

<!-- .element: class="fragment" -->

Dat noemen we **emergent gedrag**

<!-- .element: class="fragment" -->

Notes:
Dit is de kern van deze module: complexe patronen ontstaan uit simpele regels. Dit kun je niet voorspellen door alleen naar één individu te kijken. Je moet het systeem simuleren.

***

## Wat is een model?

&nbsp;

Notes:
Waar denken jullie aan bij het woord "model"?

Laat studenten voorbeelden geven. Denk aan: plattegrond, maquette, weerbericht, wiskundige formule, pop, foto...

---

## Een model is...

Een **vereenvoudigde weergave** van de werkelijkheid

<!-- .element: class="fragment" -->

Die alleen de **relevante details** laat zien

<!-- .element: class="fragment" -->

Voor een **specifieke vraag**

<!-- .element: class="fragment" -->

Notes:
Een model is ALTIJD vereenvoudigd. De kunst is: welke details zijn belangrijk en welke kun je weglaten?

---

## Voorbeeld: Evacuatie uit een gebouw

<div class="columns">
<div class="fragment">

**Wel belangrijk:**
- Positie
- Loopsnelheid
- Nooduitgangen
- Paniek

</div>
<div class="fragment">

**Niet belangrijk:**
- Haarkleur
- Favoriete muziek
- Schoenmaat

</div>
</div>

Notes:
Dit is de kunst van modelleren: bewust kiezen wat je meeneemt en wat niet. Hoe meer details, hoe complexer het model - maar niet per se beter!

---

## De gouden regel

Een model is altijd **fout**

(het is immers vereenvoudigd)

<!-- .element: class="fragment" -->

Maar het kan wel **nuttig** zijn!

<!-- .element: class="fragment" -->

Notes:
"All models are wrong, but some are useful" - George Box. Het gaat erom dat je model je helpt om iets te begrijpen of te voorspellen.

---

## Waarom gebruiken we modellen?

<div class="columns">
<div class="fragment" style="text-align: left">

**Beschrijven**
- Hoe ziet het systeem eruit?

**Uitleggen**
- Waarom gebeurt iets?

**Experimenteren**
- Wat als...?

</div>
<div class="fragment" style="text-align: left">

**Voorspellen**
- Wat gebeurt in de toekomst?

**Communiceren**
- Hoe leg ik iets uit?

</div>
</div>

Notes:
Modellen zijn krachtig omdat je dingen kunt testen die in het echt te gevaarlijk, te duur of onmogelijk zijn. Denk aan: pandemie, evacuatie, verkeerssysteem, klimaat...

***

## Groepsopdracht: Modelleren

Kies een fenomeen:
1. Mensen in een drukke trein
2. Auto's op een parkeerplaats
3. Klanten in een supermarkt

Bespreek in je groep (5 minuten):
- Wat is WEL belangrijk om te modelleren?
- Wat is NIET belangrijk?

Notes:
Laat groepen hun keuzes delen. Let op de overwegingen: waarom is iets belangrijk? Hangt af van de vraag die je wilt beantwoorden!

***

## Agent-Based Modeling

In deze module werken we met **agents**

Een agent kan van alles zijn:
- Een persoon
- Een auto
- Een mier
- Een bloedcel

<!-- .element: class="fragment" -->

Notes:
ABM = Agent-Based Modeling. Je bouwt een model door individuele entiteiten (agents) te simuleren die regels volgen.

---

## Wat maakt iets een agent?

**1. Agents hebben eigenschappen**

Voorbeeld: een persoon heeft `leeftijd`, `besmet?`, `energie`

<!-- .element: class="fragment" -->

**2. Agents hebben gedrag**

Voorbeeld: `beweeg-naar-doel`, `besmet-anderen`, `zoek-voedsel`

<!-- .element: class="fragment" -->

**3. Agents reageren op hun omgeving**

Voorbeeld: ga naar rechts als de uitgang daar is

<!-- .element: class="fragment" -->

---

## Het conceptueel model

Vijf vragen om een fenomeen te modelleren:

1. Wat zijn de **agents**?
2. Welke **eigenschappen** hebben ze?
3. Welk **gedrag** vertonen ze?
4. In welke **omgeving** opereren ze?
5. Hoe **reageren** ze op elkaar en de omgeving?

Notes:
Dit stappenplan gaan jullie de komende weken veel gebruiken. Het helpt je om systematisch van een fenomeen naar een model te gaan.

---

## Voorbeeld: Virus-verspreiding

**1. Agents:** Individuele mensen

**2. Eigenschappen:** `besmet?`, `immuun?`, `positie-x`, `positie-y`

**3. Gedrag:** Beweeg willekeurig; als besmet, besmet je buren; na 5 dagen word je immuun

**4. Omgeving:** 2D-wereld waar mensen rondlopen

**5. Interactie:** Besmetting vindt plaats bij nabijheid

<!-- .element: class="fragment" -->

Notes:
Dit is een simpel maar krachtig model. Let op: elke agent besluit zelf wat hij doet op basis van zijn regels. Er is geen "baas" die alles aanstuurt.

---

## Belangrijk: Autonoom

Agents zijn **autonoom**: ze beslissen zelf wat ze doen

Geen centrale "regisseur"

<!-- .element: class="fragment" -->

Dit is anders dan traditionele modellen met één grote formule

<!-- .element: class="fragment" -->

***

## Emergent gedrag

Het gedrag van het **systeem als geheel**

dat **niet** expliciet is geprogrammeerd

<!-- .element: class="fragment" -->

maar **ontstaat** door interacties tussen agents

<!-- .element: class="fragment" -->

Notes:
Dit is het échte magische van ABM. Je programmeert simpele regels, maar er ontstaat complex groepsgedrag dat je niet had voorzien.

---

## Voorbeeld 1: Mieren zoeken voedsel

<div class="columns">
<div>

**Simpele regels per mier:**

1. Beweeg willekeurig
2. Vind je voedsel? Pak op, loop naar nest
3. Leg een geurspoor achter
4. Ruik je een spoor? Loop die kant op

</div>
<div class="fragment">

**Emergent resultaat:**

Een "snelweg" van mieren tussen nest en voedsel

Zonder dat er een "baas-mier" is!

</div>
</div>

Notes:
Individuele mieren zijn dom. Ze hebben geen kaart, geen plan. Maar samen zijn ze efficiënt. Het pad ontstaat vanzelf doordat mieren elkaar versterken via het geurspoor.

---

## Voorbeeld 2: Mexican wave

<div class="columns">
<div>

**Simpele regels per persoon:**

1. Als je buurman opstaat, wacht 1 seconde
2. Sta op en blijf 2 seconden staan
3. Ga zitten

</div>
<div class="fragment">

**Emergent resultaat:**

Een prachtige golf door het stadion

Zonder regisseur!

</div>
</div>

Notes:
Niemand heeft de golf geprogrammeerd. Elke persoon reageert alleen op zijn directe buurman. Maar van bovenaf zie je een complex patroon. Dat is emergent gedrag.

---

## Herken emergent gedrag

Vraag jezelf af:

*"Staat dit gedrag in de regels van één agent?"*

<!-- .element: class="fragment" -->

- Nee, maar het gebeurt wel? → **Emergent!**
- Ja? → Niet emergent

<!-- .element: class="fragment" -->

Notes:
Een mier die willekeurig beweegt = niet emergent (staat in haar regel)
Een pad dat mieren vormen = emergent (staat nergens, ontstaat vanzelf)

---

## Voorbeeld 3: Schelling segregatie

Thomas Schelling (jaren '70): simulatie van mensen in een stad

**Regel per persoon:** minimaal 60% van je buren moet je eigen groep zijn

<!-- .element: class="fragment" -->

**Verrassend resultaat:** Sterke segregatie in wijken

<!-- .element: class="fragment" -->

Niemand wilde dat, maar het gebeurde toch!

<!-- .element: class="fragment" -->

Notes:
Dit is krachtig: je ziet patronen ontstaan die je niet verwachtte. Met ABM kun je dit soort vragen onderzoeken: wat gebeurt er als we de tolerantie verhogen? Wat als mensen liever diversiteit willen?

***

## Samenvatting tot nu toe

**Model:** Vereenvoudigde weergave van de werkelijkheid

**Agent:** Entiteit met eigenschappen, gedrag en autonomie

**Emergent gedrag:** Complex groepsgedrag dat ontstaat uit simpele regels

**ABM:** Agent-Based Modeling

Notes:
Dit zijn de kernbegrippen die je nu kent. We gaan ze nu in actie zien in NetLogo!

***

## Demo tijd: NetLogo

Laten we een paar modellen bekijken

Notes:
Laat 2-3 modellen zien:
1. Virus spread (simpel, zie besmetting ontstaan)
2. Ants (zie paden ontstaan)
3. Segregation (zie wijken ontstaan)

Laat studenten parameters aanpassen en het effect zien.

---

## NetLogo

<div class="columns">
<div>

**Gratis tool** voor Agent-Based Modeling

Speciaal ontworpen voor onderwijs

Bibliotheek met 100+ voorbeeldmodellen

</div>
<div class="fragment">

**Twee versies:**

- Desktop (download)
- Web (online, geen installatie)

[netlogoweb.org](https://www.netlogoweb.org)

</div>
</div>

Notes:
NetLogo is dé standaard voor ABM in het onderwijs. Makkelijk te leren, maar krachtig genoeg voor serieus onderzoek.

---

## Jullie beurt!

Open NetLogo (web of desktop)

Zoek het **Virus** model (Biology → Virus)

<!-- .element: class="fragment" -->

Druk op **Setup**, dan **Go**

<!-- .element: class="fragment" -->

Experimenteer met de sliders!

<!-- .element: class="fragment" -->

Notes:
Laat studenten 5-10 minuten experimenteren. Loop rond, help waar nodig. Laat ze ontdekken:
- Wat gebeurt er als je infectiosity verhoogt?
- Wat als duration korter is?
- Kan je het virus uitroeien?

***

## Afsluitingsquiz

Tijd om te checken wat je hebt geleerd!

---

Wat is een model?

- Een perfecte kopie van de werkelijkheid
- Een vereenvoudigde weergave van de werkelijkheid
- Een foto van een systeem
- Een computer programma

<!-- .element: class="mc" -->

Notes:
Antwoord: Een vereenvoudigde weergave van de werkelijkheid. Dat is de definitie!

---

Wat is emergent gedrag?

- Gedrag dat je expliciet programmeert
- Gedrag van één agent
- Groepsgedrag dat ontstaat uit simpele regels
- Foutief gedrag in je model

<!-- .element: class="mc" -->

Notes:
Antwoord: Groepsgedrag dat ontstaat uit simpele regels. Het is niet geprogrammeerd, maar ontstaat vanzelf door interacties.

---

Een mier legt een geurspoor achter. Is dit emergent gedrag?

- Ja, want het is complex
- Nee, want het staat in de regel van die mier
- Ja, want andere mieren volgen het
- Nee, want het is te simpel

<!-- .element: class="mc" -->

Notes:
Antwoord: Nee, want het staat in de regel van die mier. Dit is gedrag van één agent. Het PAD dat ontstaat is wel emergent!

---

Wat zijn de drie kenmerken van een agent?

- Groot, klein, snel
- Eigenschappen, gedrag, autonomie
- Kleur, vorm, positie
- Code, regels, variabelen

<!-- .element: class="mc" -->

Notes:
Antwoord: Eigenschappen, gedrag, autonomie. Agents hebben eigenschappen (variabelen), gedrag (acties), en reageren autonoom op hun omgeving.

---

## Goed gedaan!

Je kent nu:
- Wat modellen zijn en waarom we ze gebruiken
- Wat agents zijn
- Wat emergent gedrag is
- Hoe NetLogo werkt

<!-- .element: class="fragment" -->

***

## Huiswerk voor volgende week

**1. Lees hoofdstuk 1 in de syllabus** (Modellen en emergent gedrag)

**2. Schrijf een korte reflectie (250 woorden):**
- Welk fenomeen met emergent gedrag vind jij interessant?
- Waarom?
- Welke agents zou je kunnen gebruiken?

**3. Exploreer NetLogo** - probeer 2-3 modellen uit de bibliotheek

Notes:
Dit is jullie voorbereiding. Volgende week gaan we dieper in op hoe je van een fenomeen naar een conceptueel model komt.

---

## Syllabus

Check de syllabus voor:
- Planning van de 7 weken
- Alle hoofdstukken
- Eindopdracht criteria
- Deadlines

Notes:
Zet de syllabus in je favorieten. Alles wat je nodig hebt staat daar.

---

## Volgende week

Fysieke bijeenkomst

Van fenomeen naar conceptueel model

<!-- .element: class="fragment" -->

Neem je **opgeladen** laptop mee met NetLogo geïnstalleerd!

<!-- .element: class="fragment" -->

Notes:
Zorg dat NetLogo werkt voordat je komt. Test het deze week!
