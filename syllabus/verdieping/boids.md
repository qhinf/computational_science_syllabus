# Verdieping: Boids - Collectief gedrag in zwermen

Waarom vliegen vogels in formatie? Hoe blijven visscholen synchroon bewegen? En waarom botsen ze niet, zelfs in grote groepen? Dit hoofdstuk duikt in **boids**: een klassieker model uit 1986 door Craig Reynolds. Met slechts **drie simpele regels** ontstaat complex zwermgedrag. Je leert het model uitbreiden met nieuwe mechanismen (roofdieren, obstakels), experimenten uitvoeren, en dit gebruiken als VWO-variant voor je eindproject.

**Leerdoel:** Na dit hoofdstuk begrijp je hoe lokale regels leiden tot globaal zwermgedrag, kun je het boids-model uitbreiden met minimaal 2 nieuwe mechanismen, en een parameter-sweep uitvoeren met interpretatie.

## Inhoud

In dit hoofdstuk behandelen we:

- Historische context: Reynolds' boids (1986)
- Conceptueel model: drie simpele regels
- NetLogo implementatie basis
- Uitbreiding 1: Roofdier (predator)
- Uitbreiding 2: Obstakels en grenzen
- Parameter-sweep experiment: cohesie vs separatie
- 4 verdiepende opgaven
- VWO-variant voor eindproject

---

## Historische context: Reynolds' boids (1986)

### De ontdekking

In **1986** publiceerde computergraficus **Craig Reynolds** een baanbrekend algoritme: **boids** (bird-oid objects, "vogel-achtige objecten"). 

**Probleem:** Animatiefilms wilden realistische zwermen tonen, maar handmatig animeren van 100+ vogels is onmogelijk.

**Oplossing:** Reynolds ontdekte dat je geen centrale controle nodig hebt. Elk individu volgt **lokale regels** → emergent zwermgedrag ontstaat.

**Impact:**
- Gebruikt in films: *Batman Returns* (1992), *The Lion King* (1994), *Finding Nemo* (2003)
- Robotica: drone-zwermen, autonome voertuigen
- Biologie: verklaart hoe echte zwermen werken zonder leider


### Waarom is dit belangrijk?

**Centrale controle (klassiek):**
- 1 "leider" stuurt hele zwerm
- Als leider faalt → hele systeem faalt
- Moeilijk te schalen (1000+ vogels)

**Gedecentraliseerd (boids):**
- Elk individu beslist zelf op basis van buren
- Robuust: als 1 vogel verdwijnt, zwerm blijft werken
- Schaalt makkelijk naar duizenden agents

**Filosofische vraag:** Wie "bestuurt" een zwerm? **Antwoord:** Niemand. Het is **zelforganisatie**.

---

## Conceptueel model: drie simpele regels

Reynolds definieerde **drie regels** die elk individu (boid) volgt:

### Regel 1: Separatie (avoid crowding)

**Simpel:** "Blijf uit de buurt van je directe buren."

**Mechanisme:** Als een andere boid te dichtbij komt (binnen `minimum-separation`), stuur weg van die boid.

**Waarom?** Voorkomt botsingen.

**Visualisatie:**
```
   Boid A  →  ●  ←  Boid B
              ↑
          (te dichtbij!)
          
Na separatie:
   ●  ←→  ●
   (verder uit elkaar)
```

### Regel 2: Uitlijning (align with neighbors)

**Simpel:** "Vlieg in dezelfde richting als je buren."

**Mechanisme:** Bereken gemiddelde heading (richting) van boids binnen `vision`, draai je eigen heading die kant op.

**Waarom?** Zorgt voor synchrone beweging.

**Visualisatie:**
```
Voor:
  → ● ↑ ● ← ●
  (verschillende richtingen)
  
Na uitlijning:
  → ● → ● → ●
  (allen dezelfde richting)
```

### Regel 3: Cohesie (move toward center)

**Simpel:** "Beweeg naar het centrum van je buren."

**Mechanisme:** Bereken gemiddelde positie van boids binnen `vision`, stuur die kant op.

**Waarom?** Houdt de zwerm bij elkaar.

**Visualisatie:**
```
Voor:
     ●
  ●     ●
     ●
  (verspreide boids)
  
Na cohesie:
    ●●
    ●●
  (geclusterd)
```

### Hoe werken ze samen?

