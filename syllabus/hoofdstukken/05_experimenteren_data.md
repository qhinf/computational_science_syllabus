(hoofdstukken/05_experimenteren_data)=
# Experimenteren en data verzamelen

Je hebt nu een werkend model met emergent gedrag. Maar één keer runnen is niet genoeg om wetenschappelijke conclusies te trekken. In dit hoofdstuk leer je **systematisch experimenteren**: hoe ontwerp je een experiment, hoe verzamel je betrouwbare data, en hoe trek je conclusies zonder te overdrijven. Je leert waarom "one run is no run", hoe je parameters varieert, data samenvat in tabellen en grafieken, en hoe je onderscheid maakt tussen correlatie en causatie. Dit is waar computational science échte wetenschap wordt.

**Leerdoel:** Na dit hoofdstuk kun je een systematisch experiment opzetten, betrouwbare data verzamelen, resultaten samenvatten in tabellen en grafieken, en gefundeerde conclusies trekken over je model.

## Inhoud

In dit hoofdstuk behandelen we:

- Waarom meerdere runs? (toeval en ruis)
- Experimentopzet: parameter kiezen, range en stappen
- Meten: welke output verzamel je?
- Runs uitvoeren: handmatig plan en BehaviorSpace
- Data samenvatten: tabellen en grafieken
- Conclusies trekken zonder te overdrijven

---

## Waarom meerdere runs?

### Het probleem: randomness

Je model bevat waarschijnlijk random-elementen:

- Mieren bewegen willekeurig rond
- De startpositie van agents is random
- Voedsel verschijnt op random plekken
- Kansen (20% om te besmetten) leiden tot verschillende uitkomsten

**Gevolg:** Elke run geeft **andere resultaten**, zelfs met dezelfde parameters!

**Voorbeeld:** Mieren-model met verdampingssnelheid = 0.05

- Run 1: 87 eenheden voedsel verzameld na 500 ticks
- Run 2: 91 eenheden verzameld
- Run 3: 83 eenheden verzameld
- Run 4: 89 eenheden verzameld
- Run 5: 86 eenheden verzameld

**Vraag:** Hoeveel eenheden verzamelen mieren gemiddeld? Antwoord: **87.2** (het gemiddelde).

### "One run is no run"

Dit is een gouden regel in computational science. Waarom?

1. **Toeval:** Je kunt toevallig een extreme run hebben (lucky of unlucky)
2. **Geen variatie-inzicht:** Je weet niet of resultaat 87 normaal is of een uitzondering
3. **Niet reproduceerbaar:** Een ander krijgt andere resultaten, kan je werk niet verifiëren

**Vuistregel:** Doe minimaal **5-10 runs** per parameter-waarde. Bij meer variatie: meer runs nodig.

### Variatie meten: standaarddeviatie

**Standaarddeviatie** (SD) meet hoe ver resultaten uit elkaar liggen.

- Kleine SD (bijv. 2.1) → resultaten liggen dicht bij elkaar → betrouwbaar
- Grote SD (bijv. 15.3) → resultaten variëren veel → onzeker

**Voorbeeld:** 
- Run 1: 87, Run 2: 91, Run 3: 83, Run 4: 89, Run 5: 86
- Gemiddelde: 87.2
- Standaarddeviatie: 2.9 (relatief klein)

**Notatie:** 87.2 ± 2.9 (lees: "87 punt 2 plus-minus 2 punt 9")

:::{tip}
**Hoe bereken je standaarddeviatie?**  
In Excel: `=STDEV.S(bereik)` (bijv. `=STDEV.S(A1:A5)`)  
In Python: `import statistics; statistics.stdev([87, 91, 83, 89, 86])`  
In je hoofd: Lastig, gebruik een tool!
:::

### Wanneer is variatie acceptabel?

- **Kleine variatie (< 5% van gemiddelde):** Prima, je model is stabiel
- **Matige variatie (5-15%):** Acceptabel, vermeld de onzekerheid in je verslag
- **Grote variatie (> 15%):** Probleem! Doe meer runs of zoek de oorzaak

