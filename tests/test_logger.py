import pytest
from src.logger import setup_logger

def test_setup_logger(tmp_path):
    log_file = tmp_path / "test.log"
    logger = setup_logger(str(log_file))
    logger.info("Teste de log")
    with open(log_file, 'r') as f:
        assert "Teste de log" in f.read()