**Separatie** vs **Cohesie** = tegengestelde krachten!
- Separatie: "ga weg"
- Cohesie: "kom dichterbij"

**Resultaat:** Boids blijven op **optimale afstand** van elkaar → zwerm blijft bij elkaar, maar bots niet.

**Uitlijning** = zorgt dat zwerm als geheel beweegt (niet stilstaat).

:::{tip}
**Balans is cruciaal!**  
Te veel separatie → zwerm valt uiteen  
Te veel cohesie → boids clusteren in 1 punt  
Te veel uitlijning → stijve beweging  
Te weinig uitlijning → chaotisch

De magie zit in de **juiste verhouding**.
:::

---

## NetLogo implementatie basis

Laten we de drie regels implementeren in NetLogo.

### Setup

```scheme
breed [boids boid]  ; Definieer breed

globals [
  max-separate-turn   ; Max hoek voor separatie
  max-align-turn      ; Max hoek voor uitlijning
  max-cohere-turn     ; Max hoek voor cohesie
]

boids-own [
  flockmates          ; Agentset van nabije boids
  nearest-neighbor    ; Dichtstbijzijnde boid
]

to setup
  clear-all
  
  ; Parameters
  set max-separate-turn 1.5
  set max-align-turn 5
  set max-cohere-turn 3
  
  ; Maak boids
  create-boids aantal [
    set color blue
    set size 3
    setxy random-xcor random-ycor
    set heading random 360
  ]
  
  reset-ticks
end
```

### Go-procedure

```scheme
to go
  ask boids [
    find-flockmates       ; Stap 1: Vind buren
    
    if any? flockmates [  ; Als er buren zijn:
      separate            ; Regel 1
      align               ; Regel 2
      cohere              ; Regel 3
    ]
    
    forward 1             ; Beweeg vooruit
  ]
  
  tick
end
```

### Regel 1: Separatie

```scheme
to separate  ; Turtle procedure
  ; Vind boids die te dichtbij zijn
  let nearby-boids flockmates with [distance myself < minimum-separation]
  
  if any? nearby-boids [
    ; Bereken gemiddelde heading weg van nabije boids
    let average-heading mean [subtract-headings heading towards myself] of nearby-boids
    
    ; Draai maximaal max-separate-turn graden
    turn-at-most average-heading max-separate-turn
  ]
end
```

### Regel 2: uitlijning

```scheme
to align  ; Turtle procedure
  ; Bereken gemiddelde heading van flockmates
  let average-heading mean [heading] of flockmates
  
  ; Draai richting gemiddelde heading
  turn-towards average-heading max-align-turn
end
```

### Regel 3: Cohesie

```scheme
to cohere  ; Turtle procedure
  ; Bereken centroid (gemiddelde positie) van flockmates
  let average-x mean [xcor] of flockmates
  let average-y mean [ycor] of flockmates
  
  ; Draai richting centroid
  let target-heading towardsxy average-x average-y
  turn-towards target-heading max-cohere-turn
end
```

### Hulpfuncties

```scheme
to find-flockmates  ; Turtle procedure
  ; Vind alle boids binnen vision (behalve jezelf)
  set flockmates other boids in-radius vision
  set nearest-neighbor min-one-of flockmates [distance myself]
end

to turn-towards [new-heading max-turn]  ; Turtle procedure
  ; Draai richting new-heading, maar max max-turn graden per tick
  let difference subtract-headings new-heading heading
  ifelse abs difference > max-turn [
    ifelse difference > 0
      [ rt max-turn ]
      [ lt max-turn ]
  ][
    rt difference
  ]
end

to turn-at-most [new-heading max-turn]  ; Turtle procedure
  ; Simpelere versie voor separatie
  turn-towards new-heading max-turn
end
```

### Interface-elementen

**Sliders:**
- `aantal`: 50 (aantal boids)
- `vision`: 5 (hoe ver boids kijken)
- `minimum-separation`: 1.5 (minimale afstand)

**Buttons:**
- `setup`
- `go` (forever)

**Monitor:**
- `count boids`


:::{admonition} Let op: wrapping
:class: warning
NetLogo's standaard wereld is **wrapping**: agents die rechts uit lopen, komen links weer binnen. Dit is handig voor boids (geen grenzen), maar kan vreemd lijken (zwerm splitst visueel). Later voegen we obstakels toe om dit realistischer te maken.
:::

---

## Uitbreiding 1: Roofdier (predator)

