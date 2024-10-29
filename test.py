# import logging

# # Настройка логирования
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)

# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# # Добавление фильтра по имени логгера
# console_handler.addFilter(logging.Filter(name='my_logger'))

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# console_handler.setFormatter(formatter)

# logger.addHandler(console_handler)

# logger.debug("Это сообщение DEBUG")   # Появится
# logger.info("Это сообщение INFO")     # Появится
# logger.warning("Это сообщение WARNING")  # Появится

# import logging

# # Создаем фильтр, который пропускает только записи с уровнем WARNING и выше
# class WarningFilter(logging.Filter):
#     def filter(self, record):
#         return record.levelno >= logging.WARNING

# # Создаем логгер
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # Создаем обработчик для вывода в консоль
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# # Добавляем фильтр к обработчику
# console_handler.addFilter(WarningFilter())

# # Добавляем обработчик к логгеру
# logger.addHandler(console_handler)

# # Выводим сообщения разных уровней
# logger.debug("Это сообщение DEBUG")
# logger.info("Это сообщение INFO")
# logger.warning("Это сообщение WARNING")
# logger.error("Это сообщение ERROR")
# logger.critical("Это сообщение CRITICAL")

import logging

# Создаем фильтр, который пропускает только записи для логгера 'my_module'
class ModuleFilter(logging.Filter):
    def filter(self, record):
        return record.name == 'my_module'

# Создаем логгеры
logger1 = logging.getLogger('my_module')
logger2 = logging.getLogger('another_module')
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)

# Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Добавляем фильтр к обработчику
console_handler.addFilter(ModuleFilter())

# Добавляем обработчик к логгерам
logger1.addHandler(console_handler)
logger2.addHandler(console_handler)

# Выводим сообщения для разных логгеров
logger1.debug("Это сообщение для my_module")
logger2.debug("Это сообщение для another_module")
