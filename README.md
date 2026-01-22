# Nowatorski Projekt Indywidualny - DevOps

**Autor:** Katarzyna Lisiecka
**Nr indeksu:** 54163  
**Kierunek:** Informatyka - Inzynier Aplikacji i Systemów Chmurowych

---

## 1. Opis projektu

Celem projektu było stworzenie środowiska Continuous Integration / Continuous Deployment (CI/CD) dla aplikacji webowej opartej na mikroserwisach.
Aplikacja składa się z:

- **Backend:** Python (FastAPI)
- **Baza danych:** PostgreSQL
- **Konteneryzacja:** Docker (Multi-stage build)

Architektura realizuje zasady _12-Factor App_, oddzielając konfigurację od kodu i wykorzystując konteneryzację do zapewnienia spójności środowisk.

## 2. Instrukcja uruchomienia

### Wymagania

- Docker & Docker Compose
- Git

### Uruchomienie lokalne

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/keepitfoxy/devops-training-project
   cd devops-training-project
   ```

2. Utwórz plik .env (opcjonalnie, domyślne wartości są w docker-compose):

   ```bash
   APP_VERSION=v1.0-local
   ```

3. Uruchom środowisko:

   ```bash
   docker compose up --build
   ```

4. Aplikacja dostępna jest pod adresem: http://localhost:8000

- Dokumentacja API (Swagger): http://localhost:8000/docs

## 3. Opis Pipeline CI/CD

Projekt wykorzystuje GitHub Actions do automatyzacji procesów.

### Workflow: Pull Request Check

Uruchamiany przy każdym Pull Requeście do gałęzi main.

- **Linting:** Sprawdza jakość kodu przy użyciu ruff.

- **Testy:** Uruchamia testy jednostkowe pytest.

### Workflow: Build and Publish

Uruchamiany po zaakceptowaniu zmian (merge) do main.

1. Ponowne sprawdzenie jakości (testy).

2. Zbudowanie obrazu Docker (Multi-stage).

3. Publikacja obrazu do GitHub Container Registry (GHCR).

## 4. Uzasadnienie decyzji technicznych

- **Multi-stage build:** Użyto w celu zminimalizowania rozmiaru obrazu produkcyjnego i usunięcia zbędnych zależności kompilacji.

- **GitHub Container Registry:** Wybrano ze względu na natywną integrację z GitHub Actions i bezpieczeństwo.

- **FastAPI:** Wybrano ze względu na wysoką wydajność i asynchroniczność, kluczową w środowiskach chmurowych.
