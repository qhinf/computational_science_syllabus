<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #3498db, #ffffff)" -->

# Experimenteren & Data

Q-highschool / Bijeenkomst 5

Notes:
Welkom bij les 5! Jullie model zou nu moeten werken. Tijd om te experimenteren en data te verzamelen.

---

## Vandaag

**25 min:** Klassikaal
- Quiz: terugblik H1-4
- Check-in: waar sta je?
- Experimenteren: waarom en hoe

**65 min:** Zelfstandig werken
- Experimenteren met je model
- Data verzamelen en analyseren

Notes:
Korte klassikale intro, daarna veel tijd om te werken aan je experimenten.

***

## Opfrisquiz

Wat heb je onthouden van de afgelopen weken?

---

Wat is de gouden regel over modellen?

- Een model moet perfect zijn
- Een model is altijd fout, maar kan nuttig zijn
- Een model moet alles bevatten
- Een model is hetzelfde als de werkelijkheid

<!-- .element: class="mc" -->

Notes:
Antwoord: Een model is altijd fout, maar kan nuttig zijn. "All models are wrong, but some are useful" - George Box.

---

Wat vergeet je NOOIT in je `go` procedure?

- `setup`
- `tick`
- `clear-all`
- `reset-ticks`

<!-- .element: class="mc" -->

Notes:
Antwoord: tick! Vergeet je die, dan staat de tijd stil en werken plots niet. Setup en reset-ticks horen in setup, niet in go.

---

Wat is het verschil tussen verificatie en validatie?

- Geen verschil, zelfde begrip
- Verificatie = klopt de code, Validatie = klopt het met realiteit
- Validatie = klopt de code, Verificatie = klopt het met realiteit
- Beide betekenen "testen"

<!-- .element: class="mc" -->

Notes:
Antwoord: Verificatie = klopt de code (doet het wat je wilde?), Validatie = klopt het met realiteit (komt het overeen met de echte wereld?).

---

Welke volgorde bouw je je model?

- Alles tegelijk programmeren
- Eerst compleet design, dan code
- Incrementeel: klein beginnen, steeds uitbreiden, testen
- Random code schrijven en dan fixen

<!-- .element: class="mc" -->

Notes:
Antwoord: Incrementeel bouwen. Klein beginnen, steeds iets toevoegen, na elke toevoeging testen. Zo vind je fouten makkelijk.

---

Wat is emergent gedrag?

- Gedrag dat je expliciet programmeert per agent
- Complex groepsgedrag uit simpele individuele regels
- Foutief gedrag in je simulatie
- Het gedrag van één specifieke agent

<!-- .element: class="mc" -->

Notes:
Antwoord: Complex groepsgedrag uit simpele regels. Het patroon ontstaat spontaan door interacties, zonder dat je het direct hebt geprogrammeerd.

---

## Mooi! Je hebt de basis scherp

Nu door naar experimenteren

<!-- .element: class="fragment" -->

Notes:
Deze quiz laat zien: je kent de concepten. Nu gaan we ze gebruiken voor wetenschappelijk onderzoek.

***

## Check-in: Waar sta je?

Tijd voor een rondje

Notes:
Ik wil even checken waar iedereen staat met de eindopdracht. Zo kan ik beter helpen en weet ik wat jullie vandaag nodig hebben.

---

## Poll: Status eindopdracht

Waar sta jij nu? Beantwoord de poll in de chat.

**A:** Conceptueel model nog niet af

**B:** Model bouwen in NetLogo (werk-in-uitvoering)

**C:** Model werkt, klaar voor experimenteren

**D:** Al bezig met experimenten/data verzamelen


Notes:
Steek je hand op of type in de chat. Geen oordeel, gewoon checken waar iedereen staat. Ideaal: je zit op C of D.

---

## Verwachting vandaag

**Ideaal scenario:** Je model werkt en je kunt experimenteren

**Plan B:** Je model werkt bijna, vandaag afronden

**Plan C:** Je zit nog vroeger in het proces

<!-- .element: class="fragment" -->

&nbsp;

**Voor iedereen:** We gaan vandaag door met waar JIJ staat

<!-- .element: class="fragment" -->

Notes:
Het is oké als je nog niet bij experimenteren bent. Dan werk je vandaag aan wat je nodig hebt. Maar wél belangrijke info over experimenteren, want dat komt eraan.

