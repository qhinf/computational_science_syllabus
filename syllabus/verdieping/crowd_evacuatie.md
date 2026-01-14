# Verdieping: Crowd-evacuatie - Paniek en veiligheid

Hoe evacueer je 50.000 mensen uit een stadion? Waarom ontstaat er paniek bij nooduitgangen? En hoe voorkom je dodelijke mensenmassa's? Dit hoofdstuk duikt in **crowd dynamics**: hoe massa's mensen zich gedragen in crisissituaties. Je leert een evacuatiemodel bouwen, uitbreiden met paniek-gedrag en obstakels, en experimenteren met uitgangsbreedte. Cruciaal voor architecten, event-organisatoren, en rampenbestrijding.

**Leerdoel:** Na dit hoofdstuk begrijp je hoe emergent crowd-gedrag ontstaat, kun je een evacuatiemodel bouwen met minimaal 2 uitbreidingen (paniek, obstakels), en parameter-sweeps uitvoeren over evacuatietijd.

## Inhoud

In dit hoofdstuk behandelen we:

- Historische context: Hillsborough disaster (1989) en andere rampen
- Conceptueel model: agents zoeken uitgang, vermijden massa
- NetLogo implementatie basis-evacuatie
- Uitbreiding 1: Paniek-gedrag (push, snelheid ↑)
- Uitbreiding 2: Obstakels en meerdere uitgangen
- Parameter-sweep experiment: uitgangsbreedte vs evacuatietijd
- 4 verdiepende opgaven
- VWO-variant voor eindproject

---

## Historische context: Hillsborough en crowd-rampen

### Hillsborough disaster (1989)

**Datum:** 15 april 1989, Sheffield, Engeland  
**Locatie:** Hillsborough stadion, FA Cup halve finale  
**Slachtoffers:** 97 doden, 766 gewonden

**Wat gebeurde er?**

1. **Overcrowding:** Te veel supporters in een vak (3.000 in ruimte voor 2.200)
2. **Hekken:** Veiligheidshekken rondom veld (om pitch invasion te voorkomen) blokkeerden ontsnapping
3. **Domino-effect:** Mensen vooraan werden plat gedrukt door massa achter hen
4. **Late reactie:** Politie opende hekken te laat

**Oorzaak:** Geen paniek, maar **fysieke krachten in dichte massa**. Bij >5 personen/m², ontstaat **crowd crush**: mensen kunnen niet meer bewegen, worden geplet.

[Screenshot: Foto Hillsborough-hekken (historisch archief)]

### Andere crowd-rampen

| Ramp | Locatie | Jaar | Doden | Oorzaak |
|------|---------|------|-------|---------|
| **Love Parade** | Duisburg, Duitsland | 2010 | 21 | Tunnelpaniek, te smalle uitgang |
| **Mekka Hadj** | Saudi-Arabië | 2015 | 2.400+ | Stampede bij pelgrimstocht |
| **The Station nightclub** | Rhode Island, VS | 2003 | 100 | Brand, smalle deur, paniek |
| **IKEA opening** | Saudi-Arabië | 2004 | 3 | Stampede bij opening (kortingen) |

**Patroon:** Rampen ontstaan bij combinatie van:
1. **Hoge dichtheid** (>4 personen/m²)
2. **Beperkte uitgangen** (flessenhals)
3. **Stress** (brand, paniek, urgentie)

### Waarom modelleren?

**Doel:** Voorkom toekomstige rampen door:
- **Architectuur testen:** Zijn uitgangen breed genoeg?
- **Scenario's simuleren:** Wat als brand uitbreekt? Hoe snel evacueren?
- **Veiligheidsregels:** Hoeveel mensen passen veilig in een ruimte?

**Voordeel ABM:** Je kunt duizenden evacuaties simuleren zonder echte mensen in gevaar te brengen.

---

## Conceptueel model: agents zoeken uitgang, vermijden massa

### Agents (mensen)

**Eigenschappen:**
- Positie (x, y)
- Snelheid (hoe snel bewegen)
- Geduld (hoe snel paniek ontstaat)
- Status: `calm` of `panicked`

**Doel:** Bereik de uitgang zo snel mogelijk.

### Omgeving

**Ruimte:** Rechthoekige ruimte (bijv. stadion-sectie, nightclub)

**Uitgangen:** 1 of meer patches aan de rand (groen = uitgang)

