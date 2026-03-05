<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #3498db, #ffffff)" -->

# Verificatie, Validatie & Verslag

Q-highschool / Bijeenkomst 6

Notes:
Welkom bij de laatste inhoudelijke bijeenkomst van deze module! Jullie hebben nu een werkend model en waarschijnlijk al wat data verzameld. Vandaag: hoe check je of je model klopt, hoe vergelijk je met de werkelijkheid, en hoe schrijf je dit op in een wetenschappelijk verslag.

---

## Vandaag

**25 min:** Klassikaal
- Quiz: terugblik H1-5
- Check-in: waar sta je met je verslag?
- Verificatie, validatie, verslagstructuur

**65 min:** Zelfstandig werken
- Verslag outline maken
- V&V checklist uitvoeren

Notes:
Dit is de laatste bijeenkomst voor je het eindproject afrondt. Focus vandaag: zorgen dat je model betrouwbaar is en je verslag wetenschappelijk sterk.

***

## Opfrisquiz

Wat heb je onthouden van H1-5?

---

Wat is het belangrijkste kenmerk van emergent gedrag?

- Het wordt centraal aangestuurd
- Het ontstaat uit simpele lokale interacties
- Het is altijd voorspelbaar
- Het vereist complexe regels

<!-- .element: class="mc" -->

Notes:
Antwoord: Het ontstaat uit simpele lokale interacties. Emergentie is het kernidee: complex patroon uit simpele regels, bottom-up zonder centrale sturing.

---

Wat is het verschil tussen `setup` en `go` procedures in NetLogo?

- setup maakt agents, go verwijdert ze
- setup initialiseert, go runt per tick
- setup is voor patches, go voor turtles
- Er is geen verschil

<!-- .element: class="mc" -->

Notes:
Antwoord: setup initialiseert, go runt per tick. Basis NetLogo structuur: setup definiëert startpunt (1×), go bevat de dynamiek (elke tick).

---

Wat betekent "one run is no run" bij experimenteren?

- Je moet je model minimaal 2× runnen
- Eén run geeft geen betrouwbare conclusies vanwege toeval
- Je moet altijd BehaviorSpace gebruiken
- Lange runs zijn beter dan korte runs

<!-- .element: class="mc" -->

Notes:
Antwoord: Eén run geeft geen betrouwbare conclusies vanwege toeval. Door randomness verschillen uitkomsten per run. Meerdere runs + gemiddelde = betrouwbaar.

---

In welke volgorde doe je een parameter-sweep?

- Willekeurige waarden testen
- Eerst extreme waarden, dan verfijnen
- Van laag naar hoog in gelijke stappen
- Alleen de standaardwaarde testen

<!-- .element: class="mc" -->

Notes:
Antwoord: Van laag naar hoog in gelijke stappen. Systematisch variëren (bijv. 0.1, 0.2, 0.3, ...) geeft compleet beeld van parameter-effect en helpt patronen identificeren.

---

Wat is het doel van BehaviorSpace?

- Je model sneller maken
- Bugs vinden in je code
- Automatisch veel runs uitvoeren met verschillende parameters
- Je model delen met anderen

<!-- .element: class="mc" -->

Notes:
Antwoord: Automatisch veel runs uitvoeren met verschillende parameters. BehaviorSpace automatiseert parameter sweeps: set configuratie → NetLogo doet de rest. Je robotassistent voor grootschalige experimenten.

---

## Mooi! Je hebt de basis scherp

Nu door naar verificatie en validatie

<!-- .element: class="fragment" -->

Notes:
Als je minder dan 3 goed had: lees H1-5 kort door voordat je verder gaat met je verslag. Deze concepten zijn essentieel voor je eindproject.

***

## Check-in: Waar sta je?

Tijd voor een rondje

## Check-in: Waar sta je?

Tijd voor een rondje

Notes:
Ik wil even checken waar iedereen staat met het verslag. Zo kan ik beter helpen en weet ik waar we nadruk op moeten leggen.


---

## Verwachting vandaag

**Ideaal scenario:** Je hebt minimaal een complete outline van je verslag

**Plan B:** Je maakt vandaag die outline