***

## Experimenteren: Het waarom

Je model werkt. Nu wordt het wetenschap.

---

## One run is no run

Je model bevat **randomness**:
- Startposities zijn random
- Beweging is random  
- Kansen leiden tot verschillende resultaten

<!-- .element: class="fragment" -->

**Gevolg:** Elke run geeft andere resultaten!

<!-- .element: class="fragment" -->

Notes:
Als je model random-elementen bevat (en dat doet het waarschijnlijk), dan krijg je elke keer andere uitkomsten. Één run is niet betrouwbaar.

---

## Voorbeeld: Mieren voedsel verzamelen

5 runs met **exact dezelfde parameters**:

- Run 1: 87 eenheden verzameld
- Run 2: 91 eenheden
- Run 3: 83 eenheden  
- Run 4: 89 eenheden
- Run 5: 86 eenheden

<!-- .element: class="fragment" -->

**Gemiddelde:** 87.2 eenheden

<!-- .element: class="fragment" -->

Notes:
Zie je? Variatie van 83 tot 91. Als je maar één run doet (bijv. 83), denk je dat het resultaat slechter is dan het echt is.

---

## Waarom meerdere runs

**1. Toeval uitfilteren** - Gemiddelde is betrouwbaarder

**2. Variatie meten** - Hoe groot zijn de verschillen?

<!-- .element: class="fragment" -->

**3. Reproduceerbaarheid** - Anderen kunnen je resultaat checken

<!-- .element: class="fragment" -->

**Vuistregel:** Minimaal **5 runs** per parameter-waarde

<!-- .element: class="fragment" -->

Notes:
Met meerdere runs krijg je een compleet beeld: gemiddelde én spreiding. Dit is essentieel voor wetenschappelijke conclusies.

***

## Experimenteren: Het hoe

Systematisch je parameters variëren

---

## Stap 1: Kies één parameter

Begin simpel: varieer **één ding tegelijk**

❌ **Fout:** Verander aantal-mieren EN verdampingssnelheid tegelijk

✅ **Goed:** Verander alleen verdampingssnelheid

<!-- .element: class="fragment" -->

Waarom? Anders weet je niet wat het effect veroorzaakt!

<!-- .element: class="fragment" -->

Notes:
Dit is cruciaal: als je twee dingen tegelijk verandert, kun je niet zeggen wat het effect veroorzaakt. Wetenschappelijke methode = isoleer variabelen.

---

## Stap 2: Bepaal de range

**Te klein:** $0.04, 0.045, 0.05$  
→ Weinig variatie, klein verschil

**Te groot:** $0.01, 0.5, 1.0$  
→ Extreme waarden zijn niet interessant

**Goed:** $0.01, 0.03, 0.05, 0.07, 0.1$  
→ Verwacht interessante dynamiek in dit bereik

<!-- .element: class="fragment" -->

Notes:
Bepaal je range op basis van verkennende runs. Test eerst twee extremen om te zien waar interessant gedrag zit.

---

## Stap 3: Kies stapgrootte

Hoeveel waarden test je?

**Richtlijn:** 5-8 verschillende waarden

**Voorbeeld:** $0.01, 0.03, 0.05, 0.07, 0.1$

<!-- .element: class="fragment" -->

**Totaal aantal runs:**  
Waarden × Runs per waarde = 5 × 5 = **25 runs**

<!-- .element: class="fragment" -->

Notes:
Niet te veel (te veel werk), niet te weinig (te grof). 5-8 waarden is goed uitvoerbaar en geeft goede inzichten.

---

## Stap 4: Wat ga je meten?

Je **output** moet je onderzoeksvraag beantwoorden

**Voorbeelden:**

| Vraag | Goede output |
|-------|--------------|
| Efficiëntie voedsel verzamelen? | Verzameld voedsel na 500 ticks |
| Bij welke reactie-tijd sterft wave uit? | Aantal rondes |
| Effect besmettingskans op piek? | Max aantal besmetten |

<!-- .element: class="fragment" style="font-size: 0.6em"-->

Notes:
Output moet relevant zijn. "Aantal ticks" is geen goede output als je altijd tot 500 ticks laat runnen. Meet iets dat varieert!

