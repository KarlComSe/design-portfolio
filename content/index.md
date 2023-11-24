---
Title: Startsida
Description: .
---

Design portfolio
==========================

Hej! Det här är en uppgift i en kurs som handlar om design. 

Jag som läser kursen heter __Karl__. Jag är 36 år och bor i Göteborg. Jag gillar IT, programmering och webbutveckling. Det är en av anledningarna till att jag går läser denna kurs. Ja, det ska bli kul att lära sig om att skapa bra design, eller i alla fall, design som går obemärkt förbi och inte kräver timmar av arbete.


<figure>
<img src="%assets_url%/img/karl_large.jpg" alt="En selfie där Karl står på fjället "/>
</figure>

## Uppgift 1 / Del 1
I första delen av kursen introducerades labbmiljön, kursmaterial presenterades, grundläggande info om CSS repeterades, osv. Själva inlämningen för uppgift 1 kretsade kring att:
* Skapa ett eget tema i PICO (CMS:et). 
* Redigera lite sidor i PICO (bl.a. denna, lägga till en bild, osv.).
* Initiera ett GITHUB-repo och använd taggar.

Den innehöll också sin beskärda del av felsökning. Ominstallation av Composer, installation av GD för Apache, diverse ändringar i php.ini osv. 

### Reflektion
Det här var en intro-vecka. Jag läste allt material och lite till. Kursboken verkar vara ganska oteknisk, d.v.s. den innehåller lite info om CSS, men mer om design. Övrigt kursmaterial innehåller mycket info om CSS, men för att det ska sätta sig behöver jag öva, men en bra start att ha läst igenom det.

Jag lekte en del med olika färgverktyg, framför allt Adobes. Det hade två funktioner som verkar relevanta, 1) att **säkerställa att kontrasten mellan text- och bakgrundsfärg är ok**, och 2) att **säkerställa att de olika färgerna uppfattas av färgblinda** (och det finns tre olika typer av färgblindhet som det testas för).

När det gäller min design på denna sida, så ändrade jag snabbt lite färger. Jag skulle behöva ta ett helhetsgrepp på färgerna, för t.ex. kod-stycken med vit bakgrund och text i sidans text-färg, samt länkar, ser sådär ut. Ja, det är rent ut lite vågat att köra en brun hemsida.  Jag ändrade också bredden. Jag gillar inte hemsidor som sträcker sig över min 34" breda skärm. Det är bara möjligt att enkelt läsa när det är mindre än ca 900 px brett.

En annan reflektion är om hur man ska presentera bilder av olika storlekar bredvid varandra. Jag läste inte kursbokens kapitel om bilder, men surfade runt lite och läste en annan bok, utan att bli så mycket klokare på hur jag ska jobba med bilder av olika storlek. Det slutade med att jag manuellt beskärde bilderna så att de fick samma proportioner. **Min nuvarande slutsats kring hur jag ska hantera bilder är att jag kan göra designer som klarar av ett par olika proportioner.** 

## Uppgift 2 / Del 2
I andra delen av kursen introduceras SASS, flertalet NPM paket används och konfigureras och det är fokus på typgrafi. 

Själva inlämningen för uppgift 2 krävde bl.a.:
* Skapa ett nytt / modifiera ett tema som använder SASS. Använd ett par olika SASS-konstruktioner utöver grundläggande CSS.  
* Lägg till en undersida med lite text. 
* Använd Font Awesome eller Google Fonts. 
* Validera kod med Stylelint enligt SASS guidelines. 
* Säkerställ att webbsidan fungerar ok på olika enheter (mobiltelefon + dator).
* Använd normalize.css via NPM. 

