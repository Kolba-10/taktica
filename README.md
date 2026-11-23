# Taktica / Tablica taktyczna

Boisko piłkarskie ma dwie stałe bramki tła: światło 7,32 m i głębokość rzutu 2 m. Są widoczne również w miniaturach, animacji oraz eksportach SVG, PNG i MP4. Puste tło je ukrywa. Nie należą do obiektów projektu; narzędzie ruchomej bramki pozostaje niezależne. Pełny kadr mieści je z marginesem, a zapisane własne kadry nie są automatycznie zmieniane.

Po zaznaczeniu pola ćwiczenia białe uchwyty narożne zmieniają jego wymiary z nieruchomym przeciwległym narożnikiem. Shift zachowuje początkowe proporcje, Escape anuluje przeciąganie. Zwykła zawartość zachowuje położenie; sprzęt przypięty do geometrii podąża za narożnikami.

Złote uchwyty na liniach podziału przesuwają pojedyncze granice w lokalnych osiach pola. Sekcja „Podział pola” pozwala wybrać „Własny”, wpisać dokładne odległości od początkowego boku oraz przywrócić równe strefy poleceniem „Wyrównaj podział”. Własne granice zachowują proporcje po zmianie wymiarów pola.

Opis automatycznie mieści się nad obrysem. Przeciągnięcie samego napisu zapisuje własne położenie względem pola. Sekcja „Opis pola” pozwala przywrócić położenie automatyczne.

Command+A / Ctrl+A zaznacza wszystkie obiekty aktywnej klatki, również poza kadrem. Skrót pozostawia standardową obsługę tekstu w formularzach i nie działa na tablicę podczas otwartych okien. Blokady pozostają aktywne.

Działająca aplikacja internetowa dla trenera piłki nożnej. Interfejs jest po polsku. Nie wymaga konta, serwera aplikacji ani instalowania bibliotek.

## Praca w Codex

Otwórz ten folder jako projekt w Codex. Kod aplikacji znajduje się w `dist/index.html`, `dist/style.css` i `dist/app.js`. Folder `dist` jest obecnie źródłem aplikacji, a nie plikiem generowanym. Zmiany wprowadzaj właśnie w nim.

W Terminalu, w folderze projektu, uruchom:

```sh
python3 scripts/serve.py
```

Otwórz http://localhost:8000. Serwer zatrzymasz przez Ctrl+C. Używaj stale tego samego adresu i przeglądarki, ponieważ lokalne projekty są związane z adresem aplikacji. Eksport MP4 zależy od dostępności kodera H.264 w WebCodecs przeglądarki.

## Zachowanie dotychczasowych projektów

Przed przejściem z poprzedniego pliku HTML otwórz go i wyeksportuj każdy ważny projekt przez Projekty → Eksport JSON. W aplikacji pod nowym adresem użyj Import JSON. Kod w repozytorium nie zawiera prywatnych projektów zapisanych w Twojej przeglądarce. Przeniesienie plików z kodem nie przenosi automatycznie tego zapisu.

## Przenośny plik HTML

```sh
python3 scripts/build.py
```

Wynik: `build/Tablica_taktyczna.html`. To samodzielna wersja bez dodatkowych plików. Nie edytuj jej ręcznie, tylko ponownie wygeneruj ze źródeł.

## Kontrola zmian

```sh
node --check dist/app.js
python3 scripts/build.py
git diff
```

Pierwsza komenda wymaga Node.js. Kontrola składni i budowanie nie zastępują sprawdzenia działania w przeglądarce. Przy zmianach przetestuj zaznaczanie i przeciąganie, edycję, cofanie, zapis/odświeżenie, animację i eksport. Sprawdź stare projekty oraz powiązane linie i strefy, jeśli zmiana ich dotyczy.

Repozytorium projektu: https://github.com/Kolba-10/taktica. Pliki wynikowe w `build/` są generowane lokalnie i nie są przechowywane w Git.

## Kompaktowy interfejs Taktica

Pasek u góry zawiera nazwę projektu, przełącznik Tablica/Animacja, status zapisu,
cofanie/ponawianie, eksport PNG i Skupienie. Narzędzia przy lewej krawędzi mają
podpowiedzi po najechaniu. Dolna część paska otwiera Bibliotekę projektów, Właściwości,
Warstwy, Widok i kadr oraz Edycję i pomoc (kopiowanie/wklejanie).