***

## Uitvoeren: <br/>Handmatig vs BehaviorSpace

Twee manieren om runs te doen

---

## Optie A: Handmatig

**Stappen:**
1. Maak tabel in Excel
2. Voor elke run: pas parameter aan, klik Setup, klik Go
3. Noteer output in tabel
4. Herhaal 25 keer

<!-- .element: class="fragment" -->

**Voordeel:** Simpel, ziet wat gebeurt  
**Nadeel:** Saai, foutgevoelig

<!-- .element: class="fragment" -->

Notes:
Voor je eerste experiment: doe het handmatig. Je leert het proces kennen. Voor grote experimenten (25+ runs): overweeg BehaviorSpace.

---

## Optie B: BehaviorSpace

NetLogo's ingebouwde experiment-tool

**Hoe:**
1. Tools → BehaviorSpace → New
2. Vul in: parameters, repetities, output
3. Klik Run → NetLogo doet alles automatisch
4. Export naar CSV

<!-- .element: class="fragment" -->

**Voordeel:** Automatisch, geen fouten, CSV export  
**Nadeel:** Leer-curve

<!-- .element: class="fragment" -->

Notes:
BehaviorSpace is krachtig voor grote experimenten. Het bespaart uren werk. In de syllabus staat een uitgebreide handleiding.

---

## Data verwerken

Als je runs klaar zijn:

1. **Bereken gemiddelden** per parameter-waarde
2. **Maak een grafiek** (parameter op x-as, output op y-as)
3. **Zoek patronen** - Wat zie je gebeuren?

<!-- .element: class="fragment" -->

Notes:
Een grafiek maakt je data inzichtelijk. Vaak zie je duidelijk waar het optimum ligt of hoe het gedrag verandert.

***

## Zelfstandig Werken

**65 minuten** om aan je eindopdracht te werken

Notes:
Nu krijgen jullie tijd om te doen wat JIJ nodig hebt. Experimenteren, model afmaken, of data analyseren.

---

## Waar werk je aan?

**Nog aan model bouwen?**  
→ Maak het af, test grondig

**Model werkt?**  
→ Begin met experimenteren (volg de stappen!)

**Al data verzameld?**  
→ Maak grafieken en analyseer

Notes:
Check voor jezelf: wat is mijn volgende stap? Werk daar de komende 65 minuten aan.

---

## Tips voor vandaag

**Test je output** - Klopt wat je meet?

**Begin klein** - Doe eerst 5 runs handmatig

**Noteer alles** - Welke parameter, welke waarde, welk resultaat

**Vraag hulp** - Steek je hand op als je vastloopt

<!-- .element: class="fragment" -->

Notes:
Incrementeel werken geldt ook voor experimenteren. Begin simpel, breid uit als het werkt.

---

# Aan de slag!

<!-- .element: class="fragment" -->

**Succes!**

<!-- .element: class="fragment" -->

Notes:
Veel succes allemaal! Vergeet niet: experimenteren is het leukste deel. Je ontdekt hoe je model zich gedraagt bij verschillende instellingen.

***

## Welkom terug!

Hoe ging het experimenteren?

Notes:
Laat een paar studenten delen: wat heb je gevonden? Wat was verrassend? Waar loop je tegenaan?

---

## Veelvoorkomende uitdagingen

**"Mijn resultaten variëren enorm"**  
→ Doe meer runs (10 in plaats van 5)

**"Ik zie geen verschil tussen waarden"**  
→ Mogelijk te kleine stappen, probeer grotere range

**"BehaviorSpace crasht"**  
→ Bug in je model, test handmatig eerst

<!-- .element: class="fragment" -->

Notes:
Dit zijn normale problemen. Experimenteren is iteratief: je past aan, test opnieuw, leert van fouten.

---

## Volgende stappen

**Voor volgende les:**
- Minimaal 1 compleet experiment gedaan
- Data in tabel en grafiek
- Eerste conclusies getrokken

<!-- .element: class="fragment" -->

Notes:
Dit is essentieel voor je verslag. Zonder data geen conclusies, zonder conclusies geen wetenschappelijk verslag.

---

## Vragen?

&nbsp;

Notes:
Check of er nog vragen zijn over experimenteren, data verzamelen, of de eindopdracht.
