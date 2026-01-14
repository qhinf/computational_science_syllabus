# Onderzoek doen: verificatie, validatie en verslag

Je hebt een model gebouwd en data verzameld. Maar hoe weet je of je model **klopt**? En hoe presenteer je je onderzoek professioneel? In dit hoofdstuk leer je het verschil tussen verificatie ("werkt mijn code?") en validatie ("lijkt het op de werkelijkheid?"). Je maakt je abstractie-keuzes expliciet, identificeert beperkingen, en schrijft een gestructureerd verslag waarin je jezelf geen dingen aanpraat. Dit is het sluitstuk: van spelen met code naar wetenschappelijk onderzoek.

**Leerdoel:** Na dit hoofdstuk kun je je model kritisch controleren (verificatie), vergelijken met de werkelijkheid (validatie), een compleet onderzoeksverslag schrijven, en veelgemaakte fouten in conclusies vermijden.

## Inhoud

In dit hoofdstuk behandelen we:

- Abstractie-keuzes expliciet maken
- Verificatie: werkt je model zoals bedoeld? (checklist)
- Validatie: lijkt het gedrag op de echte wereld/casus?
- Beperkingen en aannames
- Verslagstructuur (kopjes + voorbeeldzinnen)
- Veelgemaakte fouten in conclusies

---

## Abstractie-keuzes expliciet maken

### Waarom abstractie-keuzes belangrijk zijn

Een **model** is altijd een **vereenvoudiging** van de werkelijkheid. Je hebt keuzes gemaakt: wat neem je mee, wat laat je weg?

**Voorbeeld mieren-model:**

| Aspect werkelijkheid                            | Gemodelleerd? | Waarom wel/niet?            |
| ----------------------------------------------- | ------------- | --------------------------- |
| Mieren leggen feromonen                         | **Ja**        | Kernmechanisme voor paden   |
| Feromonen verdampen                             | **Ja**        | Essentieel voor dynamiek    |
| Mieren hebben energie                           | **Nee**       | Te complex voor basis-model |
| Wind waait feromonen weg                        | **Nee**       | Buiten scope van dit model  |
| Verschillende mieren-rollen (koningin, werkers) | **Nee**       | Focus op collectief gedrag  |
| 3D-omgeving (ook verticaal)                     | **Nee**       | 2D is genoeg voor concept   |

**Het probleem:** Als je deze keuzes niet expliciet maakt, weet niemand (inclusief jijzelf over 2 weken) waarom je model zo werkt.

### Hoe maak je keuzes expliciet?

**In je verslag (Methode-sectie):**

"Dit model vereenvoudigt mieren-foerageren tot 2D-beweging op een grid. Mieren leggen een chemisch geurspoor (feromoon) dat verdampt over tijd. Het model negeert energie-verlies, dag/nacht-cyclus, en verschillende mieren-rollen, omdat de focus ligt op het emergente patroon van collectieve pad-vorming."

**Template:**

> "Dit model [beschrijft fenomeen X] door [hoofd-mechanismen Y]. Het model negeert [aspecten A, B, C], omdat [reden: focus op emergentie / te complex / buiten scope]."

### Veelvoorkomende abstracties in ABM

1. **Discrete tijd (ticks):** Werkelijkheid is continu, model werkt per tick
2. **Grid-wereld:** Werkelijkheid is continu ruimte, model gebruikt vakjes
3. **Identieke agents:** Werkelijkheid heeft variatie, model start met uniforme agents
4. **Geen externe factoren:** Werkelijkheid heeft weer/temperatuur/etc., model heeft vaste omgeving
5. **Perfecte informatie:** Agents "weten" meer dan echte wezens (bijv. kunnen alle patches zien)

:::{tip}
**Hoe kies je wat te vereenvoudigen?**  
Vraag: "Als ik dit weglaat, kan ik nog steeds mijn onderzoeksvraag beantwoorden?"  
Ja → weglaten is OK  
Nee → moet erin
:::

**Voorbeeld Mexican wave:**

**Abstracties:**
- Mensen reageren uniform (werkelijkheid: sommigen zijn sneller)
- Geen vermoeidheid (werkelijkheid: na 10 rondes word je moe)
- Perfecte zichtlijn (werkelijkheid: je ziet alleen je buren)
- Geen afleiding (werkelijkheid: mensen kijken naar hun telefoon)

**Reden:** Focus ligt op **simpele regels → emergent patroon**, niet op realistische mensmodellering.

---

## Verificatie: werkt je model zoals bedoeld?

**Verificatie** = controleren of je **code** doet wat je **wilde** dat het deed.

**Vraag:** Niet "is dit realistisch?", maar "werkt dit technisch correct?"

### Verificatie-checklist

Doorloop deze punten systematisch:

#### 1. Initialisatie-test

**Vraag:** Start je model in de gewenste begintoestand?

**Checks:**
- Aantal agents klopt (bijv. 50 mieren als slider op 50 staat)
- Startposities correct (bijv. mieren starten in nest, niet random)
- Parameters zijn toegepast (bijv. verdampingssnelheid = slider-waarde)
- Omgeving is correct (bijv. voedsel op goede plekken)

