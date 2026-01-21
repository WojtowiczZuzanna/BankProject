# Symulacja banku

Projekt konsolowy w języku Python

- Wielowątkowa obsługa klientów po stronie serwera
- Klienci działają jako niezależne procesy
- Komunikacja klient–serwer oparta na protokole TCP (bez współdzielonej pamięci)
- Synchronizacja dostępu do kont za pomocą locków

Instrukcja:
1. python server.py
2. w osobnym terminalu: python client.py
3. terminali z klientami może być więcej, wtedy w kolejnym terminalu: python client.py
4. sprawdź/porównaj wykonane operacje dla klientów


Działanie programu krok po kroku:

1. Uruchomienie pliku server.py:
	- tworzenie obiektu Bank
	- inicjalizacja kilku kont (ID, saldo początkowe, lock)
	- otwarcie socket TCP na porcie 5000 i adresie 127.0.0.1
	- serwer przechodzi w tryb nasłuchiwania

2. Uruchomienie client.py, który:
	- tworzy swój proces
	- otwiera socket TCP
	- łączy się z serverem banku
Może byc kilku aktywnych klientów, gdzie każdy działa w osobnym procesie.

3. Server odbiera połączenie klienta:
	- tworzy nowy wątek, który obsługugje tylko z tym klientem
Wielu klientów może byc obsługiwanych równolegle.

4. Klient wybiera konto źródłowe, docelowe oraz kwotę przelewu (tutaj losowo, aby symulacja przebiegała sprawnie), po czym wysyła komunikat do serwera i oczekuje odpowiedzi.
Komunikacja sieciowa przez TCP.

5. Serwer odbiera komunikat od klienta:
	- blokuje konta (lock)
	- sprawdza dostępność środków
	- wykonuje przelew lub go odrzuca
	- odsyła odpowiedź "OK" lub "FAILED"

6. Serwer zwraca aktualne salda kont.

7. Klient kończy wysyłanie operacji, zamyka połączenie TCP.
Serwer kończy wątek obsługi tego klienta, ale nadal działa i czeka na kolejnych klientów.


Wielu klientów może wysyłać przelewy w tym samym czasie.
Serwer może obsługiwać klientów w wielu wątkach.
Pobieranie locków w stałej kolejności ID zapobiega deadlockom.

Aspekty techniczne implementacji: 
- Model klient-serwer
- Gniazda(sockety) TCP
- Wielowątkowość
- Ryglowanie za pomocą threading.Lock
- Brak współdzielonej pamięci pomiędzy procesami


