import eyed3
from eyed3 import AudioFile
import requests
from pathlib import Path


def meta_data(path: str, parameters: dict) -> None:
    audio_file: AudioFile = eyed3.load(path)
    response = requests.get(parameters['Album Art'])

    if parameters['Title']:
        audio_file.tag.title = parameters['Title']
    if parameters.get('Artist'):
        audio_file.tag.artist = str(parameters['Artist'])
    if parameters['Album']:
        audio_file.tag.album = parameters['Album']
    if parameters['Track Number']:
        audio_file.tag.track_num = parameters['Track Number']
    if parameters['Album Art']:
        audio_file.tag.images.set(3, response.content, 'image/jpeg')

    audio_file.tag.save()


def bulk_update_album_art(image_link: str):
    path = input('Enter a File Path: ')
    for mp3_file in Path(path).iterdir():
        if mp3_file.suffix == '.mp3':
            response = requests.get(image_link)
            audio_file = eyed3.load(mp3_file)
            audio_file.tag.images.set(3, response.content, 'image/jpeg')
            audio_file.tag.save()


file_path = Path('/Users/tyrone/Documents/Music/Corbin - Early Quiet (MOURN 2016).mp3')

if __name__ == '__main__':
    pass