**Test:** Klik Setup, kijk in Command Center:
```scheme
; Test in Command Center
count turtles  ; → moet 50 zijn als slider = 50
[color] of patch 0 0  ; → moet nest-kleur zijn
verdampingssnelheid  ; → moet slider-waarde zijn
```

#### 2. Regel-uitvoering test

**Vraag:** Doen agents wat je bedoelde?

**Methode:** Vertraag model (speed slider) en **observeer gedrag** van individuele agents.

**Voorbeelden:**
- **Mieren random zoeken:** Draait elke mier een willekeurige hoek? Beweegt elke mier vooruit?
- **Mieren met voedsel:** Draait mier 180° als voedsel opgepakt? Loopt mier terug naar nest?
- **Mexican wave:** Staat persoon op als ≥1 buur staat? Gaat persoon zitten na 1 tick?

**Veelgemaakte bugs:**

| Probleem                          | Oorzaak                                    | Oplossing                            |
| --------------------------------- | ------------------------------------------ | ------------------------------------ |
| Agents bewegen niet               | `go` roept `move` niet aan                 | Voeg `ask turtles [move]` toe        |
| Regel geldt niet voor alle agents | `ask turtle 0` in plaats van `ask turtles` | Gebruik meervoud: `turtles`          |
| Regel geldt dubbel                | `go` roept functie 2× aan                  | Check `go`-code, verwijder duplicaat |
| Parameter werkt niet              | Slider heet anders dan globale variabele   | Hernoem slider of variabele          |

#### 3. Output-test

**Vraag:** Meet je wat je denkt te meten?

**Test:** Vergelijk monitor-waarde met visuele telling.

**Voorbeeld:**
- Monitor toont "Verzameld voedsel: 23"
- Tel handmatig: hoeveel groene patches zijn verdwenen? → Moet 23 zijn

**Als niet klopt:** Je reporter is fout. Debug!

#### 4. Extreme-waarden test

**Vraag:** Wat gebeurt er bij extreme parameter-waarden?

**Tests:**
- Verdampingssnelheid = 0 → Sporen blijven **eeuwig** (verwacht)
- Verdampingssnelheid = 1 → Sporen verdwijnen **meteen** (verwacht)
- Aantal mieren = 1 → Model werkt, maar geen paden (verwacht)
- Aantal mieren = 500 → Model werkt, misschien traag (verwacht)

**Reden:** Extreme waarden onthullen bugs. Als model crasht bij aantal-mieren = 0, had je dat moeten verwachten en voorkomen.

#### 5. Reproduceerbaarheid-test

**Vraag:** Geeft dezelfde setup dezelfde resultaten (tot op toeval)?

**Methode:**
1. Noteer alle parameter-waarden
2. Run 1: Klik Setup, laat 100 ticks lopen, noteer output
3. Run 2: Klik Setup (opnieuw), laat 100 ticks lopen, noteer output
4. Vergelijk: Output verschilt door randomness, maar patronen moeten lijken

**Verwacht:** Resultaten variëren (random!), maar gemiddelde over 5 runs moet stabiel zijn.

**Als grote verschillen:** Mogelijk vergeet je iets te resetten in `setup`, of een globale variabele blijft oude waarde houden.

:::{admonition} Let op: random seed
:class: warning
NetLogo gebruikt **random seed** voor reproduceerbaarheid. Als je wilt dat twee runs **identiek** zijn (tot op agent-niveau), gebruik:
```scheme
random-seed 42  ; Elke run met seed 42 is identiek
```
Gebruik dit ALLEEN voor debugging! Echte experimenten moeten verschillende seeds hebben.
:::

```{exercise} Oefening (Oefenen)
:label: oef-6-1

Schrijf **5 verificatie-checks** voor jouw model:

1. **Initialisatie:** Wat controleer je na Setup? (bijv. "Aantal agents = slider-waarde")
2. **Regel-uitvoering:** Welk gedrag observeer je visueel? (bijv. "Agents draaien random")
3. **Output-meting:** Hoe test je of je output klopt? (bijv. "Tel handmatig, vergelijk met monitor")
4. **Extreme waarde 1:** Wat verwacht je bij minimale parameter? (bijv. "Verdamping = 0 → sporen blijven")
5. **Extreme waarde 2:** Wat verwacht je bij maximale parameter? (bijv. "Verdamping = 1 → sporen weg")

Presenteer als **tabel** met kolommen: Check | Verwacht resultaat | Getest? (ja/nee)

Voer minimaal 3 van de 5 checks uit. Noteer: Klopte het? Zo nee: wat heb je aangepast?
```

---

## Validatie: lijkt het gedrag op de echte wereld/casus?

**Validatie** = controleren of je model **realistisch gedrag** vertoont vergeleken met de werkelijkheid.

**Vraag:** Niet "werkt mijn code?", maar "komt dit overeen met hoe het écht gaat?"

### Drie niveaus van validatie

#### Niveau 1: Kwalitatieve validatie (gedragspatronen)

