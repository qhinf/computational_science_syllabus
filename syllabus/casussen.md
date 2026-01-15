(casussen)=
# Casussen voor de eindopdracht

Voor de eindopdracht mag je een van de onderstaande casussen kiezen. Je mag ook zelf een casus bedenken, maar overleg dan eerst met de docent of de casus geschikt is om deze module mee af te sluiten.

## Verkeersplein

**Context:** Bij een druk kruispunt met stoplichten ontstaan regelmatig files tijdens het spitsuur. De wachttijd kan oplopen tot 5 minuten per auto. De gemeente overweegt het kruispunt te vervangen door een rotonde (verkeersplein) om de doorstroming te verbeteren.

**Scenario:** Modelleer beide situaties – een kruispunt met stoplichten en een rotonde – onder verschillende verkeersdrukte. Vergelijk de gemiddelde wachttijd en doorstroming.

**Modelaanwijzingen:**
- **Agents:** Auto's die van verschillende kanten komen en verschillende bestemmingen hebben (rechtdoor, links, rechts)
- **Omgeving:** Kruispunt met 4 wegen, of rotonde met 4 in- en uitgangen
- **Parameters:** aantal auto's per minuut per richting, stoplichtcyclus (groen/rood tijd), grootte rotonde, maximale snelheid
- **Metingen:** gemiddelde wachttijd per auto, aantal auto's dat per uur passeert, aantal vastgelopen situaties

