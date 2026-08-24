import importlib
import sys


def test_import_python_ait_ml(monkeypatch, tmp_path):
    monkeypatch.setenv("PROJECT_NAME", "python_ait_ml")
    monkeypatch.setenv("LOG_DIR", str(tmp_path))
    monkeypatch.setenv("LOG_NAME", "main.log")
    monkeypatch.setenv("LOG_ROTATE_NAME", "main_rotate.log")
    monkeypatch.setenv("REDIS_URL", "redis://localhost:6379/0")
    monkeypatch.setenv("BUILD_VERSION", "test")

    for module_name in list(sys.modules):
        if module_name == "python_ait_ml" or module_name.startswith("python_ait_ml."):
            del sys.modules[module_name]

    module = importlib.import_module("python_ait_ml")
    assert module.cli is not None