**Vraag:** Lijkt het **patroon** op wat je in de werkelijkheid ziet?

**Methode:** Vergelijk visueel gedrag met echte observaties/video's/beschrijvingen.

**Voorbeeld mieren-model:**

| Gedrag in werkelijkheid                        | Gedrag in model                       | Conclusie                  |
| ---------------------------------------------- | ------------------------------------- | -------------------------- |
| Mieren vormen **paden** tussen nest en voedsel | Model toont **blauwe paden**          | ✅ Overeenkomst             |
| Paden worden **sterker** bij meer gebruik      | Geurspoor accumuleert bij passage     | ✅ Overeenkomst             |
| **Kortste pad** wordt dominanter               | Model optimalisiert naar korte routes | ✅ Overeenkomst             |
| Paden blijven lang bestaan na voedsel op       | In model verdampen paden geleidelijk  | ✅ Overeenkomst             |
| Mieren vermijden obstakels                     | Model heeft geen obstakels            | ❌ Verschil (bewuste keuze) |

**Conclusie:** Model toont **kwalitatief** realistisch gedrag voor kern-mechanisme (pad-vorming).

**Voorbeeld Mexican wave:**

| Gedrag in werkelijkheid                       | Gedrag in model                     | Conclusie                  |
| --------------------------------------------- | ----------------------------------- | -------------------------- |
| Golf loopt **rond** in stadion                | Model toont **ronde golf**          | ✅ Overeenkomst             |
| Golf kan **uitsterven** bij trage reactie     | Bij hoge reactie-tijd stopt golf    | ✅ Overeenkomst             |
| Golf gaat **sneller** bij enthousiaste mensen | Bij lage reactie-tijd snellere golf | ✅ Overeenkomst             |
| Meerdere golven kunnen tegelijk ontstaan      | Model start met 1 golf              | ❌ Verschil (simplificatie) |

#### Niveau 2: Semi-kwantitatieve validatie (orde-van-grootte)

**Vraag:** Komen de **aantallen** ongeveer overeen?

**Methode:** Vergelijk output-waardes met reële data (geschatte orde-van-grootte).

**Voorbeeld mieren-model:**

- **Werkelijkheid:** Leafcutter mieren verzamelen ~50-100 kg voedsel per dag voor een kolonie van 8 miljoen mieren.
- **Model:** 50 mieren verzamelen ~100 eenheden voedsel in 500 ticks (gesimuleerd: ~1 uur).
- **Orde-van-grootte check:** 50 mieren / 1 uur ≈ 1200 mieren / dag (als 24 uur). Geschaald naar 8M mieren: ~6667× meer → 100 × 6667 = 666.700 eenheden. Ongeveer vergelijkbaar met 50-100 kg.

**Conclusie:** Model is **niet exact**, maar **orde-van-grootte klopt** (niet 1000× te veel of te weinig).

**Voorbeeld Mexican wave:**

- **Werkelijkheid:** Wave in stadion maakt 1 rondje in ~20-30 seconden, snelheid ~12 m/s.
- **Model:** Wave maakt 1 rondje in ~50 ticks (gesimuleerd: ~25 seconden bij 2 ticks/sec).
- **Conclusie:** Tijdsduur komt **ruwweg overeen**.

:::{tip}
**Geen exacte data beschikbaar?**  
Dat is OK! Schat een orde-van-grootte:  
- "Mieren verzamelen tientallen kilo's per dag" → model moet niet 1 gram of 10 ton voorspellen  
- "Mexican wave duurt tientallen seconden" → model moet niet 2 seconden of 10 minuten voorspellen
:::

#### Niveau 3: Kwantitatieve validatie (met echte data)

**Vraag:** Komen de **exacte waardes** overeen met metingen?

**Methode:** Vergelijk model-output met wetenschappelijke dataset.

**Voorbeeld:** Als je een **epidemie-model** bouwt:
- Verzamel echte data: aantal besmettingen per dag tijdens COVID-19 in Nederland (maart 2020)
- Run je model met vergelijkbare parameters (bevolkingsdichtheid, besmettingskans)
- Plot beide curves naast elkaar
- Bereken: Hoe groot is de afwijking? (bijv. model voorspelt 5% meer besmettingen dan echt)

**Voor dit niveau heb je:**
- Toegang tot echte data nodig (niet altijd beschikbaar voor HAVO/VWO-projecten)
- Calibratie nodig: parameters aanpassen tot model past bij data

**Conclusie:** Kwantitatieve validatie is **goudstandaard**, maar **niet altijd haalbaar** op middelbare school niveau.

### Validatie-aanpak kiezen

**Voor je project:**

1. **Minimaal:** Kwalitatieve validatie (gedragspatronen kloppen)
2. **Beter:** Semi-kwantitatieve validatie (orde-van-grootte klopt)
3. **Ideaal:** Kwantitatieve validatie (als je data hebt)

### Bronnen voor validatie

**Waar vind je vergelijkingsmateriaal?**

