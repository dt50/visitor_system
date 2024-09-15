import re
from typing import Iterable

TRANSTABLE: Iterable = (
    ("'", "'"),
    ('"', '"'),
    ("‘", "'"),
    ("’", "'"),
    ("«", '"'),
    ("»", '"'),
    ("“", '"'),
    ("”", '"'),
    ("–", "-"),  # en dash
    ("—", "-"),  # em dash
    ("‒", "-"),  # figure dash
    ("−", "-"),  # minus
    ("…", "..."),
    ("№", "#"),
    # UPPER
    # three-symbols replacements
    ("Щ", "Sch"),
    # on russian->english translation only first replacement will be done
    # i.e. Sch
    # but on english->russian translation both variants (Sch and SCH) will play
    ("Щ", "SCH"),
    # two-symbol replacements
    ("Ё", "Yo"),
    ("Ё", "YO"),
    ("Ж", "Zh"),
    ("Ж", "ZH"),
    ("Ц", "Ts"),
    ("Ц", "TS"),
    ("Ч", "Ch"),
    ("Ч", "CH"),
    ("Ш", "Sh"),
    ("Ш", "SH"),
    ("Ю", "YU"),
    ("Ю", "Yu"),
    ("Я", "Ya"),
    ("Я", "YA"),
    # one-symbol replacements
    ("А", "A"),
    ("Б", "B"),
    ("В", "V"),
    ("Г", "G"),
    ("Д", "D"),
    ("Е", "E"),
    ("З", "Z"),
    ("И", "I"),
    ("Й", "J"),
    ("К", "K"),
    ("Л", "L"),
    ("М", "M"),
    ("Н", "N"),
    ("О", "O"),
    ("П", "P"),
    ("Р", "R"),
    ("С", "S"),
    ("Т", "T"),
    ("У", "U"),
    ("Ф", "F"),
    ("Х", "H"),
    ("Э", "E"),
    ("Ъ", "`"),
    ("Ь", "'"),
    ("Ы", "Y"),
    # LOWER
    # three-symbols replacements
    ("щ", "sch"),
    # two-symbols replacements
    ("ё", "yo"),
    ("ж", "zh"),
    ("ц", "ts"),
    ("ч", "ch"),
    ("ш", "sh"),
    ("ю", "yu"),
    ("я", "ya"),
    # one-symbol replacements
    ("а", "a"),
    ("б", "b"),
    ("в", "v"),
    ("г", "g"),
    ("д", "d"),
    ("е", "e"),
    ("з", "z"),
    ("и", "i"),
    ("й", "j"),
    ("к", "k"),
    ("л", "l"),
    ("м", "m"),
    ("н", "n"),
    ("о", "o"),
    ("п", "p"),
    ("р", "r"),
    ("с", "s"),
    ("т", "t"),
    ("у", "u"),
    ("ф", "f"),
    ("х", "h"),
    ("э", "e"),
    ("ъ", "`"),
    ("ь", "'"),
    ("ы", "y"),
    # Make english alphabet full: append english-english pairs
    # for symbols which is not used in russian-english
    # translations. Used in slugify.
    ("c", "c"),
    ("q", "q"),
    ("y", "y"),
    ("x", "x"),
    ("w", "w"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("0", "0"),
)  #: Translation table

RU_ALPHABET = [x[0] for x in TRANSTABLE]  #: Russian alphabet that we can translate
EN_ALPHABET = [
    x[1] for x in TRANSTABLE
]  #: English alphabet that we can detransliterate
ALPHABET = RU_ALPHABET + EN_ALPHABET  #: Alphabet that we can (de)transliterate


def translify(in_string, strict=True):
    """
    Translify russian text

    @param in_string: input string
    @type in_string: C{str}

    @param strict: raise error if transliteration is incomplete.
        (True by default)
    @type strict: C{bool}

    @return: transliterated string
    @rtype: C{str}

    @raise ValueError: when string doesn't transliterate completely.
        Raised only if strict=True
    """
    translit = in_string
    for symb_in, symb_out in TRANSTABLE:
        translit = translit.replace(symb_in, symb_out)

    if strict and any(ord(symbol) > 128 for symbol in translit):
        raise ValueError(
            "Unicode string doesn't transliterate completely, is it russian?"
        ) from None

    return translit


def detranslify(in_string):
    """
    Detranslify

    @param in_string: input string
    @type in_string: C{basestring}

    @return: detransliterated string
    @rtype: C{str}

    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    try:
        russian = str(in_string)
    except UnicodeDecodeError:
        raise ValueError(
            "We expects if in_string is 8-bit string, then it consists only ASCII chars, but now it doesn't. "
            "Use unicode in this case."
        ) from None

    for symbol_out, symbol_in in TRANSTABLE:
        russian = russian.replace(symbol_in, symbol_out)

    return russian


def slugify(in_string):
    """
    Prepare string for slug (i.e. URL or file/dir name)

    @param in_string: input string
    @type in_string: C{basestring}

    @return: slug-string
    @rtype: C{str}

    @raise ValueError: if in_string is C{str}, but it isn't ascii
    """
    try:
        u_in_string = str(in_string).lower()
    except UnicodeDecodeError:
        raise ValueError(
            "We expects when in_string is str type,"
            + "it is an ascii, but now it isn't. Use unicode "
            + "in this case."
        ) from None

    # convert & to "and"
    u_in_string = re.sub(r"\&amp\;|\&", " and ", u_in_string)

    # replace spaces by hyphen
    u_in_string = re.sub(r"[-\s]+", "-", u_in_string)

    # remove symbols that not in alphabet
    u_in_string = "".join([symbol for symbol in u_in_string if symbol in ALPHABET])

    # translify it
    out_string = translify(u_in_string)

    # remove non-alpha
    return re.sub(r"[^\w\s-]", "", out_string).strip().lower()


def dirify(in_string):
    """
    Alias for L{slugify}
    """
    slugify(in_string)
