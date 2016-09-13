# coding=utf-8
import json
from django.core.management import BaseCommand
from search.models import Presentation


class Command(BaseCommand):
    help = 'import_json reads provided json file and will import it to database'

    def handle(self, *args, **options):
        with open('prezis.json') as json_file:
            presentations = json.load(json_file)

            for presentation in presentations:
                self.add_record(presentation)

    def add_record(self, record):
        if record:
            presentation = Presentation(
                custom_id=record.get('id', ''),
                title=record.get('title', ''),
                thumbnail=record.get('thumbnail', ''),
                creator_name=record.get('creator', {}).get('name', ''),
                creator_profile_url=record.get('creator', {}).get('profileUrl', ''),
            )
            presentation.save()