**Plan C:** Je begint met verificatie en validatie

<!-- .element: class="fragment" -->

&nbsp;

**Voor iedereen:** Vandaag minimaal naar C (complete outline)!

<!-- .element: class="fragment" -->

Notes:
Het is oké waar je ook staat. Maar vandaag moet je minimaal een complete outline hebben met verificatie en validatie checklist. Dit is de basis voor je eindverslag.

***

# Verificatie & Validatie

Hoe weet je dat je model klopt?

Notes:
Goed, nu de kern: verificatie en validatie. Dit zijn misschien wel de belangrijkste stappen voor een wetenschappelijk sterk project.

---

## Het probleem

Je hebt een model gebouwd en data verzameld...

**Maar:**

Werkt je code wel zoals bedoeld? (verificatie)

<!-- .element: class="fragment" -->

Lijkt het op de werkelijkheid? (validatie)

<!-- .element: class="fragment" -->

&nbsp;

Zonder deze checks zijn je conclusies **onbetrouwbaar**

<!-- .element: class="fragment" -->

Notes:
Verificatie = technisch correct (geen bugs). Validatie = realistisch (lijkt op werkelijkheid). Beide zijn nodig voor betrouwbare wetenschap.

---

## Verificatie vs Validatie

| Aspect        | Verificatie                                | Validatie                            |
| ------------- | ------------------------------------------ | ------------------------------------ |
| **Vraag**     | Werkt de code zoals bedoeld?               | Lijkt het model op de werkelijkheid? |
| **Focus**     | Technische correctheid                     | Realisme                             |
| **Methode**   | Tests uitvoeren (edge cases, initieel)     | Vergelijken met data/observaties     |
| **Voorbeeld** | _"Worden er altijd 50 mieren aangemaakt?"_ | _"Vormen mieren paden zoals echt?"_  |

<!-- .element: style="font-size: 0.6em;" -->

💡 **Beide zijn nodig** voor een compleet project!

<!-- .element: class="fragment" style="font-size: 0.6em;" -->

Notes:
Verificatie komt eerst (code moet kloppen). Validatie komt daarna (gedrag moet realistisch zijn).

---

## Verificatie: 5-punten checklist

Minimaal deze 5 tests uitvoeren:

1. **Initialisatie** - Klopt startconditie? (bijv. juist aantal agents)
2. **Regel-uitvoering** - Doen agents wat je bedoelt? (bijv. volgen ze spoor?)
3. **Output-meting** - Klopt gemeten data met visueel?
4. **Extreme waarden** - Gedraagt model zich logisch bij randgevallen? (bijv. 0 mieren of 1 mier)
5. **Reproduceerbaarheid** - Geeft zelfde seed zelfde resultaat?

<!-- .element: style="font-size: 0.8em" -->

Notes:
Deze 5 checks dekken de meest kritieke aspecten. Je hoeft niet alles te testen, maar deze 5 zijn essentieel.

---

## Voorbeeld: Verificatie mieren-model

| Check               | Test                             | Verwacht | Resultaat | Status |
| ------------------- | -------------------------------- | -------- | --------- | ------ |
| Initialisatie       | `count turtles`                  | 50       | 50        | ✅      |
| Regel-uitvoering    | Mier volgt spoor bij detectie    | Ja       | Ja        | ✅      |
| Output-meting       | Verzameld voedsel = visueel telt | Match    | Match     | ✅      |
| Extreme waarden     | 0 mieren → 0 voedsel verzameld   | 0        | 0         | ✅      |
| Reproduceerbaarheid | Seed 123 geeft zelfde data       | Ja       | Ja        | ✅      |

<!-- .element: style="font-size: 0.65em" -->

Notes:
Dit is hoe je verificatie documenteert in je verslag (tabel in Methode-sectie).

---

## Validatie: 3 niveaus

**Niveau 1: Kwalitatief** - Lijken patronen op werkelijkheid? (makkelijkst)

**Niveau 2: Semi-kwantitatief** - Klopt orde-van-grootte? (realistisch voor jullie)

<!-- .element: class="fragment" -->

**Niveau 3: Kwantitatief** - Exacte fit met data? (lastig, vaak niet haalbaar)

