# Emergent gedrag bouwen: mieren of Mexican wave

Je hebt in hoofdstuk 3 geleerd hoe je turtles maakt en beweegt in NetLogo. Nu komt het échte werk: **emergent gedrag bouwen**. In dit hoofdstuk kies je één van twee klassieke ABM-voorbeelden – mieren die voedsel zoeken of een Mexican wave – en bouwt het stap voor stap. Je leert hoe simpele regels leiden tot verrassend complex groepsgedrag, hoe je parameters gebruikt om te experimenteren, en hoe je het emergente patroon zichtbaar maakt en verklaart. Aan het eind heb je een werkend model met duidelijk emergent gedrag.

**Leerdoel:** Na dit hoofdstuk kun je een compleet ABM-model bouwen dat emergent gedrag toont, parameters toevoegen om te experimenteren, en uitleggen waarom het patroon ontstaat.

## Inhoud

In dit hoofdstuk behandelen we:

- Doel: welk emergent patroon wil je zien?
- Regels stap-voor-stap implementeren
- Parameters: welke sliders zijn zinvol?
- Output: hoe maak je het zichtbaar?
- Verklaren: waarom ontstaat het patroon?
- Variaties: ruis, obstakels, sight-radius

---

## Doel: welk emergent patroon wil je zien?

Voordat je begint met programmeren, moet je helder hebben: **welk emergent gedrag wil ik zien ontstaan?**

### Optie 1: Mieren zoeken voedsel (Ant Foraging)

**Emergent patroon:** Mieren vinden voedsel en vormen spontaan **paden** tussen nest en voedsel, zonder dat er een centrale coördinator is.

**Wat je ziet:**
- Eerst: Mieren bewegen random rond (chaotisch)
- Na een tijdje: Duidelijke "snelwegen" van nest naar voedselbronnen
- Het pad wordt steeds sterker (meer mieren gebruiken het)
- Als voedsel op is, verdwijnt het pad langzaam

**Onderzoeksvraag voorbeeld:**  
"Hoe beïnvloedt de verdampingssnelheid van geursporen de efficiëntie van voedsel verzamelen?"

### Optie 2: Mexican Wave

**Emergent patroon:** Een golf van staande mensen loopt door het stadion, zonder dat iemand het stuurt. De wave kan rondgaan, splitsen, of uitdoven.

**Wat je ziet:**
- Eén persoon staat op (start)
- Buren zien dit en staan ook op (na vertraging)
- Een "golf" loopt door de rij
- De golf kan meerdere keren rondgaan of stoppen

**Onderzoeksvraag voorbeeld:**  
"Bij welke reactiesnelheid blijft de wave minimaal 3 rondes doorgaan?"

:::{tip}
**Kies op basis van interesse**  
Mieren = ruimtelijk, visueel, met omgeving (patches). Mexican wave = simpeler, 1D, goed voor eerste model. Beide tonen prachtig emergent gedrag!
:::

**Kies nu:** Ga je mieren of Mexican wave bouwen? De rest van dit hoofdstuk geeft voor beide stap-voor-stap instructies.

---

## Regels stap-voor-stap implementeren

### Optie A: Mieren zoeken voedsel

We bouwen dit in 6 stappen, van simpel naar complex.

#### Stap 1: Basis-setup (nest, mieren, voedsel)

**Doel:** Maak de wereld met een nest, mieren, en voedsel.

```scheme
patches-own [
  nest?          ; Is dit patch onderdeel van het nest?
  voedsel        ; Hoeveel voedsel ligt hier? (getal)
  geurspoor      ; Sterkte van het geurspoor (getal, 0-100)
]

to setup
  clear-all
  
  ; Maak nest in het midden
  ask patches with [distancexy 0 0 < 5] [
    set nest? true
    set pcolor yellow
  ]
  
  ; Plaats voedsel op 3 random plekken
  ask n-of 3 patches with [not nest? and distancexy 0 0 > 10] [
    set voedsel 50
    set pcolor green
  ]
  
  ; Maak rest van wereld bruin (grond)
  ask patches with [not nest? and voedsel = 0] [
    set pcolor brown
  ]
  
  ; Maak mieren op het nest
  create-turtles aantal-mieren [  ; aantal-mieren = slider
    setxy 0 0
    set color red
    set shape "bug"
  ]
  
  reset-ticks
end
```

