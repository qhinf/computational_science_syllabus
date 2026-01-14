# Verdieping: Segregatie - Schelling's model van woonwijken

Waarom ontstaan er etnische buurten in steden? Kan segregatie ontstaan zonder dat mensen racistisch zijn? En hoe beïnvloedt een kleine voorkeur voor "eigen groep" de hele samenleving? Dit hoofdstuk duikt in **Schelling's segregatiemodel** (1971): een baanbrekende studie die won de Nobelprijs Economie (2005). Met verrassend simpele regels ontstaat sterke segregatie. Je leert dit model implementeren, uitbreiden met economische factoren en stadsplanning, en experimenteren met tolerantie-niveaus.

**Leerdoel:** Na dit hoofdstuk begrijp je hoe individuele voorkeuren leiden tot macro-segregatie, kun je Schelling's model implementeren met minimaal 2 uitbreidingen (economie, urban planning), en parameter-sweeps uitvoeren over tolerantie.

## Inhoud

In dit hoofdstuk behandelen we:

- Historische context: Schelling's model (1971) en Nobelprijs
- Conceptueel model: mild voorkeur → sterke segregatie (emergent)
- NetLogo implementatie basis-segregatie
- Uitbreiding 1: Economische factoren (rijke vs arme buurten)
- Uitbreiding 2: Urban planning (groene zones, voorzieningen)
- Parameter-sweep experiment: tolerantie vs segregatie-index
- 4 verdiepende opgaven
- VWO-variant voor eindproject

---

## Historische context: Schelling's doorbraak (1971)

### De ontdekking

In **1971** publiceerde economist **Thomas Schelling** een baanbrekend artikel: *"Dynamic Models of Segregation"*.

**Vraag:** Waarom zijn Amerikaanse steden zo gesegregeerd? (zwarte vs witte buurten)

**Gangbare verklaring (destijds):** Extreme racisme, discriminatie, wetten (zoals Jim Crow-wetten).

**Schelling's inzicht:** Segregatie kan ontstaan **zonder extreme voorkeuren**!

**Experiment (met munten):**
1. Leg een schaakbord neer
2. Plaats zwarte en witte munten random
3. Regel: "Als <30% van je buren dezelfde kleur heeft, verhuus naar een plek waar dat wel zo is"
4. Herhaal tot niemand meer wil verhuizen

**Resultaat:** Na 10-20 rondes ontstaan **homogene clusters**, ondanks milde voorkeur!

**Impact:**
- **Nobelprijs Economie** (2005): Schelling kreeg de prijs voor dit werk
- **Sociologie:** Verklaart segregatie zonder racisme te postuleren
- **Urban planning:** Invloed op beleid (diversiteit bevorderen)

