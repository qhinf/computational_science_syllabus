(hoofdstukken/03_netlogo_basis)=
# NetLogo basis: wereld, patches, turtles

Je hebt in hoofdstuk 1 en 2 geleerd hoe je een fenomeen ontleedt in agents, regels en parameters. Nu wordt het tijd om dit te bouwen! In dit hoofdstuk maak je kennis met **NetLogo**, een programmeertaal speciaal ontworpen voor Agent-Based Modeling. Je leert de basis: hoe maak je agents (turtles), hoe beweeg je ze, hoe stel je de omgeving in (patches), en hoe meet je wat er gebeurt. Aan het eind bouw je je eerste werkende model: een random walk met metingen. Dit is de fundering voor alle modellen die volgen.

**Leerdoel:** Na dit hoofdstuk kun je NetLogo installeren, een eenvoudig model bouwen met turtles en patches, en metingen doen met monitors en plots.

## Inhoud

In dit hoofdstuk behandelen we:

- NetLogo downloaden en installeren
- NetLogo interface: Code/Interface/Info, buttons en sliders
- Setup/go en ticks: het hart van elk model
- Turtles: agents maken, bewegen, random gedrag
- Patches: de omgeving met kleuren en waarden
- Monitors en eenvoudige plots
- Mini-model: random walk met meetwaarde

---

## NetLogo downloaden en installeren

**Wat is NetLogo?**

NetLogo is een programmeeromgeving specifiek voor Agent-Based Modeling. Het is gratis, open-source, en werkt op Windows, macOS en Linux. NetLogo maakt het makkelijk om honderden agents te simuleren zonder dat je expert-programmeur hoeft te zijn.

**Downloaden en installeren:**

