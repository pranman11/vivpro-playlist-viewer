import json
from django.core.management.base import BaseCommand, CommandError
from ...models import Song

class Command(BaseCommand):
    help = 'Imports songs from a JSON file and save them to the database using a single bulk insert query'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file to be imported')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r') as file:
                data = json.load(file)

            # Get the number of songs from one of the maps
            num_songs = len(data['id'])

            # List to hold all the Song instances
            songs_to_create = []

            for i in range(num_songs):
                
                song = Song(
                    id=data['id'][str(i)],
                    title=data['title'][str(i)],
                    danceability=data['danceability'][str(i)],
                    energy=data['energy'][str(i)],
                    key=data['key'][str(i)],
                    loudness=data['loudness'][str(i)],
                    mode=data['mode'][str(i)],
                    acousticness=data['acousticness'][str(i)],
                    instrumentalness=data['instrumentalness'][str(i)],
                    liveness=data['liveness'][str(i)],
                    valence=data['valence'][str(i)],
                    tempo=data['tempo'][str(i)],
                    duration_ms=data['duration_ms'][str(i)],
                    time_signature=data['time_signature'][str(i)],
                    num_bars=data['num_bars'][str(i)],
                    num_sections=data['num_sections'][str(i)],
                    num_segments=data['num_segments'][str(i)],
                    song_class=data['class'][str(i)],
                )

                # Add the song instance to the list
                songs_to_create.append(song)

            # Bulk create all the song instances
            Song.objects.bulk_create(songs_to_create)

            self.stdout.write(self.style.SUCCESS(f"{num_songs} songs imported successfully"))

        except FileNotFoundError:
            raise CommandError(f"File {json_file} does not exist")
        except json.JSONDecodeError:
            raise CommandError("Invalid JSON format in file")