<!-- .element: class="fragment" -->

&nbsp;

**Doel voor jullie:** minimaal niveau 1, idealiter niveau 2

<!-- .element: class="fragment" -->

Notes:
Niveau 1 is vaak genoeg voor schoolproject. Niveau 2 is prima als je schattingen kunt doen. Niveau 3 vereist echte dataset (vaak niet beschikbaar).

---

## Niveau 1: Kwalitatieve validatie

**Vraag:** Lijkt het **patroon** op werkelijkheid?

**Methode:** Vergelijk visueel gedrag met observaties/video's

**Voorbeeld mieren:**

- Paden vormen tussen nest en voedsel
- Paden versterken bij meer gebruik
- Kortste pad wordt dominanter

<!-- .element: class="fragment" style="font-size: 0.8em" -->

_**Bron:** YouTube video "Ant trail formation"_

<!-- .element: class="fragment" style="font-size: 0.6em" -->

Notes:
Dit niveau is goed haalbaar: zoek video/artikel, vergelijk gedrag. Dit is al genoeg om je model "plausibel realistisch" te noemen.

---

## Niveau 2: Semi-kwantitatief

**Vraag:** Klopt de **orde-van-grootte**?

**Methode:** Vergelijk getallen met schattingen (niet exact, maar ruwweg)

**Voorbeeld Mexican wave:**

Werkelijkheid: wave maakt rondje in ~20-30 sec

<!-- .element: class="fragment" -->

Model: wave maakt rondje in ~25 sec (50 ticks @ 2 ticks/sec)

<!-- .element: class="fragment" -->

✅ Orde-van-grootte klopt (niet 2 sec of 10 minuten)

<!-- .element: class="fragment" -->

Notes:
Je hoeft geen perfecte match, alleen "in de buurt". Als je model 100× te snel of te langzaam is, dan klopt er iets niet.

---

## Validatie bronnen

**Waar vind je vergelijkingsmateriaal?**

- YouTube video's (bijv. "ant foraging behavior")
- Wetenschappelijke artikelen (Google Scholar)
- Schoolboeken / documentaires
- Logische schattingen (bijv. "mieren lopen ~1 cm/sec")

&nbsp;

Tip: Start met Google "[jouw fenomeen] model validation"

<!-- .element: class="fragment" -->

Notes:
Je hebt vaak geen perfecte data. Dat is prima! Schattingen + video's + artikelen zijn genoeg voor niveau 1-2.

***

# Verslagstructuur

**IMRAD**: de wetenschappelijke standaard

Notes:
Nu naar het verslag: hoe schrijf je dit allemaal op? We gebruiken IMRAD, de standaard wetenschappelijke structuur.

---

## Wat is IMRAD?

**I**ntroductie - Waarom is dit interessant?

**M**ethode - Hoe werkt je model?

**R**esultaten - Wat heb je gemeten?

**A**nalyse & Discussie - Wat betekent dit?

**B**ronnen - Waar komt je info vandaan?

&nbsp;

Deze structuur is standaard in de empirisch wetenschappelijke artikelen

<!-- .element: class="fragment" -->

Notes:
IMRAD = internationale standaard voor rapporteren. Zelfde structuur als echte wetenschappers gebruiken.

---

## 1. Introductie (~300 woorden)

**Kopjes:**
- Achtergrond (wat is het fenomeen?)
- Onderzoeksvraag (wat wil je weten?)
- Hypothese (wat verwacht je?)

&nbsp;

**Voorbeeld:**

_"Mieren gebruiken feromonen om voedsel te vinden zonder centrale coördinatie. Dit emergente gedrag is een voorbeeld van zelforganisatie."_

<!-- .element: class="fragment" style="font-size: 0.7em" -->

_"Onderzoeksvraag: Hoe beïnvloedt de verdampingssnelheid van feromonen de efficiëntie van voedsel-verzameling?"_

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Introductie geeft context: waarom is dit interessant en wat ga je onderzoeken?

---

## 2. Methode (~400 woorden)

