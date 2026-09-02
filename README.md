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

git clone https://github.com/dariuschis08/discord-bot-python.git
cd discord-bot-python


2. **Creează și activează un mediu virtual:**

python -m venv venv
venv\Scripts\activate


3. **Instalează dependențele:**

pip install discord.py python-dotenv requests openai


4. **Configurează variabilele de mediu:**
   Creează un fișier `.env` în directorul rădăcină și adaugă cheile tale:

DISCORD_TOKEN=tokenul_tau_de_discord
DEEPSEEK_API_KEY=cheia_ta_de_deepseek


5. **Pornește botul:**

python main.py


## Probleme Întâmpinate

**Gestionarea cererilor asincrone pentru AI:** Pentru a preveni blocarea aplicației în timpul apelurilor către API-ul DeepSeek, a fost necesară rularea cererilor în executorul asincron (`run_in_executor`), menținând botul fluid și receptiv pe serverul de Discord.

**Analiza de imagini:** Prima variantă a folosit OCR local (Tesseract + pytesseract) pentru citire de text din poze, ceea ce necesita instalare separată pe fiecare mașină și nu putea descrie conținut vizual, doar text. Am înlocuit-o cu modelul multimodal `deepseek-v4-flash-vision-exp`, care primește imaginea codificată în base64 direct în request și poate descrie orice conținut vizual, nu doar text.

## Ce am Învățat

* Cum să interconectez un API de inteligență artificială (OpenAI/DeepSeek) într-o aplicație bazată pe evenimente (Discord bots).
* Implementarea sistemelor de istoric conversațional per utilizator în memorie.
* Trimiterea și procesarea conținutului multimodal (imagini + text) către un model AI.
* Integrarea unui API extern de generare de imagini (Pollinations.ai).
* Crearea unui set complex de comenzi de utilitate și moderare folosind permisiunile native din discord.py.
