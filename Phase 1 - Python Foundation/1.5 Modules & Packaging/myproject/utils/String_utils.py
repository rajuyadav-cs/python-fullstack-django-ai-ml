# utils/String_utils.py


class StringUtils:

    def uppercase(self, text):

        return text.upper()

    def lowercase(self, text):

        return text.lower()

    def reverse(self, text):

        return text[::-1]

    def count_characters(self, text):

        return len(text)

    def count_words(self, text):

        return len(text.split())

    def is_palindrome(self, text):

        cleaned = text.lower()

        return cleaned == cleaned[::-1]

    def remove_spaces(self, text):

        return text.replace(" ", "")