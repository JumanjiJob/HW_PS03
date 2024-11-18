import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_englesh_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        translator = Translator()

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        rus_words = translator.translate(english_words, dest="ru")
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        rus_defenition = translator.translate(word_definition, dest="ru")

        return {
          "rus_words": rus_words.text,
          "rus_defenition": rus_defenition.text
        }
    except:
        print("Error")

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_englesh_words()
        word = word_dict.get("rus_words")
        word_defenition = word_dict.get("rus_defenition")

        print(f"Значение слова - {word_defenition}")
        user = input("Что это за слово?")

        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру! ")
            break

word_game()


