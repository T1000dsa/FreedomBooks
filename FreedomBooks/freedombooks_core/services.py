import FreedomBooks.settings as sett
import os
from charset_normalizer import detect
class TextLoad:
      def __init__(self, data):
          self.data = data

      def push_text(self):
        adress = os.path.join(sett.MEDIA_ROOT, str(self.data.text_hook.file))
        text_view = 'No text'
        encod = 'utf-8'

        with open(adress, 'rb') as file:
            detector = detect(file.read())

        encod = detector['encoding']
        with open(adress, encoding=encod) as file:
            text_view = file.read()

        return text_view