- **Video's:** YouTube (bijv. "ant trail formation", "Mexican wave stadium")
- **Wetenschappelijke artikelen:** Google Scholar (zoek op "ant foraging model")
- **Schoolboeken/documentaires:** Biologieboek over mieren, natuurdocumentaire
- **Schattingen:** Gebruik logisch nadenken ("50 mieren kunnen niet 10 ton voedsel dragen")

```{exercise} Oefening (Toepassen)
:label: oef-6-2

Schrijf **1 validatie-aanpak** voor jouw model:

1. **Kies niveau:** Kwalitatief, semi-kwantitatief, of kwantitatief (realistisch: kwalitatief of semi)
2. **Kies bron:** Wat ga je gebruiken als vergelijking? (video, artikel, schatting, etc.)
3. **Definieer criterium:** Wat moet kloppen? (bijv. "Paden moeten zichtbaar worden na 100 ticks")
4. **Verwacht resultaat:** Denk je dat je model valide is? Waarom wel/niet?

Schrijf 150-200 woorden. Als je al data hebt: voer validatie uit en rapporteer resultaat. Zo niet: beschrijf hoe je het zou doen.
```

---

## Beperkingen en aannames

Elk model heeft **beperkingen** en **aannames**. Dit erkennen is geen zwakte, maar **wetenschappelijke eerlijkheid**.

### Wat zijn beperkingen?

**Beperkingen** = dingen die je model **niet kan** vanwege simplificaties.

**Voorbeelden mieren-model:**

1. **2D-wereld:** Echte mieren bewegen ook verticaal (klimmen), dit model niet
2. **Geen energie:** Mieren worden niet moe, kunnen eeuwig zoeken
3. **Perfecte detectie:** Mieren "ruiken" voedsel direct als ze ernaast staan (werkelijkheid: graduele concentratie-gradient)
4. **Geen obstakels:** Echte wereld heeft stenen/planten, dit model niet (tenzij je het toevoegt)
5. **Identieke mieren:** Alle mieren zijn hetzelfde, geen koningin/werkers

### Wat zijn aannames?

**Aannames** = dingen die je **aanneemt** zonder te testen.

**Voorbeelden mieren-model:**

1. **Verdampingssnelheid is constant:** Aanname dat temperatuur/vochtigheid niet varieert
2. **Geurspoor is binair (ja/nee):** Aanname dat mieren niet onderscheid maken in intensiteit
3. **Mieren bewegen 1 stap per tick:** Aanname over snelheid
4. **Voedsel is oneindig deelbaar:** Aanname dat elke mier 1 eenheid kan dragen

### Waarom is dit belangrijk?

**Reden 1:** Je conclusies zijn alleen geldig **binnen** deze beperkingen.

**Verkeerd:** "Mieren gebruiken altijd het kortste pad."  
**Goed:** "In dit 2D-model zonder obstakels optimaliseren mieren naar het kortste pad."

**Reden 2:** Het toont dat je **kritisch** nadenkt over je model.

**Reden 3:** Het biedt **vervolgonderzoek** aan: "In de toekomst kan energie-verlies toegevoegd worden."

### Hoe schrijf je beperkingen?

**Template:**

> "Dit model heeft de volgende beperkingen:  
> 1. [Beperking 1]: [Effect op conclusies]  
> 2. [Beperking 2]: [Effect op conclusies]  
>  
> Deze beperkingen betekenen dat de resultaten [wat betekent het voor geldigheid]. Vervolgonderzoek kan [wat zou verbetering zijn]."

**Voorbeeld:**

> "Dit model heeft de volgende beperkingen:
> 1. **2D-wereld:** Verticale beweging van mieren wordt genegeerd. Effect: Paden kunnen in werkelijkheid ook over obstakels heen gaan, wat hier niet gemodelleerd is.  
> 2. **Geen energie:** Mieren worden niet moe. Effect: In werkelijkheid kunnen mieren stoppen met zoeken, wat hier niet gebeurt.
>
> Deze beperkingen betekenen dat de resultaten vooral geldig zijn voor **vlak terrein** en **korte zoektijden**. Vervolgonderzoek kan energie-verlies en 3D-beweging toevoegen voor realistischer gedrag."

:::{admonition} Let op: beperkingen zijn geen excuus
:class: warning
Beperkingen benoemen betekent NIET: "Mijn model is slecht, dus negeer de resultaten."  

Het betekent: "Mijn model is vereenvoudigd (zoals elk model), dit zijn de grenzen waarbinnen conclusies gelden."

**Goed model met beperkingen erkend** > **Perfect model geclaimd zonder bewijs**
:::

---

## Verslagstructuur

Je hebt een model, data, verificatie en validatie. Nu: **schrijf het op** in een gestructureerd verslag.

### Standaard wetenschappelijk verslag: IMRAD

**IMRAD** = Introduction, Method, Results, Analysis, Discussion

We passen dit aan voor je ABM-project:

### Structuur ABM-verslag

#### 1. Introductie (~300 woorden)

**Doel:** Context geven, onderzoeksvraag stellen.

