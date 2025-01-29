# MBO Cinema Website
Een gebruiksvriendelijke website waar gebruikers films kunnen bekijken en tickets kunnen reserveren!

## 📌 Inhoudsopgave  
1.🔥 [Over dit project](#over-dit-project)  
2.📁 [Projectstructuur](#projectstructuur)  
3.⚙️ [Installatie](#installatie)  
4.🎟️ [Gebruik](#gebruik)  
5.🤝 [Contributie](#contributie)  
6.📜 [Licentie](#licentie)

---

## Over dit project
Dit is een bioscoopwebsite gebouwd met Django. Gebruikers kunnen films bekijken, reserveringen maken en hun account beheren.

---

## Projectstructuur
Hier is een overzicht van de mappen en bestanden:

```plaintext
├── ./
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── main.py
│   ├── manage.py
│   ├── accounts/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   ├── cinema_Project_3/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── __init__.py
│   ├── films/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   ├── reserveringen/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_event_id.py
│   │   │   ├── __init__.py
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css
│   │   │   ├── componenten/
│   │   │   │   ├── buttons.css
│   │   │   │   ├── cards.css
│   │   │   │   ├── form.css
│   │   │   │   ├── marquee.css
│   │   ├── layout/
│   │   │   ├── footer.css
│   │   │   ├── header.css
│   │   │   ├── modal.css
│   │   │   ├── navbar.css
│   │   ├── page_componenten/
│   │   │   ├── film_detail.css
│   │   │   ├── film_list.css
│   │   │   ├── medewerkers_dashboard.css
│   │   ├── js/
│   │   │   ├── marquee.js
│   │   │   ├── medewerkers_actions.js
│   │   │   ├── navbar_sidebar.js
│   │   │   ├── user_actions.js
```

---

## Installatie
Volg deze stappen om het project lokaal te draaien:

1. Clone de repository:
   ```sh
   git clone https://github.com/jouw-gebruikersnaam/mbo-cinema.git
   ```
2. Ga naar de projectmap:
   ```sh
   cd mbo-cinema
   ```
3. Installeer de vereiste pakketten:
   ```sh
   pip install -r requirements.txt
   ```
4. Voer migraties uit:
   ```sh
   python manage.py migrate
   ```
5. Start de server:
   ```sh
   python manage.py runserver
   ```

---

## Gebruik
1. Open een browser en ga naar `http://127.0.0.1:8000/`
2. Registreer of log in om reserveringen te maken
3. Bekijk en filter beschikbare films

---

## Contributie
Wil je bijdragen? Volg deze richtlijnen:
- Fork de repository
- Maak een feature branch: `git checkout -b feature/nieuwe-feature`
- Commit je wijzigingen: `git commit -m 'Voeg nieuwe feature toe'`
- Push naar GitHub en maak een pull request

---

## Licentie
Dit project valt onder de MIT-licentie.

---

## Gebruikte talen en frameworks
✅ **Python**  
✅ **HTML5**  
✅ **JavaScript**  
✅ **CSS**  
✅ **Django**  

---
