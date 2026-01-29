<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #27ae60, #ffffff)" -->

# Computational Science

Q-highschool / Bijeenkomst 2

Notes:
Welkom bij de tweede bijeenkomst! Vandaag gaan we van fenomenen naar concrete conceptuele modellen. Jullie hebben allemaal een reflectie geschreven over een interessant fenomeen - daar gaan we mee aan de slag.

---

## Vandaag

- Bespreking huiswerk bijeenkomst 1
- Van fenomeen naar conceptueel model
- Stappenplan voor modelleren
- Groepsopdracht: ontwerp je eigen model
- Peer feedback

Notes:
Fysieke bijeenkomst - we gaan veel samenwerken en elkaar feedback geven. Zorg dat je laptop en NetLogo werken!

***

## Check-in: huiswerk

Wat was de opdracht?

1. Lees hoofdstuk 1
2. Reflectie (250 woorden): interessant fenomeen
3. Exploreer 2-3 NetLogo modellen

<!-- .element: class="fragment" -->

Wie heeft alles gedaan?

<!-- .element: class="fragment" -->

Notes:
Poll de klas. Vraag wie heeft gelezen, wie heeft reflectie ingeleverd, wie heeft NetLogo uitgeprobeerd. Dit geeft gevoel voor betrokkenheid.

---

## Reflecties: fenomenen

Wat voor fenomenen hebben jullie gekozen?

Notes:
Laat 3-4 studenten hun gekozen fenomeen in 1 minuut pitchen. Schrijf ze op het bord. Voorbeelden kunnen zijn: voetgangers op straat, vis-scholen, verkeer, crowdfunding, epidemieën, marktdynamiek, evacuaties, etc.

Vraag: "Waarom is dit interessant voor jou?"

---

## NetLogo ervaring

Welke modellen heb je uitgeprobeerd?

Wat viel je op?

<!-- .element: class="fragment" -->

Wat was verrassend?

<!-- .element: class="fragment" -->

Notes:
Laat studenten kort delen wat ze hebben ontdekt. Typische antwoorden:
- "Ik zag patronen die ik niet verwachtte"
- "Kleine veranderingen in parameters hadden grote effecten"
- "Het was moeilijk te voorspellen wat er zou gebeuren"

Dit zijn perfecte bruggetjes naar emergent gedrag!

---

## Veelgemaakte misvattingen

Laten we een paar dingen rechtzetten

Notes:
Dit is het moment om misvattingen uit hoofdstuk 1 te adresseren. Vraag studenten wat ze lastig vonden.

---

## Misvatting 1

"Een agent weet wat er in het hele systeem gebeurt"

<!-- .element: class="fragment" -->

**Nee!** Agents zijn **lokaal**

Een mier weet niet waar het nest is, alleen of ze een spoor ruikt

<!-- .element: class="fragment" -->

Notes:
Dit is cruciaal. Agents hebben beperkte informatie - alleen wat ze direct waarnemen. Dit is anders dan traditionele modellen waar je alles overziet.

---

## Misvatting 2

"Emergent gedrag = gedrag van één agent"

<!-- .element: class="fragment" -->

**Nee!** Emergent gedrag ontstaat op **systeemniveau**

Het staat niet in de regels van één agent

<!-- .element: class="fragment" -->

Notes:
Een mier die beweegt = niet emergent
Een pad dat mieren maken = wel emergent

Vraag: "Kan iemand een voorbeeld geven uit hun gekozen fenomeen?"

---

## Misvatting 3

"Een goed model moet zo gedetailleerd mogelijk zijn"

<!-- .element: class="fragment" -->

**Nee!** Een goed model is zo **eenvoudig als mogelijk**

Voor de vraag die je wilt beantwoorden

<!-- .element: class="fragment" -->

Notes:
Herhaal de gouden regel: "All models are wrong, but some are useful". Je moet bewust versimpelen.

***

## Van fenomeen naar model

Hoe ga je van een idee naar een werkend model?

Daar hebben we een **stappenplan** voor

<!-- .element: class="fragment" -->

Notes:
Dit is de kern van vandaag. Jullie gaan dit stappenplan toepassen op jullie eigen gekozen fenomeen.

---

## De 5 vragen van een conceptueel model