**Kopjes:**
- **Achtergrond:** Wat is het fenomeen? Waarom interessant?
- **Onderzoeksvraag:** Wat wil je weten?
- **Hypothese:** Wat verwacht je? (optioneel, maar goed)

**Voorbeeldzinnen:**

> "Mieren zijn in staat om efficiënt voedsel te vinden zonder centrale coördinatie. Ze gebruiken chemische geursporen (feromonen) om informatie te delen. Dit emergente gedrag is een voorbeeld van zelfsorganisatie in de natuur."

> "De onderzoeksvraag is: **Hoe beïnvloedt de verdampingssnelheid van feromonen de efficiëntie van voedsel-verzameling door mieren?**"

> "Hypothese: Een optimale verdampingssnelheid bestaat waarbij goede paden blijven bestaan en slechte paden vervagen, leidend tot maximale efficiëntie."

#### 2. Methode (~400 woorden)

**Doel:** Leg uit hoe je model werkt (reproduceerbaar).

**Kopjes:**
- **Model-beschrijving:** Wat zijn de agents, de omgeving, de regels?
- **Parameters:** Welke kun je aanpassen? Standaardwaarden?
- **Abstractie-keuzes:** Wat is vereenvoudigd? Waarom?
- **Experimentopzet:** Welke parameter gevarieerd? Hoeveel runs?
- **Meetmethode:** Wat heb je gemeten? Hoe?

**Voorbeeldzinnen:**

> "Het model bestaat uit **agents** (mieren) die bewegen op een **grid** (2D-omgeving). De omgeving bevat een nest (centrum) en voedsel-patches (random verdeeld)."

> "Mieren volgen drie regels: (1) Zoek random als geen voedsel, (2) Keer terug naar nest met voedsel, (3) Volg geursporen als gedetecteerd."

> "De belangrijkste parameter is **verdampingssnelheid** (range: 0.01 - 0.1), die bepaalt hoe snel geursporen vervagen. Constante parameters: aantal-mieren = 50, hoeveelheid-voedsel = 50."

> "Het experiment varieerde verdampingssnelheid in 5 stappen (0.01, 0.03, 0.05, 0.07, 0.1), met 5 runs per waarde (totaal 25 runs). Elke run duurde 500 ticks."

#### 3. Resultaten (~300 woorden + grafiek)

**Doel:** Presenteer data objectief (zonder interpretatie).

**Kopjes:**
- **Dataset:** Samenvatting van metingen (tabel)
- **Grafiek:** Visualisatie van trend
- **Patroon-beschrijving:** Wat zie je? (beschrijven, niet verklaren)

**Voorbeeldzinnen:**

> "Tabel 1 toont het gemiddeld verzameld voedsel per verdampingssnelheid, met standaarddeviaties."

> "Figuur 1 illustreert dat verzameld voedsel eerst stijgt van 87.2 (bij 0.01) naar een maximum van 100.0 (bij 0.05), en daarna daalt naar 88.0 (bij 0.1)."

> "De standaarddeviatie is klein (< 3 voor alle waardes), wat wijst op betrouwbare metingen."

[Tabel en grafiek invoegen]

#### 4. Analyse en discussie (~500 woorden)

**Doel:** Interpreteer resultaten, beantwoord onderzoeksvraag.

**Kopjes:**
- **Interpretatie:** Waarom zie je dit patroon?
- **Hypothese-toets:** Klopte je hypothese?
- **Vergelijking met werkelijkheid:** Validatie (klopt het?)
- **Beperkingen:** Wat kan je model niet?
- **Conclusie:** Antwoord op onderzoeksvraag

**Voorbeeldzinnen:**

> "Het optimum bij verdampingssnelheid = 0.05 kan verklaard worden doordat bij deze waarde **goede paden** lang genoeg blijven bestaan om mieren te leiden, terwijl **slechte paden** (naar lege plekken) snel genoeg vervagen."

> "De hypothese dat een optimale verdampingssnelheid bestaat, wordt bevestigd door de data."

> "Kwalitatieve validatie toont dat het model realistisch gedrag vertoont: paden ontstaan, versterken bij gebruik, en optimaliseren naar korte routes, zoals bij echte mieren (Voorbeeld: Leafcutter mieren, Hölldobler & Wilson, 1990)."

> "Beperkingen: Het model negeert energie-verlies en 3D-beweging. Resultaten zijn daarom vooral geldig voor **vlak terrein** en **korte zoektijden**."

> "Conclusie: Binnen dit model is de optimale verdampingssnelheid **0.05**, wat een balans biedt tussen pad-persistentie en flexibiliteit. Dit suggereert dat in de natuur een vergelijkbaar optimum kan bestaan, afhankelijk van omgevingsfactoren."

#### 5. Bronnen

**Doel:** Vermeld waar je informatie vandaan hebt.

**Voorbeelden:**
- Video's (YouTube + URL)
- Artikelen (auteur, jaar, titel)
- Modellen (NetLogo Library)
- Boeken (auteur, titel, pagina)

**Format:** Gebruik standaard bronvermelding (APA of MLA, check met docent).

### Checklist verslag-kwaliteit

