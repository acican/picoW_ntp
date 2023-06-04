# picoW_npt
 
Un exemplu de cod in micropython pentru afisarea orei exacte, folosind controlerul pi picoW.
- afisaj OLED: SSO1315
- interpretor: rp2-pico-w-20230426-v1.20.0.uf2

Conectarea la reteaua wifi se face prin libraria "network", furnizand ssid si password-ul ruter-ului.
Dupa conectare se acceseaza site-ul ntp printr-o conecxiune tip socket. Din mesajul de raspuns se decodeaza informatia privind data si ora,
din pozitia corespunzatoare (40:44). Se initializeaza RTC microcontroler la valorile citite.
Afisarea se face pe un display SSO1315 conectat la microcontroler printr-o conexiune I2C, folosind libraria micropython "ssd1306".
Intr-un ciclu continuu se afiseaza sirurile preformatate, data si ora, cu cadenta de o secunda.
