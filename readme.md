## Kom igång
#### Skapa din venv:
>python -m venv venv

>.\venv\Scripts\activate

#### Installera biblioteken
>pip install -r requirements.txt

>Sedan: `pip install -r requirements.txt`

#### Starta applicationen
>Kör `py.exe .\run.py`, se till så att du kör från övermappen dvs i samma mapp som `run.py` finns i.


## Service architecture

[Database] ←→ [Backend Service] ←→ [Frontend]

Applikationen består av en databas (SQLite), en backend-tjänst (Flask) och en frontend (HTML i templates/index.html). Backend hanterar lösenord genom både hashing och kryptering samt visar varningar efter en viss tid.

## Lösenordshantering webbapplikationen

Min app description:

- Användaren anger en tjänst (t.ex. Steam) och ett tillhörande lösenord.

- Lösenordet lagras i databasen som en hash för säkerhet.

- En enkel krypterings- och dekrypteringsmetod används vid sidan om för att tillfälligt kunna visa lösenordet i klartext.

- Efter en förutbestämd tid (t.ex. 10 sekunder) varnas användaren om vilka lösenord som bör bytas ut om man klickar på visa lösenord att uppdatera.