**Kopjes:**
- Model-beschrijving (agents, omgeving, regels)
- Parameters (welke, met standaardwaarden)
- Abstractie-keuzes (wat is vereenvoudigd?)
- Experimentopzet (welke parameter? hoeveel runs?)
- Meetmethode (wat meet je? hoe?)

&nbsp;

**Doel:** Iemand anders moet je experiment kunnen **reproduceren**

<!-- .element: class="fragment" style="font-size: 0.7em"  -->

Notes:
Methode = instructiehandleiding voor je experiment. Als details ontbreken, kan niemand je onderzoek herhalen.

---

## 3. Resultaten (~300 woorden + grafiek/tabel)

**Kopjes:**
- Dataset (samenvatting metingen in tabel)
- Grafiek (visualisatie van trend)
- Patroon-beschrijving (wat zie je?)

**Let op:** Hier alleen **beschrijven**, niet **interpreteren**!

<!-- .element: class="fragment" style="font-size: 0.7em" -->

**Goed:** _"Verzameld voedsel stijgt van 87 (0.01) naar 100 (0.05), daalt daarna naar 88 (0.1)."_

<!-- .element: class="fragment" style="font-size: 0.7em" -->

**Fout:** _"De daling bij 0.1 komt doordat sporen te snel verdampen."_ ← Dit hoort in Discussie!

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Resultaten = objectieve feiten. Discussie = interpretatie. Houd deze twee strikt gescheiden.

---

## 4. Analyse & Discussie (~500 woorden)

**Kopjes:**
- Interpretatie (waarom zie je dit patroon?)
- Hypothese-toets (klopte je verwachting?)
- Vergelijking met werkelijkheid (validatie)
- Beperkingen (wat kan je model niet?)
- Conclusie (antwoord op onderzoeksvraag)

&nbsp;

**Dit is de belangrijkste sectie:** hier laat je zien dat je **kritisch** nadenkt!

<!-- .element: class="fragment" style="font-size: 0.8em" -->

Notes:
Discussie = van data naar betekenis. Hier leg je verbanden, verklaar je patronen, en benoem je grenzen van je model.

---

## 5. Bronnen

**Vermeld alle bronnen:**

- Video's (met URL)
- Artikelen (auteur, jaar, titel)
- NetLogo modellen (Library naam)
- Boeken (auteur, titel, pagina)

&nbsp;

**Format:** Gebruik het APA format bij bronvermeldingen. Weet je niet wat dat is? Google weet het!

<!-- .element: class="fragment" style="font-size: 0.8em" -->

Notes:
Bronvermelding = wetenschappelijke integriteit. Geef credit aan waar je ideeën vandaan komen.

***

# Veelgemaakte fouten

Vermijd deze 7 klassiekers!

Notes:
Ik zie elk jaar dezelfde fouten terugkomen. Hier zijn de top 7 - vermijd ze en je verslag wordt stukken beter!

---

## Fout 1: Causaliteit zonder mechanisme

**Fout:** _"Hogere verdampingssnelheid veroorzaakt minder voedsel."_

**Probleem:** Je zegt **wat** (correlatie), niet **waarom** (mechanisme)

<!-- .element: class="fragment" -->

**Beter:** _"Hogere verdampingssnelheid leidt tot snellere verdamping van sporen, waardoor mieren minder guidance hebben, resulterend in minder verzameld voedsel."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

Elke causale claim moet een **mechanisme-verklaring** hebben.

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Correlatie zien is makkelijk. Mechanisme uitleggen is wetenschap!

---

## Fout 2: Generaliseren buiten scope

**Fout:** _"Alle zwermen gedragen zich volgens deze regels."_

**Probleem:** Je testte **mieren**, niet vissen/vogels/mensen

<!-- .element: class="fragment" -->

**Beter:** _"Binnen het mieren-foerageren model gelden deze regels. Andere zwermen (bijv. vissen) hebben mogelijk andere mechanismen."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

Conclusies gelden alleen binnen de **scope van je model**

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Je model is specifiek. Conclusies ook!

---

## Fout 3: Kleine verschillen overdrijven

**Fout:** _"Bij 0.05 is het 100, dus dit is **significant beter** dan 95 bij 0.03."_

**Probleem:** 5% verschil kan **toeval** zijn (binnen variatie)