**Test:** Klik setup. Zie je een geel nest in het midden, 3 groene voedsel-patches, en rode mieren?

#### Stap 2: Random zoekgedrag

**Doel:** Mieren bewegen random rond tot ze voedsel vinden.

```scheme
turtles-own [
  heeft-voedsel?    ; Draagt deze mier voedsel? (Boolean)
]

to go
  ask turtles [
    ifelse heeft-voedsel? [
      ; Als ik voedsel heb, ga naar nest (komt later)
      set color orange
    ] [
      ; Als ik geen voedsel heb, zoek willekeurig
      zoek-voedsel
    ]
  ]
  tick
end

to zoek-voedsel  ; Turtle procedure
  ; Beweeg iets willekeurig
  right random 60 - 30    ; Draai -30 tot +30 graden
  forward 1
  
  ; Check: sta ik op voedsel?
  if [voedsel] of patch-here > 0 [
    set heeft-voedsel? true
    ask patch-here [
      set voedsel voedsel - 1     ; Pak 1 eenheid voedsel
      if voedsel = 0 [ set pcolor brown ]  ; Als op: word bruin
    ]
  ]
end
```

**Test:** Mieren bewegen random, worden oranje als ze voedsel vinden.

#### Stap 3: Terug naar nest met voedsel

**Doel:** Mieren met voedsel gaan terug naar het nest.

```scheme
to go
  ask turtles [
    ifelse heeft-voedsel? [
      keer-terug-naar-nest
    ] [
      zoek-voedsel
    ]
  ]
  tick
end

to keer-terug-naar-nest  ; Turtle procedure
  ; Draai richting nest (0, 0)
  facexy 0 0
  forward 1
  
  ; Ben ik bij het nest?
  if [nest?] of patch-here [
    set heeft-voedsel? false
    set color red              ; Word weer rood (zoekend)
  ]
end
```

**Test:** Mieren met voedsel (oranje) lopen richting nest, worden rood als ze er zijn.

#### Stap 4: Geurspoor leggen

**Doel:** Mieren leggen een geurspoor als ze terug naar nest gaan.

```scheme
to keer-terug-naar-nest
  facexy 0 0
  forward 1
  
  ; Leg geurspoor op deze patch
  ask patch-here [
    set geurspoor min (list (geurspoor + 10) 100)  ; Max 100
    set pcolor scale-color cyan geurspoor 0 100    ; Blauw = spoor
  ]
  
  if [nest?] of patch-here [
    set heeft-voedsel? false
    set color red
  ]
end
```

**Test:** Je ziet blauwe sporen verschijnen waar mieren met voedsel lopen.

#### Stap 5: Geurspoor volgen

**Doel:** Mieren zonder voedsel volgen geursporen (liever dan random).

```scheme
to zoek-voedsel
  ; Kijk om je heen: is er een geurspoor?
  let beste-patch max-one-of patches in-radius 2 [geurspoor]
  
  ifelse [geurspoor] of beste-patch > 0 [
    ; Er is een spoor! Ga erheen
    face beste-patch
    forward 1
  ] [
    ; Geen spoor: beweeg random
    right random 60 - 30
    forward 1
  ]
  
  ; Check: voedsel?
  if [voedsel] of patch-here > 0 [
    set heeft-voedsel? true
    ask patch-here [
      set voedsel voedsel - 1
      if voedsel = 0 [ set pcolor brown ]
    ]
  ]
end
```

**Test:** Mieren volgen blauwe sporen! Je ziet paden ontstaan.

#### Stap 6: Geurspoor verdampen

**Doel:** Sporen vervagen over tijd, anders blijven ze eeuwig.

```scheme
to go
  ask turtles [
    ifelse heeft-voedsel? [
      keer-terug-naar-nest
    ] [
      zoek-voedsel
    ]
  ]
  
  ; Sporen verdampen
  verdamp-sporen
  
  tick
end

to verdamp-sporen
  ask patches with [geurspoor > 0] [
    set geurspoor geurspoor * (1 - verdampingssnelheid)  ; slider 0-0.1
    set pcolor scale-color cyan geurspoor 0 100
    if geurspoor < 0.1 [ 
      set geurspoor 0 
      if not nest? and voedsel = 0 [ set pcolor brown ]
    ]
  ]
end
```

**Klaar!** Je hebt nu een werkend mieren-model met emergent gedrag: paden ontstaan vanzelf.

