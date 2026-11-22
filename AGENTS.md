# Praca nad Tablicą taktyczną

Pisz do użytkownika naturalnie i po polsku. Zachowuj istniejące funkcje oraz zgodność ze starszymi projektami.

Źródła są w dist/index.html, dist/style.css i dist/app.js. Aplikacja nie wymaga frameworka ani zewnętrznych bibliotek. Nie zamieniaj całej aplikacji na nową implementację przy drobnej poprawce. Nie edytuj wygenerowanego build/Tablica_taktyczna.html.

Uruchomienie: python3 scripts/serve.py. Pakowanie: python3 scripts/build.py. Kontrola składni: node --check dist/app.js. Nie twierdź, że sprawdzono interfejs lub rzeczywisty eksport MP4, jeśli wykonano tylko kontrolę kodu.

Dane projektów są w localStorage. Nigdy nie czyść ich podczas prac. Zachowuj migracje i stałe identyfikatory obiektów. Nowe właściwości muszą działać w historii, klatkach, kopiowaniu, JSON i rendererach SVG/Canvas. Zmiany renderowania sprawdzaj także pod kątem PNG i MP4.

Kamera ma osobny obrót boiska i format kadru. Po zatwierdzeniu kadr jest zablokowany. Podpisy zawodników pozostają niezależne. Narzutki są usunięte. Tekst wewnątrz kapsla jest centrowany na podstawie rzeczywistych granic znaków.

Nie publikuj strony ani nie wysyłaj kodu do zewnętrznego repozytorium bez wyraźnego polecenia użytkownika.