**Obstakels:** Muren, pilaren (zwart)

### Regels (basis)

#### Regel 1: Beweeg naar dichtstbijzijnde uitgang

**Simpel:** "Kijk waar de uitgang is, loop die kant op."

**Mechanisme:**
```scheme
let target-exit nearest-exit
face target-exit
forward speed
```

#### Regel 2: Vermijd botsingen

**Simpel:** "Als er iemand voor je staat, loop eromheen."

**Mechanisme:**
- Check patch-ahead: zijn er andere agents?
- Zo ja: draai 45° en probeer opnieuw
- Zo nee: loop rechtdoor

#### Regel 3: Vermijd overcrowding

**Simpel:** "Als het te druk is, vertraag."

**Mechanisme:**
- Tel agents binnen radius 1
- Als >4: verlaag snelheid (realistisch: je kunt niet hard lopen in menigte)

#### Regel 4: Evacueer bij uitgang

**Simpel:** "Als je bij uitgang bent, verlaat de ruimte."

**Mechanisme:**
```scheme
if pcolor = green [  ; Groen = uitgang
  die  ; Agent verlaat simulatie
]
```

---

## NetLogo implementatie basis-evacuatie

### Setup

```scheme
breed [people person]

people-own [
  speed          ; Hoe snel bewegen (0.5 - 1.0)
  panic-level    ; 0 = calm, 100 = panicked
  target-exit    ; Welke uitgang zoeken
]

globals [
  evacuated      ; Aantal geëvacueerde mensen
  evacuation-time  ; Ticks tot iedereen weg is
]

to setup
  clear-all
  
  ; Maak ruimte (walls = zwart)
  ask patches [set pcolor white]
  
  ; Maak uitgangen (aan rechterkant)
  ask patches with [pxcor = max-pxcor and pycor > -5 and pycor < 5] [
    set pcolor green  ; Uitgang
  ]
  
  ; Maak muren (optioneel)
  ask patches with [pxcor = 0] [
    set pcolor black  ; Verticale muur (demonstratie)
  ]
  
  ; Maak mensen
  create-people aantal-mensen [
    set color blue
    set size 1
    set shape "person"
    setxy random-xcor random-ycor
    
    ; Vermijd spawnen op muur of uitgang
    while [pcolor != white] [
      setxy random-xcor random-ycor
    ]
    
    set speed 0.5 + random-float 0.5  ; Variatie in snelheid
    set panic-level 0
    set target-exit min-one-of patches with [pcolor = green] [distance myself]
  ]
  
  set evacuated 0
  set evacuation-time 0
  
  reset-ticks
end
```

### Go-procedure

```scheme
to go
  ; Stop als iedereen geëvacueerd is
  if not any? people [
    if evacuation-time = 0 [
      set evacuation-time ticks  ; Eerste tick dat iedereen weg is
    ]
    stop
  ]
  
  ask people [
    move-towards-exit
    check-evacuation
  ]
  
  tick
end
```

### Beweging naar uitgang

```scheme
to move-towards-exit  ; Person procedure
  ; Regel 1: Richting uitgang
  face target-exit
  
  ; Regel 2: Vermijd botsingen
  let ahead-agents people-on patch-ahead 1
  
  ifelse any? ahead-agents [
    ; Er staat iemand, probeer om te lopen
    rt 45
    
    ; Check opnieuw
    if not any? people-on patch-ahead 1 [
      forward speed * 0.5  ; Halve snelheid (navigeren)
    ]
  ][
    ; Vrij pad, loop rechtdoor
    
    ; Regel 3: Vertraag bij overcrowding
    let nearby-count count people in-radius 1
    let adjusted-speed speed
    
    if nearby-count > 4 [
      set adjusted-speed speed * 0.3  ; Veel trager in menigte
    ]
    
    ; Check voor muren
    if [pcolor] of patch-ahead 1 != black [
      forward adjusted-speed
    ]
  ]
end

to check-evacuation  ; Person procedure
  ; Regel 4: Evacueer bij uitgang
  if pcolor = green [
    set evacuated evacuated + 1
    die
  ]
end
```

### Interface-elementen

**Sliders:**
- `aantal-mensen`: 100 (aantal mensen in ruimte)

**Buttons:**
- `setup`
- `go` (forever)

**Monitors:**
- `evacuated`: Aantal geëvacueerd
- `count people`: Aantal nog in ruimte
- `evacuation-time`: Totale evacuatietijd

