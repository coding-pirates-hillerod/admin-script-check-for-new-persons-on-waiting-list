# Admin script til at tjekke for nye personer på CP venteliste
Python script lavet for at kunne tjekke, hvorvidt der er nye opskrivning på ens CP afdelings venteliste.

## Baggrunden for script
Baggrunden for dette script er, at vi i Coding Pirates Hillerød gerne vil vide, når børn skriver sig op til vores venteliste. Det vil vi af 2 årsager.

For det første synes vi, at det er på sin plads blot at bekræfte opskrivninger og sige tak til folk, når de skriver sig op til vores venteliste.

For det andet vil denne viden også give os en mulighed for at komme i kontakt med potentielle nye frivillige, da vi, via viden om et barns opskrivning, kan bruge denne mulighed til at skrive barnets forældre og gøre opmærksom på, at hvis de (altså den voksne) selv deltager i vores afdeling som frivillig, så vil de kunne tage deres eget ene barn gratis med i afdelingen, og dermed bypasse at skulle stå på venteliste.

Disse 2 årsager har været baggrunden for overhovedet at lave dette script.

## Om scriptet
For nu fungerer scriptet som følger.

### Step #1 - Automatisk login i medlemssystem og udtræk venteliste
Først og fremmest logger scriptet automatisk ind i medlemssystemet - forudsat at man har husket at skabe en txt fil kaldet "credentials.txt" med sit brugernavn og password adskilt af blot et mellemrum - og udtrækker ens afdelings nuværende venteliste.

### Step #2 - Tjek om script er blevet kørt før
Dernæst tjekker scriptet om det er blevet kørt før - reelt set hvorvidt der er blevet skabt en sqlite database eller ej.

#### Step #2.1 - Scriptet _er ikke_ kørt før
Er scriptet ikke kørt før, så opretter det blot en database kaldet "waitinglist.db" med tabel kaldet "persons", hvori personerne fra den udtrukket venteliste indsættes.

Når dette er gjort, så afsluttes scriptet blot, da der således ingen grund er til at gå videre med scriptets kode indtil næste gang det køres for tjek af nye opskrivninger.

#### Step #2.2 - Scriptet _er_ kørt før
Er scriptet kørt før, så hentes først alle personer fra databasen (dvs. fra "waitinglist.db").

Dernæst tjekkes der for, hvor nogen af de netop udtrukket personer fra medlemssystemets venteliste *ikke* er at finde "persons" tabellen i databasen.

Er der personer fra den udtrukne venteliste som ikke findes i databasen, så indsættes først en ny record for hver person i databasen - da denne jo skal opdateres til næste gang scriptet køres - og afslutningsvist gemmes samme person(er) umiddelbart blot i txt fil kaldet "persons_not_on_waiting_list.txt", hvorudfra man så selv kan afgøre, hvordan man vil håndtere disse nye opskrivning på ens venteliste.

## Hvordan man sætter scriptet op
Hvis nogen vil gøre brug af scriptet, så følger her en vejledning til, hvordan dette gøres.

### Step #1 - download og installer Python
Først og fremmest skal man have Python installeret for at køre scriptet.

Gå derfor til [python.org](https://www.python.org/) og download og installer Python.

### Step #2 - download, installer og opsæt Git og GitHub og klon dette repo
I'm sorry .. men hvis ikke du ved, hvordan man gør det her (hvilket er helt, HELT fair!), så få lige en til at hjælpe dig med det (for det er lidt "bøvlet" at forklare, og jeg, Jonas, orker det ikke rigtigt lige nu .. sorry).

### Step #3 - installer dependencies
Installer projektets dependencies ved at køre denn kommando:

```python
pip install -r requirements.txt
```

### Step #4 - skab en "credentials.txt" fil med dit login
Skab i roden af projektet en fil kaldet "credentials.txt", hvor du blot på én linje indtaster:
1. dit brugernavn til medlemssystemet
2. laver et mellemrum
3. dit password

Her er et eksempel på, hvordan filen med brugernavn og password ville se ud for en fiktiv bruger:
```txt
mogens@iamgod.com EsmunTus%1968%
```

### Step #5 - kør scriptet
Med dette sat op burde du nu være i stand til at køre scriptet. Om du så vælger at køre det manuelt fra terminalen en gang imellem, eller sætter det op til at køre automatisk via fx 'crontab' for macOS eller 'Task Scheduler' på Windows, ja, det må være op til dig selv.

## Afsluttende bemærkninger
Scriptet finder således for nu blot ud af, hvorvidt der er nye opskrivninger på ens CP venteliste. Og dette er gjort med FULDT overlæg! For om du blot vil have en Desktop notifikation, når nye børn skriver sig op, eller gerne automatisk vil sende emails ud til nye opskrivninger på ventelisten, ja, det er jo op til DIG at afgøre, og ikke mig/os.

Om ikke andet kan du i hvert fald (nu) bruge dette scriptet til enten manuelt eller automatisk at udtrække oplysninger om nye opskrivning på din/jeres CP venteliste. Og hvad du som sagt så vil gøre med det, ja, det er - "tadaaa ..!!" - op til DIG.


