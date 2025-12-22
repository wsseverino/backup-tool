import os
import shutil
import datetime

def perform_backup(source_dir, dest_dir, logger):
    """
    Realiza o backup de arquivos de source_dir para dest_dir, com versionamento por timestamp.

    :param source_dir: Diretório de origem.
    :param dest_dir: Diretório de destino base.
    :param logger: Objeto logger para registrar operações.
    :raises ValueError: Se diretórios não existirem.
    """
    if not os.path.exists(source_dir):
        raise ValueError(f"Diretório de origem inexistente: {source_dir}")
    
    # Cria pasta versionada com timestamp (ex.: 20251218_120000)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    versioned_dest = os.path.join(dest_dir, timestamp)
    os.makedirs(versioned_dest, exist_ok=True)
    
    try:
        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            if os.path.isfile(source_file):
                dest_file = os.path.join(versioned_dest, file_name)
                shutil.copy2(source_file, dest_file)
                logger.info(f"Arquivo copiado: {source_file} -> {dest_file}")
        logger.info(f"Backup concluído com sucesso para pasta: {versioned_dest}")
    except Exception as e:
        logger.error(f"Erro durante o backup: {str(e)}")
        raise