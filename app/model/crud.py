import sqlite3


def insert_search(currency_abbreviation: str):
    try:
        conn = sqlite3.connect('../identifier.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cotacao (CURRENCY_ABBREVIATION) VALUES (?)", currency_abbreviation)
        conn.commit()
    except sqlite3.Error as err:
        raise "ERRO"


def insert_convert(acronym_quoted_currency: str, base_currency_acronym: str, final_value: float, value_convert: float):
    try:
        conn = sqlite3.connect('../identifier.sqlite')
        cusor = conn.cursor()
        cusor.execute(
            "INSERT INTO convert_simple (acronym_quoted_currency, base_currency_acronym, value_final, initial_value)"
            " VALUES (?,?,?,?)", acronym_quoted_currency, base_currency_acronym, final_value, value_convert)
        conn.commit()
    except sqlite3.Error as err:
        raise 'ERRO'


def multiple_convert(currency_one: str, currence_two: str, currence_three: str, base_currency_acronym: str,
                     final_value_one: float, final_value_two: float, final_value_three: float, value_convert: float):
    try:
        conn = sqlite3.connect('../identifier.sqlite')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO multiple_convert(currency_one, currency_two, currency_three, base_currency, final_value_one, final_value_two, final_value_three, value_convert) VALUES (?,?,?,?,?,?,?,?,?)",
            currency_one, currence_two, currence_three, base_currency_acronym, final_value_one, final_value_two,
            final_value_three, value_convert
        )
    except sqlite3.Error as err:
        raise 'ERRO'


def history_coin(currency: str):
    try:
        conn = sqlite3.connect('../identifier.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cotacao (CURRENCY_ABBREVIATION) VALUES (?)", currency)
        conn.commit()
    except sqlite3.Error as err:
        raise "ERRO"


def select(table: str):
    try:
        conn = sqlite3.connect('../identifier.sqlite')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        conn.commit()
    except sqlite3.Error as err:
        raise "ERRO"
