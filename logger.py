import logging

basic_logger = logging.getLogger("basic")
basic_logger.setLevel("DEBUG")
basic_formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s %(pathname)s >> %(funcName)s")

basic_stream_handler = logging.StreamHandler()
basic_logger.addHandler(basic_stream_handler)
basic_stream_handler.setFormatter(basic_formatter)

basic_file_handler = logging.FileHandler("logs/basic.txt")
basic_logger.addHandler(basic_file_handler)
basic_file_handler.setFormatter(basic_formatter)

basic_file_handler_errors = logging.FileHandler("logs/errors.txt")
basic_file_handler_errors.setLevel("ERROR")
basic_logger.addHandler(basic_file_handler_errors)
basic_file_handler_errors.setFormatter(basic_formatter)


sql_logger = logging.getLogger("sql")
sql_logger.setLevel("DEBUG")
sql_formatter = logging.Formatter("%(levelname)s %(asctime)s : %(message)s %(pathname)s >> %(funcName)s")

sql_stream_handler = logging.StreamHandler()
sql_logger.addHandler(sql_stream_handler)
sql_stream_handler.setFormatter(sql_formatter)

sql_file_handler = logging.FileHandler("logs/sql.txt")
sql_logger.addHandler(sql_file_handler)
sql_file_handler.setFormatter(sql_formatter)