- [ ] **Objectief:** Geen "ik vind", maar "de data toont"
- [ ] **Precies:** Geen "veel" of "weinig", maar "87.2 ± 2.9"
- [ ] **Gestructureerd:** Duidelijke kopjes, logische volgorde
- [ ] **Reproduceerbaar:** Iemand anders kan je experiment herhalen
- [ ] **Kritisch:** Beperkingen benoemd, voorzichtige conclusies
- [ ] **Compleet:** Alle IMRAD-secties aanwezig

:::{tip}
**Start met verslag-outline**  
Schrijf EERST de kopjes en bulletpoints (wat komt waar?). Vul DAARNA de tekst in. Dit voorkomt rommelige structuur.
:::

---

## Veelgemaakte fouten in conclusies (±10 min)

Je bent bijna klaar. Laatste check: vermijd deze klassieke fouten!

### Fout 1: Causaliteit claimen zonder mechanisme

**Fout:** "Hogere verdampingssnelheid veroorzaakt minder verzameld voedsel."

**Probleem:** Je beschrijft **wat** (correlatie), niet **waarom** (mechanisme).

**Beter:** "Hogere verdampingssnelheid leidt tot snellere verdamping van geursporen, waardoor mieren minder guidance hebben en meer random zoeken, resulterend in minder verzameld voedsel."

**Regel:** Elke causale claim moet een **mechanisme-verklaring** hebben.

### Fout 2: Generaliseren buiten je scope

**Fout:** "Alle zwermen gedragen zich volgens deze regels."

**Probleem:** Je testte **mieren**, niet vissen/vogels/mensen.

**Beter:** "Binnen het mieren-foerageren model gelden deze regels. Andere zwermen (bijv. vissen) hebben mogelijk andere mechanismen."

**Regel:** Conclusies gelden alleen binnen de **scope van je model**.

### Fout 3: Kleine verschillen overdrijven

**Fout:** "Bij 0.03 is het 95, bij 0.05 is het 100, dus 0.05 is **significant beter**."

**Probleem:** 5% verschil kan **toeval** zijn (binnen variatie).

**Beter:** "Bij 0.05 is het gemiddelde iets hoger (100 vs 95), maar gegeven de variatie (SD ~2) is dit verschil klein."

**Regel:** Check of verschillen **groter zijn dan de standaarddeviatie**. Zo niet: voorzichtig formuleren.

### Fout 4: Verificatie en validatie verwarren

**Fout:** "Mijn model is gevalideerd omdat de code geen bugs heeft."

**Probleem:** Geen bugs = **verificatie**. Validatie = vergelijken met werkelijkheid.

**Beter:** "Het model is geverifieerd (regels werken zoals bedoeld) en kwalitatief gevalideerd (gedragspatronen lijken op echte mieren)."

**Regel:** **Verificatie** = technisch correct, **Validatie** = realistisch gedrag.

### Fout 5: Beperkingen negeren

**Fout:** "Dit bewijst dat mieren altijd optimaal foerageren."

**Probleem:** Je model heeft beperkingen (2D, geen energie, etc.), dus je **bewijst** niet alles.

**Beter:** "Binnen de beperkingen van dit model (2D, geen energie) tonen mieren optimalisatie-gedrag."

**Regel:** **Modellen suggereren/wijzen op/ondersteunen**, ze **bewijzen** zelden.

### Fout 6: Mening vermommen als conclusie

**Fout:** "Ik vind dit een interessant resultaat."

**Probleem:** Wetenschap is niet gebaseerd op mening.

**Beter:** "Dit resultaat toont een onverwacht optimum bij 0.05, wat suggereert..."

**Regel:** Vermijd **"ik vind/denk/geloof"**. Gebruik **"de data toont/suggereert"**.

### Fout 7: Correlatie = causatie

**Fout:** "Meer geurspoor correleert met meer voedsel, dus geurspoor veroorzaakt meer voedsel."

**Probleem:** Mogelijk is het andersom: meer voedsel → meer mieren lopen → meer geurspoor.

**Beter:** "Meer geurspoor en meer verzameld voedsel gaan samen. Mogelijk is dit een cyclische relatie: mieren volgen sporen → vinden voedsel → leggen meer sporen."

**Regel:** **Correlatie** betekent "gaan samen", niet "veroorzaakt". Leg mechanisme uit.

```{exercise} Oefening (Reflecteren)
:label: oef-6-3

**Wanneer is je model "goed genoeg"?**

Stel: Je hebt 3 opties voor je eindproject:

**Optie A:** Model werkt (geverifieerd), maar niet gevalideerd. Geen echte data gevonden.  
**Optie B:** Model werkt, kwalitatief gevalideerd (gedragspatronen kloppen met video's).  
**Optie C:** Model werkt, kwantitatief gevalideerd (exact gefitteerd op wetenschappelijke data).

Vragen:
1. Welke optie is **minimaal acceptabel** voor een voldoende? Waarom?
2. Welke optie is **realistisch haalbaar** voor HAVO/VWO niveau? Waarom?
3. **Trade-off:** Stel Optie C kost 20 uur extra werk. Is dat het waard? Argumenteer.

Schrijf 250-300 woorden. Gebruik argumenten over wetenschappelijke kwaliteit vs realisme vs tijd-investering.
```

