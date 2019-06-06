# Deze repo bevat het totaalproject van de geautomatiseerde plantage met Raspberry Pi

## Omschrijving

Als de PI opstart word het main programma opgestart dat eerst de ph van het water meet en vervolgens een water loop opstart zodat de zaailingen vers water krijgen. Als de ph van de main water loop te laag is krijgt deze een portie voeding.

De main loop methode is er zo op voorzien dat vanaf de PI opstart deze volledig autonoom kan draaien. De ingestelde tijden ( 6 seconden aan 2 seconden uit ) zijn zo gekozen dat het project makkelijk toonbaar is, maar deze kunnen uiteraard ook uren voorstellen. 

Als er op de knop geduwd wordt, gaat de schakeling in 'remote mode' zodat deze vanop afstand bestuurd kan worden. Deze kent verschillende standen: De motor van de waterloop van de plantage aan en uit zetten, de water loop aanzetten maar ook de planten voeden.

![img](/images/TotaalSchakeling.JPG)
> foto schakeling