Zwermen in de natuur reageren op **gevaar**. Voeg een roofdier toe!

### Conceptueel

**Nieuwe regel 4: Vlucht van roofdier**

**Simpel:** "Als je een roofdier ziet, vlieg er direct vandaan."

**Mechanisme:** Als roofdier binnen `vision`, draai 180° weg en verhoog snelheid tijdelijk.

### Implementatie

```scheme
breed [predators predator]  ; Nieuwe breed

predators-own [
  hunger  ; Hoe hongerig (bepaalt agressiviteit)
]

to setup
  ; ... bestaande code ...
  
  ; Maak 1 roofdier
  create-predators 1 [
    set color red
    set size 5
    set shape "default"  ; Of "bird" als beschikbaar
    setxy random-xcor random-ycor
    set heading random 360
    set hunger 100
  ]
  
  reset-ticks
end

to go
  ask boids [
    find-flockmates
    
    ; Nieuwe regel: check voor roofdier
    let nearby-predator min-one-of predators in-radius vision [distance myself]
    
    ifelse nearby-predator != nobody [
      ; Roofdier detectie: vlieg weg!
      escape-from nearby-predator
    ][
      ; Normale zwermregels
      if any? flockmates [
        separate
        align
        cohere
      ]
    ]
    
    forward 1
  ]
  
  ask predators [
    hunt-boids
  ]
  
  tick
end

to escape-from [threat]  ; Boid procedure
  ; Draai weg van roofdier
  let escape-heading subtract-headings heading towards threat
  face threat
  rt 180  ; Draai 180 graden om
  
  ; Verhoog snelheid (vluchtrespons)
  forward 0.5  ; Extra stap
end

to hunt-boids  ; Predator procedure
  ; Zoek dichtstbijzijnde boid
  let target min-one-of boids [distance myself]
  
  if target != nobody [
    ; Beweeg richting target
    face target
    forward 0.8  ; Sneller dan boids (0.8 vs 1.0)
    
    ; Vang boid als binnen bereik
    if distance target < 1 [
      ask target [die]  ; Boid wordt gevangen
      set hunger hunger + 50  ; Roofdier wordt minder hongerig
    ]
  ]
  
  ; Hunger neemt af per tick
  set hunger hunger - 0.1
  if hunger < 0 [set hunger 0]
end
```

### Observaties

**Verwacht gedrag:**
- Zwerm **splitst** als roofdier nadert (boids vluchten verschillende kanten op)
- Na roofdier passeert: zwerm **herformeert** door cohesie
- Roofdieren vangen **langzamere** of **geïsoleerde** boids (natuurlijke selectie!)

**Experimenteer:**
- Wat gebeurt er bij 2 roofdieren?
- Wat als roofdier even snel is als boids?
- Wat als boids meer vision hebben (eerder roofdier detecteren)?


---

## Uitbreiding 2: Obstakels en grenzen

Echte zwermen navigeren om obstakels heen. Voeg muren toe!

### Conceptueel

**Nieuwe regel 5: Ontwijken van obstakels**

**Simpel:** "Als je een obstakel ziet, draai eromheen."

**Mechanisme:** Als patch voor je een obstakel is (bijv. zwart), draai 45° (herhaal tot vrij pad).

### Implementatie

```scheme
to setup
  ; ... bestaande code ...
  
  ; Maak obstakels (muren)
  ask patches with [pxcor = 0 or pycor = 0] [
    set pcolor black  ; Verticale en horizontale muur
  ]
  
  ; Of: random obstakels
  ask n-of 50 patches [
    set pcolor black
  ]
  
  reset-ticks
end

to go
  ask boids [
    find-flockmates
    
    ; Check obstakels VOOR andere regels
    if obstacle-ahead? [
      avoid-obstacle
    ]
    
    ; ... rest van code (roofdier, zwermregels) ...
    
    forward 1
  ]
  
  ; ... rest van code ...
  
  tick
end

to-report obstacle-ahead?  ; Boid procedure reporter
  ; Check patch voor je (op afstand 'vision')
  let ahead-patch patch-ahead 2
  
  if ahead-patch != nobody [
    report [pcolor] of ahead-patch = black
  ]
  
  report false
end

to avoid-obstacle  ; Boid procedure
  ; Draai 45 graden en check opnieuw
  rt 45
  
  ; Als nog steeds obstakel, blijf draaien
  while [obstacle-ahead? and heading < (heading + 180)] [
    rt 45
  ]
end
```

