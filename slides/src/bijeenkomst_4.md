<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #3498db, #ffffff)" -->

# Emergent Gedrag Bouwen

Q-highschool / Bijeenkomst 4

Notes:
Welkom! Vandaag kort klassikaal moment, daarna vooral zelfstandig werken aan jullie eindopdracht.

---

## Vandaag

**20 min:** Klassikaal
- Quiz: terugblik op H1-3
- Show-and-tell: emergent gedrag bouwen

**70 min:** Zelfstandig werken
- Iedereen op eigen tempo aan eindopdracht

Notes:
Kort maar krachtig klassikaal moment, daarna de ruimte om te werken aan wat JIJ nodig hebt.

***

## Quiz: Terugblik

Tijd om te checken wat je hebt onthouden!

---

Wat is emergent gedrag?

- Gedrag dat je expliciet programmeert
- Complex groepsgedrag uit simpele regels
- Fouten in je model
- Het gedrag van één agent

<!-- .element: class="mc" -->

Notes:
Antwoord: Complex groepsgedrag uit simpele regels. Dit is de kern van ABM!

---

Welke procedure roep je één keer aan, aan het begin?

- `go`
- `setup`
- `tick`
- `create`

<!-- .element: class="mc" -->

Notes:
Antwoord: setup. Deze maakt je wereld klaar. Go roep je herhaaldelijk aan.

---

Wat doet `tick` in je code?

- Maakt nieuwe turtles
- Verhoogt de tijdsteller met 1
- Beweegt alle agents
- Reset het model

<!-- .element: class="mc" -->

Notes:
Antwoord: Verhoogt de tijdsteller met 1. Vergeet je tick? Dan werken plots niet en staat de tijd stil!

---

Wat is het verschil tussen turtles en patches?

- Turtles bewegen, patches niet
- Patches zijn rood, turtles blauw
- Turtles zijn groot, patches klein
- Geen verschil

<!-- .element: class="mc" -->

Notes:
Antwoord: Turtles bewegen, patches niet. Turtles zijn agents, patches zijn de omgeving (het grid).

---

Hoe maak je 100 turtles in setup?

- `make-turtles 100`
- `create-turtles 100`
- `new turtles [100]`
- `turtles = 100`

<!-- .element: class="mc" -->

Notes:
Antwoord: create-turtles 100. Dit is de NetLogo syntax.

---

Wat is een goede onderzoeksvraag voor ABM?

- "Hoe werkt een virus?"
- "Is evacuatie gevaarlijk?"
- "Hoe beïnvloedt uitgang-breedte de evacuatietijd?"
- "Waarom bewegen mensen?"

<!-- .element: class="mc" -->

Notes:
Antwoord: "Hoe beïnvloedt uitgang-breedte de evacuatietijd?" - Specifiek, meetbaar, beantwoordbaar met een model.

---

## Goed gedaan!

Je hebt de basis goed zitten

Nu gaan we kijken naar **emergent gedrag bouwen**

<!-- .element: class="fragment" -->

Notes:
Deze quiz toont aan: je kent de concepten. Nu tijd om ze toe te passen!

***

## Emergent Gedrag Bouwen

Van regels naar patronen

---

## Het doel bepalen

**Eerst helder krijgen:** Welk emergent patroon wil ik zien?

Voorbeelden:
- Mieren vormen paden
- Mexican wave loopt rond
- Vogels vliegen in formatie
- Files ontstaan en verdwijnen

<!-- .element: class="fragment" -->

Notes:
Je begint niet met code, maar met: WAT wil ik zien gebeuren? Welk groepsgedrag moet ontstaan?

---

## Twee klassieke voorbeelden

<div class="columns">
<div>

**Mieren zoeken voedsel**

Simpele regels:
- Zoek random
- Vind voedsel → ga naar nest
- Leg geurspoor
- Volg geursporen

**Emergent:** Paden ontstaan!

</div>
<div class="fragment">

**Mexican Wave**

Simpele regels:
- Zie buurman opstaan
- Wacht 1 seconde
- Sta 2 seconden
- Ga zitten

**Emergent:** Golf door stadion!

</div>
</div>

Notes:
Beide: geen centrale sturing, geen agent die het "organiseert". Het patroon ontstaat vanzelf uit lokale regels.

---

## Stapsgewijs bouwen

❌ Niet: Alles in één keer programmeren

✅ Wel: Incrementeel opbouwen

<!-- .element: class="fragment" -->

1. Basis (agents plaatsen)
2. Simpel gedrag (random bewegen)
3. Eerste regel (vind voedsel)
4. Tweede regel (ga terug)
5. Interactie (geurspoor)
6. Verfijning (verdamping)

<!-- .element: class="fragment" -->

Notes:
Elke stap test je! Werkt stap 2? Dan pas naar stap 3. Zo vind je fouten makkelijk en bouw je robuuste code.

---

## Parameters om mee te experimenteren

Niet alleen bouwen, ook **experimenteren**!

Voorbeelden sliders:
- Aantal agents
- Verdampingssnelheid geurspoor
- Reactiesnelheid
- Sight-radius (hoe ver kijken agents?)

<!-- .element: class="fragment" -->

Notes:
Parameters zijn de knoppen waar je aan draait. Dit maakt je model interessant: wat gebeurt er als ik X verander?

---

## Het patroon verklaren

Als je model werkt, vraag jezelf af:

**Waarom ontstaat dit patroon?**

Leg uit met de regels:
- Mieren versterken elkaar via sporen
- Meer mieren → sterker spoor → nóg meer mieren
- **Positieve feedback loop**

<!-- .element: class="fragment" -->

Notes:
Dit is het verschil tussen "ik heb code" en "ik begrijp mijn model". Je moet kunnen uitleggen WAAROM het patroon ontstaat.

***

## Zelfstandig Werken

<div class="columns" style="grid-template-columns: 1fr 1fr 1fr; text-align: left; align-items: top, center; font-size: 0.4em;" >
<div style="border: 1px solid black; background-color: lightgray; padding-left: 10px; margin-right: 10px;">

**Opdracht:**

70 minuten voor je eindopdracht

Iedereen werkt op eigen tempo

Ik ben beschikbaar voor vragen
</div>
<div>

**Check voor jezelf:**

**Nog bij H1-2?** Conceptueel model afmaken

**H3-4?** NetLogo model bouwen

**H5?** Experimenten draaien

**H6?** Verslag schrijven
</div>
<div>

**Tips voor effectief werken:**

**Test regelmatig** - Na elke kleine wijziging

**Sla op met versies** - model-v1, model-v2, etc.

**Vraag hulp als je vastloopt** - Steek je hand op of stuur bericht
</div>

Notes:
Nu krijgen jullie de tijd om te werken aan wat JIJ nodig hebt. Sommigen werken aan conceptueel model, anderen aan NetLogo code, weer anderen aan experimenten.

***

## Terugblik!

Waar ben je trots op vandaag?

Notes:
Laat een paar studenten delen wat ze vandaag hebben bereikt. Vier de kleine overwinningen!

---

## Volgende keer

Verder werken aan je model

Experimenteren met parameters

<!-- .element: class="fragment" -->

Zorg dat je model **werkt** voordat je gaat experimenteren

<!-- .element: class="fragment" -->

Notes:
Bouw eerst een werkend model, daarna experimenteer je. Niet te snel naar de experimenten!

---

## Vragen?

&nbsp;

Notes:
Check of er nog vragen zijn voor het einde van de les.