**Plot:** "Evacuatie over tijd"
- X-as: ticks
- Y-as: count people (daalt naar 0)

[Screenshot: NetLogo interface met mensen (blauw) die naar groene uitgang bewegen]

:::{tip}
**Visualisatie verbeteren:**  
Voeg kleuren toe op basis van dichtheid:
```scheme
ask patches [
  let crowd-here count people-here
  if crowd-here > 0 [
    set pcolor scale-color red crowd-here 0 5  ; Roder = drukker
  ]
]
```
Dit toont "hotspots" waar files ontstaan.
:::

---

## Uitbreiding 1: Paniek-gedrag

In crisissituaties gedragen mensen zich anders. Voeg **paniek** toe!

### Conceptueel

**Paniek-triggers:**
- Tijd verstrijkt (urgentie neemt toe)
- Hoge dichtheid (claustrofobie)
- Langzame voortgang (frustratie)

**Paniek-effecten:**
1. **Snelheid ↑:** Mensen rennen (maar botsen vaker)
2. **Pushen:** Mensen duwen anderen opzij (egoïstisch gedrag)
3. **Rationeel ↓:** Kiezen niet meer de beste uitgang

### Implementatie

```scheme
to move-towards-exit  ; Person procedure (aangepast)
  ; Update paniek
  update-panic
  
  ; ... rest van bestaande code ...
  
  ; Pas snelheid aan op basis van paniek
  let panic-multiplier 1 + (panic-level / 100)  ; 1.0 - 2.0
  set adjusted-speed adjusted-speed * panic-multiplier
  
  ; ... movement code ...
end

to update-panic  ; Person procedure
  ; Paniek stijgt per tick (urgentie)
  set panic-level panic-level + 0.1
  
  ; Paniek stijgt bij overcrowding
  let nearby-count count people in-radius 1
  if nearby-count > 4 [
    set panic-level panic-level + 0.5
  ]
  
  ; Paniek stijgt als je vast zit (niet bewogen)
  ; (Implementatie: vergelijk positie met vorige tick)
  
  ; Cap op 100
  if panic-level > 100 [set panic-level 100]
  
  ; Visueel: kleur wordt roder bij paniek
  set color scale-color red panic-level 0 100
end
```

### Pushen (geavanceerd)

```scheme
to push-forward  ; Person procedure
  ; Als paniek hoog EN iemand staat voor je, duw opzij
  if panic-level > 50 [
    let blocker one-of people-on patch-ahead 1
    
    if blocker != nobody [
      ask blocker [
        ; Duw blocker opzij (perpendiculair)
        rt 90
        if [pcolor] of patch-ahead 1 != black [
          forward 0.5
        ]
        lt 90
      ]
    ]
  ]
end
```

### Observaties

**Verwacht gedrag:**
- **Zonder paniek:** Nette rij bij uitgang, stabiele evacuatie
- **Met paniek:** Chaos bij uitgang, mensen duwen, files worden erger (paradox!)

**Paradox:** Paniek **vertraagt** evacuatie! Waarom?
- Mensen rennen → meer botsingen → files
- Pushen → anderen vallen → blokkades
- Iedereen naar 1 uitgang → overbelasting (andere uitgangen leeg)

**Les:** In echte evacuaties: **blijf kalm** is niet alleen advies, het is **efficiënter**.

[Screenshot: Visualisatie met rode (paniek) en blauwe (calm) mensen, file bij uitgang]

---

## Uitbreiding 2: Meerdere uitgangen en obstakels

### Meerdere uitgangen

**Realistischer:** Gebouwen hebben meerdere nooduitgangen.

```scheme
to setup
  ; ... bestaande code ...
  
  ; Maak 2 uitgangen
  ask patches with [pxcor = max-pxcor and pycor > 5 and pycor < 10] [
    set pcolor green  ; Uitgang 1 (boven)
  ]
  
  ask patches with [pxcor = max-pxcor and pycor > -10 and pycor < -5] [
    set pcolor green  ; Uitgang 2 (onder)
  ]
  
  ; ... rest ...
end
```

**Uitdaging:** Hoe kiezen mensen welke uitgang?

**Optie A: Dichtstbijzijnde** (rationeel)
```scheme
set target-exit min-one-of patches with [pcolor = green] [distance myself]
```

