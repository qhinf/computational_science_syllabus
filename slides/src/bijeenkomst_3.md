<!-- .slide: data-background-gradient="linear-gradient(to bottom right, #3498db, #ffffff)" -->

# NetLogo Programmeren

Q-highschool / Bijeenkomst 3

Notes:
Vandaag gaan jullie zelf code schrijven in NetLogo! Dit is een hands-on les waar je veel zelfstandig gaat werken.

---

## Vandaag

- Setup en Go: basis van elk model
- Turtles maken en bewegen
- Zelfstandig werken aan opdrachten
- Hulp vragen en elkaar helpen

---

## Programma

**10 min:** Introductie & uitleg opdrachten

**70 min:** Zelfstandig werken in breakout rooms

**10 min:** Terugkomen & delen

Notes:
De meeste tijd besteden jullie aan het zelf bouwen en experimenteren. Ik loop langs in de breakout rooms om te helpen.

***

## De opdrachten

In hoofdstuk 3 van de syllabus staan alle opdrachten

Je werkt in **volgorde** door de opdrachten heen

<!-- .element: class="fragment" -->

Elke opdracht bouwt voort op de vorige

<!-- .element: class="fragment" -->

Notes:
Niet springen tussen opdrachten! De volgorde is belangrijk: je leert stap voor stap meer complexe concepten.

---

## Scaffolding aanpak

**Fase 1:** Code kopiëren en uitproberen

**Fase 2:** Code aanpassen (kleine veranderingen)

<!-- .element: class="fragment" -->

**Fase 3:** Zelf code schrijven

<!-- .element: class="fragment" -->

Notes:
We beginnen met voorbeeldcode die je kopieert. Dan pas je kleine dingen aan. Uiteindelijk schrijf je zelf code vanaf nul. Zo bouw je vaardigheden op.

---

## Hulp nodig?

1. Lees de foutmelding goed

2. Check je code met je duo-partner

3. Kijk in de voorbeeldcode

4. Stuur een berichtje in de chat met een tag op de docent

<!-- .element: class="fragment" -->

Notes:
Probeer eerst zelf. Vaak staat het antwoord in de foutmelding of in de voorbeeldcode. Als je echt vast zit, help ik.

***

## Quick Start: NetLogo Interface

Open NetLogo (desktop of web)

Drie tabbladen:

**Interface** - Knoppen en visualisatie

**Code** - Hier schrijf je je programma

**Info** - Documentatie

Notes:
Zorg dat iedereen NetLogo open heeft. Web versie werkt ook prima als je het niet geïnstalleerd hebt.

---

## Eerste stappen

**Oefening 3.1** in de syllabus:

1. Maak een `setup` procedure
2. Maak een `go` procedure  
3. Voeg buttons toe op Interface

Start simpel, test vaak!

<!-- .element: class="fragment" -->

Notes:
Dit is jullie eerste opdracht. De code staat in het hoofdstuk. Kopieer, begrijp wat het doet, test het.

---

## Setup en Go - Het patroon

```scheme
to setup
  clear-all          ; Maak schoon
  create-turtles 50  ; Maak agents
  reset-ticks        ; Zet tijd op 0
end

to go
  ask turtles [
    forward 1        ; Agents doen iets
  ]
  tick               ; Tel tijd op
end
```

Notes:
Setup = voorbereiding. Go = wat er elke tijdstap gebeurt. Dit patroon zie je in ELK NetLogo model.

***

## Breakout Rooms

Je krijgt nu **70 minuten** om zelfstandig te werken

Je zit in kleine groepen om elkaar te kunnen helpen

<!-- .element: class="fragment" -->

Ik kom langs in de rooms

<!-- .element: class="fragment" -->

Notes:
Jullie zitten in kleine groepen zodat je elkaar om hulp kunt vragen. Maar iedereen werkt aan zijn eigen code. Veel succes!

---

## Checklist voor vandaag

Als je klaar bent met Oefening 3.1:

- `setup` button werkt zonder errors
- `go` button laat turtles bewegen
- Je begrijpt wat elke regel code doet

Ga daarna door naar Oefening 3.2

<!-- .element: class="fragment" -->

Notes:
Heb je oefening 3.1 af? Mooi! Test alles, wissel van rol, en ga door naar 3.2 over energie.

---

## Tips voor onderweg

**Test na elke wijziging** - Niet alles in één keer bouwen

**Gebruik comments** - `; Dit doet...` helpt je onthouden

**Save vaak** - Niks frustrerender dan werk verliezen

Notes:
Incrementeel werken is key. Voeg één ding toe, test of het werkt, voeg dan het volgende toe.

***

## Terug over 70 minuten!

Veel succes met programmeren 🚀

Notes:
Start de breakout rooms. Zet een timer. Loop actief langs in alle rooms om te helpen en te monitoren.

***

## Welkom terug!

Hoe ging het?

---

## Reflectie

Denk even na:

1. Wat was het moeilijkste?
2. Wat snapte je verrassend snel?
3. Waar ben je trots op?


Notes:
Laat een paar studenten delen. Dit helpt met metacognitie: bewust worden van je leerproces.

---

## Veelgemaakte fouten

**Fout 1:** `tick` vergeten in `go`

→ Model hangt, plots werken niet

<!-- .element: class="fragment" -->

**Fout 2:** Haakjes niet gesloten `]`

→ Syntax error

<!-- .element: class="fragment" -->

**Fout 3:** `pcolor` gebruiken bij turtles

→ Scope error (patches ≠ turtles)

<!-- .element: class="fragment" -->

Notes:
Dit zijn de top 3 beginners-fouten. Als je deze herkent, ben je al een stuk verder!

---

## Wat hebben we geleerd?

**Setup en go** - Basis structuur

**Turtles** - Agents maken en bewegen

**Procedures** - Code organiseren

**Debugging** - Fouten vinden en oplossen


Notes:
Dit zijn de fundamenten. Alles wat je verder in NetLogo doet, bouwt hierop voort.

***

## Huiswerk

**Maak af waar je nu bent** - Minimaal t/m Oefening 3.2

**Lees verder in Hoofdstuk 3** - Patches en monitors

**Experimenteer** - Verander getallen, kijk wat er gebeurt


Notes:
Het belangrijkste: zorg dat je een werkend setup/go model hebt. Daarop bouwen we volgende week verder.

---

## Volgende week

Emergent gedrag implementeren

Je eigen model gaan bouwen

Neem je **werkende code** en je opgeladen laptop mee!

Notes:
Week 4 wordt spannend: jullie gaan je eigen onderzoeksmodel bouwen. Zorg dat je basis op orde is.

---

## Laatste vragen?

&nbsp;

Notes:
Check of er nog vragen zijn. Help eventueel met technische problemen voor volgende week.