1. Wat zijn de **agents**?
2. Welke **eigenschappen** hebben ze?
3. Welk **gedrag** vertonen ze?
4. In welke **omgeving** opereren ze?
5. Hoe **reageren** ze op elkaar en de omgeving?

Notes:
Deze vragen heb je vorige week al gezien. Nu gaan we ze systematisch toepassen. Schrijf ze op het bord of projecteer ze - studenten gaan ze de hele dag gebruiken.

---

## Voorbeeld uitwerken: Voetgangers op een zebrapad

Laten we dit samen doen

Notes:
Kies een simpel, herkenbaar voorbeeld. Werk het stap voor stap uit met input van de klas.

---

## Vraag 1: Agents?

Wat zijn de agents in ons model?

Notes:
Laat studenten roepen. Antwoord: individuele voetgangers en auto's.

Waarschuw: begin simpel! Niet meteen "fietsen, trams, honden, politie". Focus op de kern.

---

**Agents:** Voetgangers en auto's

<!-- .element: class="fragment" -->

Simpel beginnen!

<!-- .element: class="fragment" -->

(Later kun je altijd uitbreiden)

<!-- .element: class="fragment" -->

---

## Vraag 2: Eigenschappen?

Welke eigenschappen hebben deze agents?

Notes:
Laat studenten brainstormen. Schrijf suggesties op. Dan: welke zijn ECHT nodig?

Voorbeelden eigenschappen:
- Voetganger: positie, snelheid, wil-oversteken?
- Auto: positie, snelheid, gestopt?

Niet nodig: kleur haar, favoriete muziek, humeur (tenzij je specifiek gedrag daarvan wilt modelleren!)

---

**Voetganger:**
- Positie (x, y)
- Snelheid
- `wil-oversteken?` (waar/onwaar)

<!-- .element: class="fragment" -->

**Auto:**
- Positie (x, y)
- Snelheid
- `gestopt?` (waar/onwaar)

<!-- .element: class="fragment" -->

---

## Vraag 3: Gedrag?

Wat kunnen de agents **doen**?

Notes:
Dit zijn acties/procedures. Laat studenten roepen.

---

**Voetganger:**
- Beweeg naar zebrapad
- Check of auto's stoppen
- Steek over (of wacht)

<!-- .element: class="fragment" -->

**Auto:**
- Rijd vooruit
- Rem als voetganger bij zebrapad
- Versnel weer na doorgang

<!-- .element: class="fragment" -->

---

## Vraag 4: Omgeving?

Waar speelt dit zich af?

Notes:
Dit is de "wereld" waarin agents leven. In NetLogo vaak een grid, maar kan ook continue ruimte zijn.

---

**Omgeving:**

Een weg met een zebrapad

Mogelijk: verkeerslichten, stoep

<!-- .element: class="fragment" -->

In NetLogo: een 2D-grid met wegvakken en zebrapad-vakken

<!-- .element: class="fragment" -->

Notes:
Belangrijk: de omgeving kan eigenschappen hebben! Bijv. een vakje kan "zebrapad" of "weg" zijn.

---

## Vraag 5: Interacties?

Hoe reageren agents op elkaar en de omgeving?

Notes:
Dit is vaak het interessantste deel. Hier komen de regels die leiden tot emergent gedrag.

---

**Interacties:**

- Auto ziet voetganger → remt
- Voetganger ziet gestopte auto → steekt over
- Auto ziet geen voetganger meer → versnelt

<!-- .element: class="fragment" -->

**Emergent gedrag:** File kan ontstaan als veel voetgangers oversteken

<!-- .element: class="fragment" -->

Notes:
Het emergente gedrag is NIET geprogrammeerd - het ontstaat uit de regels van individuele agents. Dit is de magie!

---

## Samenvatting: conceptueel model zebrapad

| Vraag | Antwoord |
|-------|----------|
| Agents | Voetgangers, auto's |
| Eigenschappen | Positie, snelheid, wil-oversteken?, gestopt? |
| Gedrag | Beweeg, check, steek-over, rem, versnel |
| Omgeving | 2D-grid met weg en zebrapad |
| Interacties | Auto reageert op voetganger, voetganger op auto |

Notes:
Dit is een compleet conceptueel model. Nog niet geprogrammeerd, maar wel concreet genoeg om te gaan bouwen in NetLogo.

***

