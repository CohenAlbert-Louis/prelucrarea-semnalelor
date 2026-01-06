**Componente**
Modulul hamming74 implementeaza codarea hamming(7,4) prin 2 metode statice:
***encode***
In cadrul acestei metode, datele primite ca parametru sunt codate folosit matricea G predefinita apoi se adauga un bit de paritate pentru a detecta erori duble
***decode***
Aceasta metoda decodeaza un codeword primit ca parametru si returneaza o pereche formata din:
- datele decodate dupa corectie (sau datele initiale daca corectia nu a putut fi efectuata)
- pozitia corectiei indexata de la 0 sau, -1 daca nu s-au gasit erori sau -2 daca s-a gasit o eroare, dar bit-ul de paritate nu o semnaleaza (i.e. exista o eroare dubla, aceasta neschimband paritatea datelor)

In fisierul main.py, se genereaza date corecte care sunt codate, iar apoi, se adauga una sau doua erori peste acestea, testand eficienta implementarii.