[Screenshot: Mieren-model met blauwe paden tussen geel nest en groene voedsel]

---

### Optie B: Mexican Wave

We bouwen dit in 5 stappen.

#### Stap 1: Basis-setup (rij mensen)

**Doel:** Maak een rij mensen die kan opstaan en gaan zitten.

```scheme
turtles-own [
  zit-of-staat?    ; "zit" of "staat"
  timer            ; Teller voor timing
]

to setup
  clear-all
  
  ; Maak een rij van aantal-personen mensen
  create-turtles aantal-personen [  ; slider: 50-200
    set shape "person"
    set zit-of-staat? "zit"
    set color gray
    set timer 0
  ]
  
  ; Zet ze in een rij (y=0, x varieert)
  let afstand 2
  let start-x (- aantal-personen * afstand / 2)
  
  ask turtles [
    setxy (start-x + (who * afstand)) 0
  ]
  
  reset-ticks
end
```

**Test:** Je ziet een rij grijze mensen (zitten).

#### Stap 2: Handmatig opstaan en zitten

**Doel:** Mensen kunnen opstaan en gaan zitten.

```scheme
to go
  ask turtles [
    if zit-of-staat? = "staat" [
      set timer timer + 1
      
      ; Na 2 ticks: ga zitten
      if timer >= 2 [
        set zit-of-staat? "zit"
        set color gray
        set timer 0
      ]
    ]
  ]
  tick
end

; Test: maak een button "sta-op-persoon-0" met: 
; ask turtle 0 [ set zit-of-staat? "staat" set color yellow ]
```

**Test:** Als je turtle 0 laat opstaan, gaat hij na 2 ticks weer zitten.

#### Stap 3: Buurman-check

**Doel:** Als je linker-buurman staat, begin je timer.

```scheme
to go
  ask turtles [
    ifelse zit-of-staat? = "zit" [
      ; Check: staat mijn linker-buur?
      let linker-buur turtle (who - 1)
      
      if who > 0 [  ; Niet de eerste persoon
        if [zit-of-staat?] of linker-buur = "staat" [
          set timer timer + 1
          
          ; Na reactie-tijd ticks: sta op
          if timer >= reactie-tijd [  ; slider: 1-5
            set zit-of-staat? "staat"
            set color yellow
            set timer 0
          ]
        ]
      ]
    ] [
      ; Als ik sta, tel ticks
      set timer timer + 1
      if timer >= 2 [
        set zit-of-staat? "zit"
        set color gray
        set timer 0
      ]
    ]
  ]
  tick
end
```

**Test:** Laat turtle 0 opstaan → turtle 1 staat op na reactie-tijd ticks → turtle 2, etc. Golf!

#### Stap 4: Start-trigger

**Doel:** Eerste persoon staat automatisch op om de wave te starten.

```scheme
to setup
  clear-all
  create-turtles aantal-personen [
    set shape "person"
    set zit-of-staat? "zit"
    set color gray
    set timer 0
    
    ; Eerste persoon: spontane starter
    if who = 0 [
      set timer 0  ; Na 3 ticks staat hij op
    ]
  ]
  
  ; Positionering...
  reset-ticks
end

to go
  ; Eerste persoon: auto-start
  ask turtle 0 [
    if zit-of-staat? = "zit" and ticks = 3 [
      set zit-of-staat? "staat"
      set color yellow
      set timer 0
    ]
  ]
  
  ; Rest van de code...
  tick
end
```

**Test:** Na 3 ticks start turtle 0 automatisch de wave.

#### Stap 5: Rond maken (optioneel)

**Doel:** Maak het een cirkel, zodat de wave kan rondgaan.

```scheme
to go
  ask turtles [
    ifelse zit-of-staat? = "zit" [
      ; Check linker-buur (met wrap-around)
      let linker-buur-nummer ifelse-value (who = 0) 
        [aantal-personen - 1]  ; Eerste kijkt naar laatste
        [who - 1]
      
      let linker-buur turtle linker-buur-nummer
      
      if [zit-of-staat?] of linker-buur = "staat" [
        set timer timer + 1
        if timer >= reactie-tijd [
          set zit-of-staat? "staat"
          set color yellow
          set timer 0
        ]
      ]
    ] [
      ; Sta-gedrag
      set timer timer + 1
      if timer >= 2 [
        set zit-of-staat? "zit"
        set color gray
        set timer 0
      ]
    ]
  ]
  tick
end
```

