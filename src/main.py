import sys
from logger import setup_logger
from backup import perform_backup

def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <diretorio_origem> <diretorio_destino>")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    logger = setup_logger('backup.log')
    logger.info("Iniciando backup...")
    
    try:
        perform_backup(source_dir, dest_dir, logger)
    except ValueError as ve:
        logger.error(str(ve))
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()