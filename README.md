# DariusBot (Asistent inteligent și de moderare pentru Discord)

Un bot de Discord complet scris în Python, care integrează inteligența artificială DeepSeek pentru conversații directe, analiză și generare de imagini, alături de comenzi utile pentru vreme, utilități de profil și unelte de moderare pentru server.

## Tehnologii Folosite

* **Limbaj:** Python
* **Librărie principală:** Discord.py
* **Integrare AI (text):** DeepSeek API (modelul `deepseek-chat`)
* **Integrare AI (vedere/analiză poze):** DeepSeek API (modelul experimental `deepseek-v4-flash-vision-exp`)
* **Generare de imagini:** Pollinations.ai
* **Utilitare:** Requests, Python-Dotenv
* **Controlul versiunilor:** Git și GitHub

## Comenzi Disponibile

* `!ask` (sau `!deepseek`) `[întrebare]` - Discută cu AI-ul DeepSeek (memorează contextul conversației tale).
* `!ask reset` - Resetează memoria discuției cu AI-ul.
* `!look` - Atașează o imagine și botul o analizează/descrie folosind AI-ul cu vedere.
* `!imagine` (sau `!draw`, `!genereaza`) `[descriere]` - Generează o imagine pe baza descrierii tale (funcționează cel mai bine cu prompturi în engleză).
* `!credits` - Afișează panoul informativ despre bot.
* `!vremea [oraș]` - Verifică starea vremii în timp real.
* `!avatar [@utilizator]` - Arată poza de profil a unui membru.
* `!userinfo [@utilizator]` - Afișează detalii despre un membru al serverului.
* `!clear [număr]` - Șterge în masă mesaje din canal (necesită permisiuni).
* `!kick` / `!ban [@utilizator] [motiv]` - Unelte de moderare pentru server.

## Cum îl Rulezi Local

Urmează pașii de mai jos pentru a rula botul pe calculatorul tău:

1. **Clonează repository-ul:**