### Alternatief: Edge-avoidance (grens-vermijding)

```scheme
to avoid-edges  ; Boid procedure
  ; Als te dicht bij rand, draai naar binnen
  if abs pxcor > max-pxcor - 5 [
    facexy 0 ycor  ; Draai naar centrum (x-richting)
  ]
  
  if abs pycor > max-pycor - 5 [
    facexy xcor 0  ; Draai naar centrum (y-richting)
  ]
end
```

### Observaties

**Verwacht gedrag:**
- Zwerm **stroomt** om obstakels heen (als water)
- Bij smalle doorgangen: zwerm **comprimeert**, daarna **expandeert**
- Bij doodlopende hoek: zwerm **draait om** en vindt uitweg

**Experimenteer:**
- Wat gebeurt er bij een **doolhof** van obstakels?
- Kunnen boids uit een **afgesloten ruimte** ontsnappen? (Nee, tenzij je regels toevoegt!)

:::{tip}
**Realisme toevoegen:**  
Echte vogels anticiperen op obstakels (zien ze al van ver). Je kunt `obstacle-ahead?` aanpassen om verder vooruit te kijken:
```scheme
let ahead-patch patch-ahead 5  ; Kijk 5 stappen vooruit
```
Dit geeft gladder navigatiegedrag.
:::

---

## Parameter-sweep experiment: cohesie vs separatie

Nu gaan we **systematisch experimenteren**: hoe beïnvloedt de balans tussen cohesie en separatie het zwermgedrag?

### Onderzoeksvraag

**Vraag:** Wat is de optimale verhouding tussen cohesie-kracht en separatie-kracht voor compacte, stabiele zwermen?

**Hypothese:** Te veel cohesie → boids clusteren (te weinig ruimte). Te veel separatie → zwerm valt uiteen.

### Experimentopzet

**Variabele parameter:** `max-cohere-turn` (cohesie-kracht)  
**Range:** 0, 1, 2, 3, 4, 5  
**Constante parameters:**
- `max-separate-turn = 1.5`
- `max-align-turn = 5`
- `aantal = 50`
- `vision = 5`

**Output:**
1. **Zwerm-compactheid:** Gemiddelde afstand tussen boids en centrum-van-massa
2. **Stabiliteit:** Standaarddeviatie van afstanden (lage SD = stabiele zwerm)

**Runs:** 5 runs per waarde × 6 waarden = 30 runs  
**Duur:** 500 ticks per run

### Implementatie meting

```scheme
globals [
  ; ... bestaande globals ...
  avg-distance-to-center  ; Gemiddelde afstand tot centrum
]

to go
  ; ... bestaande go-code ...
  
  ; Meet compactheid
  measure-compactness
  
  tick
end

to measure-compactness
  ; Bereken centrum van zwerm
  let center-x mean [xcor] of boids
  let center-y mean [ycor] of boids
  
  ; Bereken gemiddelde afstand tot centrum
  set avg-distance-to-center mean [distancexy center-x center-y] of boids
end
```

**Monitor toevoegen:** `avg-distance-to-center`

### Resultaten (hypothetisch)

| max-cohere-turn | Gem. afstand | SD | Observatie |
|-----------------|--------------|-----|------------|
| 0 | 25.3 | 12.1 | Zwerm valt uiteen, geen cohesie |
| 1 | 18.7 | 8.4 | Losse zwerm, regelmatig splitst |
| 2 | 12.4 | 4.2 | Stabiele zwerm, beweegt synchroon |
| 3 | 8.1 | 3.1 | **Compacte, stabiele zwerm** ✅ |
| 4 | 5.2 | 5.8 | Te compact, boids clusteren |
| 5 | 3.8 | 7.2 | Zwerm collapst tot 1 punt, instabiel |


### Interpretatie

**Patroon:** Er is een **optimum bij max-cohere-turn = 3**:
- Lage cohesie (0-1): Zwerm te los, valt uiteen
- Optimale cohesie (2-3): Balans tussen samenblijven en ruimte
- Hoge cohesie (4-5): Te veel aantrekking, zwerm comprimeert

**Mechanisme:** Bij optimale cohesie werken cohesie en separatie **in balans**:
- Cohesie trekt boids naar elkaar → zwerm blijft bij elkaar
- Separatie duwt boids weg als te dicht → voorkomt clustering
- Resultaat: **Dynamisch evenwicht** op optimale afstand