## Jullie beurt: groepsopdracht

**Tijd:** 30 minuten

**Groepjes:** 2-3 personen

**Opdracht:** Werk de 5 vragen uit voor één van jullie gekozen fenomenen

<!-- .element: class="fragment" -->

Notes:
Verdeel de klas in groepjes. Laat ze kiezen wiens fenomeen ze uitwerken (mag ook een nieuw fenomeen als ze het eens worden).

Loop rond en help waar nodig. Typische vragen: "Is dit detail belangrijk?" → Vraag terug: "Hangt af van je onderzoeksvraag - wat wil je weten?"

---

## Tips voor de groepsopdracht

1. **Begin simpel** - je kunt altijd later uitbreiden
2. **Focus op de kern** - wat is echt nodig voor je vraag?
3. **Denk na over emergent gedrag** - wat zou er kunnen ontstaan?
4. **Gebruik voorbeelden** - denk aan concrete situaties

Notes:
Zet deze tips op het scherm tijdens de groepsopdracht. Studenten kunnen hiernaar terugverwijzen.

---

## Tijdens het werken

Gebruik dit sjabloon:

```
FENOMEEN: [beschrijf in 1 zin]

1. AGENTS: [wie/wat?]
2. EIGENSCHAPPEN: [per agent-type]
3. GEDRAG: [wat kunnen ze doen?]
4. OMGEVING: [waar speelt het?]
5. INTERACTIES: [hoe reageren ze?]

VERWACHT EMERGENT GEDRAG: [wat zou kunnen ontstaan?]
```

Notes:
Dit sjabloon kunnen ze invullen op papier of laptop. Zorg dat iedereen het heeft.

---

## Tijd om te werken!

**30 minuten**

Start nu!

<!-- .element: class="fragment" -->

Notes:
Zet een timer. Loop actief rond, stel vragen, help groepjes die vastlopen. Luister mee bij discussies - vaak interessante inzichten!

Typische hulp:
- "Te complex? Schrap details die niet nodig zijn"
- "Te vaag? Maak het concreter met voorbeelden"
- "Wat is je onderzoeksvraag precies?"

***

## Presentaties

Elke groep: **3 minuten**

Presenteer je conceptuele model

<!-- .element: class="fragment" -->

Anderen: stel **1 kritische vraag**

<!-- .element: class="fragment" -->

Notes:
Laat groepen naar voren komen (of vanaf hun plek presenteren). Moedig vragen aan - dit is hoe je leert kritisch naar modellen te kijken.

Typische vragen:
- "Waarom heb je X eigenschap niet meegenomen?"
- "Hoe weet een agent Y?"
- "Wat gebeurt er als...?"

---

## Presentatie checklist

Vertel ons:

1. Welk **fenomeen** modeleer je?
2. Wat zijn je **agents**?
3. Belangrijkste **eigenschappen** en **gedrag**?
4. Welk **emergent gedrag** verwacht je?

Notes:
Dit houdt presentaties gestructureerd en beknopt. Focus op de kern.

---

## Groep 1

Ga je gang!

Notes:
Laat eerste groep presenteren. Applaus na afloop. Vraag wie een vraag heeft. Faciliteer discussie, maar houd het kort (max 2 minuten vragen).

---

## Groep 2

<!-- Herhaal voor elk groepje -->

---

## Groep 3

---

## Groep 4

---

## Groep 5

---

## Groep 6

Notes:
Pas het aantal slides aan op basis van je klasgrootte. Voor elke groep: korte presentatie + 1-2 vragen.

***

## Peer feedback ronde

Nu gaan we elkaar **scherper** maken

**Doel:** Help elkaar om modellen beter te maken

<!-- .element: class="fragment" -->

Notes:
Peer feedback is krachtig. Leg uit: dit is niet kritiek om te kraken, maar om elkaar te helpen sterker te worden.

---

## Feedback geven: WWWH methode

**W**at werkt er goed?

**W**at zou beter kunnen?

**W**at mis je nog?

**H**oe zou je het aanpakken?

<!-- .element: class="fragment" -->

Notes:
WWWH = What works, What's missing, What to improve, How to do it.

Moedig constructieve feedback aan: begin met iets positiefs, dan verbeterpunten.

---

## Opdracht: feedback exchange

**15 minuten**