**Klaar!** Je wave gaat nu rond in een cirkel. Emergent gedrag: de golf blijft zichzelf onderhouden!

[Screenshot: Mexican wave in cirkel, gele "golf" loopt rond]

:::{admonition} Let op: Edge cases
:class: warning
**Valkuil bij neighbour-checks:**  
Als je `turtle (who - 1)` aanroept bij who=0, crasht je model (er is geen turtle -1!). Gebruik altijd een check:

```scheme
if who > 0 [
  let linker-buur turtle (who - 1)
  ; ... doe iets met linker-buur
]
```

Of gebruik `ifelse-value` voor wrap-around (zie stap 5).
:::

```{exercise} Oefening (Oefenen)
:label: oef-4-1

Kies mieren óf Mexican wave. Implementeer minimaal de eerste 3 stappen (basis-setup + beweging + interactie).

Vereisten:
- Werkende `setup` en `go`
- Minimaal 3 regels geïmplementeerd
- Agents tonen visueel gedrag (kleuren veranderen, bewegen, etc.)

Test je model: zie je het begin van emergent gedrag? Noteer: wat werkt? Wat werkt nog niet?
```

---

## Parameters: welke sliders zijn zinvol?

Parameters zijn cruciaal voor experimenteren. Welke moet je toevoegen?

### Voor mieren-model

| Parameter | Min | Max | Increment | Start | Effect |
|-----------|-----|-----|-----------|-------|--------|
| `aantal-mieren` | 10 | 200 | 10 | 50 | Meer mieren = sneller voedsel vinden |
| `verdampingssnelheid` | 0 | 0.1 | 0.01 | 0.05 | Hoger = sporen vervagen snel |
| `hoeveelheid-voedsel` | 10 | 100 | 10 | 50 | Meer voedsel = langer model loopt |
| `zoekradius` | 1 | 5 | 1 | 2 | Hoe ver kunnen mieren sporen ruiken? |

**Experimenteer:**
- Hoge verdamping (0.1) → sporen verdwijnen snel, moeilijk om paden te vormen
- Lage verdamping (0.01) → sporen blijven lang, sterke paden

### Voor Mexican wave

| Parameter | Min | Max | Increment | Start | Effect |
|-----------|-----|-----|-----------|-------|--------|
| `aantal-personen` | 20 | 200 | 10 | 100 | Meer personen = langere wave |
| `reactie-tijd` | 0.5 | 5 | 0.5 | 1 | Hoger = tragere wave, kan uitdoven |
| `sta-tijd` | 1 | 5 | 1 | 2 | Hoe lang blijf je staan? |

**Experimenteer:**
- Reactie-tijd < 1 → wave blijft rondgaan (snel genoeg)
- Reactie-tijd > 2 → wave sterft uit (te traag)

:::{tip}
**Parameters koppelen aan je onderzoeksvraag**  
Kies parameters die relevant zijn voor je onderzoeksvraag. Als je vraag is "Hoe beïnvloedt verdamping de efficiëntie?", dan is `verdampingssnelheid` je belangrijkste parameter.
:::

---

## Output: hoe maak je het zichtbaar?

### Visuele output: kleuren en shapes

**Mieren:**
- Rood = zoekend
- Oranje = heeft voedsel
- Blauw = geurspoor (patches)
- Groen = voedsel (patches)
- Geel = nest (patches)

**Mexican wave:**
- Grijs = zit
- Geel = staat

### Monitors toevoegen

**Voor mieren:**

```scheme
; Monitor 1: Hoeveel voedsel is verzameld?
to-report verzameld-voedsel
  report sum [voedsel-in-nest] of patches with [nest?]
end

; Monitor 2: Gemiddelde geurspoor-sterkte
to-report gem-geurspoor
  let spoor-patches patches with [geurspoor > 0]
  ifelse any? spoor-patches [
    report mean [geurspoor] of spoor-patches
  ] [
    report 0
  ]
end

; Monitor 3: Aantal mieren met voedsel
to-report mieren-met-voedsel
  report count turtles with [heeft-voedsel?]
end
```

**Voor Mexican wave:**