<!-- .element: class="fragment" -->

**Beter:** _"Bij 0.05 is het gemiddelde iets hoger (100 vs 95), maar gegeven de standaarddeviatie (~2) is dit verschil klein."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

Check of verschillen **groter zijn dan variatie** (SD)

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Kleine verschillen kunnen ruis zijn. Wees voorzichtig met claims.

---

## Fout 4: Verificatie ≠ Validatie verwarren

**Fout:** _"Mijn model is gevalideerd omdat de code geen bugs heeft."_

**Probleem:** Geen bugs = **verificatie**, niet validatie!

<!-- .element: class="fragment" -->

**Beter:** _"Het model is geverifieerd (code werkt zoals bedoeld) en kwalitatief gevalideerd (patronen lijken op echte mieren)."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

**Verificatie** = technisch correct. <br/> **Validatie** = realistisch gedrag

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Deze twee begrippen door elkaar halen is een veel voorkomende fout!

---

## Fout 5: Beperkingen negeren

**Fout:** _"Dit bewijst dat mieren altijd optimaal foerageren."_

**Probleem:** Je model heeft beperkingen (2D, geen energie), dus je **bewijst** niet alles

<!-- .element: class="fragment" -->

**Beter:** _"Binnen de beperkingen van dit model (2D, geen energie) tonen mieren optimalisatie-gedrag."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

Modellen **suggereren/wijzen op**, ze **bewijzen** zelden

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Beperkingen benoemen maakt je verslag sterker, niet zwakker!

---

## Fout 6: Mening als conclusie

**Fout:** _"Ik vind dit een interessant resultaat."_

**Probleem:** Wetenschap is niet gebaseerd op mening

<!-- .element: class="fragment" -->

**Beter:** _"Dit resultaat toont een onverwacht optimum bij 0.05, wat suggereert dat een balans bestaat tussen..."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

Vermijd **"ik vind/denk/geloof"**. Gebruik **"de data toont/suggereert"**

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
"Ik vind" hoort niet in wetenschappelijk schrijven. Laat data spreken!

---

## Fout 7: Correlatie = Causatie

**Fout:** _"Meer geurspoor correleert met meer voedsel, dus geurspoor veroorzaakt meer voedsel."_

**Probleem:** Het kan andersom zijn: meer voedsel → meer mieren → meer spoor

<!-- .element: class="fragment" -->

**Beter:** _"Meer geurspoor en meer voedsel gaan samen. Mogelijk is dit een cyclische relatie: mieren volgen sporen → vinden voedsel → leggen meer sporen."_

<!-- .element: class="fragment" style="font-size: 0.7em; border: 1px solid black; background-color: lightgrey" -->

**Correlatie** = "gaan samen", niet "veroorzaakt". <br/> Leg mechanisme uit

<!-- .element: class="fragment" style="font-size: 0.7em" -->

Notes:
Klassieke wetenschappelijke fout. Correlatie is niet causaliteit!

---

## Samenvatting

- **Verificatie:** Test of je code klopt (5-punten checklist)
- **Validatie:** Vergelijk met werkelijkheid (minimaal kwalitatief)
- **IMRAD-structuur:** Introductie, Methode, Resultaten, Discussie, Bronnen
- **Vermijd fouten:** Mechanismen uitleggen, beperkingen benoemen, objectief blijven

&nbsp;

**Doel vandaag:** Complete outline + V&V checklist

<!-- .element: class="fragment" -->

Notes:
Dit zijn de bouwstenen voor je eindproject. Nu aan de slag: verslag outline maken!

***

# Zelfstandig werken

65 minuten aan je verslag

Notes:
De rest van de tijd werk je aan je verslag. Focus: outline maken en verificatie/validatie uitvoeren.

---

## Opdracht vandaag

1. Complete verslag **outline** (alle IMRAD kopjes + 3-5 bullets per sectie)
2. **Verificatie checklist** (minimaal 3 checks uitgevoerd + gedocumenteerd)
3. **Validatie beschrijving** (minimaal 1 niveau, met bron)
4. **Beperkingen lijst** (3-5 beperkingen van je model)