**Voorbeeld:** Gemiddelde = 87.2, SD = 2.9  
Variatie = 2.9 / 87.2 = 3.3% → Kleine variatie, goed!

---

## Experimentopzet: parameter kiezen + range + stappen 

Nu je weet waarom meerdere runs nodig zijn, tijd om je experiment te ontwerpen.

### Stap 1: Kies één parameter

Begin simpel: varieer **één parameter** tegelijk. Houd de rest constant.

**Slechte opzet:**
- Varieer aantal-mieren EN verdampingssnelheid tegelijk
- Je weet niet welke parameter het effect veroorzaakt!

**Goede opzet:**
- Varieer alleen verdampingssnelheid
- Houd aantal-mieren, hoeveelheid-voedsel, etc. constant

**Voorbeelden van interessante parameters:**

| Model | Parameter | Onderzoeksvraag |
|-------|-----------|-----------------|
| Mieren | verdampingssnelheid | Wat is de optimale verdamping? |
| Mieren | aantal-mieren | Leidt meer mieren tot efficiënter verzamelen? |
| Mexican wave | reactie-tijd | Bij welke reactie-tijd sterft de wave uit? |
| Virus | besmettingskans | Hoe beïnvloedt dit de piek-besmetting? |

### Stap 2: Bepaal de range (bereik)

**Range** = het bereik van waarden dat je test.

**Te klein bereik:**
- Test: verdampingssnelheid 0.04, 0.045, 0.05
- Probleem: Je ziet alleen kleine verschillen, mist het grote plaatje

**Te groot bereik:**
- Test: verdampingssnelheid 0.01, 0.5, 1.0
- Probleem: Bij 1.0 verdampen sporen meteen, geen paden mogelijk → niet interessant

**Goed bereik:**
- Test: 0.01, 0.03, 0.05, 0.07, 0.1
- Reden: Verwacht dat ergens tussen 0.01 en 0.1 de interessante dynamiek zit

**Hoe bepaal je de range?**

1. **Verkennende runs:** Test een paar extremen (0.01 en 0.1)
2. **Zoek interessant gebied:** Waar verandert het gedrag?
3. **Focus daar:** Neem meer meetpunten in dat gebied

### Stap 3: Kies stapgrootte

**Stapgrootte** = verschil tussen twee opeenvolgende waarden.

**Te kleine stappen:**
- Test: 0.040, 0.041, 0.042, 0.043, 0.044, 0.045
- Probleem: Veel werk, weinig nieuwe inzichten (verschil is te klein)

**Te grote stappen:**
- Test: 0.01, 0.1, 1.0
- Probleem: Je mist interessante waarden tussen 0.01 en 0.1

**Goede stappen:**
- Test: 0.01, 0.03, 0.05, 0.07, 0.1
- Reden: Redelijk verdeeld, niet te veel werk, goede coverage

**Richtlijn:** Kies 5-8 verschillende waarden. Minder = te grof, meer = te veel werk voor dit niveau.

### Stap 4: Aantal runs per waarde

**Minimaal:** 3 runs per waarde (om gemiddelde + variatie te berekenen)  
**Beter:** 5 runs per waarde (betrouwbaarder)  
**Ideaal:** 10+ runs per waarde (voor serieus onderzoek)

**Totaal aantal runs:**  
Aantal parameter-waarden × aantal runs per waarde

Voorbeeld: 5 waarden × 3 runs = **15 runs totaal**

### Voorbeeld: Complete experimentopzet

**Onderzoeksvraag:** Hoe beïnvloedt verdampingssnelheid de efficiëntie van voedsel verzamelen bij mieren?

**Hypothese:** Optimale verdamping ligt tussen 0.03 en 0.07. Te laag → oude sporen blijven, te hoog → geen paden.

**Experimentopzet:**

