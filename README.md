# Admin script til at tjekke for nye personer på CP venteliste
Python script lavet for at kunne tjekke, hvorvidt der er nye opskrivning på ens CP afdelings venteliste.

## Baggrunden for script
Baggrunden for dette script er, at vi i Coding Pirates Hillerød gerne vil vide, når børn skriver sig op til vores venteliste. Det vil vi af 2 årsager.

For det første synes vi, at det er på sin plads blot at bekræfte opskrivninger og sige tak til folk, når de skriver sig op til vores venteliste.

For det andet vil denne viden også give os en mulighed for at komme i kontakt med potentielle nye frivillige, da vi, via viden om et barns opskrivning, kan bruge denne mulighed til at skrive barnets forældre og gøre opmærksom på, at hvis de (altså den voksne) selv deltager i afdelingen som frivillig, så vil de kunne tage deres eget ene barn gratis med i afdelingen, og dermed bypasse at skulle stå på venteliste.

Disse 2 årsager har været baggrunden for overhovedet at lave dette script.

## Om scriptet
For nu fungerer scriptet som følger.

### Step #1 - Automatisk login i medlemssystem og udtræk venteliste
Først og fremmest logger scriptet automatisk ind i medlemssystemet - forudsat at man har husket at skabe en txt fil kaldet "credentials.txt" med sit brugernavn og password adskilt af blot et mellemrum - og udtrækker ens afdelings nuværende venteliste.

### Step #2 - Tjek om script er blevet kørt før
Dernæst tjekker scriptet om det er blevet kørt før - reelt set hvorvidt der er blevet skabt en sqlite database eller ej.

#### Step #2.1 - Scriptet _er ikke_ kørt før