Panele zamkniesz krzyżykiem, ponownym kliknięciem ich ikony lub Escape.
Właściwości wybranego obiektu są dostępne przez ikonę Właściwości; dwuklik
lub prawy przycisk otwierają pływający edytor, przesuwany za jego nagłówek.
Wybierz kadr otwiera jawną edycję kamery. Zamykanie tego panelu przed
zatwierdzeniem anuluje zmianę kadru. Obrót boiska i format kadru są niezależne.

F przełącza Skupienie, jeśli kursor nie jest w polu tekstowym.
Oś czasu w trybie Animacja można zwinąć, pozostawiając sterowanie odtwarzaniem.
Rzadziej używane polecenia są w menu Ustawienia klatek.

Układ paneli nie jest częścią danych projektu i nie zmienia zapisanej kamery,
pozycji obiektów, klatek ani historii. Adres pozostaje http://localhost:8000.

## Kolor i koszenie boiska

W panelu Widok i kadr wybierz Kolor boiska (Białe, Jasnozielone,
Ciemnozielone), a następnie miniaturę Wzoru koszenia. Puste białe tło
pozostaje osobną opcją Tła. Wygląd jest wspólny dla klatek danego projektu,
tak jak dotychczasowe tło, i jest zapisywany w JSON oraz historii.
Pełne pasy mają 5,5 m; wyrównanie długości jest przy środku, a szerokości
przy liniach bocznych. Zielona murawa i wybrany wzór wypełniają całą
powierzchnię tablicy oraz cały eksportowany kadr, również poza boiskiem.
Wzór obraca się z boiskiem i jest obecny w SVG, PNG i MP4. Rozmiar okna
zmienia wyłącznie prezentację tła, bez zmiany zapisanego kadru i obiektów.


## Panel zawodnika, ramka i biblioteka

Numer, średnica i kolor kapsla są na początku panelu. Podpis nad i pod
zawodnikiem mają niezależne przełączniki. Wyłączenie zachowuje tekst i styl.
Starsze niepuste podpisy pozostają włączone. Warstwy i ustawienia ścieżki
ruchu są w zwijanych sekcjach; usuwanie jest na dole.

Command+klik (macOS) lub Ctrl+klik zaznacza grupę. Dwuklik na zaznaczonym
zawodniku otwiera wspólną średnicę i kolor bez utraty zaznaczenia.
Średnicę zatwierdza Enter lub opuszczenie pola. Wspólna zmiana stanowi
jedną operację historii i zachowuje położenia, numery oraz podpisy.

W Widok i kadr kliknij Wybierz kadr. Przesuwaj wnętrze ramki i skaluj ją
uchwytami narożników lub boków. Proporcje wynikają z wybranego formatu.
Zatwierdź kadr dopasowuje widok i blokuje kamerę; Anuluj lub Escape
przywraca poprzedni kadr. Ręczny zoom i przesuwanie gestami są wyłączone.
Kadry zapisane w animacji nadal działają i są eksportowane.

Ikona folderu otwiera bibliotekę z miniaturami i wyszukiwaniem. Import,
eksport JSON oraz usuwanie otwartego projektu są w bibliotece.
Nowy, Zapisz, Zapisz jako i Duplikuj są ikonami w nagłówku. Zapisz jako
pyta o nazwę w oknie aplikacji i tworzy osobny projekt. Podpowiedzi ikon
pojawiają się po zatrzymaniu kursora oraz przy fokusie klawiatury.

Ikona Pełny ekran korzysta z API przeglądarki; ponowne kliknięcie lub
Escape wyłącza ten tryb. Skupienie (F) jest osobnym trybem interfejsu.

## Półprzestrzenie

Przycisk boiska z pięcioma sektorami na bocznym pasku (nad kadrowaniem)
włącza i wyłącza cztery podłużne linie. Podział wynika z bocznych krawędzi
pól bramkowych i karnych. Jest częścią tła, niezależną od siatki pomocniczej;
nie należy do obiektów ani warstw. Obraca się z boiskiem i jest obecny
w animacji, PNG, MP4 oraz miniaturach. Ustawienie jest wspólne dla klatek
projektu, zapisywane w JSON i historii. Starsze projekty mają je wyłączone.

Kolor półprzestrzeni dobiera się automatycznie: przygaszona biel #D8DED8
na obu zielonych wariantach i ciemnoszary #30383b na białym. SVG, Canvas,
miniatury oraz eksporty korzystają ze wspólnej reguły wyboru koloru.

## Organizowanie biblioteki projektów

