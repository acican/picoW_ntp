# picoW_npt
 
Un exemplu de cod in micropython pentru afisarea orei exacte, folosind controlerul pi picoW.
- afisaj OLED: SSO1315, GROVE v1.0
- interpretor: rp2-pico-w-20230426-v1.20.0.uf2

Conectarea la reteaua wifi se face prin libraria "network", furnizand ssid si password-ul ruter-ului.
Dupa conectare se acceseaza serverul ntp printr-o conexiune tip socket. Din mesajul de raspuns se decodeaza informatia privind data si ora,
din pozitia corespunzatoare (40:44). Se initializeaza RTC microcontroler la valorile citite.
Afisarea se face pe un display SSO1315 conectat la microcontroler printr-o conexiune I2C, folosind libraria micropython "ssd1306".
Intr-un ciclu continuu se afiseaza sirurile preformatate, data si ora, cu cadenta de o secunda.
Obs:
- timpul dat de serverul ntp are ca origine anul 1900, cel folosit in python are referinta anul 1970 (de fapt in majoritatea librariilor ce
trateaza timpul). Pentru aceasta se introduce valoarea de corectie NTP_DELTA.
- pentru corectia de fus orar (+2, Bucuresti) se insumeaza diferenta la ora. De asemenea trebuie avuta in vedere si corectia pentru ora de vara.
