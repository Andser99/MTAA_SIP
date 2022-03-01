**Slovak Technical University**

**Faculty of Informatics and Information Technologies![](Aspose.Words.a3630bad-47a5-4a9c-b90b-0e2f45272311.001.png)**

Andrej Byrtus

**SIP Proxy![](Aspose.Words.a3630bad-47a5-4a9c-b90b-0e2f45272311.002.png)**

**Predmet:** Mobilné technológie a aplikácie **Ročník:** 2021/2022

**Implementácia**

SIP proxy stavia nad existujúcou knižnicou PySipFillProxy [^1] Riešenie je implemen- tované v jazyku Python 2.7, súbor main.py konfiguruje a spúšťa potrebné funkcie knižnice. Z nepovinných funkcionalít sú implementované všetky okrem logovania "den- níka hovorov".

**Vzorky pcap**

**Povinné**

- frames\_register.pcap - príklad registrácie klienta
- frames\_ring.pcap - zvonenie hovoru
- frames\_call.pcap - zodvihnutý hovor a jeho priebeh
- frames\_cancel\_other.pcap - zloženie hovoru druhou stranou

**Nepovinné**

- frames\_conference.pcap
- frames\_redirect.pcap
- frames\_video\_call.pcap
  - konferenčný hovor medzi 3 zariadeniami
- presmerovanie hovoru na 3. zariadenie
  - videohovor, video zapnuté po zdvihnutí

- frames\_200\_DOBRE- odpoveď 200 OK je premenovaná na 200 DOBRE pri reg- istrácií.

**1 Program**

**1.1 Požiadavky**

- Python 2.7

Program je možné spustiť cez konzolu pomocou python main.py , je možné aj zadať adresu na ktorej bude fungovať

[^1]: Zdroj - https://github.com/tirfil/PySipFullProxy

    1