Ikona folderu otwiera okno Projekty. Nawigacja obejmuje wszystkie aktywne
projekty, ostatnio otwierane, ulubione, szablony, foldery, archiwum i kosz.
Folder główny obejmuje także swój jeden poziom podfolderów. Usunięcie folderu
zachowuje projekty, przenosząc je do Bez folderu.

Menu ⋯ karty zawiera organizację projektu: opis (do 500 znaków), folder,
tagi, ulubione i klatkę miniatury. Foldery… oraz Tagi… otwierają zarządzanie
nazwami, strukturą i scalaniem tagów. Gwiazdka działa bez otwierania projektu.
Wyszukiwarka pomija polskie znaki i szuka wszystkich wpisanych słów w nazwie,
opisie oraz tagach. Rozwijane Filtry pozwalają łączyć folder, tagi i animację.
Kafelki i lista mają sortowanie oraz strony po 24 pozycje; widok i sortowanie
są zapamiętywane. Pola wyboru uruchamiają działania grupowe, a Zaznacz wszystkie
wyniki obejmuje także kolejne strony aktualnych wyników.

Utwórz szablon zapisuje osobny wzorzec. Użyj szablonu tworzy niezależny projekt
bez folderu i gwiazdki, zachowując opis oraz tagi. Edytuj szablon otwiera sam
wzorzec, z wyraźnym oznaczeniem nad boiskiem. Zmiany wzorca nie zmieniają kopii.

Archiwum umożliwia podgląd bez edycji i przywrócenie. Usuwanie przenosi projekt
do kosza; dopiero potwierdzone Usuń trwale lub Opróżnij kosz usuwa go ostatecznie.
Archiwum i kosz nadal są lokalnymi danymi, nie kopią zapasową. Eksport JSON
przenosi także nazwy tagów, ścieżkę folderu i rodzaj projektu. Import tworzy
osobną kopię i dopasowuje organizację po nazwach, bez nadpisywania projektów.

Migracja biblioteki zachowuje stary zapis. Błąd zapisu blokuje przełączenie
projektu i jest widoczny w statusie. Metadane biblioteki są oddzielone od
historii edycji sceny. Nigdy nie należy czyścić localStorage w celu aktualizacji.

Testy logiki biblioteki (bez przeglądarki): `node work/check-library.js`.
Korzystają z syntetycznego zestawu 300 projektów, bez danych użytkownika.

## Sprzęt, pola ćwiczeń i pomiary

Na bocznym pasku są trzy nowe narzędzia: Sprzęt, Pole ćwiczenia i Pomiar
odległości. Sprzęt otwiera wybór dziewięciu symboli z miniaturami. Ustaw
wymiary w metrach i klikaj boisko, aby dodawać kolejne elementy. Escape kończy
wstawianie. Ten sam sposób działa na pustym tle. Przecinek i kropka są
obsługiwane w polach wymiarów. Skala wynosi 10 jednostek modelu na metr,
niezależnie od kamery i rozmiaru okna.

Utwórz układ… pozwala rozmieścić sprzęt w rzędzie, slalomie lub okręgu.
Przed zatwierdzeniem widać podgląd i liczbę elementów. W edycji pola dostępny
jest też układ na obwodzie, z podanym odstępem i bez powielania narożników.
Cały układ tworzy się jednym krokiem historii. Dwuklik otwiera edycję;
Command/Ctrl+klik i prostokąt zaznaczają wiele obiektów. Alt+przeciągnięcie
pozwala zacząć zaznaczanie prostokątem także wewnątrz pola ćwiczenia.

Pole ma własną szerokość i długość, obrys, przezroczyste wypełnienie, nazwę
i podziały. Szerokość odpowiada krótszej osi boiska, a długość jego osi
podłużnej przed obrotem. Sekcje dodatkowe zawierają podziały według liczby
lub rozmiaru komórki, sprzęt narożny, obrót, zawartość i warstwy. Niepełny
ostatni pas zachowuje rzeczywisty rozmiar. Podziały są zawsze pod sprzętem.

Przypisz zaznaczone do pola jest jawnym poleceniem; samo położenie wewnątrz
prostokąta nie tworzy przypisania. Przesuwaj z zawartością obejmuje przesuwanie
i obrót, ale zmiana samych wymiarów pola pozostawia zwykłą zawartość na miejscu.
Sprzęt przypięty do narożników lub obwodu zawsze śledzi geometrię pola, dopóki
nie zostanie jawnie odłączony. Skaluj całe ćwiczenie jest osobną operacją;
domyślnie nie zmienia rozmiarów sprzętu, kapsli, tekstów i grubości linii.
Blokady zatrzymują operację całego pola bez częściowego przekształcenia.