**Validatie:** Dit komt overeen met echte zwermen! Biologen observeren dat vogels op ~1-2 lichaamslengtes van elkaar vliegen (niet te dicht, niet te ver).

---

## Verdiepende opgaven

Klaar voor uitdagingen? Deze opdrachten brengen boids naar hoger niveau.

```{exercise} Opdracht 1: Wind en turbulentie
:label: verd-boids-1

**Realisme toevoegen: omgevingskrachten**

Echte zwermen vliegen in wind. Voeg een **windkracht** toe die boids beïnvloedt.

**Implementatie-hints:**
1. Maak globale variabelen: `wind-direction` en `wind-strength`
2. In `go`: Voor elke boid, voeg wind toe aan heading:
   ```scheme
   ; Na normale beweging
   let wind-effect wind-strength * 0.1
   set heading heading + (wind-direction - heading) * wind-effect
   ```
3. Varieer wind-direction elke 50 ticks (simuleer windvlagen)

**Experiment:**
- Hoe reageert de zwerm op sterke wind (strength = 5)?
- Bij welke wind-kracht verliest de zwerm zijn formatie?
- Voeg een **plot** toe: gemiddelde heading van zwerm vs wind-direction (blijven ze aligned?)

**Schrijf:** 400-500 woorden + 2 grafieken (zwerm met/zonder wind, plot heading vs wind)
```

```{exercise} Opdracht 2: Subgroepen en leiders
:label: verd-boids-2

**Complexiteit: niet alle boids zijn gelijk**

In echte zwermen hebben sommige individuen meer **invloed** (ervaren vogels). Implementeer **leiders**.

**Aanpak:**
1. Bij setup: Maak 10% van boids `leader` (nieuwe boolean variabele)
2. Geef leiders andere kleur (groen) en groter size
3. In `align`: Normale boids letten **2× zoveel** op leiders:
   ```scheme
   ; Bereken gewogen gemiddelde heading
   let leader-weight 2
   let follower-weight 1
   ; ... implementeer gewogen mean ...
   ```
4. Leiders bewegen iets sneller (`forward 1.2` vs `forward 1`)

**Onderzoek:**
- Kan een kleine groep leiders (5%) de hele zwerm sturen?
- Wat gebeurt er als leiders verschillende richtingen kiezen? (Zwerm splitst?)
- Voeg een `target` toe (bijv. groene patch) waar leiders naartoe vliegen. Volgt de zwerm?

**Schrijf:** 500-600 woorden + vergelijkingstabel (zwerm met/zonder leiders)
```

```{exercise} Opdracht 3: 3D-zwermen
:label: verd-boids-3

**Van 2D naar 3D: vogels vliegen niet vlak!**

NetLogo ondersteunt 3D (NetLogo 3D). Pas boids aan naar 3D-ruimte.

**Stappen:**
1. Download NetLogo 3D
2. Pas regels aan:
   - Separatie/uitlijning/cohesie werken met `distance` (3D) in plaats van 2D
   - Gebruik `pitch` (op/neer) naast `heading` (links/rechts)
3. Visualisatie: Gebruik `setxyz` in plaats van `setxy`

**Nieuwe uitdaging:**
- Voeg **hoogte-preferentie** toe: Boids willen op hoogte ~50 blijven (simuleer luchtdruk)
- Roofdier vliegt **van boven** (duikvlucht): Hoe reageert zwerm?

**Lastig!** Dit is een flinke stap. Verwacht 6-8 uur werk.

**Schrijf:** 600-800 woorden + beschrijving van 3D-zwerm (verschillende perspectieven)
```

```{exercise} Opdracht 4: Machine learning optimalisatie
:label: verd-boids-4

**Geavanceerd: vind optimale parameters met algoritme**

In plaats van handmatig experimenteren, laat een **algoritme** de beste parameters vinden.

**Aanpak (Genetic Algorithm):**
1. Start met 20 random parameter-sets (bijv. `[max-cohere-turn, max-align-turn, max-separate-turn]`)
2. Run elke set 100 ticks, bereken "fitness" (bijv. compactheid + uitlijning)
3. Selecteer top 10 (beste fitness)
4. "Muteer" deze 10 (verander parameters iets) → nieuwe 20 sets
5. Herhaal 50 generaties

**Output:** Welke parameter-set scoort het beste?

**Tools:** Gebruik NetLogo's BehaviorSpace + Python-script (of spreadsheet) voor analyse.

**Zeer uitdagend!** Verwacht 10+ uur werk. Geschikt voor VWO-eindproject.

**Schrijf:** 800-1000 woorden + convergentie-grafiek (fitness per generatie)
```

