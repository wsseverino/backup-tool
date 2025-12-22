import pytest
import os
from src.backup import perform_backup
from src.logger import setup_logger

@pytest.fixture
def mock_logger(tmp_path):
    log_file = tmp_path / "test.log"
    return setup_logger(str(log_file))

def test_perform_backup_success(tmp_path, mock_logger):
    source = tmp_path / "source"
    dest = tmp_path / "dest"
    source.mkdir()
    dest.mkdir()
    test_file = source / "test.txt"
    test_file.write_text("Conteúdo")
    
    perform_backup(str(source), str(dest), mock_logger)
    
    # Verifica se pasta versionada foi criada
    versioned_dirs = [d for d in os.listdir(dest) if os.path.isdir(os.path.join(dest, d))]
    assert len(versioned_dirs) == 1
    versioned_path = os.path.join(dest, versioned_dirs[0])
    assert os.path.exists(os.path.join(versioned_path, "test.txt"))

def test_perform_backup_failure(mock_logger):
    with pytest.raises(ValueError):
        perform_backup("/diretorio_inexistente", "/dest", mock_logger)