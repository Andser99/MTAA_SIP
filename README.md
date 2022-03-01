**Implementácia**

SIP proxy stavia nad existujúcou knižnicou PySipFillProxy [^1] Riešenie je implementované v jazyku Python 2.7, súbor main.py konfiguruje a spúšťa potrebné funkcie knižnice. Z nepovinných funkcionalít sú implementované všetky okrem logovania "denníka hovorov".

**Vzorky pcap**

**Povinné**

- frames\_register.pcap - príklad registrácie klienta
- frames\_ring.pcap - zvonenie hovoru
- frames\_call.pcap - zodvihnutý hovor a jeho priebeh
- frames\_cancel\_other.pcap - zloženie hovoru druhou stranou

**Nepovinné**

- frames\_conference.pcap
    - konferenčný hovor medzi 3 zariadeniami
- frames\_redirect.pcap
    - presmerovanie hovoru na 3. zariadenie
- frames\_video\_call.pcap
    - videohovor, video zapnuté po zdvihnutí
- frames\_200\_DOBRE 
    -odpoveď 200 OK je premenovaná na 200 DOBRE pri registrácií.

**1 Program**

**1.1 Požiadavky**

- Python 2.7

Program je možné spustiť cez konzolu pomocou python main.py, je možné aj zadať adresu na ktorej bude fungovať

[^1]: Zdroj - https://github.com/tirfil/PySipFullProxy
