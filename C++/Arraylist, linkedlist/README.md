# PROJECT2_IN1910
Bruker Cmake. IDEn min krevde at jeg brukte header/cpp implentasjon , så det er flere filer enn vanlig. Navnene på  filene har også blitt endret til selve navnet til klassen.
Jeg rakk ikke å gjøre circLinked list ferdig. Koden til denne filen er blitt kommentert ut så jeg slipper feilmeldinger tilknyttet de andre filene.
Prosjektet har blitt pushet til et repo utenfor IN1910 siden den andre deltageren aldri svarte. Jeg valgte derfor å gjøre koden lokalt og pushe til dette repoet senere.

# Hente element etter indeks
ArrayList er o(1) imens LinkList er O(n) fordi det må iterere over hver lenke til den finner elementet

# Insert 
Når man inserter på starten av listen så er Linklist mer effektivt (O(1)) siden Linklist starter på det første elementet og må ikke endre hele listen. Arraylist er O(n) siden den må iterere over hele arrayet og endre indeksene.

Hvis man inserter på slutten så er arraylist mer effektivt ( O(1) ), imens Linklist er O(n) siden den må iterere over alle lenkene.

Hvis man inserter midt i er begge listemetodene O(n). Arraylist på iterere og endre indeksene fra slutten til indeksen. LinkList på iterere over nodene, finne noden og endre pekern til den nye.

# Fjerne 
På starten: Linkedlist er O(1) imens ArrayList er O(n) siden den må endre indeksene over hele arrayet

På slutten : Begge er O(n), arraylist på iterere over hele arrayet og endre indeks. linkedlist på iterere over alle lenkene.

På midten : Begge to er O(n), begge to må iterere over halvparten av arrayet. Arraylist må endre indeksene imens Linkedlist må finne lenken og endre peker.

# Print
Begge to er O(n), men ArrayList er mer minneeffektivt, siden Linkedlist må lagre både elementet og pekeren til neste element.



