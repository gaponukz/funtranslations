import requests
from dict2object.dict2object import Object

class FunTranslationError(Exception):
    ''' Base API error exception '''
    def __init__(self, message):
        super().__init__(message)

class FunTranslation:
    def __init__(self, language: str):
        self.language = language

        self.__base_url = "https://api.funtranslations.com/translate/"
        self.__text_param = ".json?text="

    def translate(self, message: str) -> str:
        url = f"{self.__base_url}{self.language}{self.__text_param}{message}"
        response: Object = self.__get_response(url)

        if "success" in response.keys():
            return response.contents.translated

        else:
            raise FunTranslationError(response.error.message)

    def __get_response(self, url: str) -> Object:
        response: requests.Response = requests.get(url)

        return Object.load(response.text)