| Element | Waarde |
|---------|--------|
| Variabele parameter | verdampingssnelheid |
| Constante parameters | aantal-mieren = 50, hoeveelheid-voedsel = 50, zoekradius = 2 |
| Range | 0.01 tot 0.1 |
| Waarden | 0.01, 0.03, 0.05, 0.07, 0.1 (5 waarden) |
| Runs per waarde | 5 |
| Totaal runs | 25 |
| Duur per run | 500 ticks |
| Output | Verzameld voedsel na 500 ticks |

:::{admonition} Let op: tijdsinvestering
:class: warning
**Bereken je tijd!**  
Als 1 run = 2 minuten, en je doet 25 runs, kost dat 50 minuten. Plan dit in. Je kunt het model sneller laten lopen (View → Update View → schakel uit), maar het blijft tijd kosten.
:::

```{exercise} Oefening (Oefenen)
:label: oef-5-1

Ontwerp een parameter-sweep (systematische variatie van één parameter) voor je eigen model:

1. **Kies één parameter** om te variëren
2. **Bepaal de range:** Minimale en maximale waarde (met beredenering)
3. **Kies 5 waarden** binnen die range (gelijk verdeeld)
4. **Bepaal constante parameters:** Welke houd je vast? Op welke waarde?
5. **Aantal runs:** 3 runs per waarde (totaal 15 runs)
6. **Output:** Wat ga je meten?

Presenteer als tabel (zie voorbeeld hierboven). Leg in 3-5 zinnen uit: Waarom deze parameter? Waarom deze range?
```

---

## Meten: welke output verzamel je?

Je hebt je parameter gekozen. Nu: **wat ga je meten?**

### Output moet je onderzoeksvraag beantwoorden

**Slechte keuze:** Meet het aantal ticks (dat is altijd 500 als je tot 500 ticks laat runnen!)

**Goede keuze:** Meet iets dat **varieert** en **relevant** is voor je vraag.

**Voorbeelden:**

| Onderzoeksvraag | Goede output | Waarom? |
|-----------------|--------------|---------|
| "Efficiëntie van voedsel verzamelen?" | Aantal verzamelde voedsel-eenheden | Direct antwoord op "efficiëntie" |
| "Bij welke reactie-tijd sterft wave uit?" | Aantal rondes die wave maakt | Lage rondes = uitgestorven, hoge = blijft gaan |
| "Effect van besmettingskans op piek?" | Maximaal aantal besmetten tegelijk | Dit is letterlijk de "piek" |
| "Hoe snel verspreidt virus zich?" | Tijd tot 50% besmet is | Meet snelheid van verspreiding |

### Soorten output

1. **Eindwaarde:** Waarde aan het eind van de run
   - Voorbeeld: Voedsel verzameld na 500 ticks
   - Pro: Simpel te meten
   - Con: Je mist het proces

2. **Maximum/minimum:** Hoogste of laagste waarde tijdens run
   - Voorbeeld: Maximaal aantal besmetten (de piek)
   - Pro: Belangrijk voor crisismodellen
   - Con: Je moet bijhouden tijdens run

3. **Tijd tot gebeurtenis:** Hoe lang duurt het tot X gebeurt?
   - Voorbeeld: Tijd tot wave stopt, tijd tot 50% besmet
   - Pro: Meet snelheid/dynamiek
   - Con: Gebeurtenis moet wel optreden

4. **Gemiddelde tijdens run:** Gemiddelde waarde over alle ticks
   - Voorbeeld: Gemiddeld aantal mieren met voedsel
   - Pro: Geeft overall beeld
   - Con: Verbergt pieken/dalen

### Output implementeren in NetLogo

**Optie A: Gebruik bestaande reporters**

Als je al een monitor hebt met `verzameld-voedsel`, noteer aan het eind van elke run die waarde.

**Optie B: Maak een specifieke reporter**