&nbsp;

Zie H6 voor gedetailleerde uitleg en voorbeelden!

Notes:
Dit zijn de bouwstenen voor je eindverslag. Als je deze vandaag afhebt, ben je goed op weg!

---

## Werkwijze

**Stap 1 (20 min):** Verificatie uitvoeren
- Test je model met de 5-punten checklist
- Documenteer in tabel (verwacht vs werkelijk)
- Fix bugs als je die vindt!

**Stap 2 (15 min):** Validatie zoeken
- Zoek bronnen (video/artikel/schatting)
- Vergelijk gedrag of getallen met je model
- Schrijf bevindingen op (niveau 1 of 2)

Notes:
Begin met verificatie - als je code bugs heeft, moet je die eerst fixen! Daarna validatie: zoek extern materiaal om mee te vergelijken.

---

## Werkwijze (vervolg)

**Stap 3 (20 min):** Outline maken
- Maak IMRAD-structuur met kopjes
- Vul bullets in (wat komt in elke sectie?)
- Voeg placeholders toe voor grafiek/tabel

**Stap 4 (10 min):** Beperkingen identificeren
- Wat heeft je model **niet**?
- Wat heb je **vereenvoudigd**?
- Schrijf 3-5 beperkingen op

Notes:
Outline = skelet van je verslag. Eerst structuur, dan inhoud! Beperkingen identificeren is kritisch nadenken over je eigen werk.

---

## Hulp beschikbaar

**Vastgelopen?**

- Overleg met klasgenoten
- Lees H6 voor uitgebreide voorbeelden
- Kijk naar voorbeeldtabellen in syllabus
- Steek hand op

&nbsp;

Notes:
Ik loop rond om te helpen. Dit is serieus werk, geen gezellig kletsen - maar overleg mag!

---

## Checklist: je bent klaar als...

- Alle 5 verificatie-checks gedaan + gedocumenteerd
- Minimaal 1 validatie (met bron) beschreven
- Complete IMRAD outline (kopjes + 3-5 bullets per sectie)
- 3-5 beperkingen geïdentificeerd

&nbsp;

**Klaar met checklist?** → Begin met volledig uitschrijven van een sectie (bijv. Introductie)

Notes:
Deze checklist = minimale output voor vandaag. Als je sneller klaar bent: prima, ga door met uitschrijven!

---

## Tijd om te beginnen!

**Succes!**

<!-- .element: class="fragment" -->

Notes:
Breakout rooms gaan nu open. Zet focus-modus aan en ga aan de slag. Tot over 65 minuten voor afsluiting!

***

# Afsluiting

Wat hebben we bereikt?

Notes:
Breakout rooms gesloten. Hopelijk heeft iedereen nu een goede basis!

---

## Volgende week

**Geen nieuwe stof!**

- Werktijd voor eindproject (90 min)
- Individuele feedback op outlines
- Q&A over verificatie/validatie/verslag

&nbsp;

**Doel:** Volledige verslag geschreven, klaar voor inleveren!

Notes:
Volgende week is puur werktijd. Kom met vragen en gebruik de tijd efficiënt!

---

## Huiswerk / Voorbereiding

**Voor volgende week:**

1. Outline omzetten naar volledige tekst (Introductie + Methode + Resultaten)
2. Validatie afmaken (als nog niet compleet)
3. Beperkingen-sectie schrijven in Discussie
4. Bronnenlijst compleet maken

&nbsp;

Start met Introductie en Methode - die zijn vaak makkelijkst!

Notes:
Realistische inzet: 3-4 uur werk deze week. Spreidt het uit!

---

## Laatste tips

**Outline eerst, schrijven later** - Structuur voorkomt rommelig verslag

**Verificatie = basis** - Fix bugs voordat je verder gaat

**Beperkingen zijn geen zwakte** - Het toont kritisch denken

**Data laten spreken** - Vermijd "ik vind/denk", gebruik "de data toont"

Notes:
Onthoud deze principes en je verslag wordt sterk!

---

## Tot volgende week, online!

Succes met het uitwerken van je verslag

Notes:
Laatste kans voor vragen. Anders: tot volgende week! Zet 'm op!