```scheme
; Monitor 1: Aantal staande personen
to-report aantal-staat
  report count turtles with [zit-of-staat? = "staat"]
end

; Monitor 2: Positie van de golf (wie staat er?)
to-report golf-positie
  let staan-nu turtles with [zit-of-staat? = "staat"]
  ifelse any? staan-nu [
    report [who] of one-of staan-nu
  ] [
    report "niemand"
  ]
end

; Monitor 3: Aantal rondes (teller)
; (Dit vereist een globale variabele aantal-rondes die je verhoogt als turtle 0 weer opstaat)
```

### Plots toevoegen

**Mieren-plot: "Voedsel over tijd"**

```scheme
; Plot-pen: verzameld-voedsel
plot verzameld-voedsel

; Plot-pen: resterend-voedsel
plot sum [voedsel] of patches
```

**Mexican wave-plot: "Golf-activiteit"**

```scheme
; Plot-pen: aantal staande personen
plot aantal-staat
```

[Screenshot: Mieren-model interface met 3 monitors en 1 plot]

[Screenshot: Mexican wave interface met 2 monitors en 1 plot]

```{exercise} Oefening (Toepassen)
:label: oef-4-2

Voeg aan je model toe:

1. **2 parameters (sliders)** die zinvol zijn voor je model
2. **2 monitors** die outputs tonen
3. **1 plot** die iets over tijd toont

Experimenteer: Verander één parameter en beschrijf het effect in 3-5 zinnen. Bijvoorbeeld:
- "Als ik verdampingssnelheid verhoog van 0.05 naar 0.1, verdwijnen de paden sneller en vinden mieren minder efficiënt voedsel."

Maak een [Screenshot: jouw model met duidelijk effect] en plaats deze notitie in je document.
```

---

## Verklaren: waarom ontstaat het patroon?

Je ziet nu emergent gedrag. Maar **waarom** ontstaat het? Dit is de wetenschappelijke vraag.

### Voor mieren: Positieve feedback loop

**Mechanisme:**

1. Mier A vindt toevallig voedsel
2. Mier A legt geurspoor naar nest
3. Mier B ruikt het spoor, volgt het, vindt ook voedsel
4. Mier B versterkt het spoor (legt er ook een)
5. Meer mieren volgen → spoor wordt sterker → meer mieren volgen
6. **Positieve feedback loop** ontstaat → PAD

**Zonder centrale sturing!** Geen mier "weet" dat er een pad is. Elke mier volgt alleen lokale regels (ruik spoor → volg spoor).

**Waarom verdampen belangrijk is:**

- Zonder verdampen blijven alle sporen eeuwig
- Oude sporen naar lege plekken zouden mieren misleiden
- Verdampen zorgt ervoor dat alleen **verse, nuttige** sporen blijven

### Voor Mexican wave: Lokale coördinatie

**Mechanisme:**

1. Persoon A staat op
2. Persoon B ziet dit, wacht kort, staat ook op
3. Persoon C ziet B staan, staat ook op
4. Een golf loopt door de rij

**Waarom blijft het rondgaan?**

- Als reactie-tijd kort genoeg is, "haalt de golf zichzelf in"
- Persoon 1 is weer gaan zitten als de golf bij persoon 50 is
- Als de golf bij persoon 100 is, staat persoon 1 weer op
- Golf blijft zichzelf "voeden"

**Waarom sterft het uit bij hoge reactie-tijd?**

- Als reactie-tijd > 2 seconden, is de golf te traag
- De "energie" van de golf is op voordat hij rondkomt
- Niemand staat meer op = golf dood

:::{tip}
**Verklaren = mechanisme + geen centrale sturing**  
Goede verklaring: "Het patroon ontstaat omdat [lokale regel X] leidt tot [positieve feedback / zelfversterking / lokale coördinatie], zonder dat er een agent is die het geheel overziet."
:::

```{exercise} Oefening (Reflecteren)
:label: oef-4-3

Beantwoord in 200-300 woorden:

**Welke regel in jouw model is cruciaal voor emergentie?**

Beredeneer:
1. Welke regel creëert de feedback loop of coördinatie?
2. Wat gebeurt er als je die regel **uitschakelt**? (Test dit!)
3. Waarom is deze regel essentieel voor het emergente patroon?

```

---

## Variaties: ruis, obstakels, sight-radius

Je hebt nu een werkend basis-model. Tijd om te experimenteren met **variaties**!

### Variatie 1: Ruis (willekeurige fouten)

**Idee:** Agents volgen niet altijd perfect de regels. Ze maken soms "fouten".

**Voor mieren:**

