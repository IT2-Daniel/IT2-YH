27/10 Begynt å lage spillerklassen og en underklasse til den. Ikke gjort veldig mye på hovedklassen enda så ser enda ikke likhet mellom de to, men det kommer, jobber mer med det neste gang.

Foreløopig begynt på kampfunksjonen hvor en kan ta forskjellige valg om hva en vil gjøre

30/10
Lagd flere metoder i klassene og et par flere klasser
Lagd klassediagram 
brukt chatgpt til å kjapt finne ut hvordan det er med arv over flere generasjoner


03/11

egt bare sett på grafikk

brukt chatgpt til å finne ut kordan eg bruker rich pixels til å lage pixelart og gi meg hexkoder å bruke

10/11

Mer grafikk

13/11
Satt sammen kodene i de forskjellige filene til et noe funksjonelt program
brukt chat til å hjelpe med grafikken spesielt flytting av figurer i griden


19/11 
siste justeringer
lagt til items
kommentert kode 



## Hva programmet gjør og hvordan det kjøres

Programmet er et turbasert rpg spill som hvor man starter med å velge mellom to klasser som har sine egne stats ogabilities 

Etter det kommer man inn på hovedbrettet hvor man kan flytte seg rundt med wasd og dersom man skulle treffe en fiende starter en encounter 

Kampsystemet er turbasert. Spilleren kan utføre vanlige angrep, bruke abilities, stikke av eller bruke items fra inventory. Etter spillerens tur angriper fienden dersom den ikke er dau. Spillet bruker tilfeldige terningkast for å bestemme hvor mye skade angrepene gjør. Spilleren må slime fiendene uten å dø selv.

Programmet er delt inn i tre Python-filer:

- **Brett.py:** Håndterer hovedbrettet, bevegelse, klassevalg og start av encounters.
- **Klasser.py:** Inneholder klassene for karakterene, fiendene og funksjonene som styrer kampene.
- **Encounter1.py:** Håndterer kampbrettet og oppretter fiendene som spilleren skal kjempe mot.

For å kjøre programmet starter man `Brett.py`. Dette starter først klassevalget, før hovedbrettet vises. Når spilleren møter en encounter, blir `start_battle()` fra `Encounter1.py` kalt. Denne starter kampene ved å bruke funksjonene og klassene fra `Klasser.py`.

Programmet bruker bibliotekene `rich_pixels` og `rich` for å vise grafikken i terminalen, mens `msvcrt` brukes til å registrere tastetrykk under spillingen. Derfor må programmet kjøres i en Windows-terminal som støtter disse bibliotekene.





Brukt Chatgpt til det som er nevnt i loggen samt å kommentere deler som er fått av AI som jeg ikke helt forsto i utgangspunktet og bare en liten ramme på hvordan jeg kunne sette opp forklaringen over.