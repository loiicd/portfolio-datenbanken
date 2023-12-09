# Requirements

Inhalt:
1. [Aufgabe](#aufgabe)
2. [Bearbeitungszeitraum](#bearbeitungszeitraum)
3. [Abgabe](#abgabe)
4. [Präsentation](#präsentation)

## Aufgabe

Verschiedene lokale Unternehmen sind an Euch herangetreten, und brauchen Hilfe bei der folgenden Fragestellung:

"wie können wir Yelp-Reviews nutzen, um unser Unternehmen zu unterstützen/fördern".

Die Unternehmen möchten 

1. eine einfache Quelle (WebAPI mit PUT und GET Endpoints) haben, um Reviews über ihr eigenes Unternehmen abzufragen, (d.h. Ihr seid Service-Provider, die Unternehmen wollen keine lokalen Datenbanken installieren, sondern nur auf ein Web-API zugreifen) und 
2. zusätzlich auch noch aktiv benachrichtig werden, wenn eine bestimmte Prozentzahl der letzten n Reviews unter einer bestimmte Schwelle (z.B. unter 2 von 5 Sternen) ist.
Eure Aufgabe ist es mit Hilfe der bekannten Yelp-Daten (Yelp academic dataset), ein entsprechendes System aufzubauen, das die oben genannten Anforderungen erfüllt.

abzugeben sind:

- eine funktionierende Implementation des Systems (bei der Präsentation bitte vorführen)
- in der Ausarbeitung: 
1. eine Erläuterung derAnnahmen, die Ihr getroffen habt
2. die Designentscheidungen, die Ihr gemacht habt, inkl einer Analyse der Möglichkeiten, die Ihr in Betracht gezogen habt, und eine Begründung für/gegen bestimmte Technologien und Umsetzungansätze.
3. Betriebswirtschaftliche Auswertung: idealerweise ein paar "real world" performance-tests um herauszufinden, wie schnell das Ganze im Echtbetrieb laufen würde (welche Anforderungen werden wie erfüllt), und was man machen könnte, um das Ganze ggf schneller zu machen (anderes DB-Design, Indexing, Caching, etc). Außerdem: wie viel Speicherplatz wird benötigt, mit wie vielen Anfragen rechnet Ihr, ist das System schnell/performant genug, was kostet das wenn man es in der Cloud hostet, kann man die Daten anders aufbereiten um Zeit und Geld zu sparen etc.
4. eine Darstellung, wie Ihr die Daten ins System bekommt, frisch haltet etc.
5. bitte auf mySQL, MongoDB und Redis beschränken (und Tools wie FastAPI)
6. Da Ihr die Daten besser kennt als die durchschnittlichen Unternehmen, dürft Ihr auch gerne Vorschläge machen, wie die Unternehmen die Yelp-Daten auch anders nutzen könnten. Ihr könnt, wo es Sinn macht, auch andere Datenquellen hinzufügen
7. Es gibt keine Mindestseitenzahl, sondern bitte so wenig wie möglich, so viel wie nötig. Bilder sind immer gut!

## Bearbeitungszeitraum

08.12.2023 09:00 Uhr - 15.12.2023 06:95 Uhr

## Abgabe

15.12.2023 von 07:00 - 09:00 Uhr

## Präsentation

Am 15.12.2023 Vormittags ab 09:00 Uhr

Termine und Zeitslots für die Präsentation stelle ich ein, sobald ich von EINER Person (Kurssprecher) die Liste der Gruppen (mit Namen und Martrikelnummern bitte) bekommen habe.

Die Präsentation wird am Freitag den 15.12 stattfinden. Sie besteht aus einer LIVE-Demo Eures Systems und ein Übersicht über die Highlights der Ausarbeitung, gefolgt von Fragen. Bitte eine Kamera haben, damit wir uns sehen können.