**Onderzoeksvraag:** Bij welke verkeersdrukte (aantal auto's per minuut) is een rotonde effectiever dan een kruispunt met stoplichten, gemeten in gemiddelde wachttijd per auto?

## Leven op Mars

**Context:** NASA[^Nasa] en SpaceX[^SpaceX] werken aan permanente nederzettingen op Mars. Een cruciale vraag is of kolonisten zelfvoorzienend kunnen worden in voedsel, water en zuurstof, of dat ze afhankelijk blijven van bevoorrading vanaf Aarde (kosten: $200.000 per kg).

**Scenario:** Modelleer een Mars-nederzetting met een bepaald aantal kolonisten. Produceer zuurstof uit CO₂, water uit grondijs, en voedsel in kassen. Elk systeem vraagt onderhoud en energie (zonnepanelen). Houd rekomen met storingen, oogsten die mislukken, en groeiende bevolking.

**Modelaanwijzingen:**
- **Agents:** Kolonisten (consumeren voedsel/water/zuurstof, onderhouden systemen), planten (groeien, produceren voedsel/zuurstof)
- **Omgeving:** Nederzetting met kassen, waterproductie-units, zuurstofgeneratoren, opslagtanks
- **Parameters:** aantal kolonisten, grootte kassen, efficiency systemen, kans op storing, zonlicht (seizoenen op Mars)
- **Metingen:** voedselvoorraad, watervoorraad, zuurstofniveau, aantal overlevenden, aantal benodigde bevoorradingen vanaf Aarde

**Onderzoeksvraag:** Hoeveel kolonisten kunnen met een kas van 100 m² en 10 zuurstofgeneratoren zelfvoorzienend overleven op Mars, en hoeveel maanden duurt het voordat dit evenwicht bereikt is?

## Wachtrij

**Context:** Een bank opent een nieuw filiaal. Klanttevredenheidsonderzoek toont aan dat wachttijden boven 10 minuten leiden tot klachten. De bank wil de service optimaal organiseren: één wachtrij voor alle balies, of aparte wachtrijen per type dienst?

**Scenario:** Modelleer een bankfiliaal waar klanten binnenkomen met verschillende vragen. Vergelijk twee organisatievormen: (1) één centrale wachtrij voor alle balies, en (2) aparte wachtrijen voor snelle/middellange/lange diensten. Meet de wachttijden.

**Modelaanwijzingen:**
- **Agents:** Klanten met verschillende types vragen (snelle: 1-5 min, middellang: 3-10 min, lang: 5-20 min)
- **Omgeving:** Bankfiliaal met meerdere balies, wachtrijen, ingang en uitgang
- **Parameters:** aantal balies (2-6), klanten per uur (10-50), verdeling vraagtypen (bijv. 50% snel, 30% middellang, 20% lang)
- **Metingen:** gemiddelde wachttijd per klant, maximale wachttijd, aantal klanten met wachttijd >10 minuten, bezettingsgraad balies

**Onderzoeksvraag:** Bij welk organisatiesysteem (één centrale wachtrij vs. aparte wachtrijen per dienst) is de gemiddelde wachttijd het laagst bij 30 klanten per uur, en hoeveel balies zijn daarvoor minimaal nodig om 95% van de klanten binnen 10 minuten te helpen?

## Kaaspakhuis

**Context:** Een kleine biologische kaasproducent wil zijn winst maximaliseren. Kaas wordt waardevoller naarmate het langer rijpt (jonge kaas €8/kg, belegen €12/kg, oude €18/kg na respectievelijk 2, 6 en 12 maanden), maar opslag kost €0,50 per kaas per maand. De producent moet kiezen tussen snelle verkoop aan de biologische winkel (vaste afname, lage prijzen) of de streekmarkt (hogere prijzen, variabele vraag).

**Scenario:** Modelleer de kaasproductie en -opslag over 3 jaar. Elke maand komen 25 nieuwe kazen bij. Test verschillende strategieën: alles jong verkopen, alles lang laten rijpen, of een mix. Houd rekening met opslaglimiet (400 kazen) en wisselende vraag op de streekmarkt.

**Modelaanwijzingen:**
- **Agents:** Kazen (met leeftijd en rijpheid), klanten op streekmarkt (met vraag)
- **Omgeving:** Pakhuis met beperkte capaciteit (400 plaatsen), biologische winkel (vaste afname), streekmarkt (variabele vraag)
- **Parameters:** productie per maand (25), opslagkosten (€0,50/kaas/maand), prijzen per rijpheid, maximale afname biowinkel (bijv. 50/maand), vraag streekmarkt (gemiddeld 30/maand ±15)
- **Metingen:** totale winst per jaar, aantal verkochte kazen per type, bezettingsgraad pakhuis, aantal weggegeven kazen

**Onderzoeksvraag:** Wat is de optimale verhouding tussen jong/belegen/oude kaas verkopen om de winst over 3 jaar te maximaliseren, gegeven een productie van 25 kazen per maand en opslaglimiet van 400?

## Aardappels

**Context:** Een biologische aardappelteler wil zijn winst maximaliseren zonder chemische bestrijdingsmiddelen. Meer planten per m² geeft meer opbrengst, maar verhoogt ook de kans op verspreiding van Phytophthora (aardappelziekte). Aangetaste planten leveren geen verkoopbare aardappels en kunnen buren besmetten. De teler moet kiezen: dicht planten (hoog risico, potentieel hoge opbrengst) of wijd planten (laag risico, lagere opbrengst)?

**Scenario:** Modelleer een aardappelveld (bijv. 50×50 patches) waar planten groeien en Phytophthora zich verspreidt via buurplanten. Test verschillende plantafstanden en interventiestrategieën (bijv. aangetaste planten direct verwijderen). Bereken de netto-winst na 1 teeltseizoen.

**Modelaanwijzingen:**
- **Agents:** Aardappelplanten (gezond, ziek, of geoogst)
- **Omgeving:** Veld (patches kunnen geplant worden of leeg blijven), weer (regen verhoogt besmettingskans)
- **Parameters:** plantafstand (aantal patches tussen planten), initiële besmettingskans (1-5%), verspreidingskans bij contact, kosten per plant (€0,30), opbrengst per gezonde plant (€2), kosten verwijderen zieke plant (€0,10)
- **Metingen:** aantal gezonde planten bij oogst, aantal besmette planten, totale kosten, totale opbrengst, netto-winst

**Onderzoeksvraag:** Wat is de optimale plantafstand (in patches) om de netto-winst te maximaliseren bij een initiële besmettingskans van 3% en een verspreidingskans van 15% per contact?

## Brand op school

**Context:** Bij brand moet een schoolgebouw binnen 3 minuten geëvacueerd zijn (Nederlandse brandveiligheidsnorm). De schoolleiding wil weten of de huidige nooduitgangen en alarmen voldoende zijn. Speciale aandacht gaat uit naar rolstoelgebruikers, die langzamer bewegen en bredere doorgangen nodig hebben.

**Scenario:** Modelleer de begane grond van je eigen school (of een fictieve school met gangen, lokalen, en uitgangen). Simuleer een brandalarm: mensen lopen naar de dichtstbijzijnde uitgang. Test verschillende scenario's: huidige situatie, extra uitgangen toevoegen, uitgangen verbreden, of alarmen op andere plekken.

**Modelaanwijzingen:**
- **Agents:** Leerlingen en docenten (normale snelheid: 1-2 m/s), rolstoelgebruikers (langzamer: 0,5-1 m/s, breder: 2 patches)
- **Omgeving:** Plattegrond van school met gangen (breed/smal), lokalen, nooduitgangen (met breedte), muren, alarmen (hoorbare straal)
- **Parameters:** aantal mensen per lokaal, aantal rolstoelgebruikers, breedte uitgangen (1-4 m), aantal en positie alarmen, loopsnelheden
- **Metingen:** evacuatietijd (wanneer laatste persoon buiten is), aantal mensen dat binnen 3 minuten evacueerde, opstoppingen bij uitgangen (aantal wachtenden)

**Onderzoeksvraag:** Hoeveel nooduitgangen met welke minimale breedte zijn nodig om 500 personen (waarvan 5 rolstoelgebruikers) binnen 3 minuten te evacueren, en waar moeten deze uitgangen het beste geplaatst worden?

## Weerstand

**Context:** Natuurkundewetten zoals de wet van Ohm zijn vaak afgeleid uit wiskundige theorie. Maar kunnen we hetzelfde resultaat krijgen door het fysieke proces (elektronen die door een circuit bewegen) te simuleren met een agent-based model? Dit is een mooi voorbeeld van hoe ABM fundamentele fysica kan valideren.

**Scenario:** Modelleer een elektrisch circuit als een pad van patches waar elektronen (agents) doorheen bewegen. Patches kunnen verschillende weerstand hebben (hoe moeilijk het is om door te laten). Bouw serieschakelingen (elektronen volgen één pad) en parallelschakelingen (elektronen kiezen uit meerdere paden). Meet de totale weerstand en vergelijk met de theoretische formules.

**Modelaanwijzingen:**
- **Agents:** Elektronen die bewegen door het circuit, met snelheid bepaald door weerstand
- **Omgeving:** Circuit-paden (patches) met variabele weerstand (R₁, R₂, etc.), splitsingen voor parallel circuit
- **Parameters:** weerstand per component (bijv. R₁=100Ω, R₂=200Ω), aantal elektronen (stroomsterkte), voltage (drijvende kracht)
- **Metingen:** aantal elektronen per tijdseenheid (stroomsterkte I), spanning over weerstanden (U), berekende totale weerstand (R_totaal = U/I)

**Onderzoeksvraag:** 
1. Komt de gemeten totale weerstand in een serieschakeling overeen met $R_v = \sum^n_{i=1}R_i$?
2. Komt de gemeten totale weerstand in een parallelschakeling overeen met $\frac{1}{R}=\sum^n_{i=1}\frac{1}{R_i}$?
3. Bij welke afwijking (in procenten) kunnen we concluderen dat het ABM-model de natuurkundewetten valideert?

## Epidemie

**Context:** Na COVID-19 wil de GGD beter voorbereid zijn op nieuwe uitbraken. Bij een ziekte met reproductiegetal R₀=3 (elk ziek persoon besmet gemiddeld 3 anderen) kan een epidemie exponentieel groeien. Groepsimmuniteit door vaccinatie kan dit stoppen, maar wat is de minimale vaccinatiegraad?

**Scenario:** Modelleer een populatie van 1000 mensen waar een ziekte zich verspreidt door contact. Mensen kunnen 4 staten hebben: gezond, ziek, hersteld (immuun), of gevaccineerd. Zieke mensen besmetten gezonde buren. Test verschillende vaccinatiepercentages en meet wanneer de epidemie stopt.

**Modelaanwijzingen:**
- **Agents:** Mensen met status (gezond/ziek/hersteld/gevaccineerd), besmettelijkheid (hoeveel dagen iemand anderen kan besmetten)
- **Omgeving:** Grid waar mensen bewegen en contact maken met buren
- **Parameters:** vaccinatiegraad (0-100%), besmettingskans bij contact (bijv. 20%), ziekteduur (bijv. 14 dagen), mobiliteit (hoe ver mensen per dag bewegen), R₀ (reproductiegetal: 2-4)
- **Metingen:** aantal zieken per dag, totaal aantal besmettingen, piekmoment epidemie, moment waarop epidemie stopt (0 nieuwe gevallen), percentage dat besmet raakte

**Onderzoeksvraag:** Bij welke vaccinatiegraad (%) stopt een epidemie met R₀=3 voordat meer dan 30% van de populatie besmet is geraakt, en hoeveel dagen duurt de epidemie dan?

## Festivalterrein

**Context:** Een festival verwacht 5000 bezoekers verspreid over een dag. Bij het Loveparade-ongeluk in Duisburg (2010) stierven 21 mensen door te nauwe doorgangen. De organisatie wil gevaarlijke situaties voorkomen en berekenen: hoeveel toiletten, eetgelegenheden, en hoe breed moeten paden zijn om drukte te vermijden?

**Scenario:** Modelleer een festivalterrein met 2 podia, toiletten, eetgelegenheden en verbindende paden. Bezoekers bewegen tussen deze locaties met verschillende doelen. Meet de drukte op paden en wachttijden bij voorzieningen. Test verschillende configuraties: meer toiletten, bredere paden, of andere posities.

**Modelaanwijzingen:**
- **Agents:** Bezoekers met behoeftes (honger, toiletbehoefte) en voorkeuren (welk podium), loopsnelheid vertraagt bij drukte
- **Omgeving:** Festivalterrein met podia (locaties), toiletten (aantal cabines), eetgelegenheden (aantal counters), paden (variabele breedte), ingangen/uitgangen
- **Parameters:** aantal bezoekers (3000-7000), aantal toiletten, aantal eetgelegenheden, padbreedte (2-10 meter), gemiddelde tijd per toiletbezoek (3 min), tijd per eetbestelling (5 min)
- **Metingen:** maximale drukte op paden (personen/m²), gemiddelde wachttijd toilet, gemiddelde wachttijd eten, aantal "kritieke situaties" (>4 personen/m² = gevaarlijk)

**Onderzoeksvraag:** Hoeveel toiletten (minimum) zijn nodig en wat is de minimale padbreedte om bij 5000 bezoekers te garanderen dat wachttijden onder 15 minuten blijven en drukte nergens boven 4 personen/m² komt?

## Schapenpopulatie met wolven

**Context:** In sommige natuurgebieden worden wolven geherintroduceerd om grazers (zoals schapen of herten) te reguleren. Te veel wolven betekent dat schapen uitsterven, te weinig wolven leidt tot overbegrazing. Ecologen willen weten: wat is het natuurlijke evenwicht, en is dat stabiel?

**Scenario:** Modelleer een natuurgebied waar schapen gras eten en zich voortplanten, en wolven schapen jagen en zich voortplanten. Gras groeit langzaam terug na begrazing. Test verschillende startverhoudingen (bijv. 100 schapen en 5 wolven) en kijk of beide populaties stabiel blijven of dat er cycli ontstaan (zoals bij de Canadese lynx en sneeuwhaas).

**Modelaanwijzingen:**
- **Agents:** Schapen (eten gras, planten voort bij voldoende energie, sterven van honger of door wolf), wolven (jagen schapen, planten voort bij voldoende energie, sterven van honger)
- **Omgeving:** Veld met graspatches die langzaam teruggroeien na begrazing
- **Parameters:** startaantal schapen (50-200), startaantal wolven (2-20), voortplantingsdrempel (energie nodig om jong te krijgen), grasgroeisnelheid, energie uit gras (voor schapen), energie uit schaap (voor wolf)
- **Metingen:** aantal schapen per tick, aantal wolven per tick, aantal lege graspatches, moment van uitsterven (indien van toepassing), stabiliteit (standaarddeviatie populaties over laatste 100 ticks)

**Onderzoeksvraag:** Bij welke startverhouding wolven:schapen (bijv. 1:20 of 1:30) ontstaat een stabiel evenwicht waarbij beide populaties minimaal 500 ticks overleven zonder uit te sterven, en hoe groot zijn de natuurlijke schommelingen in beide populaties?

## Geruchten op school

**Context:** Een gerucht over een docent verspreidt zich razendsnel via WhatsApp-groepen en mondeling contact op school. Uit onderzoek blijkt dat 60% van de leerlingen berichten direct deelt zonder te checken, 30% is sceptisch en checkt soms, en 10% weigert ongecontroleerde berichten te delen. De school wil weten: hoe snel verspreidt desinformatie, en helpt mediawijsheid-onderwijs?

**Scenario:** Modelleer een school van 500 leerlingen waar 1 persoon een gerucht start. Leerlingen zijn verbonden in een sociaal netwerk (vrienden kunnen berichten delen). Test verschillende percentages "kritische denkers" die geruchten niet delen, en meet hoe snel en hoe ver het gerucht zich verspreidt.

**Modelaanwijzingen:**
- **Agents:** Leerlingen met type (direct-delers 60%, sceptici 30%, critici 10%), status (gerucht niet/wel gehoord, wel/niet gedeeld), sociale connecties (vrienden)
- **Omgeving:** Sociaal netwerk (wie kent wie), school met lokalen waar leerlingen elkaar fysiek tegenkomen
- **Parameters:** percentage critici (0-50%), deelbereidheid sceptici (20-80%), gemiddeld aantal vrienden per leerling (5-20), kans op mondeling delen bij fysiek contact (30%)
- **Metingen:** aantal leerlingen dat gerucht hoorde per tijdseenheid, totaal percentage bereikte leerlingen, snelheid verspreiding (hoe snel bereikt het 50%?), stopmoment (geen verdere verspreiding)

**Onderzoeksvraag:** Bij welk percentage "kritische denkers" (die geruchten niet delen) wordt de verspreiding gestopt voordat 50% van de school het gerucht heeft gehoord, en hoe lang duurt het dan voordat de verspreiding stopt?

## Fietsenstalling school

**Context:** Bij de fietsenstalling van school worden fietsen vaak dubbel geparkeerd omdat leerlingen de dichtstbijzijnde plek zoeken bij de ingang. Dit leidt tot blokkades: fietsen zijn niet meer uit het rek te halen. 's Middags moeten soms 10 fietsen worden verzet om er 1 uit te krijgen. De school overweegt dubbeldeks-rekken of een extra stalling verder weg.

**Scenario:** Modelleer de fietsenstalling met 300 plekken. 's Ochtends komen 400 fietsers aan (piek tussen 8:15-8:30), 's middags halen ze hun fiets weer op. Leerlingen kiezen de dichtstbijzijnde vrije plek, maar parkeren dubbel als alles vol is. Test verschillende oplossingen: dubbeldeks-rekken (600 plekken op zelfde oppervlak), extra stalling 50 meter verder, of verplichte spreiding.

**Modelaanwijzingen:**
- **Agents:** Fietsers met aankomsttijd (Gauss-verdeling rond 8:20), vertrektijd (variabel), voorkeuren (liefst dicht bij ingang)
- **Omgeving:** Fietsenstalling met rekken (aantal plekken), afstand tot ingang (in meters), dubbel geparkeerde zones
- **Parameters:** aantal fietsen (350-450), aantal rekplekken (300/600), extra stalling (ja/nee, afstand 50m, capaciteit 100), bereidheid om verder te lopen (laag/gemiddeld/hoog)
- **Metingen:** aantal dubbel geparkeerde fietsen per dag, gemiddelde tijd om fiets op te halen 's middags, aantal blokkades (fiets niet bereikbaar zonder verzetten), bezettingsgraad per zone

**Onderzoeksvraag:** Reduceert een dubbeldeks-systeem (600 plekken) het aantal dubbel geparkeerde fietsen met minimaal 80% vergeleken met het huidige systeem (300 plekken), en wat is de gemiddelde tijdwinst bij het ophalen van fietsen 's middags?

---

[^Nasa]: https://www.nasa.gov/image-article/nasas-journey-mars/

[^SpaceX]: http://www.spacex.com/mars
