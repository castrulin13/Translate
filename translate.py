from googletrans import Translator

what = input("Переклад з: ")
what2 = input("Переклад на: ")
what3 = input("Текст: ")

translator = Translator()
translated = translator.translate(what3,src=what, dest=str(what2))

print(translated.text)