```scheme
to zoek-voedsel
  ; Met kans 10%: negeer spoor en beweeg random
  ifelse random-float 1 < 0.1 [
    right random 60 - 30
    forward 1
  ] [
    ; Normale gedrag: volg spoor
    let beste-patch max-one-of patches in-radius 2 [geurspoor]
    ; ... rest van code
  ]
end
```

**Effect:** Paden worden minder recht, maar mieren ontdekken soms nieuwe, betere routes!

**Voor Mexican wave:**

```scheme
; Met kans 5%: sta NIET op, ook al staat je buur
ifelse random-float 1 < 0.05 [
  ; Negeer buur (afleidend door telefoon!)
] [
  ; Normale reactie
]
```

**Effect:** Golf kan "breken" of stoppen als te veel mensen afgeleid zijn.

### Variatie 2: Obstakels

**Idee:** Voeg obstakels toe in de wereld die agents moeten omzeilen.

**Voor mieren:**

```scheme
to setup
  ; ... bestaande code ...
  
  ; Voeg obstakels toe
  ask n-of 10 patches [
    set pcolor black
    set obstakel? true
  ]
end

to zoek-voedsel
  ; Voor beweging: check of patch vrij is
  let doel-patch patch-ahead 1
  if [obstakel?] of doel-patch [
    ; Obstakel! Draai
    right 90
  ]
  forward 1
  ; ... rest
end
```

**Effect:** Mieren moeten om obstakels heen, paden worden complexer.

### Variatie 3: Sight-radius (bereik)

**Idee:** Hoe ver kan een agent "zien" of "ruiken"?

**Voor mieren:**

```scheme
; Slider: zoekradius (1-5)

to zoek-voedsel
  let beste-patch max-one-of patches in-radius zoekradius [geurspoor]
  ; Gebruik slider-waarde!
end
```

**Experiment:**
- Zoekradius = 1 → mieren zien weinig, langzaam paden vormen
- Zoekradius = 5 → mieren zien ver, snelle paden, maar minder realistisch

**Voor Mexican wave:**

```scheme
; Variatie: kijk naar beide buren (links én rechts)

let linker-buur turtle (who - 1)
let rechter-buur turtle (who + 1)

if [zit-of-staat?] of linker-buur = "staat" or 
   [zit-of-staat?] of rechter-buur = "staat" [
  ; Sta op als één van beide staat
]
```

**Effect:** Golf kan van beide kanten komen, interessante botsingen!

[Screenshot: Mieren-model met obstakels, paden gaan eromheen]

---

## Verdiepende opgaven

Klaar voor uitdaging? Deze opdrachten verdiepen je begrip.

```{exercise} Opdracht (Optimale pad-vorming)
:label: verd-4-1

**Onderzoek: Wat is de optimale verdampingssnelheid?**

Hypothese: Er is een "sweet spot" voor verdamping. Te snel = geen paden, te langzaam = slechte paden blijven bestaan.

Experiment:
1. Test verdampingssnelheid: 0.01, 0.03, 0.05, 0.07, 0.1
2. Meet per waarde: Hoeveel voedsel is verzameld na 500 ticks?
3. Run elke setting 5 keer, neem het gemiddelde (randomness!)

Presenteer:
- Tabel met resultaten
- Grafiek (verdampingssnelheid op x-as, verzameld voedsel op y-as)
- Conclusie: Welke waarde is optimaal? Waarom?

Schrijf 300-400 woorden + tabel + grafiek.
```

```{exercise} Opdracht (Wave collapse analyse)
:label: verd-4-2

**Onderzoek: Bij welke reactie-tijd sterft de wave uit?**

Experimenteer:
1. Start met reactie-tijd = 0.5
2. Verhoog stap voor stap: 1.0, 1.5, 2.0, 2.5, 3.0
3. Run elk 10 keer, meet: Hoeveel rondes gaat de wave? (voeg een ronde-teller toe!)

Bepaal de **kritische drempel**: Bij welke reactie-tijd gaat de wave van "blijft rondgaan" naar "sterft uit"?

Verklaar: Waarom is er een drempel? Wat bepaalt deze waarde? (Hint: vergelijk reactie-tijd met sta-tijd)

Schrijf 250-350 woorden met onderbouwing.
```