1. Ga naar [https://ccl.northwestern.edu/netlogo/](https://ccl.northwestern.edu/netlogo/)
2. Klik op "Download" (versie 6.4 of hoger)
3. Kies je besturingssysteem (Windows/Mac/Linux)
4. Download en installeer zoals gebruikelijk
5. Start NetLogo

**Eerste indruk:**

Als je NetLogo opent, zie je drie tabbladen bovenin: **Interface**, **Info** en **Code**. Dit zijn de drie kernonderdelen van elk NetLogo-model.


:::{tip}
**NetLogo Models Library**  
NetLogo komt met honderden voorbeeldmodellen! Ga naar File → Models Library om ze te verkennen. Kijk bijvoorbeeld eens naar "Biology → Ants" of "Social Science → Segregation". Je kunt leren door andermans code te bekijken.
:::

---

## NetLogo interface: Code/Interface/Info, buttons en sliders

### De drie tabbladen

1. **Interface:** Hier zie je je model in actie. De wereld (het grid), buttons om het model te starten/stoppen, sliders voor parameters, en monitors/plots voor metingen.

2. **Code:** Hier schrijf je de programmacode. Alle regels voor agents en omgeving staan hier.

3. **Info:** Hier schrijf je uitleg over je model: wat doet het, hoe werkt het, welke vragen beantwoord je ermee? Dit is belangrijk voor verslaglegging.

### Interface-elementen toevoegen

Op het Interface-tabblad kun je elementen toevoegen door rechts te klikken:

- **Button:** Een knop om code uit te voeren (bijv. "setup" of "go")
- **Slider:** Een schuifbalk om parameters in te stellen (bijv. "aantal-mieren")
- **Monitor:** Toont een enkele waarde (bijv. "gemiddelde-energie")
- **Plot:** Een grafiek die waarden over tijd toont
- **Switch:** Aan/uit schakelaar (bijv. "toon-sporen?")
- **Chooser:** Dropdown-menu met keuzes
- **Input:** Tekstveld voor invoer

**Toevoegen van een button:**

1. Klik rechts op Interface en kies "Button"
2. Klik ergens op het Interface om de button te plaatsen
3. Vul in: Commands: `setup` (de naam van de procedure)
4. Vink aan: "Forever" (nee voor setup, ja voor go)
5. Klik OK

**Toevoegen van een slider:**

1. Klik rechts en kies "Slider"
2. Plaats de slider
3. Vul in:
   - Global variable: `aantal-turtles`
   - Minimum: 1
   - Maximum: 200
   - Increment: 1
   - Value: 50 (startwaarde)
4. Klik OK


:::{tip}
**Naamgeving in NetLogo**  
NetLogo gebruikt `kebab-case` voor namen: woorden gescheiden door streepjes. Dus `aantal-turtles`, niet `aantalTurtles` of `aantal_turtles`. Dit is de standaard-conventie.
:::

---

## Setup/go en ticks: het hart van elk model

Elk NetLogo-model heeft twee kernprocedures: **setup** en **go**.

### Setup: de beginsituatie

De `setup` procedure maakt de wereld klaar en creëert agents. Dit is als het opzetten van een bordspel: pionnen plaatsen, dobbelsteen klaarzetten.

**Basis-structuur:**

```scheme
to setup
  clear-all           ; Maak alles schoon (verwijder oude agents)
  create-turtles 50   ; Maak 50 turtles aan
  reset-ticks         ; Zet tijdsteller op 0
end
```

**Wat doet dit?**

- `clear-all`: Verwijdert alle oude turtles, patches worden gereset, variabelen worden gewist
- `create-turtles 50`: Maakt 50 nieuwe turtles op willekeurige posities
- `reset-ticks`: Zet de tick-teller op 0 (essentieel voor plots!)

### Go: de simulatie laten lopen

De `go` procedure is wat er gebeurt elke tick. Dit is het "stapje verder" dat je model zet.

**Basis-structuur:**

```scheme
to go
  ask turtles [      ; Vraag alle turtles om iets te doen
    forward 1        ; Beweeg 1 stap vooruit
  ]
  tick               ; Tel 1 tijdstap verder
end
```

**Wat doet dit?**

- `ask turtles [ ... ]`: Alle turtles voeren de acties tussen [ ] uit
- `forward 1`: Elke turtle beweegt 1 cel vooruit in zijn huidige richting
- `tick`: Verhoog de tick-teller met 1 (cruciaal!)

### Buttons koppelen

Maak twee buttons op het Interface:

- **Setup button:** Commands = `setup`, Forever = uit
- **Go button:** Commands = `go`, Forever = aan

Nu kun je het model runnen:
1. Klik op "Setup" → 50 turtles verschijnen
2. Klik op "Go" → de turtles bewegen

:::{admonition} Let op
:class: warning
**Vergeet nooit `tick`!**  
Als je `tick` vergeet aan het einde van `go`, staat de tijd stil. Plots werken niet, ticks tellen niet op, en je model "hangt". Dit is een veelgemaakte fout.
:::

```{exercise} Oefening (Oefenen)
:label: oef-3-1

Maak een nieuw NetLogo-model met:

1. Een `setup` procedure die:
   - Alles schoonmaakt
   - 50 turtles aanmaakt
   - Ticks reset

2. Een `go` procedure die:
   - Alle turtles 1 stap laat bewegen
   - De tick verhoogt

3. Twee buttons op het Interface (setup en go)

Test je model: klik op setup, dan op go. Zien je turtles bewegen? Tel mee: hoeveel ticks gaat je model vooruit in 5 seconden?
```

---

## Turtles: maken, bewegen, random

Turtles zijn je agents. Ze kunnen bewegen, draaien, eigenschappen hebben, en met elkaar interacteren.

### Turtles maken

```scheme
create-turtles 100           ; Maak 100 turtles, willekeurige positie
create-turtles 10 [          ; Maak 10 turtles EN voer code uit
  set color red              ; Maak ze rood
  setxy 0 0                  ; Zet ze in het midden (x=0, y=0)
]
```

### Turtles bewegen

**Basis-bewegingen:**

```scheme
forward 1        ; Beweeg 1 stap vooruit
back 2           ; Beweeg 2 stappen achteruit
right 90         ; Draai 90 graden naar rechts (kloksgewijs)
left 45          ; Draai 45 graden naar links
```

**Naar een positie:**

```scheme
setxy 10 5       ; Ga naar coördinaten x=10, y=5
move-to patch 3 7  ; Ga naar de patch op (3, 7)
```

### Random gedrag

Om turtles willekeurig te laten bewegen, gebruik je `random`:

```scheme
to go
  ask turtles [
    right random 360      ; Draai een willekeurige hoek (0-359 graden)
    forward 1             ; Beweeg 1 stap vooruit
  ]
  tick
end
```

**Random-functies:**

- `random 10`: Geeft een random getal van 0 tot 9 (niet inclusief 10!)
- `random-float 1.0`: Geeft een random kommagetal tussen 0 en 1
- `one-of [red blue green]`: Kies willekeurig één optie uit de lijst

**Voorbeeld: random walk (willekeurige wandeling)**

```scheme
to setup
  clear-all
  create-turtles 20 [
    set color blue
    set size 2           ; Maak ze iets groter (standaard = 1)
  ]
  reset-ticks
end

to go
  ask turtles [
    right random 360     ; Draai willekeurige richting
    forward 1            ; Beweeg 1 stap
    
    ; Als je de rand raakt, stuit terug
    if xcor > max-pxcor or xcor < min-pxcor [ set heading (- heading) ]
    if ycor > max-pycor or ycor < min-pycor [ set heading (180 - heading) ]
  ]
  tick
end
```

**Wat gebeurt hier?**

- Turtles draaien elke tick een random hoek
- Ze bewegen 1 stap
- Als ze de rand van de wereld raken, "stuiteren" ze terug


:::{tip}
**Turtles volgen**  
Rechtermuisknop op een turtle → "Watch" om die turtle te volgen. Super handig om te zien wat één individuele turtle doet. Klik "Reset Perspective" om terug te gaan naar de normale weergave.
:::

---

## Patches: de omgeving met kleuren en waarden

Patches zijn de cellen van je grid. Ze vormen de omgeving waarin turtles bewegen. Patches kunnen eigenschappen hebben en kleuren.

### Patches aanpassen

```scheme
ask patches [
  set pcolor green         ; Maak alle patches groen
]

ask patch 0 0 [            ; Vraag één specifieke patch
  set pcolor red           ; Maak die patch rood
]
```

### Patches met waarden

Patches kunnen variabelen hebben:

```scheme
patches-own [
  voedsel-niveau           ; Elke patch heeft een voedsel-waarde
]

to setup
  clear-all
  ask patches [
    set voedsel-niveau random 100    ; Random waarde 0-99
    set pcolor scale-color green voedsel-niveau 0 100
    ; Hoe hoger voedsel-niveau, hoe groener
  ]
  reset-ticks
end
```

**`scale-color` uitleg:**

- `scale-color green voedsel-niveau 0 100`
- Maak de patch een tint groen, afhankelijk van de waarde
- Waarde 0 = lichtgroen, waarde 100 = donkergroen

### Patches en turtles: interactie

Turtles kunnen eigenschappen van hun patch opvragen:

```scheme
to go
  ask turtles [
    ; Als de patch waar ik sta voedsel heeft...
    if [voedsel-niveau] of patch-here > 50 [
      set color yellow      ; Word geel (ik heb voedsel gevonden!)
    ]
    forward 1
  ]
  tick
end
```

**Belangrijk:**

- `patch-here`: De patch waar deze turtle nu staat
- `[voedsel-niveau] of patch-here`: Vraag het voedsel-niveau van mijn huidige patch

### Voorbeeld: mieren zoeken voedsel (simpele versie)

```scheme
patches-own [voedsel?]      ; Boolean: heeft deze patch voedsel?

to setup
  clear-all
  
  ; Maak omgeving
  ask patches [
    set pcolor brown         ; Grond is bruin
    set voedsel? false       ; Er is geen voedsel
  ]
  
  ; Plaats voedsel op 10 random plekken
  ask n-of 10 patches [
    set voedsel? true
    set pcolor green         ; Voedsel is groen
  ]
  
  ; Maak mieren
  create-turtles 30 [
    set color red
    set shape "bug"          ; Verander vorm naar insect
  ]
  
  reset-ticks
end

to go
  ask turtles [
    ; Random walk
    right random 60 - 30     ; Draai -30 tot +30 graden
    forward 1
    
    ; Check: sta ik op voedsel?
    if [voedsel?] of patch-here [
      set color orange       ; Word oranje (ik heb voedsel!)
    ]
  ]
  tick
end
```


:::{admonition} Let op: scope en ask
:class: warning
**Veelgemaakte fout: scope-verwarring**

```scheme
; FOUT:
ask turtles [
  set pcolor red     ; ERROR: turtles hebben geen pcolor!
]

; GOED:
ask turtles [
  ask patch-here [   ; ASK de patch waar ik sta
    set pcolor red   ; NU kun je pcolor aanpassen
  ]
]
```

Onthoud: `ask` bepaalt de context. Binnen `ask turtles` werk je met turtle-eigenschappen. Binnen `ask patches` werk je met patch-eigenschappen.
:::

---

## Monitors en eenvoudige plots

Je hebt nu agents die bewegen. Maar wat gebeurt er eigenlijk? Tijd om te **meten**.

### Monitors: huidige waarde

Een monitor toont één getal.

**Monitor toevoegen op Interface:**

1. Rechtermuisknop → "Monitor"
2. Plaats de monitor
3. Vul in: Reporter: `count turtles`
4. Klik OK

**Nuttige reporters:**

```scheme
count turtles                    ; Hoeveel turtles zijn er?
count turtles with [color = red] ; Hoeveel rode turtles?
mean [xcor] of turtles           ; Gemiddelde x-positie van turtles
max [voedsel-niveau] of patches  ; Hoogste voedsel-waarde
ticks                            ; Hoeveel ticks zijn verstreken?
```

### Plots: verloop over tijd

Een plot toont hoe iets verandert.

**Plot toevoegen:**

1. Rechtermuisknip → "Plot"
2. Geef een naam: "Aantal turtles over tijd"
3. X-axis label: "Ticks"
4. Y-axis label: "Aantal"
5. Klik op de "pen" (potlood-icoon) en voeg een plot-pen toe:
   - Name: "turtles"
   - Plot pen code: `plot count turtles`
6. Klik OK

Nu zie je elke tick een punt in de grafiek verschijnen!

**Meerdere lijnen in één plot:**

```scheme
; In plot-pen 1: rode turtles
plot count turtles with [color = red]

; In plot-pen 2: blauwe turtles  
plot count turtles with [color = blue]
```

### Voorbeeld: energie-model

Laten we een model maken waar turtles energie verliezen en sterven als energie = 0.

```scheme
turtles-own [energie]    ; Elke turtle heeft een energie-waarde

to setup
  clear-all
  create-turtles 50 [
    set energie 100      ; Start met 100 energie
    set color green
  ]
  reset-ticks
end

to go
  ask turtles [
    forward 1
    set energie energie - 1   ; Verlies 1 energie per tick
    
    ; Als energie op is, sterf
    if energie <= 0 [
      die                ; Verwijder deze turtle
    ]
    
    ; Kleur geeft energie aan: groen=vol, rood=leeg
    set color scale-color red energie 0 100
  ]
  
  ; Stop als alle turtles dood zijn
  if not any? turtles [ stop ]
  
  tick
end
```

**Metingen toevoegen:**

- **Monitor 1:** `count turtles` (hoeveel leven er nog?)
- **Monitor 2:** `mean [energie] of turtles` (gemiddelde energie)
- **Plot:** Laat beide waarden over tijd zien

```{exercise} Oefening (Toepassen)
:label: oef-3-2

Pas je model uit Oefening 3.1 aan:

1. Voeg een turtle-eigenschap toe: `energie` (start = 100)
2. Elke tick: turtle verliest 1 energie
3. Als energie ≤ 0: turtle sterft (`die`)
4. Voeg een monitor toe: `mean [energie] of turtles`
5. Voeg een plot toe met twee lijnen:
   - Aantal turtles over tijd
   - Gemiddelde energie over tijd

Run je model. Wat zie je gebeuren? Na hoeveel ticks zijn alle turtles dood? Waarom?
```

---

## Mini-model: random walk met meetwaarde

Laten we alles samenvoegen in een compleet mini-model: **Random Walk met Verspreiding**.

**Onderzoeksvraag:** Hoe ver verspreiden turtles zich vanaf het centrum in een random walk? Hangt dit af van het aantal turtles?

### Code

```scheme
turtles-own [
  start-x              ; Onthoud waar turtle startte
  start-y
]

to setup
  clear-all
  
  ; Maak achtergrond zwart
  ask patches [ set pcolor black ]
  
  ; Maak turtles in het midden
  create-turtles aantal-turtles [   ; aantal-turtles = slider
    setxy 0 0                       ; Start in centrum
    set start-x 0
    set start-y 0
    set color yellow
    pen-down                        ; Laat spoor achter
  ]
  
  reset-ticks
end

to go
  ask turtles [
    right random 360                ; Willekeurige richting
    forward 1
  ]
  
  tick
  
  ; Stop na 1000 ticks
  if ticks >= 1000 [ stop ]
end

; Reporter: gemiddelde afstand tot centrum
to-report gemiddelde-afstand
  ifelse any? turtles [
    report mean [distancexy start-x start-y] of turtles
  ] [
    report 0
  ]
end

; Reporter: maximale afstand
to-report max-afstand
  ifelse any? turtles [
    report max [distancexy start-x start-y] of turtles
  ] [
    report 0
  ]
end
```

### Interface-elementen

1. **Slider:** `aantal-turtles` (min=1, max=100, increment=1, value=20)
2. **Button:** `setup`
3. **Button:** `go` (Forever = aan)
4. **Monitor 1:** `gemiddelde-afstand`
5. **Monitor 2:** `max-afstand`
6. **Plot:** "Verspreiding over tijd"
   - Pen 1: `plot gemiddelde-afstand` (kleur: blauw)
   - Pen 2: `plot max-afstand` (kleur: rood)

### Experimenteren

1. Run met aantal-turtles = 20
2. Noteer: gemiddelde-afstand na 1000 ticks
3. Run met aantal-turtles = 50
4. Vergelijk: is er verschil?

**Verwachting:** Gemiddelde-afstand zou vergelijkbaar moeten zijn (random walk is random!), maar max-afstand is groter met meer turtles (meer kans op "lucky wanderer").


```{exercise} Oefening (Reflecteren)
:label: oef-3-3

Beantwoord de volgende vragen in 3-5 zinnen per vraag:

**a)** In het random walk model hierboven: welke variabelen zijn **parameters** (inputs die je instelt), en welke zijn **outputs** (metingen)? Noem minimaal 2 van elk.

**b)** Het model gebruikt `pen-down` om sporen te tonen. Dit is visueel handig, maar kost rekenkracht. Als je 1000 turtles zou hebben, zou je `pen-down` gebruiken? Waarom wel/niet?

**c)** Stel je voegt een regel toe: "Als turtle de rand raakt, teleporteer naar het centrum". Hoe verandert dit de output `gemiddelde-afstand`? Wordt die hoger, lager, of blijft het hetzelfde? Beredeneer.
```

---

## Verdiepende opgaven

Klaar voor uitdaging? Probeer deze opdrachten om je NetLogo-vaardigheden te verdiepen.

```{exercise} Opdracht (Predator-prey basis)
:label: verd-3-1

Bouw een eenvoudig **predator-prey model** (roofdier-prooi):

- **Prooien (groene turtles):** Bewegen random, vermenigvuldigen zich met kans 5% per tick
- **Roofdieren (rode turtles):** Bewegen random, eten prooien (als ze op dezelfde patch staan), verliezen energie, sterven als energie = 0

Implementeer:
1. Setup met 50 prooien, 10 roofdieren
2. Prooien: `right random 60 - 30`, `forward 1`, met kans 5%: `hatch 1` (maak kopie)
3. Roofdieren: energie start=50, -1 per tick, +20 als ze prooi eten
4. Plot: Aantal prooien (groen) en aantal roofdieren (rood) over tijd

Experimenteer: Bij welke start-waarden overleven beide soorten? Bij welke sterft één uit?
```

```{exercise} Opdracht (Heatmap van beweging)
:label: verd-3-2

Maak een model dat bijhoudt **waar turtles het meest zijn geweest**:

1. Setup: 20 turtles, random walk
2. Elke patch heeft variabele `bezoeken` (aantal keren dat een turtle hier was)
3. Elke tick: verhoog `bezoeken` van de patch waar turtle staat met 1
4. Kleur patches op basis van `bezoeken`: blauw (weinig) → rood (veel)

Gebruik: `set pcolor scale-color red bezoeken 0 100`

Vraag: Welk patroon zie je ontstaan na 500 ticks? Is het uniform, of zijn er "hotspots"? Waarom?

Schrijf 200-250 woorden met je observaties en verklaring.
```

````{exercise} Opdracht (Debug challenge)
:label: verd-3-3

De volgende code bevat **3 fouten**. Vind en corrigeer ze:

```scheme
turtles-own [leeftijd]

to setup
  clear-all
  create-turtles 50
    set leeftijd 0        ; Fout 1: scope probleem
    set color blue
  ]
  reset-ticks
end

to go
  ask turtles [
    forward 1
    set leeftijd + 1      ; Fout 2: syntax probleem
  ]
  ask patches [
    set color red         ; Fout 3: verkeerde attribuutnaam
  ]
end
```

Leg voor elke fout uit: (1) wat is fout? (2) waarom geeft dit een error of verkeerd gedrag? (3) hoe repareer je het?
````

---

## PO-mijlpaal

Na dit hoofdstuk ben je klaar voor de derde mijlpaal: een werkend model-skelet in NetLogo.

### Wat lever je op na deze fase?

Een NetLogo-bestand (.nlogo) met de **basis-structuur van je eindproject**:

1. **Code:**
   - Werkende `setup` procedure (maakt je agents en omgeving)
   - Werkende `go` procedure (agents bewegen/handelen, tick wordt verhoogd)
   - Minimaal 1 turtle-eigenschap (bijv. `energie`, `besmet?`)
   - Minimaal 1 patch-eigenschap (optioneel, als relevant voor je model)

2. **Interface:**
   - Button: "Setup"
   - Button: "Go" (Forever = aan)
   - Slider: 1 parameter die je in je onderzoek wilt variëren (bijv. `aantal-agents`, `besmettingskans`)
   - Monitor: 1 output-meting (bijv. `count turtles`, `mean [energie] of turtles`)
   - Plot: 1 grafiek die een output over tijd toont (of placeholder met titel)

3. **Info:**
   - Je naam en datum
   - Korte beschrijving (3-5 zinnen): Wat modelleer je? Welke onderzoeksvraag?
   - Lijst van je parameters en outputs

### Checklist: je bent klaar als…

- [ ] Je model start foutloos met "Setup" (geen error messages)
- [ ] Je model loopt met "Go" zonder vast te lopen of crashes
- [ ] Je agents doen **iets** zichtbaars (bewegen, kleur veranderen, sterven, etc.)
- [ ] Je slider werkt: als je de waarde verandert en opnieuw "Setup" doet, zie je het effect
- [ ] Je monitor toont een **dynamische** waarde (verandert tijdens "Go")
- [ ] Je plot tekent een lijn (ook al is deze nog simpel)
- [ ] Je code bevat **comments** (regels die starten met `;`) om uit te leggen wat er gebeurt
- [ ] Het Info-tabblad is ingevuld (naam, onderzoeksvraag, korte uitleg)

### Waar komt dit terug in je eindproject?

Dit skelet is de **technische basis** van je hele project:

- **Hoofdstuk 4:** Je gaat dit model uitbreiden met de regels uit je conceptuele canvas (hoofdstuk 2)
- **Hoofdstuk 5:** Je gaat experimenteren met parameters en data verzamelen
- **Hoofdstuk 6:** Je gaat je model valideren en verfijnen
- **Eindverslag:** Code-snippets en grafieken komen uit dit model

**Tips voor succes:**

- **Start simpel:** Bouw eerst een werkende basis, voeg dan stap voor stap features toe
- **Test vaak:** Klik na elke wijziging op "Check" (in Code-tabblad) om syntax-errors te vinden
- **Sla op:** Gebruik Save As en bewaar verschillende versies (model-v1.nlogo, model-v2.nlogo)
- **Vraag hulp:** Als je vast zit, kijk in de NetLogo Models Library naar vergelijkbare modellen

---

**Volgende stap:** In hoofdstuk 4 ga je je conceptuele model uit hoofdstuk 2 implementeren in NetLogo. Je vertaalt je als-dan regels naar code, voegt interacties toe tussen agents, en bouwt je volledige model. Het wordt echt!