```scheme
; Global variable om bij te houden
globals [
  max-besmetten-ooit   ; Hoogste aantal besmetten tot nu toe
]

to go
  ; ... normale go-code ...
  
  ; Update maximum
  let huidig-aantal count turtles with [besmet?]
  if huidig-aantal > max-besmetten-ooit [
    set max-besmetten-ooit huidig-aantal
  ]
  
  tick
end

to setup
  clear-all
  set max-besmetten-ooit 0  ; Reset bij nieuwe run
  ; ... rest van setup ...
  reset-ticks
end

; Reporter voor monitor
to-report piek-besmetting
  report max-besmetten-ooit
end
```

**Optie C: BehaviorSpace doet het voor je (zie sectie 5.4)**

### Meerdere outputs tegelijk?

Ja, mag! Bijvoorbeeld:

- Output 1: Verzameld voedsel (efficiëntie)
- Output 2: Gemiddelde geurspoor-sterkte (hoe sterk zijn paden?)

Maar: focus op **één primaire output** voor je hoofdvraag. De rest is secundair.

:::{tip}
**Test je output-meting!**  
Voor je 25 runs doet, test of je output-meting klopt:
1. Doe 2-3 test-runs
2. Controleer: komt de output-waarde overeen met wat je visueel ziet?
3. Als niet: debug je reporter!
:::

---

## Runs uitvoeren: handmatig plan + (optioneel) BehaviorSpace

Je hebt een plan. Nu: **uitvoeren**. Twee methoden.

### Methode 1: Handmatig (simpel, maar arbeidsintensief)

**Stap-voor-stap:**

1. **Maak een tabel** in Excel/Google Sheets:

| Run nummer | Parameter-waarde | Output (verzameld voedsel) | Notities |
|------------|------------------|----------------------------|----------|
| 1 | 0.01 | | |
| 2 | 0.01 | | |
| 3 | 0.01 | | |
| 4 | 0.03 | | |
| 5 | 0.03 | | |
| ... | ... | ... | ... |

2. **Voor elke run:**
   - Pas parameter aan (slider)
   - Klik Setup
   - Klik Go (laat lopen tot 500 ticks)
   - Noteer output in tabel
   - Herhaal

3. **Let op:** Noteer ook bijzonderheden in "Notities" (bijv. "run 7: model crashte", "run 12: ongebruikelijk patroon")

**Voordeel:** Simpel, je ziet wat er gebeurt  
**Nadeel:** Saai, foutgevoelig (je vergeet een waarde te noteren), tijdrovend

### Methode 2: BehaviorSpace (automatisch)

**BehaviorSpace** is een ingebouwde tool in NetLogo om automatisch experimenten uit te voeren.

**Hoe het werkt:**

1. Ga naar Tools → BehaviorSpace
2. Klik "New" om een experiment te maken
3. Vul in:
   - **Experiment name:** bijv. "Verdamping-sweep"
   - **Vary variables as follows:**
     ```
     ["verdampingssnelheid" 0.01 0.03 0.05 0.07 0.1]
     ```
   - **Repetitions:** 5 (aantal runs per waarde)
   - **Measure runs using these reporters:**
     ```
     verzameld-voedsel
     gem-geurspoor
     ```
   - **Measure runs at every step:** Nee (alleen eindwaarde)
   - **Setup commands:** `setup`
   - **Go commands:** `go`
   - **Stop condition:** `ticks >= 500`

4. Klik OK, dan "Run"
5. NetLogo doet alle 25 runs automatisch!
6. Output wordt opgeslagen als CSV-bestand

[Screenshot: BehaviorSpace interface met ingevulde velden]

**Voordeel:** Volledig automatisch, geen fouten, CSV-export  
**Nadeel:** Leer-curve, je ziet niet wat er gebeurt tijdens runs

**CSV-output openen:**

- Open in Excel/Google Sheets
- Elke rij = 1 run
- Kolommen: parameter-waarde, outputs, run-nummer

**Voorbeeld CSV:**

```
[run number],[verdampingssnelheid],[verzameld-voedsel],[gem-geurspoor]
1,0.01,87,42.3
2,0.01,91,45.1
3,0.01,83,39.8
4,0.03,95,38.2
...
```