---

## Verdiepende opgaven

Wil je verder? Deze opdrachten brengen je naar professioneel niveau.

```{exercise} Opdracht (Gevoeligheidsanalyse)
:label: verd-6-1

**Hoe robuust zijn je conclusies?**

Een **gevoeligheidsanalyse** test: Als je parameters iets verandert, veranderen je conclusies dan?

Methode:
1. Kies je belangrijkste conclusie (bijv. "Optimum is bij 0.05")
2. Varieer een andere parameter (bijv. aantal-mieren: 30, 50, 70)
3. Run je parameter-sweep opnieuw voor elke waarde
4. Check: Blijft optimum bij 0.05? Of verschuift het?

**Scenario's:**
- **Robuust:** Optimum blijft ~0.05 voor alle aantal-mieren → Conclusie is sterk
- **Niet robuust:** Optimum verschuift naar 0.03 bij 30 mieren, 0.07 bij 70 mieren → Conclusie is context-afhankelijk

**Opdracht:** Voer gevoeligheidsanalyse uit voor 1 conclusie. Schrijf 300-400 woorden + 2 grafieken (1 per parameter-waarde). Conclusie: Is je bevinding robuust?
```

```{exercise} Opdracht (Peer review)
:label: verd-6-2

**Wetenschappelijke integriteit: beoordeel elkaars werk**

Ruil verslagen met een klasgenoot. Beoordeel hun verslag als wetenschappelijke reviewer.

**Review-checklist:**

1. **Duidelijkheid:** Snap je hoe het model werkt? (ja/nee + toelichting)
2. **Reproduceerbaarheid:** Kun je het experiment herhalen op basis van Methode-sectie? (ja/nee + wat ontbreekt?)
3. **Data-kwaliteit:** Zijn er genoeg runs? Zijn SD's berekend? (ja/nee + suggestie)
4. **Validiteit conclusies:** Volgen conclusies logisch uit data? Of zijn er sprongen? (voorbeelden geven)
5. **Beperkingen:** Zijn beperkingen benoemd? Eerlijk? (ja/nee + wat mist?)
6. **Taal:** Objectief (geen "ik vind")? Precies (geen "veel/weinig")? (voorbeelden)

**Opdracht:** Schrijf 400-500 woorden review. Geef **3 positieve punten** en **3 verbeterpunten**. Wees **constructief**, niet destructief. Dit is hoe echte wetenschap werkt: peer review zorgt voor kwaliteit.
```

```{exercise} Opdracht (Alternatief model vergelijken)
:label: verd-6-3

**Welk model is beter?**

Stel: Je hebt 2 modellen voor hetzelfde fenomeen (bijv. mieren-foerageren).

**Model A:** Simpel, 3 regels, snel, kwalitatief goed  
**Model B:** Complex, 10 regels, traag, kwantitatief preciezer

**Opdracht:**
1. Implementeer beide (of gebruik bestaande NetLogo models uit Library)
2. Vergelijk:
   - Welk model is realistischer (validatie)?
   - Welk model is begrijpelijker (reproduceerbaarheid)?
   - Welk model is sneller (computational efficiency)?
3. Beslis: Welk model kies je voor je onderzoeksvraag? Waarom?

**Schrijf:** 500-600 woorden + 1 vergelijkingstabel. Kern: **Simpeler is niet altijd beter, complexer ook niet**. Het hangt af van je **doel**.
```

```{exercise} Opdracht (Literatuuronderzoek)
:label: verd-6-4

**Wat zegt de wetenschap erover?**

Zoek **2-3 wetenschappelijke artikelen** over je fenomeen (bijv. "ant foraging pheromone trails").

Gebruik: Google Scholar, Web of Science (via schoolbibliotheek), of PubMed.

**Opdracht:**
1. Lees abstracts + conclusies (niet heel artikel, dat duurt te lang)
2. Vind: Wat zijn de belangrijkste mechanismen volgens wetenschappers?
3. Vergelijk: Heeft jouw model deze mechanismen? Zo niet: waarom niet?
4. Evalueer: Zijn jouw conclusies consistent met literatuur? Of tegenstrijdig? (Beide OK, maar leg uit!)

**Schrijf:** 400-500 woorden + bronnenlijst (3 artikelen in APA-stijl). Dit brengt je van "schoolproject" naar "serieus onderzoek".
```

---

## PO-mijlpaal

Dit is de **laatste mijlpaal** voor je eindproject. Tijd om alles samen te brengen!

### Wat lever je op?

Een compleet pakket bestaande uit:

#### 1. Verslag-outline (1-2 pagina's)

**Niet** het hele verslag, maar een **skelet** met:

- Alle kopjes (Introductie, Methode, Resultaten, Discussie, Bronnen)
- Per sectie: 3-5 bulletpoints met wat erin komt
- Placeholder voor grafiek/tabel: [Figuur 1: parameter X vs Y]

