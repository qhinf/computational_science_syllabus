# Introductie

Dit is een voorbeeld van een hoofdstuk in JupyterBook, geschreven in Markdown. Dit bestand is het eerste hoofdstuk, omdat het als eerste in de `_toc.yml` staat. De volgende twee hoofdstukken zijn een beetje fancier:

- {doc}`notebooks` is een Jupyter Notebook bestand (`.ipynb`). Om die te bewerken heb je een speciale editor nodig, bijvoorbeeld [JupyterLab](https://jupyter.org/install), de online variant [Jupyter Lite](https://jupyter.org/try-jupyter/lab/) of de [Jupyter extensie voor VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter). Het mooie is wel dat de code die je hier in speciale blokken schrijft ook uitvoerbaar is en dat leerlingen (via een paar knoppen) ook meteen met die code kunnen spelen.
- {doc}`markdown-notebooks` is een speciaal soort Markdown waarmee je Jupyter Notebook-achtige bestanden kunt schrijven, maar dan in Markdown. Je schrijft code voorbeelden dan gewoon in een Markdown codeblok (met ` ``` `), maar bij het bouwen van de website wordt de output van die code ook in de tekst van de site gezet.

Er zijn ook verscheidene extensies beschikbaar die je in alle types kunt gebruiken, standaard is in deze template de *exercise admonition* aanwezig, waarmee je dit soort oefeningen kunt toevoegen:

:::{exercise} Test
:label: test

Schrijf een pagina voor jouw syllabus.
:::

Met `:label: naam-van-de-oefening` kun je de oefening een naam geven en ernaar verwijzen bij een oplossing:

:::{solution} test
Dit is de oplossing van die oefening. (Niet echt natuurlijk, dit is geen pagina.)
:::

Zie de [documentatie](https://ebp-sphinx-exercise.readthedocs.io/en/latest/syntax.html) voor meer opties, bijvoorbeeld om een oplossing standaard te verbergen en uitklapbaar te maken. Gebruik bij voorkeur de `:::` syntax i.p.v. de ` ``` ` syntax, want daar raken Markdown editors minder van in de war.
