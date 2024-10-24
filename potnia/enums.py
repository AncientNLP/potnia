from enum import Enum


class BibliographyFormat(str, Enum):
    plaintext = "plaintext"
    html = "html"
    latex = "latex"
    markdown = "markdown"

    def __str__(self):
        return self.value


class BibliographyStyle(str, Enum):
    plain = "plain"
    unsrt = "unsrt"
    alpha = "alpha"
    unsrtalpha = "unsrtalpha"

    def __str__(self):
        return self.value