Del 2 innehöll också sin beskärda del av felsökning. Två exempel: 1) Hux flux hade mbstring extension till PHP avinstallerats och min sida slutade att fungera. Här använde jag mig av error.loggen i Apache för att hitta felet. 2) Konfigurationsfilen till stylelint ska stavas just så, och inte styleint (vilket är lätt felstavat om man jobbat med variabler av typen integer). Här läste jag först på om styleint och hur konfigurationsfilerna fungerar, och testade funktionaliteten, och plötslgit gick det bara upp för mig att jag stavat fel på filnamnet.  

### Reflektion

SASS är smidigt, även ifall CSS i många fall utvecklas. 

Jag gillar när jag förstår vad jag gör med min kod och min dator. I detta kursavsnitt upplevde jag att det var en del "gör som i instruktionerna så kommer det att fungera". 

Jag hade uppskattat
* om det varit mer praktiska övningar kring typografi, där man faktiskt får göra om en dålig design till en bättre, om och om igen. Jag lär mig genom att öva och se skillnaderna. Som det är nu läser jag om t.ex. bredd på text, typsnitt, vertikal rytm och teckenavstånd, det hade varit bra att få göra ändringarna själv och se skillnaden. 
* mer kring NPM, och även mer övningar kring SASS, så att man verkligen hade fått använda dess fulla potential. Övningarna kunde varit enkla, som att måla upp 10 st divs, med färger som ändras med hjälp av CSS nth-element pseudo-selektor, beräkningar på HSL samt variabler.   

## Uppgift 3 / Del 3
I denna del av kursen har fokus varit på flexbox och grid-layout, kursmaterialet har även innehållit inslag av vad som utgör bra design med ett par regler (t.ex. att man definiera en storleksenhet som man använder i multiplar för text, marginaler osv.). För att lösa uppgiften var man även tvungen att förstå lite kring TWIG och hur PICO fungerar. 

Själva inlämningen för uppgift 3 krävde att man:
* Anpassade en tema-fil med TWIG och att man styrde hur den fungerade baserat på sidvariabler från PICO.
* Lekte runt med grid layout och gjorde sidan flexibel.

Del 3 innehöll väldigt lite felsökning. Jag har arbetat med grid och flex-box tidigare, men fick någon ny insikt, t.ex. hur code / pre fungerar i relation till att använda enheten fr, då behvöer man specificera minmax(0%,1fr) för att det ska bli en horisontell scrollbar och att inte pre-blocket ska renderas först och då ta upp så mycket utrymme som det behöver. 

### Reflektion

Grid och flex är helt fantastiskt. Jag har gjort webbsidor innan dessa koncept fanns, och det var ungefär så jobbigt så att jag gav upp. Det var floats hit och dit, absoluta och relativa positoner, z-index, o.s.v. och, det fanns t.o.m. ramverk för att underlätta grid-layout, ta en titt på https://960.gs/. En av min undersidor till Hobbies använder flex-box layout sen tidigare, och det är bara så smidigt!

## Uppgift 4 / Del 4
Här har fokus varit färg och typografi. Uppgiften gick ut på att skapa ett mörkt och ljust tema, samt även följa ett färgschema. Tycker mig fått till det helt ok på min sida. Använder ett monokromatiskt färgtema, och behåller accentfärger i mörkt och ljust tema. En annan uppgift var att analysera en webbplats, och då bl.a. beskriva vilket färgschema de använt, det var minst sagt inte alls tydligt. 

Tidigare kritiserade jag kursen då jag tyckte den saknade tillräckligt med övningar. Jag har nu sett alla föreläsningar. Vissa av föreläsningarna innehåller övningar, och det är ju bra. Det innebär att jag delvis får ta tillbaka av min kritik. Hade dock varit bra för inlärningen om det varit inlämningsuppgifter. Jag har sett ett online-verktyg där man får poäng efter hur lik en bild man gör en design, kanske skulle det kunna vara något med automat-rättning och obegränsat antal försök. 

### Reflektion

Har haft väldigt svårt att välja färger tidigare. Min lärdom här är att vitt och svart är grundfärger, som man bör ha med i sitt färgschema oavsett. En annan lärdom är att less is more. 