1. Wissel je model uit met een ander groepje
2. Lees hun model kritisch
3. Geef feedback via WWWH
4. Ontvang feedback op jouw model

<!-- .element: class="fragment" -->

Notes:
Laat groepjes wisselen (bijv. groep 1 ↔ groep 2, groep 3 ↔ groep 4, etc.). Ze kunnen feedback opschrijven of mondeling geven.

Loop rond, help faciliteren. Moedig kritische vragen aan:
- "Hoe weet een agent dat?"
- "Wat als er 1000 agents zijn in plaats van 10?"
- "Hebben ze dit detail echt nodig?"

---

## Veelvoorkomende feedback punten

**Te complex:** Probeer te versimpelen

**Te vaag:** Maak eigenschappen concreter

**Onduidelijke interacties:** Beschrijf stap-voor-stap wat er gebeurt

**Geen emergent gedrag:** Wat zou er kunnen ontstaan uit deze regels?

<!-- .element: class="fragment" -->

Notes:
Dit zijn patronen die je vaak ziet. Gebruik ze als hulpmiddel tijdens feedback geven.

---

## Start feedback sessie!

**15 minuten**

Notes:
Zet timer. Studenten wisselen modellen en geven elkaar feedback. Faciliteer actief.

***

## Reflectie: wat hebben we geleerd?

Wat was **moeilijk** aan het maken van een conceptueel model?

<!-- .element: class="fragment" -->

Wat was **verrassend**?

<!-- .element: class="fragment" -->

Notes:
Open discussie. Typische antwoorden:
- "Kiezen wat belangrijk is en wat niet"
- "Concreet maken zonder te complex te worden"
- "Bedenken hoe agents lokaal beslissen zonder alles te weten"
- "Voorspellen wat emergent gedrag zou zijn"

---

## Veelvoorkomende uitdagingen

**Detailniveau:** Hoeveel detail is genoeg?

→ Vraag jezelf af: heb ik dit nodig voor mijn onderzoeksvraag?

<!-- .element: class="fragment" -->

**Emergent vs. geprogrammeerd:** Zit het in één agent of ontstaat het?

→ Test: staat dit gedrag in de regels van één agent? Zo ja → niet emergent

<!-- .element: class="fragment" -->

**Lokaliteit:** Hoe weet een agent iets?

→ Agents kennen alleen hun directe omgeving en eigenschappen

<!-- .element: class="fragment" -->

Notes:
Dit zijn de drie grote uitdagingen waar iedereen tegenaan loopt. Normaal en belangrijk om te herkennen!

***

## Van conceptueel model naar code

Volgende stap: **NetLogo programmeren**

Volgende week gaan we jullie conceptuele modellen **bouwen**

<!-- .element: class="fragment" -->

Notes:
Maak een brug naar week 3. Het conceptuele model dat ze vandaag hebben gemaakt, wordt volgende week code.

---

## Wat je nodig hebt

- Je conceptuele model (van vandaag)
- NetLogo geïnstalleerd en werkend
- Hoofdstuk 3 gelezen (NetLogo basics)

<!-- .element: class="fragment" -->

Notes:
Dit is essentiële voorbereiding voor volgende week. Zonder werkende NetLogo komen ze nergens.

***

## Quiz: check je begrip

Tijd om te testen wat je hebt geleerd!

---

Wat is de eerste vraag van een conceptueel model?

- Hoe programmeer ik dit?
- Wat zijn de agents?
- Welk emergent gedrag ontstaat er?
- In welke taal schrijf ik code?

<!-- .element: class="mc" -->

Notes:
Antwoord: Wat zijn de agents? Dit is altijd het startpunt.

---

Een voetganger heeft eigenschap "lievelingskleur". Is dit relevant voor een evacuatie-model?

- Ja, want het maakt het model realistischer
- Nee, want het beïnvloedt het gedrag niet
- Ja, want alle eigenschappen zijn belangrijk
- Nee, want het is te moeilijk te programmeren

<!-- .element: class="mc" -->

Notes:
Antwoord: Nee, want het beïnvloedt het gedrag niet. Irrelevante details maken je model alleen maar complexer zonder meerwaarde.

---

Welke vraag hoort NIET bij het conceptuele model?