**Optie B: Minst drukke** (intelligent)
```scheme
; Kies uitgang met minste mensen ervoor
set target-exit min-one-of patches with [pcolor = green] [
  count people in-radius 5  ; Tel drukte bij uitgang
]
```

**Optie C: Random** (paniek, irrationeel)
```scheme
set target-exit one-of patches with [pcolor = green]
```

**Experiment:** Welke strategie leidt tot snelste evacuatie?

### Obstakels

**Realistischer:** Pilaren, meubilair, trap-hekken.

```scheme
to setup
  ; ... bestaande code ...
  
  ; Maak pilaren
  ask patches with [
    (pxcor mod 10 = 0) and (pycor mod 10 = 0)
  ][
    set pcolor black
  ]
  
  ; Of: muur met smalle doorgang
  ask patches with [pxcor = 5 and abs pycor > 3] [
    set pcolor black  ; Doorgang bij pycor -3 tot 3
  ]
end
```

**Effect:** Mensen moeten eromheen navigeren → vertraging → files bij doorgang.

**Observatie:** Smalle doorgangen zijn **flessenhalzen**. In echte gebouwen: kritisch punt!

---

## Parameter-sweep experiment: uitgangsbreedte vs evacuatietijd

### Onderzoeksvraag

**Vraag:** Hoe beïnvloedt de breedte van de uitgang de evacuatietijd?

**Hypothese:** Bredere uitgang → snellere evacuatie, maar effect vlakt af (diminishing returns).

### Experimentopzet

**Variabele parameter:** `uitgang-breedte` (aantal patches breed)  
**Range:** 2, 4, 6, 8, 10, 12 patches  
**Constante parameters:**
- `aantal-mensen = 100`
- `panic-level` start op 0
- 1 uitgang (rechterkant, midden)

**Output:**
- **Evacuatietijd:** Ticks tot laatste persoon geëvacueerd

**Runs:** 5 runs per waarde × 6 waarden = 30 runs

### Implementatie

```scheme
to setup
  ; ... bestaande code ...
  
  ; Uitgang van variabele breedte
  let half-width uitgang-breedte / 2
  
  ask patches with [
    pxcor = max-pxcor and
    pycor > (0 - half-width) and pycor < (0 + half-width)
  ][
    set pcolor green
  ]
  
  ; ... rest ...
end
```

**Slider toevoegen:** `uitgang-breedte` (2-20)

### Resultaten (hypothetisch)

| Uitgang-breedte | Gem. evacuatietijd | SD | Observatie |
|-----------------|--------------------|----|------------|
| 2 | 450 ticks | 35 | Zeer langzaam, grote file |
| 4 | 280 ticks | 22 | Duidelijke verbetering |
| 6 | 195 ticks | 18 | Goede flow |
| 8 | 160 ticks | 15 | Snelle evacuatie |
| 10 | 145 ticks | 12 | Kleine verbetering |
| 12 | 140 ticks | 11 | Marginale winst |

[Screenshot: Grafiek met uitgang-breedte op x-as, evacuatietijd op y-as, exponentiële daling]

### Interpretatie

**Patroon:** **Exponentiële daling** van evacuatietijd:
- Smalle uitgangen (2-4): Enorme impact van extra breedte
- Brede uitgangen (10-12): Kleine impact (diminishing returns)

**Mechanisme:**
- Bij breedte 2: **Flessenhals**, mensen moeten wachten in rij
- Bij breedte 6-8: **Optimaal**, meerdere mensen passen tegelijk door
- Bij breedte >10: **Overkill**, hele ruimte is al leeg voordat volle breedte benut wordt

**Conclusie voor architectuur:**
- **Minimale breedte:** ~4-6 patches (in schaal: ~2-3 meter voor 100 personen)
- **Cost-benefit:** Breedte >8 is verspilling (duurder, geen tijdwinst)

**Validatie:** Nederlandse bouwregelgeving eist **minimum 0.8m per 100 personen**. Ons model: 4 patches voor 100 mensen ≈ schaal 1 patch = 0.5m → 2m totaal. **Komt overeen!**

---

## Verdiepende opgaven