Układ można grupować, obracać wokół wspólnego środka, skalować i wyrównywać
w równych odstępach. Orientacja samych elementów jest osobnym ustawieniem.
Blokadę można zdjąć w sekcji Blokada i warstwa albo ikoną w panelu Warstwy.
Podpis sprzętu ma niezależny tekst i formatowanie oraz jest domyślnie wyłączony.

Pomiar powstaje po wskazaniu dwóch punktów. Podświetlenie wskazuje przypięcie
do środka obiektu, narożnika pola lub końca bramki z pachołków. Końce można
przeciągać uchwytami. Usunięcie obiektu odłącza pomiar w ostatnim położeniu.
Pomiary są widoczne w eksporcie, chyba że wyłączysz ich widoczność w edytorze.

Kopia pola obejmuje jego przypisaną zawartość oraz pomiary pomiędzy kopiowanymi
obiektami; wszystkie wewnętrzne powiązania są przepisywane na nowe identyfikatory.
Usunięcie samego pola zachowuje zawartość. Usunięcie pola z zawartością wymaga
potwierdzenia. Dopasuj widok do ćwiczenia uwzględnia podpisy i blokuje nowy kadr.

Górne menu Eksport zawiera PNG, SVG i MP4. Nowe elementy korzystają ze wspólnej
geometrii wektorowej w SVG i Canvas. Powiązana zawartość interpoluje położenie
w obracanym polu bez podwójnego przesunięcia. Edycja dotyczy aktywnej klatki.

Testy: `node work/check-training.js`. Raport i przykładowe rzeczywiste eksporty
znajdują się w `work/training-qa/` (wyłącznie dane testowe).

## Dodaj zespół — gotowe formacje

Ikona trzech zawodników na bocznym pasku otwiera Dodaj zespół. Wybierz Mój
zespół, Przeciwnik lub Oba zespoły. Każda drużyna ma własną formację, kolor
zawodników, kolor bramkarza i średnicę kapsli. Dostępne są 4–1–3–2, 4–4–2,
4–2–3–1, 4–3–3, 3–4–3 oraz 3–5–2, z numeracją 1–11 i żółtym bramkarzem.

Wybór połowy dla jednej drużyny w trybie obu zespołów przydziela drugiej
przeciwną połowę. Zamień strony przenosi obie formacje razem z ich kolorami.
Nazwy połów i strzałki ataku odpowiadają obrotowi boiska. Podgląd zawsze
obejmuje całe boisko, także przy przybliżonym kadrze. Zbyt duża średnica,
powodująca nakładanie kapsli lub wyjście poza połowę, blokuje dodawanie.

Dodaj wstawia 11 lub 22 zwykłych zawodników jednym krokiem historii i zaznacza
ich do wspólnej edycji. Zawodnicy nie są automatycznie grupowani ani później
przyciągani do formacji. Nie są dodawane napisy ani połączenia.

Jeśli zespół ma już skład w aktywnej klatce, aplikacja pyta o anulowanie,
dodanie kolejnego lub zastąpienie wskazanego składu. Przy kilku składach wybierz
konkretny z listy. Zastąpienie zachowuje identyfikatory, połączenia, ręcznie
zmienione numery i podpisy; ustawia pozycje, kolory i średnicę według panelu.
Niepełny skład zostaje uzupełniony o brakujące role. Blokady zawodników
lub powiązanych obiektów mogą zatrzymać zmianę bez częściowej operacji.

W edycji zawodnika sekcja Skład zespołu zawiera Zmień formację tego składu.
Przypisanie jest zapisane w obiekcie jako `squad` z polami `id`, `team`,
`role`, `formation`, `half`. Rola jest stałą tożsamością, niezależną od pola
`number` i koloru. Starsi zawodnicy nie otrzymują tego przypisania automatycznie.
Klatki zachowują identyfikatory; wklejenie tworzy nowe identyfikatory zawodników
i składów oraz przepisuje kopiowane połączenia. Dodanie i zmiana formacji
dotyczą wyłącznie aktywnej klatki.

Testy: `node work/check-teams.js` oraz `python3 work/check-teams-json.py`.
Raport, zrzuty i rzeczywiste eksporty są w `work/teams-qa/`.