- Welke eigenschappen hebben agents?
- Hoe programmeer ik een loop in NetLogo?
- Hoe reageren agents op elkaar?
- In welke omgeving opereren agents?

<!-- .element: class="mc" -->

Notes:
Antwoord: Hoe programmeer ik een loop in NetLogo? Dat is implementatie, niet conceptueel model. Het conceptuele model is taal-onafhankelijk.

---

Een file ontstaat doordat veel auto's tegelijk remmen. Is dit emergent gedrag?

- Ja, want niemand wilde een file
- Nee, want elke auto remt individueel
- Ja, want het ontstaat uit individuele regels
- Nee, want files zijn geprogrammeerd

<!-- .element: class="mc" -->

Notes:
Antwoord: Ja, want het ontstaat uit individuele regels. Elke auto doet iets simpels (remmen als voorganger remt), maar het groepspatroon (file) is emergent.

---

## Goed gedaan!

Je weet nu:

- Hoe je een fenomeen vertaalt naar een conceptueel model
- De 5 kernvragen van conceptualisatie
- Hoe je feedback geeft en ontvangt
- Het verschil tussen lokaal en globaal gedrag

<!-- .element: class="fragment" -->

***

## Huiswerk voor volgende week

**1. Verfijn je conceptueel model** op basis van de feedback

**2. Lees hoofdstuk 3** (NetLogo basis: wereld, patches, turtles)

**3. Doe de NetLogo tutorial** (File → Models Library → Tutorial 1, 2, 3)

**4. Lever in:** Je definitieve conceptuele model (gebruik het sjabloon)

<!-- .element: class="fragment" -->

Notes:
Dit is serieuze voorbereiding. Zonder dit komen ze niet mee volgende week wanneer we gaan programmeren.

---

## Deadline inleveren

**Voor aanvang volgende bijeenkomst**

Format: PDF of Markdown, upload naar de inlevermap

Gebruik het sjabloon van vandaag

<!-- .element: class="fragment" -->

Notes:
Wees streng op deadline - ze hebben dit nodig voor volgende week. Zonder conceptueel model kunnen ze niet gaan bouwen.

---

## Checklist voor je inlevering

- [ ] Fenomeen helder beschreven (2-3 zinnen)
- [ ] Alle 5 vragen beantwoord
- [ ] Eigenschappen zijn concreet (geen vage termen)
- [ ] Gedrag is beschreven in acties
- [ ] Interacties zijn expliciet gemaakt
- [ ] Verwacht emergent gedrag benoemd

Notes:
Laat studenten deze checklist gebruiken voordat ze inleveren. Voorkomt onvolledige inleveringen.

---

## Tips voor thuiswerken

**Conceptueel model verfijnen:**
- Lees de feedback nog eens door
- Schrap onnodige details
- Maak vage begrippen concreet
- Test: kan iemand anders dit begrijpen?

Notes:
Moedig aan om kritisch naar eigen werk te kijken. Een goed conceptueel model is helder en minimaal.

---

## NetLogo tutorial

**Waarom is dit belangrijk?**

Je leert:
- Hoe de interface werkt
- Basis commando's
- Hoe je agents aanmaakt en bestuurt

<!-- .element: class="fragment" -->

Zonder dit kun je volgende week niet meedoen!

<!-- .element: class="fragment" -->

Notes:
De tutorial in NetLogo is interactief en heel goed. Studenten moeten dit echt doen.

Waarschuw: "Het kost 1-2 uur, maar het is essentieel."

***

## Volgende week

**Fysieke bijeenkomst**

Hands-on: bouw je eerste NetLogo model

<!-- .element: class="fragment" -->

Neem mee:
- Opgeladen laptop
- NetLogo werkend
- Je conceptueel model
- Hoofdstuk 3 gelezen

<!-- .element: class="fragment" -->

Notes:
Herhaal: zonder werkende NetLogo en conceptueel model kunnen ze niet meedoen. Zorg dat ze dit weten.

---

## Tot volgende week!

Vragen?

Notes:
Open de vloer voor laatste vragen. Bedank iedereen voor de actieve deelname. Veel succes met het huiswerk!

---

<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #27ae60, #ffffff)" -->

## Bedankt!

En veel succes met het huiswerk

Notes:
Einde van de bijeenkomst. Zorg dat je beschikbaar blijft voor 1-op-1 vragen na afloop.