**Voorbeeld outline:**

```
## Introductie
- Achtergrond: Mieren gebruiken feromonen voor foerageren
- Onderzoeksvraag: Hoe beïnvloedt verdampingssnelheid efficiëntie?
- Hypothese: Optimum bestaat tussen 0.03-0.07

## Methode
- Model: 50 mieren, grid 51×51, nest centrum, voedsel random
- Regels: (1) random zoeken, (2) terug met voedsel, (3) volg sporen
- Experiment: Varieer verdampingssnelheid 0.01-0.1, 5 runs per waarde
- Meting: Verzameld voedsel na 500 ticks

[etc.]
```

#### 2. Verificatie & Validatie checklist (1 pagina)

**Verificatie** (minimaal 3 checks uitgevoerd):

| Check                | Verwacht          | Getest | Resultaat | Actie indien fout |
| -------------------- | ----------------- | ------ | --------- | ----------------- |
| Initialisatie        | 50 mieren         | ✅      | 50        | -                 |
| Regel: random zoeken | Draait elke tick  | ✅      | Ja        | -                 |
| Output-meting        | Klopt met visueel | ✅      | Ja        | -                 |

**Validatie** (minimaal 1 niveau):

- Niveau: Kwalitatief
- Bron: YouTube video "Ant trail formation" (URL)
- Criterium: Paden moeten zichtbaar worden
- Resultaat: Paden ontstaan na ~100 ticks ✅

#### 3. Beperkingen en aannames (½ pagina)

**Beperkingen:**
1. 2D-wereld (geen verticale beweging)
2. Geen energie-verlies
3. [etc.]

**Aannames:**
1. Verdampingssnelheid is constant
2. [etc.]

#### 4. Plan voor laatste verbeteringen (½ pagina)

**Wat werkt al goed:**
- Model is geverifieerd
- Data verzameld (25 runs)
- Grafiek toont duidelijk patroon

**Wat moet nog:**
- Validatie uitbreiden (nog 1 bron zoeken)
- Beperkingen-sectie schrijven in verslag
- Bronnenlijst compleet maken
- Introducties schrijven (nu alleen outline)

**Planning:**
- Week 1: Validatie + beperkingen schrijven
- Week 2: Verslag compleet maken
- Week 3: Review + inleveren

### Checklist: je bent klaar als…

- [ ] Je hebt een **complete outline** met alle IMRAD-secties (kopjes + bulletpoints)
- [ ] Je hebt **minimaal 3 verificatie-checks** uitgevoerd en gedocumenteerd
- [ ] Je hebt **minimaal 1 validatie** gedaan (kwalitatief of hoger) en beschreven
- [ ] Je hebt **3-5 beperkingen** en **3-5 aannames** geïdentificeerd
- [ ] Je hebt een **realistisch plan** voor laatste verbeteringen (met tijdlijn)
- [ ] Je weet **welke fouten** je moet vermijden in conclusies (zie sectie 6.6)
- [ ] Je hebt feedback gevraagd aan docent/klasgenoot op je outline (optioneel maar sterk aangeraden)

### Waar komt dit terug in je eindproject?

Dit **IS** je eindproject! De mijlpaal levert:

- **Outline** → wordt volledige verslag
- **V&V checklist** → gaat in Methode-sectie (verificatie) en Discussie-sectie (validatie)
- **Beperkingen** → gaat in Discussie-sectie
- **Plan** → je roadmap naar inleveren

**Tips voor succes:**

- **Begin met outline:** Schrijf structuur VOOR je schrijft
- **Test je model grondig:** Verificatie kost tijd, maar voorkomt dat je verslag over buggy model gaat
- **Wees eerlijk over beperkingen:** Dit maakt je verslag **sterker**, niet zwakker
- **Plan realistisch:** Reken 2-3 uur voor verificatie, 1-2 uur voor validatie, 4-6 uur voor verslag schrijven

**Evaluatiecriteria:**

| Criterium                 | Onvoldoende                | Voldoende                      | Goed                          |
| ------------------------- | -------------------------- | ------------------------------ | ----------------------------- |
| Outline                   | Incomplete secties         | Alle IMRAD-secties met bullets | Gedetailleerd, logische flow  |
| Verificatie               | <3 checks of niet getest   | 3 checks uitgevoerd            | 5+ checks, systematisch       |
| Validatie                 | Geen validatie             | Kwalitatief (patroon klopt)    | Semi-kwantitatief of hoger    |
| Beperkingen               | Niet genoemd of vaag       | 3-5 beperkingen benoemd        | Kritisch, effecten beschreven |
| Plan                      | Geen plan of onrealistisch | Realistisch, met tijdlijn      | Gedetailleerd, checkpoints    |
| Wetenschappelijke houding | Vermijd fouten niet        | Bewust van fouten 6.1-6.7      | Voorbeelden in eigen werk     |

---

**Laatste stap:** Maak je verslag af en lever in! Je hebt nu alle tools: een werkend model, betrouwbare data, verificatie, validatie, en een heldere structuur. Succes!