```{exercise} Opdracht 1: Brand en zichtbaarheid
:label: verd-crowd-1

**Realisme: brand verspreidt zich**

Voeg een **brand** toe die zich verspreidt en zicht blokkeert.

**Implementatie-hints:**
1. Maak breed `[fires fire]` (rode patches)
2. Brand start op random locatie: `ask one-of patches [set pcolor red]`
3. Brand verspreidt per tick naar naburige patches (4 neighbors, 10% kans)
4. **Rook:** Patches rond brand worden grijs → mensen zien uitgang niet meer
   ```scheme
   if any? neighbors with [pcolor = red] [
     set pcolor gray  ; Rook
   ]
   ```
5. Mensen in rook bewegen **random** (gedesoriënteerd)

**Experiment:**
- Hoe beïnvloedt brand-startlocatie de evacuatietijd? (Dichtbij uitgang = catastrofaal?)
- Bij welke brand-spreidsnelheid is evacuatie onmogelijk?

**Schrijf:** 500-600 woorden + grafiek (evacuatietijd vs brand-spreidsnelheid)
```

```{exercise} Opdracht 2: Groepsgedrag en helpers
:label: verd-crowd-2

**Realisme: mensen helpen elkaar**

Niet iedereen is even mobiel. Voeg **kwetsbare personen** en **helpers** toe.

**Implementatie:**
1. 10% van mensen is `vulnerable` (ouderen, kinderen): speed = 0.2 (langzaam)
2. 20% van mensen is `helper`: Als ze kwetsbare zien, begeleiden ze (lopen naast ze)
3. Helpers passen snelheid aan aan kwetsbare persoon
   ```scheme
   if any? people in-radius 2 with [vulnerable?] [
     let helpee min-one-of people with [vulnerable?] [distance myself]
     face helpee
     set speed [speed] of helpee  ; Match snelheid
   ]
   ```

**Experiment:**
- Hoe vertraagt helpers de gemiddelde evacuatietijd?
- Wat is de optimale ratio helpers/vulnerable voor snelste evacuatie?
- Voeg "groepen" toe: families blijven bij elkaar (link tussen agents)

**Schrijf:** 600-700 woorden + vergelijkingstabel (met/zonder helpers)
```

```{exercise} Opdracht 3: Dynamische uitgangen (exit choice)
:label: verd-crowd-3

**Intelligentie: agents leren welke uitgang het beste is**

In echte evacuaties zien mensen dat een uitgang vol is, en kiezen dan een andere.

**Implementatie:**
1. Agents hebben `exit-preference` (welke uitgang ze proberen)
2. Als ze binnen 5 patches van uitgang komen, evalueren:
   - Is er een file? (>10 mensen binnen radius 5)
   - Zo ja: wissel naar andere uitgang
3. Agents communiceren (simple versie): leggen "avoid here" pheromone bij drukke uitgang
4. Nieuwe agents vermijden uitgangen met hoge pheromone-concentratie

**Experiment:**
- Leidt exit-switching tot snellere evacuatie? (Ja, bij 2+ uitgangen!)
- Wat is het optimale moment om te switchen? (Te vroeg = iedereen wisselt, chaos)

**Geavanceerd:** Gebruik "ant-like" pheromones (zoals hoofdstuk 4)

**Schrijf:** 700-800 woorden + vergelijking 3 strategieën (dichtstbijzijnde, minst drukke, pheromone-based)
```

```{exercise} Opdracht 4: Real-world case study
:label: verd-crowd-4

**Toegepast: simuleer een bestaand gebouw**

Kies een echt gebouw (je school, stadion, theater) en simuleer evacuatie.

**Stappen:**
1. **Plattegrond:** Teken layout in NetLogo (muren, uitgangen, kamers)
2. **Capaciteit:** Gebruik echte getallen (hoeveel mensen passen in aula?)
3. **Scenario:** Simuleer brand in kantine → evacueer naar buiten
4. **Analyse:** Waar ontstaan files? Zijn uitgangen breed genoeg?
5. **Advies:** Stel verbeteringen voor (extra uitgang, bredere deur, etc.)

**Presenteer aan schoolleiding!**

**Bronnen:**
- Plattegronden (vraag schoolfaciliteiten)
- Nederlandse bouwregelgeving (Bouwbesluit 2012, evacuatie-eisen)

**Zeer toegepast en maatschappelijk relevant!**

**Schrijf:** 1000-1200 woorden + plattegrond + simulatie-screenshots + adviesrapport
```

---

## VWO-variant voor eindproject

### Waarom crowd-evacuatie voor VWO?