```{exercise} Opdracht (Multi-nest uitbreiding)
:label: verd-4-3

**Uitdaging: Mieren met 2 nesten**

Bouw een versie met 2 nesten op verschillende plekken. Mieren kunnen naar hun "thuisnest" terugkeren.

Implementeer:
1. Elke mier heeft een variabele `mijn-nest` (nest 1 of 2)
2. Setup: maak 2 nesten, verdeel mieren over beide
3. Mieren gaan terug naar hun eigen nest
4. Voeg verschillende kleuren toe: nest 1 = rood, nest 2 = blauw

Observeer: Ontstaan er competitie om voedsel? Vormen de nesten aparte paden, of gebruiken ze dezelfde? Leg uit wat je ziet in 200-300 woorden + screenshots.
```

---

## PO-mijlpaal

Na dit hoofdstuk ben je klaar voor de vierde mijlpaal: een werkend model met duidelijk emergent gedrag.

### Wat levert deze fase op?

Een NetLogo-bestand (.nlogo) met de **versie 1 van je eindproject** dat emergent gedrag toont:

1. **Code:**
   - Volledige implementatie van minimaal 5 regels uit je conceptuele canvas
   - Werkende `setup` en `go` met correct gebruik van `tick`
   - Minimaal 2 reporters voor monitors/plots

2. **Interface:**
   - 2 buttons: setup en go
   - Minimaal 2 sliders voor parameters
   - Minimaal 2 monitors die outputs tonen
   - 1 plot die een relevant verloop toont

3. **Info-tabblad:**
   - Je naam, datum, versie-nummer
   - Korte beschrijving emergent gedrag (5-10 regels)
   - Lijst van parameters en wat ze doen
   - Korte verklaring: "Het patroon ontstaat omdat..." (3-5 zinnen)

4. **Document** (apart, 1 pagina A4):
   - Screenshot van je model in actie (met zichtbaar emergent patroon)
   - Korte verklaring (10 regels): Waarom ontstaat dit patroon? Welke regel is cruciaal?

### Checklist: je bent klaar als…

- [ ] Je model toont **duidelijk emergent gedrag** (patroon dat niet in individuele regels staat)
- [ ] Het gedrag is **visueel herkenbaar** (kleuren, beweging, paden, etc.)
- [ ] Je hebt minimaal 2 parameters die **significant effect** hebben (test dit!)
- [ ] Je monitors en plot tonen **dynamische waarden** (niet statisch)
- [ ] Je kunt in 3-5 zinnen uitleggen **waarom** het patroon ontstaat
- [ ] Je code bevat **comments** bij elke belangrijke regel
- [ ] Het model loopt stabiel zonder crashes (test 500+ ticks)
- [ ] Het Info-tabblad is volledig ingevuld

### Waar komt dit terug in je eindproject?

Dit model is de **kern van je eindverslag**:

- **Inleiding:** "Ik heb dit fenomeen gemodelleerd omdat..."
- **Methode:** Screenshots van interface + code, uitleg van regels
- **Resultaten (hoofdstuk 5):** Je gaat experimenteren met parameters en data verzamelen
- **Discussie:** "Het emergente gedrag ontstaat door..." (je verklaring van sectie 4.5)

**Tips voor succes:**

- **Start met één duidelijk emergent patroon:** Probeer niet alles tegelijk te bouwen
- **Test na elke regel:** Werkt het? Zo nee, debug voor je verder gaat
- **Gebruik voorbeeldmodellen:** Kijk in Models Library naar vergelijkbare modellen
- **Vraag feedback:** Laat je model zien aan een klasgenoot. Ziet die ook het emergente gedrag?

**Evaluatiecriteria:**

| Criterium | Onvoldoende | Voldoende | Goed |
|-----------|-------------|-----------|------|
| Emergent gedrag | Niet zichtbaar of niet emergent | Zichtbaar, simpel patroon | Duidelijk, complex patroon |
| Parameters | <2 of geen effect | 2, effect zichtbaar | 3+, systematisch getest |
| Verklaring | Ontbreekt of onjuist | Aanwezig, logisch | Diepgaand, onderbouwd |
| Code-kwaliteit | Veel fouten, geen comments | Werkt, basis comments | Netjes, duidelijke structuur |

---

**Volgende stap:** In hoofdstuk 5 ga je systematisch experimenteren met je model. Je varieert parameters, verzamelt data, maakt grafieken, en beantwoordt je onderzoeksvraag met bewijs. Wetenschappelijk werk! Tijd om de digitale labjas aan te trekken!