:::{tip}
**Start met handmatig, ga later naar BehaviorSpace**  
Voor je eerste experiment: doe het handmatig (5-10 runs). Je leert meer. Voor grotere experimenten (25+ runs): gebruik BehaviorSpace. Het scheelt uren!
:::

### Tijdens runs: wat let je op?

- **Stabiliteit:** Crasht je model? Fix dat eerst!
- **Visuele patronen:** Zie je verwachte gedrag? (paden bij mieren, golf bij wave)
- **Outliers:** Is één run extreem anders? Noteer dat, mogelijk een bug
- **Tijd:** Loopt je model snel genoeg? Zo niet: optimaliseer of wacht...

---

## Data samenvatten: tabel + 1 grafiek

Je hebt data! Nu: **samenvatten** zodat patronen zichtbaar worden.

### Stap 1: Bereken gemiddeldes per parameter-waarde

**Raw data (5 runs per waarde):**

| Verdampingssnelheid | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 |
|---------------------|-------|-------|-------|-------|-------|
| 0.01 | 87 | 91 | 83 | 89 | 86 |
| 0.03 | 95 | 97 | 93 | 96 | 94 |
| 0.05 | 102 | 98 | 100 | 101 | 99 |
| 0.07 | 96 | 94 | 97 | 95 | 98 |
| 0.1 | 88 | 86 | 90 | 87 | 89 |

**Samengevat (met gemiddelde en SD):**

| Verdampingssnelheid | Gemiddeld verzameld | SD | Min | Max |
|---------------------|---------------------|-----|-----|-----|
| 0.01 | 87.2 | 2.9 | 83 | 91 |
| 0.03 | 95.0 | 1.6 | 93 | 97 |
| 0.05 | 100.0 | 1.6 | 98 | 102 |
| 0.07 | 96.0 | 1.6 | 94 | 98 |
| 0.1 | 88.0 | 1.6 | 86 | 90 |

**In Excel:**
- Gemiddelde: `=AVERAGE(B2:F2)`
- SD: `=STDEV.S(B2:F2)`
- Min: `=MIN(B2:F2)`
- Max: `=MAX(B2:F2)`

### Stap 2: Maak een grafiek

**Type grafiek: lijndiagram (line chart)**

- X-as: Parameter-waarde (verdampingssnelheid)
- Y-as: Output (verzameld voedsel)
- Punten: Gemiddeldes
- (Optioneel) Foutbalken: SD tonen

[Screenshot: Lijndiagram met verdampingssnelheid op x-as, verzameld voedsel op y-as, duidelijke piek bij 0.05]

**Wat zie je in deze grafiek?**

- **Trend:** Voedsel verzameld stijgt eerst (0.01 → 0.05), dan daalt (0.05 → 0.1)
- **Optimum:** Maximaal bij verdampingssnelheid = 0.05 (100 eenheden)
- **Variatie:** Kleine foutbalken → betrouwbare data

### Stap 3: Interpreteer de grafiek

**Beschrijf wat je ziet:**

"De grafiek toont dat verzameld voedsel eerst stijgt van 87.2 (bij 0.01) naar een maximum van 100.0 (bij 0.05), en daarna daalt naar 88.0 (bij 0.1). De standaarddeviatie is klein (< 3), wat duidt op betrouwbare metingen."

**Verklaar het patroon:**

"Bij lage verdamping (0.01) blijven oude sporen lang bestaan, wat mieren misleidt. Bij optimale verdamping (0.05) blijven goede paden bestaan en slechte paden verdwijnen. Bij hoge verdamping (0.1) verdwijnen alle sporen te snel, waardoor mieren te veel random bewegen."

**Beantwoord je onderzoeksvraag:**

"De optimale verdampingssnelheid voor efficiënt voedsel verzamelen is 0.05. Dit balanceert tussen 'sporen bewaren' en 'oude sporen verwijderen'."

