# picoW_ntp
 
Un exemplu de cod in micropython pentru afisarea orei exacte, folosind controlerul pi picoW.
- afisaj OLED: SSD1315 0.96 inch, GROVE v1.0
- interpretor: rp2-pico-w-20230426-v1.20.0.uf2

Conectarea la reteaua wifi se face prin libraria "network", furnizand ssid si password-ul ruter-ului.
Dupa conectare se acceseaza serverul ntp printr-o conexiune tip socket. Mesajul trimis in cererea clientului, cat si cel de raspuns de la serverul ntp, are o structura bine precizata si este lung 64 bytes. Datele sunt structurate pe o lungime de cate 4 bytes. Prima linie contine mai multe infornmatii ce ocupa de la 2 la 16 biti (indicator de salt, versiune, mod de lucru ..., vezi documentatie). Setarea acestora da valoarea binara a mesajului inserat in cererea clientului catre server. Informatia de la bytes 48 in sus este optionala. Bytes ce poarta informatia de timp, la nivel de secunda, sunt in pozitia 40:44. Se decodeaza valoarea binara si se extrage informatia de timp cu functia python din libraria "time", dupa care se initializeaza RTC microcontroler la valorile citite.
Afisarea se face pe un display SSD1315 conectat la microcontroler printr-o conexiune I2C, folosind libraria micropython "ssd1306".
Intr-un ciclu continuu se afiseaza sirurile preformatate, data si ora, cu cadenta de o secunda.

Obs:
- timpul dat de serverul ntp are ca origine anul 1900, cel folosit in python are referinta anul 1970 (de fapt in majoritatea librariilor ce
trateaza timpul). Pentru aceasta se introduce valoarea de corectie NTP_1970. Origine de timp pe picoW este 2021 (01-01-2021 00:00:00). Aceasta e data afisata de microcontroler in lipsa sincronizarii.
- pentru corectia de fus orar (+2, Bucuresti) se insumeaza diferenta la ora. De asemenea trebuie avuta in vedere si corectia pentru ora de vara (+1).
- o sincronizare precisa a timpului trebuie sa ia in calcul si eventualele intarzieri in retea, calculul valoarii acestora este o problema mai complicata si se poate rezolva raportandu-ne la diferenta de timp determinata pe ceasul local.
