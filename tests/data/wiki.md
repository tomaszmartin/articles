**Python** – [język programowania](/wiki/J%C4%99zyk_programowania) [wysokiego poziomu](/wiki/J%C4%99zyk_wysokiego_poziomu) ogólnego przeznaczenia[[2]](#cite_note-2), o rozbudowanym pakiecie [bibliotek standardowych](/wiki/Biblioteka_standardowa)[[3]](#cite_note-3), którego ideą przewodnią jest czytelność i klarowność [kodu źródłowego](/wiki/Kod_%C5%BAr%C3%B3d%C5%82owy). Jego składnia cechuje się przejrzystością i zwięzłością[[4]](#cite_note-4)[[5]](#cite_note-5).
Python wspiera różne [paradygmaty programowania](/wiki/Paradygmat_programowania): [obiektowy](/wiki/Programowanie_obiektowe), [imperatywny](/wiki/Programowanie_imperatywne) oraz w mniejszym stopniu [funkcyjny](/wiki/Programowanie_funkcyjne). Posiada w pełni [dynamiczny](/wiki/Typowanie_dynamiczne) [system typów](/wiki/System_typ%C3%B3w) i automatyczne [zarządzanie pamięcią](/wiki/Od%C5%9Bmiecanie_pami%C4%99ci), będąc w tym podobnym do języków [Perl](/wiki/Perl), [Ruby](/wiki/Ruby_(j%C4%99zyk_programowania)), [Scheme](/wiki/Scheme) czy [Tcl](/wiki/Tcl_(j%C4%99zyk_programowania)). Podobnie jak inne [języki dynamiczne](/wiki/Dynamiczny_j%C4%99zyk_programowania) jest często używany jako [język skryptowy](/wiki/J%C4%99zyk_skryptowy). [Interpretery](/wiki/Interpreter_(program_komputerowy)) Pythona są dostępne na wiele [systemów operacyjnych](/wiki/System_operacyjny).
Python rozwijany jest jako projekt [Open Source](/wiki/Otwarte_oprogramowanie) zarządzany przez [Python Software Foundation](/wiki/Python_Software_Foundation), która jest [organizacją non-profit](/wiki/Organizacja_non-profit). Standardową implementacją języka jest [CPython](/wiki/CPython) (napisany w [C](/wiki/C_(j%C4%99zyk_programowania))), ale istnieją też inne, np. [Jython](/wiki/Jython) (napisany w [Javie](/wiki/Java)), CLPython napisany w [Common Lisp](/wiki/Common_Lisp), [IronPython](/wiki/IronPython) (na platformę [.NET](/wiki/.NET_Framework)) i [PyPy](/wiki/PyPy) (napisany w Pythonie, zob. [bootstrap](/w/index.php?title=Bootstrap_(programowanie)&action=edit&redlink=1)).
## Spis treści


- [1 Rozwój języka](#Rozwój_języka)
- [2 Filozofia Pythona](#Filozofia_Pythona)
- [3 Typy i struktury danych](#Typy_i_struktury_danych)
- [3.1 Wybrane wbudowane typy danych[7]](#Wybrane_wbudowane_typy_danych[7])
- [3.2 Kolekcje](#Kolekcje)
- [3.3 Wszystko jest obiektem](#Wszystko_jest_obiektem)
- [3.4 Emulowanie typów, przeciążanie operatorów, wywoływanie jako funkcje](#Emulowanie_typów,_przeciążanie_operatorów,_wywoływanie_jako_funkcje)
- [3.5 Zmienna liczba argumentów funkcji](#Zmienna_liczba_argumentów_funkcji)

- [4 Składnia](#Składnia)
- [4.1 Struktura przez wcięcia](#Struktura_przez_wcięcia)
- [4.2 Komentarze](#Komentarze)
- [4.3 Programowanie funkcyjne](#Programowanie_funkcyjne)
- [4.3.1 Lambda](#Lambda)
- [4.3.2 Generatory](#Generatory)

- [4.4 Operatory logiczne](#Operatory_logiczne)
- [4.5 Obsługa wyjątków](#Obsługa_wyjątków)
- [4.6 Dekoratory](#Dekoratory)

- [5 Biblioteka standardowa](#Biblioteka_standardowa)
- [5.1 Standardy dla bibliotek „zewnętrznych”](#Standardy_dla_bibliotek_„zewnętrznych”)

- [6 Inne cechy](#Inne_cechy)
- [7 Zobacz też](#Zobacz_też)
- [8 Przypisy](#Przypisy)
- [9 Linki zewnętrzne](#Linki_zewnętrzne)
## Rozwój języka

Pythona stworzył we wczesnych [latach 90.](/wiki/Lata_90._XX_wieku) [Guido van Rossum](/wiki/Guido_van_Rossum) – jako następcę [języka ABC](/wiki/ABC_(j%C4%99zyk_programowania)), stworzonego w [Centrum voor Wiskunde en Informatica](/w/index.php?title=Centrum_voor_Wiskunde_en_Informatica&action=edit&redlink=1) (CWI – Centrum Matematyki i Informatyki w [Amsterdamie](/wiki/Amsterdam)). Van Rossum jest głównym twórcą Pythona, choć spory wkład w jego rozwój pochodzi od innych osób. Z racji kluczowej roli, jaką van Rossum pełni przy podejmowaniu ważnych decyzji projektowych, często określa się go przydomkiem „[Benevolent Dictator for Life](/wiki/Benevolent_Dictator_for_Life)” (BDFL).
Nazwa języka nie pochodzi od zwierzęcia lecz od serialu komediowego emitowanego w latach siedemdziesiątych przez [BBC](/wiki/BBC) – „Monty Python’s Flying Circus” ([Latający cyrk Monty Pythona](/wiki/Lataj%C4%85cy_cyrk_Monty_Pythona)). Projektant, będąc fanem serialu i poszukując nazwy krótkiej, unikalnej i nieco tajemniczej, uznał tę za świetną[[6]](#cite_note-6).
Wersja 1.2 była ostatnią wydaną przez CWI. Od [1995](/wiki/1995) roku Van Rossum kontynuował pracę nad Pythonem w [Corporation for National Research Initiatives](/wiki/Corporation_for_National_Research_Initiatives) (CNRI) w [Reston](/wiki/Reston) w [Wirginii](/wiki/Wirginia), gdzie wydał kilka wersji Pythona, do 1.6 włącznie. W [2000](/wiki/2000) roku van Rossum i zespół pracujący nad rozwojem jądra Pythona przenieśli się do BeOpen.com by założyć zespół BeOpen [PythonLabs](/w/index.php?title=PythonLabs&action=edit&redlink=1). Pierwszą i jedyną wersją wydaną przez BeOpen.com był Python 2.0.
Po wydaniu wersji 1.6 i opuszczeniu CNRI przez van Rossuma, który zajął się programowaniem komercyjnym, uznano za wysoce pożądane, by Pythona można było używać z oprogramowaniem dostępnym na [licencji GPL](/wiki/GNU_General_Public_License). CNRI i [Free Software Foundation](/wiki/Free_Software_Foundation) (FSF) podjęły wspólny wysiłek w celu odpowiedniej modyfikacji licencji Pythona. Wersja 1.6.1 była zasadniczo identyczna z wersją 1.6, z wyjątkiem kilku drobnych poprawek oraz licencji, dzięki której późniejsze wersje mogły być zgodne z licencją GPL. Python 2.1 pochodzi zarówno od wersji 1.6.1, jak i 2.0.
Po wydaniu Pythona 2.0 przez BeOpen.com Guido van Rossum i inni programiści z PythonLabs przeszli do [Digital Creations](/w/index.php?title=Digital_Creations&action=edit&redlink=1). Cała [własność intelektualna](/wiki/W%C5%82asno%C5%9B%C4%87_intelektualna) dodana od tego momentu, począwszy od Pythona 2.1 (wraz z wersjami alpha i beta), jest własnością Python Software Foundation (PSF), niedochodowej organizacji wzorowanej na [Apache Software Foundation](/wiki/Apache_Software_Foundation).
## Filozofia Pythona

Python realizuje jednocześnie kilka paradygmatów. Podobnie do [C++](/wiki/C%2B%2B), a w przeciwieństwie do [Smalltalka](/wiki/Smalltalk) nie wymusza jednego stylu programowania, pozwalając na stosowanie różnych. W Pythonie możliwe jest [programowanie obiektowe](/wiki/Programowanie_obiektowe), [programowanie strukturalne](/wiki/Programowanie_strukturalne) i [programowanie funkcyjne](/wiki/Programowanie_funkcyjne). Typy sprawdzane są dynamicznie, a do zarządzania pamięcią stosuje się [garbage collection](/wiki/Od%C5%9Bmiecanie_pami%C4%99ci).
Choć w jego popularyzacji kładzie się nacisk na różnice w stosunku do [Perla](/wiki/Perl), Python jest pod wieloma względami do niego podobny. Jednakże projektanci Pythona odrzucili złożoną składnię Perla na rzecz bardziej oszczędnej i – ich zdaniem – bardziej czytelnej. Mimo że podobnie do Perla, Python jest czasem klasyfikowany jako język skryptowy, wykorzystuje się go do tworzenia dużych projektów jak [serwer aplikacji](/wiki/Serwer_aplikacji) [Zope](/wiki/Zope), system wymiany plików [Mojo Nation](/w/index.php?title=Mojo_Nation&action=edit&redlink=1) czy nawet oprogramowanie klasy ERP – [OpenERP](/wiki/OpenERP).
## Typy i struktury danych

W Pythonie *wartości*, a nie zmienne, posiadają typ – tak więc Python jest językiem z typami dynamicznymi, podobnie jak [Lisp](/wiki/Lisp), a w przeciwieństwie do [Javy](/wiki/Java). Wszystkie wartości przekazywane są przez [referencję](/wiki/Referencja_(informatyka)).
W porównaniu z innymi językami z typami dynamicznymi Python sprawdza typy w umiarkowanym stopniu. Nie jest ani tak liberalny, jak Perl, ani tak restrykcyjny jak [OCaml](/wiki/OCaml). Dla typów numerycznych zdefiniowana jest automatyczna konwersja, tak więc możliwe jest np. mnożenie liczby zespolonej przez liczbę całkowitą typu *long* bez rzutowania. Jednak w przeciwieństwie do Perla nie ma np. automatycznej konwersji pomiędzy napisami i liczbami; liczba nie jest prawidłowym argumentem dla operacji napisowej.
Python oferuje szeroki zakres podstawowych typów danych -- w tym typy liczbowe (całkowite, zmiennoprzecinkowe, [zespolone](/wiki/Liczby_zespolone)) oraz kolekcje.
### Wybrane wbudowane typy danych[[7]](#cite_note-7)


|Typ|Opis|Przykład
|:-|:-|:-
|Python 3: `str`
Python 2: `unicode`|Napis w Unikodzie (niezmienny)|Python 3: `'Wikipedia'` lub `"Wikipedia"`

Python 2: `u'Wikipedia'`lub `u"Wikipedia"`
|Python 3: `bytes`
Python 2: `str`|Napis w ASCII (niezmienny)|Python 3: `b'Wikipedia'` lub `b"Wikipedia"`

Python 2: `'Wikipedia'` lub `"Wikipedia"`
|`list`|Lista (zmienna, zawartość, długość)|`[4.0, 'string', True]`
|`tuple`|Krotka (niezmienna)|`(4.0, 'string', True)`
|`set`|Zbiór różnych elementów (zmienny)|Python 3: `{4.0, 'string', True}`
Python 2: `set([4.0, 'string', True])`
|`frozenset`|Zbiór różnych elementów (niezmienny)|Python 3: `frozenset({4.0, 'string', True})`
Python 2: `frozenset([4.0, 'string', True])`
|`dict`|Słownik, czyli tablica asocjacyjna (zmienny).|`{'key1': 1.0, 3: False}`
|`int` (oraz `long` w Python 2)|Liczba całkowita o dowolnej wartości|`42`
|`float`|Liczba zmiennoprzecinkowa|`3.1415927`
|`complex`|Liczba zespolona|`3+2.7j`
|`bool`|Prawda lub fałsz|`True`
`False`
|`type(None)`|Nic (odpowiednik `null`)|`None`

### Kolekcje

Część wyżej wymienionych typów to *kolekcje*.
Listy, [krotki](/wiki/Krotka_(struktura_danych)) (ang. *tuple*) i napisy są *sekwencjami*, w związku z czym udostępniają pewną liczbę wspólnych operacji (np. w identyczny sposób można iterować po kolejnych znakach napisu jak po elementach listy, czy też wskazywać elementy za pomocą indeksów). Listy to tablice o zmiennej liczbie elementów (z możliwością ich usuwania, dodawania i podmiany), zaś krotki to tablice o stałej liczbie elementów (bez możliwości usuwania, dodawania i podmiany).
Python obsługuje typowy zestaw operacji na łańcuchach tekstowych. Łańcuchy w Pythonie są niezmienne. Każda operacja, która zmieniłaby zawartość napisu (np. zamiana małych liter na wielkie) zwróci nowy napis, pozostawiając oryginalny napis bez zmian.
Innymi typami są kolekcje nieuporządkowane: *słowniki* (ang. *dict* od *dictionary* – znane w innych językach jako odwzorowania (ang. map) lub tablice asocjacyjne) oraz *zbiory* (zmienny *set* i niezmienny *frozenset*). Słownikowe klucze oraz elementy zbiorów muszą być tzw. obiektami haszowalnymi (posiadającymi metodę *__hash__()*) – co na ogół oznacza, że muszą być niezmienne (niemutowalne); np. kluczem słownika nie może być lista ani zbiór zmienny (typu *set*) – może zaś być krotka bądź zbiór niezmienny (typu *frozenset*), o ile zawiera wyłącznie elementy niezmienne.
Należy dodać, że podstawowe kolekcje w standardowej implementacji Pythona w C są wysoce zoptymalizowane pod kątem szybkości przeszukiwania, sortowania itp.
### Wszystko jest obiektem

System typów w Pythonie jest silnie powiązany z systemem klas. Chociaż typy wbudowane nie są właściwie klasami, klasa może dziedziczyć z dowolnego typu. Można więc dziedziczyć klasy z napisów czy słowników, a nawet z liczb całkowitych. Ponadto możliwe jest dziedziczenie wielokrotne.
Język umożliwia rozległą [introspekcję](/wiki/Introspekcja_(informatyka)) typów i klas. Typy można odczytywać i porównywać – podobnie, jak w [Smalltalku](/wiki/Smalltalk), typy (opisy typów) też są typem. Atrybuty obiektu można pobrać jako słownik.
W Pythonie **nie ma [enkapsulacji](/wiki/Hermetyzacja_(informatyka))**, jak to ma miejsce w C++ czy Javie, istnieją jednak mechanizmy pozwalające osiągnąć zbliżony efekt. Jednocześnie Python znacząco ułatwia introspekcję obiektów, tak więc właściwe użycie atrybutów obiektu pozostawia się programiście.
Dodatkowo każda funkcja, klasa i moduł mogą zostać opatrzone dokumentacją w [kodzie źródłowym](/wiki/Kod_%C5%BAr%C3%B3d%C5%82owy). Nie posiada ona wprawdzie rozbudowanych funkcji podobnych do [javadoc](/wiki/Javadoc), ale jest dostępna w czasie wykonania programu, a więc i w trybie interaktywnym.
### Emulowanie typów, przeciążanie operatorów, wywoływanie jako funkcje

Python pozwala dopasowywać własności danej klasy w szerokim zakresie. Implementując odpowiednie metody można sprawić, by obiekty danej klasy zachowywały się jak kolekcje, liczby, a nawet funkcje.
Przykład:

```
class Emulator: def __call__(self, x): print("Ten Emulator wywołano jako funkcję z parametrem x = {0}".format(x)) def __getitem__(self, key): return(str(key) + "-ty element w kontenerze klasy Emulator")e = Emulator()e('abc')e(123)print(e['def'])print(e[456])
```

Uruchomienie powyższego kodu da następujący rezultat:

```
Ten Emulator wywołano jako funkcję z parametrem x = abcTen Emulator wywołano jako funkcję z parametrem x = 123def-ty element w kontenerze klasy Emulator456-ty element w kontenerze klasy Emulator
```

### Zmienna liczba argumentów funkcji

Możliwe jest tworzenie funkcji ze [zmienną liczbą argumentów](/wiki/Zmienna_liczba_argument%C3%B3w), [argumentami o wartościach domyślnych](/wiki/Argument_domy%C5%9Blny) (podobnie jak w C++ lub C#), a także wywoływanie funkcji z użyciem [argumentów nazwanych](/wiki/Argument_nazwany), z podaniem nazw [parametrów](/wiki/Parametr_(informatyka)). Przykład:

```
def pokaz_argumenty(x, y, *args, **kwargs): print("x=%s, y=%s" % (x, y)) print("Argumenty pozycyjne:", end=' ') for aa in args: print(aa, end=' ') print("\nArgumenty nazwane:", end=' ') for kk in kwargs: print("%s=%s" % (kk, kwargs[kk]), end=' ')pokaz_argumenty('abc', 123, 456, 'def', k=789, m='ghi')
```

Uruchomienie powyższego kodu da następujący rezultat:

```
x=abc, y=123Argumenty pozycyjne: 456 defArgumenty nazwane: k=789 m=ghi
```

## Składnia

Czytanie kodu zajmuje wielokrotnie więcej czasu niż pisanie, a czytelny program można łatwiej zrozumieć i rozwijać. Python został zaprojektowany tak, by zapewnić możliwie dużą czytelność [kodu źródłowego](/wiki/Kod_%C5%BAr%C3%B3d%C5%82owy). Posiada prosty układ tekstu, używa wcięć lub angielskich słów tam, gdzie inne języki korzystają ze znaków interpunkcyjnych i posiada zdecydowanie mniej konstrukcji składniowych, niż wiele języków strukturalnych, takich jak [C](/wiki/C_(j%C4%99zyk_programowania)), [Perl](/wiki/Perl) czy [Pascal](/wiki/Pascal_(j%C4%99zyk_programowania)).
Dla czytelności, w Pythonie występują tylko dwa rodzaje pętli: `for`, w której [iteracja](/wiki/Iteracja) odbywa się po elementach listy (jak w [perlowym](/wiki/Perl) `foreach`), oraz `while`, która jest powtarzana, dopóki warunek logiczny jest spełniony. Python nie posiada składni `for` w stylu [C](/wiki/C_(j%C4%99zyk_programowania)), `do...while`, ani [perlowego](/wiki/Perl) `until`, choć oczywiście można uzyskać ich złożone odpowiedniki. Podobnie, Python ogranicza zestaw instrukcji wyboru do `if...elif...else` – wyeliminowano złożone [instrukcje wyboru](/wiki/Instrukcja_wyboru), czy [instrukcje skoków](/wiki/Instrukcja_skoku), które w innych językach szczególnie gmatwają czytelność.
Od wersji 2.5 Python posiada [operator warunkowy](/wiki/Operator_warunkowy), analogiczny do `warunek ? wartość1 : wartość2` znanego z [C](/wiki/C_(j%C4%99zyk_programowania)) i [Javy](/wiki/Java). Składnia: `wartość1 if warunek else wartość2`.
### Struktura przez wcięcia

Cechą wyróżniającą Pythona spośród innych języków jest stosowanie wcięć do wydzielania bloków kodu. Jest to cecha unikatowa wśród powszechnie stosowanych języków programowania, jako pierwsza rzucająca się w oczy programistom niepiszącym w Pythonie.
W językach programowania wywodzących strukturę blokową od [Algola](/wiki/ALGOL) (niekoniecznie bezpośrednio) – np. [Pascalu](/wiki/Pascal_(j%C4%99zyk_programowania)), [C](/wiki/C_(j%C4%99zyk_programowania)), czy [Perlu](/wiki/Perl) – bloki kodu zaznaczane są klamrami lub słowami kluczowymi (C i Perl używają `{ }`, Pascal używa `begin` i `end`). Jednakże we wszystkich tych językach programiści tradycyjnie stosują wcięcia, by wyróżnić bloki w otaczającym kodzie.
Natomiast Python dziedziczy cechę mniej znanego języka [ABC](/wiki/ABC_(j%C4%99zyk_programowania)) – zamiast interpunkcji czy słów kluczowych używa samych wcięć do zaznaczania bloków. Wyjaśnić to można na prostym przykładzie zamieszczonym poniżej. Przedstawiona jest w nim funkcja licząca silnię w [C](/wiki/C_(j%C4%99zyk_programowania)) i w Pythonie:
*silnia w C (zapisana bez wcięć):*

```
int silnia(int x) { if (x == 0) return 1; else return x * silnia(x-1);}
```

*silnia w Pythonie:*

```
def silnia(x): if x == 0: return 1 else: return x * silnia(x-1)
```

Dla niektórych programistów przyzwyczajonych do języków stylistycznie wzorowanych na [Algolu](/wiki/ALGOL), gdzie spacja nie ma znaczenia składniowego, może to być mylące. Spotyka się czasem niepochlebne porównanie do sztywnego systemu kolumnowego kart perforowanych stosowanego w czasach [fortranowych](/wiki/Fortran).
Istotnie, w swoim czasie możliwość stosowania zapisu, w którym decydujące były jedynie symbole, była dużym postępem. Jednak dla programistów piszących w Pythonie stosowanie składniowo znaczących wcięć jest po prostu przedłużeniem konwencji, która i tak jest stosowana np. w [C](/wiki/C_(j%C4%99zyk_programowania)). Zwolennicy tego języka zwracają także uwagę na wadę „swobodnej” składni, polegającą na tym, że skoro wcięcia kodu są ignorowane, nie można wymusić jednej dobrej konwencji (stąd też konflikty między programistami, dotyczące stosowania [spacji](/wiki/Spacja) (i różnej ich liczby) lub [tabulatorów](/wiki/Tabulacja), tzw. *indentation wars*). Nieprawidłowo wcięty kod może być mylący, gdyż czytający go programista i kompilator mogą go różnie zinterpretować.
### Komentarze

Komentarze zaczynają się od znaku „`#`” i kończą z końcem wiersza. Komentarze wieloliniowe można wstawiać w postaci wielowierszowych *stringów* (ograniczonych przez `"""` lub `'''`) bez żadnych działań (np. przypisań); *stringi* te nie są traktowane jako wyrażenia przez interpreter.
Wielowierszowy *string* umieszczony w pierwszej linii ciała funkcji lub klasy albo na początku modułu, traktowany jest jako tzw. *docstring* (napis dokumentacyjny) dla tegoż obiektu. System dokumentacji Pythona może automatycznie tworzyć sformatowaną dokumentację z *docstringów*, dając w ten sposób ograniczoną wersję *[literate programming](/wiki/Literate_programming)*. Dokumentację można przeglądać w trybie interaktywnym interpretera za pomocą funkcji `help` lub z poziomu [wiersza poleceń](/wiki/Wiersz_polece%C5%84) za pomocą skryptu `pydoc`.
### Programowanie funkcyjne

Inną cechą Pythona jest dostępność składni funkcyjnej. Jak można oczekiwać, upraszcza to znacznie obróbkę list i innych kolekcji. Jedną z takich konstrukcji jest tzw. *lista składana* (ang. *list comprehension*), przejęte z funkcjonalnego [Haskella](/wiki/Haskell), jak w przedstawionym poniżej przykładzie obliczania pięciu pierwszych [potęg dwójki](/wiki/Pot%C4%99ga_dw%C3%B3jki):

```
liczby = [1, 2, 3, 4, 5]potegi_dwojki = [2**n for n in liczby]
```

Za pomocą list składanych można elegancko wyrazić algorytm [quicksort](/wiki/Sortowanie_szybkie),chociaż taka jego implementacja jest mało wydajna:

```
def qsort(L): if L == []: return [] return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + \ qsort([x for x in L[1:] if x >= L[0]])
```

Wykorzystując [programowanie funkcyjne](/wiki/Programowanie_funkcyjne) można skrócić implementację [silni](/wiki/Silnia) do jednolinijkowca bez uciekania się do rekurencji. W poniższym przykładzie użyto operacji redukcji listy. Przykład korzysta ze składni Pythona z rodziny 2.7 oraz 3.0:

```
from functools import reducedef silnia_f(n): return int(reduce(lambda x, y: x*y, list(range(2, n+1)) or [1]))
```

#### Lambda

Nieco mylące dla zwolenników programowania funkcyjnego może być słowo kluczowe `lambda`. Bloki `lambda` mogą zawierać jedynie wyrażenia, nie instrukcje. Nie są one więc najbardziej ogólnym sposobem tworzenia funkcji. Zamiast tego można zdefiniować i zwrócić funkcję używając nazwy w zasięgu lokalnym, jak w poniższym przykładzie prostej funkcji generującej inną funkcję (ang. *curry*):

```
def zbuduj_sumator(x): def temp(y): print( "{0} + {1} = {2}".format(x, y, x+y) ) return temp
```

Funkcję tę można zaimplementować także używając zagnieżdżonych wyrażeń `lambda` tak, jak to się robi w [Scheme](/wiki/Scheme). W pythonie 2 wymaga to obejścia ograniczeń pythonowej lambdy przez zdefiniowanie funkcji obudowującej instrukcję `print`:

```
def drukuj(obj): print objzbuduj_sumator = \ lambda x : lambda y : \ drukuj( "{0} + {1} = {2}".format(x, y, x+y) )
```

Oba warianty funkcji `zbuduj_sumator` zachowują się identycznie: dla podanej liczby *x* zwracają funkcję, która dla podanej liczby *y* wydrukuje wyrażenie arytmetyczne. Choć pierwszy styl jest częściej spotykany, drugi może być czytelniejszy dla programistów wyspecjalizowanych w programowaniu funkcyjnym.
Unikalne cechy pythonowych operatorów logicznych *and* i *or* dają jeszcze jedną unikalną możliwość programowania funkcyjnego. Przy wykorzystaniu tych dwóch operatorów można w wyrażeniach `lambda` zaimplementować dowolne sterowanie przebiegiem [[1]](http://www-106.ibm.com/developerworks/linux/library/l-prog.html). Wykorzystuje się to zwykle tylko do stosunkowo prostych konstrukcji (patrz rozdział o [operatorach logicznych](/wiki/Python#Operatory_logiczne)).
#### Generatory

[Generatory](/wiki/Generator_(informatyka)) są w Pythonie mechanizmem [leniwej ewaluacji](/wiki/Warto%C5%9Bciowanie_leniwe) funkcji, która w przeciwnym razie musiałaby zwracać obciążającą pamięć lub kosztowną w obliczaniu listę. Stosowanie generatorów jest podobne do strumieni w [Scheme](/wiki/Scheme).
Przykład ze strony domowej Pythona 2:

```
def generuj_calkowite(N): for i in xrange(N): yield i
```

Można teraz użyć tego generatora:

```
for i in generuj_calkowite(N): print i
```

Przed wykonaniem drugiego fragmentu kodu należy oczywiście zdefiniować zmienną `N`.
Definicja generatora przypomina definicję funkcji, ale zamiast słowa kluczowego `return` używa się `yield`. Jednakowoż generator jest obiektem przechowującym stan, mogącym wielokrotnie wchodzić do i opuszczać ten sam dynamiczny zakres. Wywołanie generatora może być użyte zamiast listy lub innej struktury, po której elementach będziemy iterować. Za każdym razem, gdy pętla `for` w powyższym przykładzie potrzebuje następnego elementu, wywoływany jest generator, który daje następny element.
W wersji 2.4 dodano *wyrażenia generatorowe* (ang. *generator expressions*), analogiczne do listy składanej. Zapis:

```
gen_kwadratow = (i**2 for i in range(5))
```

jest odpowiednikiem:

```
def gen_kwadratow(): for i in range(5): yield i**2
```

### Operatory logiczne

W Pythonie jako fałsz logiczny traktuje się:

- liczbę zero (`0`, `0.0`, `0j` itp.)
- `False`
- `None` ([null](/wiki/Litera%C5%82_pusty))
- puste kolekcje (`[]`, `()`, `{}`, `set()` itp.)
- puste napisy (`""`, `""""""`)
- w Pythonie 2 – obiekty posiadające metodę `__nonzero__()`, jeśli zwraca ona `False` lub `0`
- w Pythonie 3 – obiekty posiadające metodę `__bool__()`, jeśli zwraca ona `False`
Wszystko inne jest prawdą logiczną.
Operatory `and` i `or` zwracają wartość ostatnio obliczonego wyrażenia, np. „`x==5 or 3`” zwróci 3. W Pythonie często pisze się instrukcje w rodzaju `print p or q`, by wykorzystać tę cechę.
Wartości logiczne zwracane przez operatory porównania (`==`, `>`, `!=`, `is` itp.), operator zawierania (`in`) oraz operator negacji (`not`) reprezentowane są przez obiekty `True` i `False`. Gdyby więc w powyższym przykładzie kolejność wyrażeń zamienić na „`3 and x==5`”, zwrócona zostałaby wartość `True`, gdyż tak ewaluowane jest `x==5`. Operatory porównania można łączyć, np. „`-1 < x < 0`” zwróci `True` dla `x` z przedziału (-1, 0) – tak, jak w zapisie matematycznym, a inaczej niż np. w [C++](/wiki/C%2B%2B).
Od Pythona 2.3 `True` i `False` są wbudowanymi obiektami typu `bool`. Wcześniej do identyfikatorów tych przypisane były obiekty liczb całkowitych, odpowiednio 1 i 0.
### Obsługa wyjątków

Python udostępnia i intensywnie wykorzystuje obsługę [wyjątków](/wiki/Wyj%C4%85tek) jako sposób wykrywania błędów.
Styl programowania w Pythonie zaleca stosowanie wyjątków zawsze, gdy może pojawić się błąd wykonania. Na przykład nie testuje się praw dostępu do pliku przed jego otwarciem, lecz po prostu próbuje się go otworzyć, przechwytując wyjątek w razie braku dostępu.
### Dekoratory

W wersji 2.4 wprowadzono nowy element składni – notację [dekoratora](/wiki/Dekorator_(wzorzec_projektowy)). Przykład: w starszych wersjach Pythona, by uzyskać metodę statyczną klasy, należało napisać:

```
class C: def metoda(obj): pass metoda = staticmethod(metoda)
```

Notacja dekoratora pozwala, bardziej czytelnie, umieścić informację o konwersji (dekoracji) przed definicją funkcji:

```
class C: @staticmethod def metoda(obj): pass
```

Ogólnie zapis:

```
@dekoratordef funkcja(): pass
```

jest równoważny zapisowi:

```
def funkcja(): passfunkcja = dekorator(funkcja)
```

## Biblioteka standardowa

Python posiada rozbudowaną [bibliotekę standardową](/wiki/Biblioteka_standardowa), umożliwiającą jego stosowanie do wielu zadań. Twórcy języka stosują politykę tzw. *Batteries Included*, czyli dostarczenia wraz z pakietem instalacyjnym możliwie dużej liczby narzędzi. Moduły standardowej biblioteki można uzupełniać modułami pisanymi w C lub w Pythonie. Biblioteka standardowa jest szczególnie dobrze dostosowana do tworzenia aplikacji sieciowych, jako że obsługuje znaczną liczbę standardowych formatów i protokołów (np. [MIME](/wiki/Multipurpose_Internet_Mail_Extensions), [HTTP](/wiki/Hypertext_Transfer_Protocol)). Dołączone są także moduły do tworzenia [GUI](/wiki/Graficzny_interfejs_u%C5%BCytkownika) (na bazie [Tcl](/wiki/Tcl_(j%C4%99zyk_programowania))/[Tk](/wiki/Tk)), obróbki [wyrażeń regularnych](/wiki/Wyra%C5%BCenie_regularne), nawet prosty serwer [WWW](/wiki/World_Wide_Web) z obsługą [CGI](/wiki/Common_Gateway_Interface).
Większa część biblioteki standardowej dostępna jest na wszystkich platformach, dzięki czemu nawet duże aplikacje mogą często być uruchamiane bez konieczności modyfikacji na [Uniksach](/wiki/Unix), pod [Windows](/wiki/Microsoft_Windows), na [Macintoshu](/wiki/Macintosh) i innych platformach. Przeciwnie, niż np. dla [Javy](/wiki/Java), nie ogranicza się zestawu dostępnych funkcji do części wspólnej dla różnych platform; np. na [uniksach](/wiki/Unix) dostępna jest funkcja `os.fork()`, choć nie ma jej np. w [Windows](/wiki/Microsoft_Windows)[[8]](#cite_note-8).
### Standardy dla bibliotek „zewnętrznych”

Podobnie, jak w wypadku innych języków, opracowany został szereg standardów tworzenia [API](/wiki/Application_Programming_Interface) pomocniczego, np. sterowników [relacyjnych baz danych](/wiki/Model_relacyjny). Ze względu na w pełni dynamiczny system typów nie ma konieczności dołączania do biblioteki standardowej „interfejsu bazowego”, jak to ma miejsce np. w przypadku [JDBC](/wiki/Java_DataBase_Connectivity). Twórca biblioteki zewnętrznej musi po prostu zapewnić, by stworzone przez niego moduły, funkcje i klasy posiadały odpowiednie atrybuty.
## Inne cechy

Interpreter Pythona posiada także *tryb interaktywny*, w którym wyrażenia można wprowadzać z terminala, otrzymując natychmiast wyniki. Zgodnie z założeniem twórców Pythona ułatwiać ma to naukę programowania, gdyż pozwala wypróbowywać fragmenty kodu ze skutkiem natychmiastowym. Standardowy shell nie jest jednakże zbyt wygodny ani nie posiada zbyt wielu funkcji (brak np. uzupełniania TAB-em) – braków tych jest pozbawiony [IPython](/w/index.php?title=IPython&action=edit&redlink=1), będący częścią pakietu [SciPy](/w/index.php?title=SciPy&action=edit&redlink=1).
Wraz z Pythonem rozpowszechniana jest także biblioteka [unittest](/w/index.php?title=Unittest_(Python)&action=edit&redlink=1) do [testów jednostkowych](/wiki/Test_jednostkowy), pozwalająca na tworzenie wyczerpujących testów poprawności tworzonego oprogramowania[[9]](#cite_note-9).
## Zobacz też


- [IronPython](/wiki/IronPython)
- [PyQt](/wiki/PyQt), [PyGTK](/wiki/PyGTK), [wxPython](/wiki/WxPython), [Tkinter](/wiki/Tkinter), [Pygame](/wiki/Pygame)
- [IDLE](/wiki/IDLE), [eric3](/wiki/Eric), [Boa Constructor](/wiki/Boa_Constructor), [Stani's Python Editor](/wiki/Stani%27s_Python_Editor), [Wing IDE](/wiki/Wing_IDE)
## Przypisy


1. ↑ [a](#cite_ref-nn_1-0) [b](#cite_ref-nn_1-1) [Download Python _ Python.org](https://www.python.org/downloads/) (ang.). [dostęp 2018-07-07].
2. [↑](#cite_ref-2) Dave Kuhlman: [A Python Book: Beginning Python, Advanced Python, and Python Exercises](http://cutter.rexx.com/~dkuhlman/python_book_01.html) (ang.).  Cytat: Python is a high-level general purpose programming language
3. [↑](#cite_ref-3) [About Python](http://www.python.org/about) (ang.). Python Software Foundation. [dostęp 24 kwietnia 2012].
4. [↑](#cite_ref-4) Mark Summerfield: *Rapid GUI Programming with Python and Qt*. Cytat: If you are new to Python: Welcome! You are about to discover a language that is clear to read and write, and that is concise without being cryptic.. (ang.)
5. [↑](#cite_ref-5) Mark Summerfield: *Rapid GUI Programming with Python and Qt*. Cytat: Python is a very expressive language, which means that we can usually write far fewer lines of Python code than would be required for an equivalent application written in, say, C++ or Java.. (ang.)
6. [↑](#cite_ref-6) Python Software Foundation: [Whetting Your Appetite – Python v2.7.2 documentation](http://docs.python.org/tutorial/appetite.html) (ang.). [dostęp 2011-08-03].
7. [↑](#cite_ref-7) [Built-in Types](http://docs.python.org/library/stdtypes.html).
8. [↑](#cite_ref-8) Python Software Foundation: [16.1. os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#os.fork) (ang.). [dostęp 07 marca 2017].  Cytat: os.fork() Fork a child process. [szczegółowy opis funkcji] Availability: Unix
9. [↑](#cite_ref-9) Python Software Foundation: [26.4. unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html) (ang.). [dostęp 07 marca 2017].  Cytat: The unittest module provides a rich set of tools for constructing and running tests.
## Linki zewnętrzne


- [http://python.org/](http://python.org/) – Oficjalna strona Pythona
- [http://python.rk.edu.pl](http://www.python.rk.edu.pl/w/p/wprowadzenie-do-pythona/) – Biblioteka języka Python
[Kontrola autorytatywna](/wiki/Pomoc:Kontrola_autorytatywna) ([obiektowy język programowania](/wiki/Obiektowy_j%C4%99zyk_programowania)):
- [LCCN](/wiki/Biblioteka_Kongresu): [sh96008834](http://lccn.loc.gov/sh96008834)
- [GND](/wiki/Gemeinsame_Normdatei): [4434275-5](http://d-nb.info/gnd/4434275-5)
- [BnF](/wiki/Biblioteka_Narodowa_Francji): [13560465c](http://catalogue.bnf.fr/ark:/12148/cb13560465c)
- [SUDOC](https://fr.wikipedia.org/wiki/Syst%C3%A8me_universitaire_de_documentation): [051626225](http://www.idref.fr/051626225)
- [WorldCat](http://www.worldcat.org/identities/lccn-sh96008834)