```{exercise} Oefening (Toepassen)
:label: oef-5-2

Voer je parameter-sweep uit (uit Oefening 5.1):

1. Doe 3 runs per waarde (totaal 15 runs)
2. Noteer alle resultaten in een tabel
3. Bereken gemiddelde en SD per parameter-waarde
4. Maak een lijndiagram (mag handmatig of in Excel)
5. **Interpreteer 2 trends:**
   - Wat zie je gebeuren als parameter stijgt?
   - Wat is het meest opvallende punt/patroon?

Schrijf je interpretatie in 5-8 zinnen. Gebruik placeholder: [Grafiek: parameter X vs output Y, met beschrijving van patroon].
```

---

## Conclusies trekken zonder te overdrijven

Je hebt data en een grafiek. Tijd voor **conclusies**. Maar pas op: niet te hard van stapel lopen!

### Fout 1: Causaliteit claimen zonder bewijs

**Fout:** "Verdampingssnelheid **veroorzaakt** meer voedsel verzamelen."

**Probleem:** Je hebt **correlatie** (samenhang) gezien, geen **causatie** (oorzaak-gevolg).

**Beter:** "Hogere verdampingssnelheid is **geassocieerd met** meer verzameld voedsel (tot 0.05), daarna daalt het weer."

**Nog beter:** "In dit model lijkt verdampingssnelheid een **invloed te hebben op** efficiëntie, omdat [mechanisme uitleggen: goede paden blijven, slechte verdwijnen]."

### Fout 2: Generaliseren naar werkelijkheid

**Fout:** "Echte mieren hebben dus een optimale feromoon-verdamping van 0.05."

**Probleem:** Dit is een **model**, geen echte mieren! Modellen zijn vereenvoudigd.

**Beter:** "Binnen dit model is 0.05 optimaal. In de natuur kunnen andere factoren een rol spelen die hier niet gemodelleerd zijn."

### Fout 3: Conclusies buiten je data-range

**Fout:** "Bij verdampingssnelheid = 0.2 zal voedsel verzamelen nog lager zijn."

**Probleem:** Je hebt 0.2 niet getest! Misschien gebeurt er iets onverwachts.

**Beter:** "Binnen het geteste bereik (0.01-0.1) zien we een optimum bij 0.05. Verder onderzoek kan testen of dit patroon doorzet bij hogere waarden."

### Fout 4: Kleine verschillen overdrijven

**Fout:** "Bij 0.03 is het resultaat 95, bij 0.05 is het 100. Dus 0.05 is **significant beter**."

**Probleem:** Het verschil is 5% en je hebt kleine sample (3-5 runs). Dat kan toeval zijn.

**Beter:** "Bij 0.05 zien we een hoger gemiddelde (100 vs 95), maar het verschil is klein en binnen de variatie van het model."

### Goede conclusie-structuur

1. **Samenvatting resultaat:** "Verzameld voedsel varieert van 87 (bij 0.01) tot 100 (bij 0.05) tot 88 (bij 0.1)."
2. **Patroon beschrijven:** "Er is een optimum bij 0.05."
3. **Verklaring geven:** "Dit komt waarschijnlijk doordat bij 0.05 goede paden lang genoeg blijven bestaan, terwijl slechte paden vervagen."
4. **Hypothese toetsen:** "Mijn hypothese dat optimum tussen 0.03 en 0.07 ligt, wordt bevestigd."
5. **Beperkingen noemen:** "Dit geldt binnen de geteste parameter-waarden en met huidige model-regels. Andere factoren (zoals aantal mieren) zijn niet gevarieerd."

:::{admonition} Let op: correlatie ≠ causatie
:class: warning
**Veelgemaakte denkfout:**  
"A en B gaan samen op → A veroorzaakt B!"  

Nee! Mogelijk veroorzaakt B juist A, of C veroorzaakt zowel A als B.

**Voorbeeld:** In je model: meer geurspoor correleert met meer verzameld voedsel. Maar wat is oorzaak en gevolg? Antwoord: Voedsel verzamelen → mieren lopen terug → leggen spoor → meer spoor. Dus verzamelen veroorzaakt spoor, niet andersom (of: cyclische relatie).
:::