---

## VWO-variant voor eindproject

Wil je boids gebruiken voor je **eindopdracht**? Zo maak je het VWO-waardig.

### Minimale eisen eindproject (recap hoofdstuk 6)

- Werkend model met minimaal 3 regels
- Parameter-sweep (minimaal 15 runs)
- Verificatie (3+ checks)
- Validatie (kwalitatief of beter)
- Verslag (IMRAD-structuur)

### Boids: VWO-niveau opties

#### Optie A: Biologische validatie (Experimenteel)

**Doel:** Vergelijk model met échte zwermen (vogels/vissen).

**Aanpak:**
1. Verzamel video's van echte zwermen (YouTube: "starling murmuration", "fish school")
2. Analyseer: Hoe dicht vliegen ze? Hoe snel reageren ze?
3. Kalibreer je model: Pas parameters aan tot gedrag overeenkomt
4. Kwantitatief: Meet afstanden in video vs model (gebruik ImageJ of Python OpenCV)

**Pluspunten:**
- Echte data-analyse (wetenschappelijk sterk)
- Interdisciplinair (biologie + computational science)

**Minpunten:**
- Tijdrovend (video-analyse = veel werk)
- Technisch uitdagend (beeldanalyse-software leren)

#### Optie B: Robotica-toepassing (Toegepast)

**Doel:** Programmeer drone-zwerm met boids-regels.

**Aanpak:**
1. Gebruik simulator (bijv. Webots, Gazebo, of ROS)
2. Implementeer boids-regels in Python/C++
3. Test: Kunnen 5 drones synchroon vliegen zonder botsingen?
4. Voeg missie toe: Drones zoeken naar target, blijven in formatie

**Pluspunten:**
- Praktische toepassing (relevant voor industrie)
- Leert echte programmeertalen (Python)

**Minpunten:**
- Veel technische setup (simulator installeren)
- Debugging is lastiger dan in NetLogo

#### Optie C: Complexe omgeving (Wiskundig)

**Doel:** Onderzoek hoe zwermen navigeren in complexe omgevingen.

**Aanpak:**
1. Bouw doolhof met obstakels
2. Onderzoek: Hoe vindt zwerm de uitgang?
3. Voeg "pheromone trails" toe (zoals mieren): Boids leggen spoor, anderen volgen
4. Optimalisatie: Wat is snelste weg door doolhof?

**Pluspunten:**
- Wiskundige diepgang (pad-optimalisatie, graph theory)
- Combineert boids + mieren-model (interdisciplinair binnen ABM)

**Minpunten:**
- Abstracte onderzoeksvraag (minder visueel spectaculair)

### Hoe kies je?

**Vraag jezelf af:**
1. **Interesse:** Biologie, robotica, of wiskunde?
2. **Vaardigheden:** Kun je video's analyseren? Wil je Python leren?
3. **Tijd:** Hoeveel weken heb je? (Optie B = meeste tijd)
4. **Beschikbare middelen:** Heb je toegang tot drones/simulators? (Optie B)

**Advies:** Start met **basismodel** (zoals in dit hoofdstuk), voeg dan **1 grote uitbreiding** toe (roofdieren OF obstakels OR leiders). Dat is genoeg voor VWO-niveau.

### Checklist VWO-niveau

- [ ] Model heeft minimaal **5 regels** (3 basis + 2 uitbreidingen)
- [ ] Minimaal **2 parameter-sweeps** uitgevoerd (niet 1)
- [ ] **Kwantitatieve validatie** (vergelijk met echte data/literatuur)
- [ ] **Sensitiviteitsanalyse** gedaan (welke parameters zijn cruciaal?)
- [ ] Verslag **> 8 pagina's**, met grondige discussie
- [ ] **Bronnenlijst** met minimaal 3 wetenschappelijke artikelen

---

**Conclusie:** Boids is een **klassieker** om goede reden. Het toont kracht van simpele regels, is eindeloos uitbreidbaar, en leert je fundamentele principes van zelforganisatie. Of je nu films maakt, drones programmeert, of biologie bestudeert: boids-principes komen overal terug. Veel succes

