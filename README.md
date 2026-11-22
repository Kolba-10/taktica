# Taktica (LINIA)

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