```{exercise} Oefening (Reflecteren)
:label: oef-5-3

Beantwoord in 200-300 woorden:

**Wat is correlatie vs oorzaak in jouw model?**

1. **Identificeer een correlatie:** Welke twee variabelen in je model gaan samen omhoog/omlaag?
2. **Is het causaal?** Veroorzaakt de ene echt de andere? Of is het toeval? Of beïnvloeden ze elkaar beide?
3. **Mechanisme:** Leg het mechanisme uit: *hoe* veroorzaakt X (mogelijk) Y?
4. **Alternatieve verklaringen:** Kan het ook anders zijn? (bijv. derde factor Z beïnvloedt zowel X als Y)

Gebruik je eigen data uit Oefening 5.2. Als je nog geen data hebt, gebruik een hypothetisch voorbeeld uit je model.
```

---

## Verdiepende opgaven

Klaar voor verdieping? Deze opdrachten brengen je naar hoger niveau.

```{exercise} Opdracht (Multi-parameter experiment)
:label: verd-5-1

**Uitdaging: Varieer 2 parameters tegelijk**

In dit hoofdstuk varieerde je 1 parameter. Nu: 2 tegelijk!

**Opzet:**
- Parameter 1: verdampingssnelheid (3 waarden: 0.03, 0.05, 0.07)
- Parameter 2: aantal-mieren (3 waarden: 30, 50, 70)
- Totaal: 3 × 3 = 9 combinaties
- Runs per combinatie: 3
- Totaal runs: 27

**Voer uit en maak:**
1. **2D-tabel** (heatmap-stijl):

|  | 30 mieren | 50 mieren | 70 mieren |
|--|-----------|-----------|-----------|
| **0.03** | 82 | 95 | 105 |
| **0.05** | 89 | 100 | 112 |
| **0.07** | 85 | 96 | 108 |

2. **Analyse:** Welke parameter heeft het grootste effect? Zijn er interactie-effecten (bijv. verdamping werkt anders bij 30 vs 70 mieren)?

Schrijf 300-400 woorden + tabel.
```

```{exercise} Opdracht (Reproduceerbaarheid)
:label: verd-5-2

**Wetenschappelijke integriteit: laat een ander je resultaten reproduceren**

1. Geef je NetLogo-model aan een klasgenoot
2. Geef je experimentopzet (welke parameter, welke waarden, hoeveel runs)
3. Klasgenoot doet het experiment opnieuw
4. Vergelijk resultaten

**Vragen:**
- Komen de gemiddeldes overeen? (binnen ±5%)
- Zo nee: waarom niet? (random seed? verschillende NetLogo versie? bug?)
- Wat leer je hiervan over reproduceerbaarheid?

Schrijf 250-350 woorden reflectie. Dit is hoe echte wetenschap werkt: anderen moeten je werk kunnen herhalen!
```

```{exercise} Opdracht (Sensitiviteitsanalyse)
:label: verd-5-3

**Hoe gevoelig is je model?**

Een **sensitiviteitsanalyse** test: Welke parameters zijn cruciaal, welke niet?

Methode:
1. Kies 3 parameters
2. Varieer elk ±10% van de standaardwaarde
3. Meet output
4. Bereken: Hoeveel procent verandert output?

Voorbeeld:

| Parameter | Standaard | +10% waarde | Output standaard | Output +10% | % verandering |
|-----------|-----------|-------------|------------------|-------------|---------------|
| aantal-mieren | 50 | 55 | 100 | 108 | +8% |
| verdamping | 0.05 | 0.055 | 100 | 96 | -4% |
| zoekradius | 2 | 2.2 | 100 | 102 | +2% |

**Conclusie voorbeeld:** Model is meest gevoelig voor aantal-mieren (+8%), matig voor verdamping (-4%), weinig voor zoekradius (+2%).

Voer dit uit voor je eigen model. Schrijf 200-300 woorden + tabel.
```

---

## PO-mijlpaal

Na dit hoofdstuk ben je klaar voor de vijfde mijlpaal: een complete dataset met onderbouwde conclusies.