[Screenshot: Schelling's originele artikel met munten op schaakbord]

### Waarom is dit controversieel?

**Probleem:** Model suggereert dat segregatie "natuurlijk" is (emergeert uit milde voorkeuren).

**Misinterpretatie:** "Dus segregatie is niet erg, het is gewoon natuurlijk!"

**Juiste interpretatie:** "Zelfs milde voorkeuren leiden tot extreme uitkomsten. Beleid moet daar rekening mee houden om diversiteit te behouden."

**Schelling zelf (1978):** "This is not a justification for segregation, but an explanation. Understanding the dynamics is essential to counter them."

### Waarom modelleren?

**Doel:** Voorspel effecten van beleid:
- Wat gebeurt er als stad sociale woningbouw verspreidt (in plaats van concentreert)?
- Hoe beïnvloeden voorzieningen (parken, scholen) menging?
- Bij welke tolerantie-drempel wordt segregatie onvermijdelijk?

---

## Conceptueel model: mild voorkeur → sterke segregatie

### Agents (bewoners)

**Eigenschappen:**
- Kleur: `red` of `blue` (representeert etnische/culturele groep, niet letterlijk huidskleur)
- Tolerantie: % buren van andere groep dat acceptabel is
- Tevredenheid: `happy` of `unhappy`

**Doel:** Woon in een buurt waar je je prettig voelt.

### Omgeving

**Grid:** Woonwijk (patches = huizen)

**States:**
- Wit: Leeg huis
- Rood/Blauw: Bezet door agent

### Regels (basis)

#### Regel 1: Check tevredenheid

**Simpel:** "Tel hoeveel van je buren dezelfde kleur hebben."

**Mechanisme:**
```scheme
let total-neighbors count neighbors with [any? turtles-here]
let similar-neighbors count neighbors with [any? turtles-here with [color = [color] of myself]]

let similarity-ratio similar-neighbors / total-neighbors

; Ben ik tevreden?
ifelse similarity-ratio >= tolerance [
  set happy? true
][
  set happy? false
]
```

**Voorbeeld:**
- Je bent rood
- 8 buren (volbezet), 5 rood, 3 blauw
- Similarity = 5/8 = 62.5%
- Als tolerance = 50% → happy!
- Als tolerance = 70% → unhappy, wil verhuizen

#### Regel 2: Verhuizen als ontevreden

**Simpel:** "Als je ontevreden bent, zoek een nieuwe plek."

**Mechanisme:**
```scheme
if not happy? [
  ; Zoek random leeg huis
  let target-patch one-of patches with [not any? turtles-here]
  
  if target-patch != nobody [
    move-to target-patch
  ]
]
```

**Belangrijk:** Agents kiezen **random** leeg huis (niet de "beste" plek). Realistische simplificatie: mensen zien niet alle huizen tegelijk.

#### Regel 3: Herhaal tot evenwicht

**Simpel:** "Blijf verhuizen tot iedereen tevreden is (of geen lege huizen meer)."

**Stop-conditie:**
```scheme
if all? turtles [happy?] or not any? patches with [not any? turtles-here] [
  stop  ; Evenwicht bereikt
]
```

### Emergent fenomeen

**Verrassende uitkomst:**

| Tolerance | Verwachting | Werkelijkheid |
|-----------|-------------|---------------|
| 30% | "Ik accepteer 70% andere groep → gemengde buurt" | **Sterke segregatie** (clusters van 80%+ zelfde kleur) |
| 50% | "Ik accepteer 50% andere groep → fifty-fifty buurt" | **Matige segregatie** (clusters van 60-70%) |
| 70% | "Ik accepteer 30% andere groep → homogene buurt" | **Totale segregatie** (100% clusters) |

**Paradox:** Milde individuele voorkeur (30%) leidt tot **extreme collectieve segregatie** (80%+).

**Mechanisme:**
1. Paar ontevreden agents verhuist → lokale concentratie neemt toe
2. Buren worden ontevreden (nu minder diversiteit) → ook verhuizen
3. **Cascade-effect:** Cluster groeit, diversiteit neemt af
4. Eindresultaat: Grote homogene clusters

:::{admonition} Let op: dit is niet deterministisch!
:class: warning
Elke run geeft een andere configuratie (random verhuizingen). Maar het **patroon** (sterke segregatie) is consistent. Dit is kenmerkend voor emergente fenomenen: verschillende details, zelfde macro-uitkomst.
:::

---

## NetLogo implementatie basis-segregatie

### Setup

```scheme
breed [residents resident]

residents-own [
  happy?       ; Boolean: tevreden met buurt?
  tolerance    ; % buren van andere groep dat OK is
]

globals [
  percent-similar  ; Gemiddelde similarity over alle agents
  percent-unhappy  ; % agents dat ontevreden is
]

to setup
  clear-all
  
  ; Maak woonwijk (patches = huizen)
  ask patches [set pcolor white]
  
  ; Plaats bewoners (random, 90% bezetting)
  ask n-of (aantal-bewoners) patches [
    sprout-residents 1 [
      ; 50/50 rood/blauw
      set color one-of [red blue]
      set shape "person"
      set size 1
      
      ; Tolerance (parameter)
      set tolerance tolerantie-niveau / 100  ; Slider 0-100, convert to 0-1
      
      ; Check initial happiness
      update-happiness
    ]
  ]
  
  update-globals
  
  reset-ticks
end
```

### Go-procedure

```scheme
to go
  ; Stop als iedereen tevreden of geen lege plekken
  if all? residents [happy?] [
    stop
  ]
  
  if not any? patches with [not any? residents-here] [
    stop  ; Geen lege huizen meer
  ]
  
  ; Vraag ontevreden agents om te verhuizen
  ask residents with [not happy?] [
    move-to-empty-patch
    update-happiness
  ]
  
  ; Update global statistieken
  update-globals
  
  tick
end
```

### Tevredenheid berekenen

```scheme
to update-happiness  ; Resident procedure
  ; Tel buren (patches met agents)
  let nearby residents-on neighbors
  
  ifelse any? nearby [
    ; Bereken similarity ratio
    let total-neighbors count nearby
    let similar-neighbors count nearby with [color = [color] of myself]
    let similarity-ratio similar-neighbors / total-neighbors
    
    ; Check tolerance
    ifelse similarity-ratio >= tolerance [
      set happy? true
      set shape "person"  ; Normale shape
    ][
      set happy? false
      set shape "person business"  ; Ontevreden shape (als beschikbaar)
    ]
  ][
    ; Geen buren → always happy (edge case)
    set happy? true
  ]
end
```

### Verhuizen

```scheme
to move-to-empty-patch  ; Resident procedure
  ; Zoek random leeg huis
  let target one-of patches with [not any? residents-here]
  
  if target != nobody [
    move-to target
  ]
end
```

### Globale statistieken

```scheme
to update-globals
  ; Bereken gemiddelde similarity
  ifelse any? residents [
    set percent-similar mean [
      let nearby residents-on neighbors
      ifelse any? nearby [
        (count nearby with [color = [color] of myself]) / (count nearby) * 100
      ][
        0
      ]
    ] of residents
  ][
    set percent-similar 0
  ]
  
  ; Bereken % ontevreden
  ifelse any? residents [
    set percent-unhappy (count residents with [not happy?]) / (count residents) * 100
  ][
    set percent-unhappy 0
  ]
end
```

### Interface-elementen

**Sliders:**
- `aantal-bewoners`: 200 (aantal bewoners)
- `tolerantie-niveau`: 30 (% zelfde kleur gewenst, 0-100)

**Buttons:**
- `setup`
- `go` (forever)
- `go-once` (go 1 tick)

**Monitors:**
- `percent-similar`: Gemiddelde similarity
- `percent-unhappy`: % ontevreden
- `ticks`: Aantal verhuisrondes

**Plot:** "Segregatie over tijd"
- X-as: ticks
- Y-as: percent-similar (stijgt naar ~80%+)

[Screenshot: NetLogo interface met rood/blauwe bewoners in clusters]

:::{tip}
**Visualisatie verbeteren:**  
Kleur patches op basis van dominante groep:
```scheme
ask patches with [any? residents-here] [
  set pcolor [color] of one-of residents-here - 2  ; Lichtere tint
]
```
Dit maakt clusters visueel duidelijker.
:::

---

## Uitbreiding 1: Economische factoren (rijke vs arme buurten)

Segregatie is niet alleen etnisch, maar ook **economisch**. Rijke mensen wonen in dure buurten, arme in goedkope.

### Conceptueel

**Nieuwe eigenschap:** Agents hebben `wealth` (rijk, midden, arm).

**Nieuwe regel:** Agents kunnen alleen verhuizen naar huizen die ze kunnen betalen.

**Effect:** Economische segregatie **versterkt** etnische segregatie (double segregation).

### Implementatie

```scheme
residents-own [
  ; ... bestaande ...
  wealth  ; 1 = arm, 2 = midden, 3 = rijk
]

patches-own [
  price  ; Huis-prijs (1-3)
]

to setup
  clear-all
  
  ; Prijs patches (wijk-structuur)
  ask patches [
    ; Centrum = duur, randen = goedkoop
    let distance-to-center distancexy 0 0
    
    ifelse distance-to-center < 10 [
      set price 3  ; Centrum: duur
      set pcolor green - 2
    ][
      ifelse distance-to-center < 20 [
        set price 2  ; Midden: middenklasse
        set pcolor green - 1
      ][
        set price 1  ; Randen: goedkoop
        set pcolor green
      ]
    ]
  ]
  
  ; Plaats bewoners met wealth
  ask n-of aantal-bewoners patches [
    sprout-residents 1 [
      set color one-of [red blue]
      set shape "person"
      
      ; Random wealth (33% per klasse)
      set wealth one-of [1 2 3]
      
      ; Visueel: size = wealth
      set size wealth * 0.5
      
      set tolerance tolerantie-niveau / 100
      update-happiness
    ]
  ]
  
  update-globals
  reset-ticks
end
```

### Verhuizen met budget

```scheme
to move-to-empty-patch  ; Resident procedure (aangepast)
  ; Zoek leeg huis dat je kunt betalen
  let affordable-patches patches with [
    not any? residents-here and
    price <= [wealth] of myself
  ]
  
  let target one-of affordable-patches
  
  if target != nobody [
    move-to target
  ]
  
  ; Als geen betaalbare huizen, blijf ontevreden (realistische constraint)
end
```

### Observaties

**Verwacht gedrag:**
- **Armen** (wealth=1) blijven in goedkope buurten (randen)
- **Rijken** (wealth=3) concentreren in centrum
- **Etnische segregatie per wijk:** Binnen arme buurten: rode vs blauwe clusters

**Double segregation:**
1. Economisch: Rijken ≠ armen (spatial segregation)
2. Etnisch: Binnen elke klasse, rood ≠ blauw (preference segregation)

**Maatschappelijke implicatie:** Arme minderheidsgroepen zijn **dubbel geïsoleerd** (arm + etnisch).

[Screenshot: Wijk met groene (goedkoop) en donkergroene (duur) patches, clustering per wealth]

---

## Uitbreiding 2: Urban planning (voorzieningen)

Steden kunnen segregatie beïnvloeden door **urban planning**: scholen, parken, sociale woningbouw.

### Conceptueel

**Nieuwe elementen:**
1. **Voorzieningen** (groene patches): Parks, scholen, bibliotheken
2. **Regel:** Agents **waarderen** buurten met voorzieningen (verhoogt tevredenheid)
3. **Beleid:** Plaats voorzieningen strategisch om diversiteit te bevorderen

### Implementatie

```scheme
patches-own [
  ; ... bestaande ...
  amenity?  ; Boolean: is dit een voorziening?
]

to setup
  ; ... bestaande code ...
  
  ; Plaats voorzieningen
  ask n-of aantal-voorzieningen patches [
    set amenity? true
    set pcolor lime  ; Groene voorziening
    
    ; Geen bewoners op voorzieningen
    if any? residents-here [
      ask residents-here [die]
    ]
  ]
  
  ; ... rest ...
end
```

### Tevredenheid met voorzieningen

```scheme
to update-happiness  ; Resident procedure (aangepast)
  ; ... bestaande similarity check ...
  
  ; Bonus: nabije voorzieningen verhogen tevredenheid
  let nearby-amenities count neighbors with [amenity?]
  
  ; Als 1+ voorziening nabij, verlaag tolerance-eis (meer tevreden)
  let adjusted-tolerance tolerance
  
  if nearby-amenities > 0 [
    set adjusted-tolerance tolerance - 0.1  ; 10% toleranter
  ]
  
  ; Check met adjusted tolerance
  ifelse similarity-ratio >= adjusted-tolerance [
    set happy? true
  ][
    set happy? false
  ]
end
```

### Beleid-experimenten

**Scenario A: Centrale voorzieningen**
- Plaats alle parken in centrum (bij rijke buurten)
- **Effect:** Rijken blijven, armen hebben geen toegang → segregatie blijft

**Scenario B: Verspreide voorzieningen**
- Plaats parken verspreid (ook in arme buurten)
- **Effect:** Arme buurten worden aantrekkelijker → diversiteit neemt toe

**Scenario C: Sociale woningbouw**
- Forceer dat 20% van huizen in dure buurten "price = 1" wordt (betaalbaar)
- **Effect:** Armen kunnen naar centrum → economische menging

**Experiment:** Welk scenario leidt tot minste segregatie?

---

## Parameter-sweep experiment: tolerantie vs segregatie-index

### Onderzoeksvraag

**Vraag:** Hoe beïnvloedt individuele tolerantie de mate van segregatie in de wijk?

**Hypothese:** Lage tolerantie → hoge segregatie, maar zelfs bij hoge tolerantie (bijv. 50%) ontstaat nog steeds segregatie.

### Experimentopzet

**Variabele parameter:** `tolerantie-niveau` (%)  
**Range:** 10, 20, 30, 40, 50, 60, 70, 80%  
**Constante parameters:**
- `aantal-bewoners = 200`
- 50/50 rood/blauw
- 90% bezettingsgraad

**Output:**
- **Segregatie-index:** Gemiddelde similarity na evenwicht (%)
- **Tijd tot evenwicht:** Aantal ticks tot iedereen tevreden

**Runs:** 5 runs per waarde × 8 waarden = 40 runs  
**Duur:** Run tot evenwicht (max 1000 ticks)

### Resultaten (hypothetisch)

| Tolerantie | Gem. segregatie-index | SD | Tijd tot evenwicht | Observatie |
|------------|-----------------------|----|--------------------|------------|
| 10% | 95.2% | 2.1 | 45 ticks | Extreme segregatie, snel evenwicht |
| 20% | 91.3% | 3.4 | 68 ticks | Zeer sterke segregatie |
| 30% | 84.7% | 4.2 | 112 ticks | Sterke segregatie (!) |
| 40% | 76.5% | 5.1 | 185 ticks | Matige segregatie |
| 50% | 68.2% | 6.3 | 290 ticks | Nog steeds segregatie |
| 60% | 61.4% | 7.8 | 450 ticks | Lichte segregatie |
| 70% | 58.1% | 9.2 | 680 ticks | Minimale segregatie |
| 80% | 56.3% | 11.5 | 920 ticks | Bijna geen segregatie |

[Screenshot: Grafiek met tolerantie op x-as, segregatie-index op y-as, afnemende curve]

### Interpretatie

**Kernbevinding:** Zelfs bij **30% tolerantie** (= "ik accepteer 70% andere groep") ontstaat **84.7% segregatie**!

**Mechanisme (cascade-effect):**
1. Bij 30% tolerantie zijn meeste agents aanvankelijk tevreden
2. Paar ontevreden agents verhuist → lokale concentratie stijgt
3. Buren worden net ontevreden (was 35% similar, nu 28%) → verhuizen ook
4. **Domino-effect:** Steeds meer agents verhuizen, clusters groeien
5. Eindresultaat: Sterke segregatie ondanks milde voorkeur

**Tijd-observatie:** Hogere tolerantie → **langer tot evenwicht**:
- Lage tolerantie: Veel ontevreden, snelle verhuizingen → snel evenwicht
- Hoge tolerantie: Weinig ontevreden, langzame cascade → traag evenwicht

**Validatie:** Schelling's originele bevindingen (1971) komen overeen: 30-40% tolerantie geeft 70-80% segregatie. **Ons model klopt!**

**Maatschappelijke implicatie:** Segregatie is **niet per se het gevolg van intolerantie**. Zelfs matig tolerante mensen creëren gesegregeerde samenleving. Beleid moet hier actief tegenwerken.

:::{admonition} Let op: modellen ≠ excuses
:class: warning
Dit model verklaart hoe segregatie ontstaat, maar **rechtvaardigt** het niet. Begrijpen ≠ goedkeuren. Het toont juist waarom **actief beleid** (zoals sociale woningbouw, diverse scholen) nodig is om segregatie tegen te gaan.
:::

---

## Verdiepende opgaven

```{exercise} Opdracht 1: Multi-groep segregatie
:label: verd-seg-1

**Realisme: niet twee, maar vijf groepen**

Echte steden hebben tientallen groepen (etniciteiten, leeftijden, religies).

**Implementatie:**
1. Agents hebben `color` uit 5 opties: `red`, `blue`, `green`, `yellow`, `pink`
2. Tolerance blijft hetzelfde: "Ik wil minimaal X% van mijn groep"
3. Run en observeer

**Vraag:** Ontstaat er segregatie per groep? Of mengen sommige groepen wel?

**Geavanceerd:** Geef groepen verschillende tolerantie-levels:
- Groep A (rood): tolerantie = 20% (intolerant)
- Groep B (blauw): tolerantie = 60% (tolerant)

**Hypothese:** Intolerante groep segregeert sterk, tolerante groep mengt. Test dit!

**Schrijf:** 500-600 woorden + vergelijkingstabel (2 groepen vs 5 groepen)
```

```{exercise} Opdracht 2: Gentrificatie-dynamiek
:label: verd-seg-2

**Actueel: waarom worden arme buurten duur?**

**Gentrificatie** = proces waarbij rijkere mensen arme buurt binnenkomen → prijzen stijgen → armen vertrekken.

**Implementatie:**
1. Start met arme buurt (price=1, bewoners wealth=1)
2. Per 50 ticks: 5 rijke agents (wealth=3) verhuizen naar deze buurt (attractie: lage prijzen, maar centraal)
3. Als >30% van bewoners rijk is: huizenprijzen stijgen (price → 2)
4. Arme agents kunnen niet meer betalen → vertrekken

**Dynamiek:**
- Fase 1: Arme buurt, homogeen
- Fase 2: Rijken komen (menging)
- Fase 3: Prijzen stijgen, armen weg (nieuwe homogeniteit, maar rijk)

**Onderzoek:** Bij welke snelheid van gentrificatie (aantal rijken/tick) blijft diversiteit behouden?

**Schrijf:** 600-700 woorden + tijdreeks-grafiek (wealth-samenstelling per 100 ticks)
```

```{exercise} Opdracht 3: Beleid-interventies testen
:label: verd-seg-3

**Toegepast: werkt anti-segregatie-beleid?**

Test 3 beleidsinterventies:

**Beleid A: Quota (verplichte diversiteit)**
- Per wijk (10×10 grid-sectie): Maximaal 60% van één kleur
- Als >60%: Verhuizing naar die wijk is geblokkeerd voor die kleur
- Effect op segregatie?

**Beleid B: Subsidie voor menging**
- Agents krijgen "bonus tevredenheid" als ze wonen in diverse buurt (50/50)
- Implementatie: Verlaag tolerance-eis met 20% als buurt diverse is
- Effect?

**Beleid C: Geforceerde menging (controversieel)**
- Bij setup: Plaats rood/blauw in checkerboard-patroon (perfect gemengd)
- Laat model runnen: Blijft menging, of ontstaat segregatie alsnog?

**Evaluatie:** Welk beleid is meest effectief? Welk is meest realistisch/uitvoerbaar?

**Schrijf:** 700-800 woorden + vergelijkingstabel 3 beleidsscenario's
```

```{exercise} Opdracht 4: Empirische validatie (Amsterdam)
:label: verd-seg-4

**Real-world: vergelijk met echte stad**

Gebruik data van Amsterdam (of je eigen stad).

**Data-bronnen:**
- CBS (Centraal Bureau Statistiek): Buurtgegevens per postcode
- Amsterdam.nl: Open data portal (etnische samenstelling per buurt)

**Aanpak:**
1. Verzamel: Welke buurten zijn gesegregeerd? (bijv. % niet-westers per buurt)
2. Kalibreer model: Pas parameters aan tot model-output overeenkomt met echte segregatie-index
3. Voorspel: Als tolerance daalt met 10% (bijv. door politieke polarisatie), wat gebeurt er?

**Validatie-metrics:**
- **Dissimilarity index:** Standaard maat voor segregatie (D = 0: perfect gemengd, D = 1: totaal gescheiden)
- Formule (complex): $D = \frac{1}{2} \sum_i \left| \frac{r_i}{R} - \frac{b_i}{B} \right|$
  (Waar $r_i$ = rood in buurt $i$, $R$ = totaal rood, etc.)

**Zeer geavanceerd en maatschappelijk relevant!**

**Schrijf:** 1000-1200 woorden + kaart (echte segregatie Amsterdam) + model-validatie-grafiek
```

---

## VWO-variant voor eindproject

### Waarom segregatie voor VWO?

**Sterke punten:**
1. **Nobelprijs-waardig onderwerp:** Direct wetenschappelijke relevantie
2. **Interdisciplinair:** Economie, sociologie, geografie, wiskunde
3. **Actueel:** Segregatie is hot topic in Nederland (rapport Sociaal Cultureel Planbureau 2024)
4. **Kwantitatief:** Duidelijke metrics (segregatie-index, dissimilarity)

### VWO-niveau aanpak

#### Optie A: Kwantitatieve validatie met CBS-data

**Doel:** Vergelijk model met echte Nederlandse steden.

**Methode:**
1. Download CBS-data: Etnische samenstelling per buurt (alle 4-cijfer postcodes)
2. Bereken dissimilarity index voor echte data
3. Kalibreer model: Pas tolerance aan tot model-output = echte D-index
4. Voorspel: Scenario's (bevolkingsgroei, beleid, polarisatie)

**Output:** Gevalideerd model + beleidsadvies voor gemeente.

#### Optie B: Multi-dimensionale segregatie

**Doel:** Niet alleen etniciteit, maar **meerdere assen tegelijk**.

**Dimensies:**
1. Etniciteit (5 groepen)
2. Wealth (3 niveaus)
3. Leeftijd (jong/oud)

**Vraag:** Hoe interacteren deze dimensies? Ontstaat er "super-segregatie" (arm + etnisch + oud)?

**Implementatie:** Agents hebben 3 eigenschappen, tolerance per dimensie.

**Zeer complex:** Geschikt voor VWO-wiskunde/informatica eindproject.

#### Optie C: Agent-based transport model

**Doel:** Combineer segregatie met mobiliteit.

**Extensie:**
1. Agents werken in centrum, wonen in buurten
2. Dagelijkse "pendel": Agents bewegen naar werk-patches, terug naar huis
3. Segregatie op woonplek, menging op werkplek
4. Effect: Hoe beïnvloedt werk-interactie woon-segregatie?

**Hypothese:** Als mensen diverse collega's hebben (werk), worden ze toleranter → minder woon-segregatie.

**Test:** Vergelijk scenario's (veel werk-interactie vs weinig).

### Checklist VWO-niveau

- [ ] **Kwantitatieve validatie:** Vergelijk met echte data (CBS, literatuur)
- [ ] **Dissimilarity index:** Bereken standaard segregatie-maat
- [ ] **Minimaal 2 uitbreidingen:** Kies uit (economie, voorzieningen, multi-groep, gentrificatie)
- [ ] **Parameterstudie:** Varieer minimaal 3 parameters
- [ ] **Sensitiviteitsanalyse:** Welke parameters zijn cruciaal?
- [ ] **Beleid-scenario's:** Test minimaal 2 interventies
- [ ] **Verslag >10 pagina's** met literatuurstudie (Schelling 1971, recente onderzoeken)

### Interdisciplinaire koppeling

**Economie:**
- Schelling's werk (micro → macro)
- Huizenmarkt dynamiek

**Sociologie:**
- Segregatie-theorieën (structural vs preference-based)
- Contact-hypothese (interactie vermindert vooroordelen)

**Geografie:**
- Spatial analysis
- Urban planning theorie

**Wiskunde:**
- Dissimilarity index (formule)
- Netwerk-theorie (buurt-connectiviteit)

**Maatschappijleer:**
- Beleid (sociale woningbouw)
- Ethiek (diversiteit vs keuzevrijheid)

### Bronnen

**Primaire bron:**
- Schelling, T. C. (1971). "Dynamic Models of Segregation." *Journal of Mathematical Sociology, 1*(2), 143-186.

**Moderne onderzoeken:**
- Clark, W. A. V. (1991). "Residential Preferences and Neighborhood Racial Segregation: A Test of the Schelling Segregation Model." *Demography, 28*(1), 1-19.
- SCP (2024). "Segregatie in Nederlandse steden." *Sociaal Cultureel Planbureau.*

**Data:**
- CBS StatLine: [https://opendata.cbs.nl](https://opendata.cbs.nl)
- Amsterdam Open Data: [https://data.amsterdam.nl](https://data.amsterdam.nl)

---

**Conclusie:** Schelling's model is **elegant en krachtig**. Het toont hoe individuele voorkeuren leiden tot onbedoelde maatschappelijke uitkomsten. Dit is de essentie van computational social science: complex gedrag ontstaat uit simpele regels. Gebruik dit model om na te denken over jouw stad, jouw buurt, jouw keuzes. Welke samenleving willen we? En hoe kunnen we die bouwen? 🏘️🌍

