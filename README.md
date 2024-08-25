# Playlist Viewer

This Django project provides APIs to manage music playlists, allowing you to bulk upload songs using JSON files, retrieve all songs,retrieve a song by title and rating a song. It also includes basic tests to ensure functionality.

## Project Features

- **Bulk Upload Songs:** Import songs from a JSON file into the database using a single query.
- **List All Songs (with Pagination):** Retrieve a paginated list of all songs.
- **Retrieve a Song by Title:** Fetch details of a song given its title.
- **Admin Interface:** Manage songs via the Django admin interface.
- **Automated Tests:** Test API endpoints and functionality.

## Installation Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pranman11/vivpro-playlist-viewer.git
   cd vivpro-playlist-viewer

2. **Set-up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the Requirements**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py makemigrations songs
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```bash
   python manage.py createsuperuser
   ```
   On running the above command, you should be prompted to enter details of the user (dummy details can be entered). This user can be used to access the admin portal from http://localhost:8000/admin and further, can be used to test the rating API mentioned below.

6. **Load Initial Data using the upload JSON feature:**

   This has been achieved using a management command "import_songs" which can be run as below:

   ```bash
   python manage.py import_songs <path_to_json_file>
   ```

## Running the Application

1. **Start the Development Server:**

   ```bash
   python manage.py runserver
   ```

2. **Access the API Endpoints:**

   Django provides an interface to interact with it's APIs. Each API endpoint can be accessed using the URL mentioned.

- **List All Songs (with Pagination):**

  - **URL:** `http://localhost:8000/songs/`
  - **Method:** `GET`
  - **Query Parameters:**
    - `page` (optional): Page number for pagination.
    - `page_size` (optional): Number of items per page.
  - **Response Example:**

    ```json
    {
        "count": 100,
        "next": "http://localhost:8000/api/songs/?page=2",
        "previous": null,
        "results": [
            {
                "id": "5vYA1mW9g2Coh1HUFUSmlb",
                "title": "3AM",
                "danceability": 0.5,
                ...
            }
        ]
    }
    ```

- **Retrieve a Song by Title:**

  - **URL:** `http://localhost:8000/songs/by-title/`
  - **Method:** `GET`
  - **Query Parameters:**
    - `title`: Title of the song to retrieve.
  - **Response Example:**

    ```json
    {
        "id": "5vYA1mW9g2Coh1HUFUSmlb",
        "title": "3AM",
        "danceability": 0.5,
        ...
    }
    ```

- **Rate a Song (user login required):**
   Django's inbuilt User model is used as a base model to create a relation between user rating and song. Therefore, easiest way to access this API would be to log into the admin portal using user details.

  - **URL:** `http://localhost:8000/rate/`
  - **Method:** `POST`
  - **Payload:**
    ```json
    {
        "song": <song_id>,
        "rating": "<rating_1/2/3/4/5>"
    }

## Testing API

1. **Run Unit Tests:**

   ```bash
   python manage.py test songs
   ```

   This command will discover and run the tests for the songs application in the project.