### Wat lever je op?

Een document (2-3 pagina's A4) met:

1. **Experimentopzet** (½ pagina):
   - Onderzoeksvraag
   - Gevarieerde parameter + range + aantal waarden
   - Constante parameters (met waarden)
   - Gemeten output
   - Aantal runs per waarde

2. **Dataset** (½ pagina):
   - Tabel met alle runs (raw data)
   - Tabel met samenvattingen (gemiddelde, SD per parameter-waarde)
   - Minimaal **15 runs totaal** (bijv. 5 waarden × 3 runs)

3. **Grafiek** (½ pagina):
   - Lijndiagram: parameter-waarde vs output
   - Duidelijke as-labels en titel
   - (Optioneel) Foutbalken voor SD

4. **Analyse en conclusies** (1 pagina):
   - Beschrijf het patroon in de grafiek (2-3 zinnen)
   - Verklaar waarom dit patroon ontstaat (mechanisme, 4-5 zinnen)
   - Beantwoord je onderzoeksvraag (2 conclusies, elk 2-3 zinnen)
   - Noem 1 onzekerheidspunt of beperking (3-4 zinnen)

### Checklist: je bent klaar als…

- [ ] Je hebt minimaal **15 runs** uitgevoerd (3+ runs per waarde, 5+ verschillende waarden)
- [ ] Alle runs zijn gedocumenteerd in een tabel (geen ontbrekende data)
- [ ] Je hebt **gemiddeldes en standaarddeviaties** berekend voor elke parameter-waarde
- [ ] Je grafiek toont een **duidelijk patroon** (trend, optimum, plateau, of iets anders)
- [ ] Je hebt **2 conclusies** getrokken die direct uit je data volgen
- [ ] Je hebt **1 onzekerheidspunt** of beperking benoemd (bijv. "Dit geldt alleen binnen deze parameter-range", "Variatie was hoog bij waarde X")
- [ ] Je conclusies zijn **voorzichtig geformuleerd** (geen wilde claims, geen causatie zonder bewijs)
- [ ] Je verklaring koppelt terug naar je **model-mechanisme** (hoe werken de regels?)

### Waar komt dit terug in je eindproject?

Deze mijlpaal is de **kern van je Resultaten-sectie** in het eindverslag:

- **Methode:** Experimentopzet (hoe je data verzamelde)
- **Resultaten:** Dataset + grafiek + patroon-beschrijving
- **Discussie:** Conclusies + verklaring + beperkingen

**Tips voor succes:**

- **Plan je tijd:** 15 runs × 2 min = 30 min minimum. Plus analyse-tijd!
- **Maak tussentijds back-ups:** Sla je tabel op na elke 5 runs (je wilt niet opnieuw beginnen)
- **Check outliers:** Is één run extreem anders? Noteer dat, onderzoek waarom
- **Wees eerlijk over beperkingen:** Goede wetenschappers erkennen wat ze niet weten

**Evaluatiecriteria:**

| Criterium | Onvoldoende | Voldoende | Goed |
|-----------|-------------|-----------|------|
| Dataset | <15 runs of incomplete | 15 runs, volledig | 20+ runs, systematisch |
| Grafiek | Onduidelijk of ontbreekt | Duidelijk, basislabels | Professioneel, foutbalken |
| Conclusies | Vaag of ongefundeerd | 2 conclusies, logisch | Diepgaand, goed onderbouwd |
| Beperkingen | Niet genoemd | 1 beperking, oppervlakkig | Kritisch, meerdere punten |
| Wetenschappelijke houding | Claims zonder bewijs | Voorzichtig, correlatie erkend | Nuance, causatie vs correlatie helder |

---

**Volgende stap:** In hoofdstuk 6 ga je je model **verifiëren en valideren**. Klopt je code? Klopt je model met de werkelijkheid? En dan: tijd voor het eindverslag, waar je alles samenbrengt in een wetenschappelijk rapport. Je bent bijna klaar!


