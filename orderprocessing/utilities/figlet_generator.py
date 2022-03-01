from pyfiglet import Figlet

INVALID_TEXT = 'Invalid Text Specified'


class FigletGenerator:
    @staticmethod
    def get_text(text):
        if text is None:
            raise Exception(INVALID_TEXT)

        figlet = Figlet(font='Standard')
        processedText = figlet.renderText(text)

        return processedText
