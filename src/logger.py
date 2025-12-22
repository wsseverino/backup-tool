import logging
import os

def setup_logger(log_file='backup.log'):
    """
    Configura o logger para registrar operações em um arquivo.

    :param log_file: Caminho do arquivo de log.
    :return: Objeto logger configurado.
    """
    logger = logging.getLogger('backup_tool')
    logger.setLevel(logging.INFO)
    
    # Handler para arquivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Formato do log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    return logger