**Sterke punten:**
1. **Maatschappelijke relevantie:** Direct toepasbaar (veiligheid)
2. **Interdisciplinair:** Psychologie (paniek), fysica (krachten), architectuur
3. **Kwantitatief:** Veel meetbare outputs (tijd, dichtheid, files)
4. **Ethisch verantwoord:** Simulatie voorkomt echte risico's

### VWO-niveau aanpak

#### Optie A: Kwantitatieve validatie met data

**Doel:** Vergelijk model met echte evacuatie-data.

**Bronnen:**
- **Wetenschappelijke artikelen:** Helbing et al. (2000) "Simulating dynamical features of escape panic"
- **Bouwregelgeving:** Nederlandse normen voor uitgangsbreedtes
- **Video-analyse:** YouTube evacuatie-oefeningen (meet snelheden, dichtheden)

**Methode:**
1. Kalibreer parameters tot model overeenkomt met literatuur-waarden
2. Test: Voorspelt model correcte evacuatietijden voor bekende cases?
3. Sensitiviteitsanalyse: Welke parameters zijn cruciaal?

**Output:** Gevalideerd model dat gebruikt kan worden voor veiligheidsadvies.

#### Optie B: Fysisch correcte krachten-model

**Doel:** Implementeer echte fysica (crowd crush forces).

**Concepten:**
- **Social force model** (Helbing & Molnár, 1995): Agents ervaren "krachten" (aantrekking tot doel, repulsie van anderen)
- **Druk-berekening:** Bij dichtheid >5 p/m², ontstaan gevaarlijke druk-krachten
- **Vallen:** Agents die te veel druk ervaren, vallen (kunnen niet meer bewegen)

**Implementatie (geavanceerd):**
```scheme
; Bereken krachten (vectoren)
let force-to-exit (towards target-exit) with magnitude based-on-distance
let force-from-others sum-of-repulsions from nearby-people
let total-force force-to-exit + force-from-others

; Update velocity en positie
set velocity velocity + total-force
set heading atan (velocity-y) (velocity-x)
forward magnitude velocity
```

**Zeer uitdagend:** Vereist begrip van vectorrekening. Geschikt voor VWO Wiskunde B.

#### Optie C: Machine learning optimalisatie

**Doel:** Laat algoritme optimale evacuatie-strategie vinden.

**Methode:**
- **Reinforcement learning:** Agents leren welke acties leiden tot snelste evacuatie
- **Genetic algorithm:** Evolutionair zoeken naar optimale gebouw-layout
- **Swarm optimization:** Agents communiceren en coördineren evacuatie

**Tools:** NetLogo's R-extension of Python-integratie (via NetLogo-Python bridge).

**Zeer geavanceerd:** Geschikt voor VWO-eindproject informatica/wiskunde combinatie.

### Checklist VWO-niveau

- [ ] **Kwantitatieve validatie** met minimaal 2 databronnen (literatuur, regelgeving)
- [ ] **Complexe uitbreiding:** Minimaal 1 van (paniek-model, fysische krachten, meerdere uitgangen met dynamische keuze)
- [ ] **Parameterstudie:** Minimaal 3 parameters gevarieerd (niet alleen 1)
- [ ] **Sensitiviteitsanalyse:** Welke parameters zijn meest cruciaal?
- [ ] **Verslag >10 pagina's** met grondige literatuurstudie
- [ ] **Toepassing:** Advies voor reëel gebouw/scenario

### Interdisciplinaire koppeling

**Natuurkunde:**
- Krachten en momentum in crowds
- Drukkrachten (Pascal's law)

**Wiskunde:**
- Vectorrekening (krachten)
- Statistiek (evacuatietijden, verdlingen)
- Differentiaalvergelijkingen (advanced: continuous crowd flow models)

**Maatschappijleer:**
- Rampenbestrijding beleid
- Ethiek: wie heeft voorrang bij evacuatie?

**Biologie:**
- Stress en paniek (fight-or-flight response)
- Groepsgedrag bij dieren (kuddes, zwermen)

---

**Conclusie:** Crowd-evacuatie is **cruciaal en onderschat**. Elk jaar sterven honderden mensen wereldwijd door slechte crowd-management. Dit model leert je niet alleen computational science, maar kan letterlijk **levens redden** als toegepast in gebouw-ontwerp. Neem dit serieus! 🚨🏃‍♂️🚪

