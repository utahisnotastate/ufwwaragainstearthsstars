import io
import sys

from fdastro.cli import main


def test_isos_command(capsys):
    assert main(["isos"]) == 0
    out = capsys.readouterr().out
    assert "3I/ATLAS" in out and "1I/2017 U1" in out


def test_tisserand_command(capsys):
    assert main(["tisserand", "--a", "5.2026", "--e", "0", "--i", "0"]) == 0
    assert "3.0000" in capsys.readouterr().out
    assert main(["tisserand", "--examples"]) == 0
    assert "2015 BZ509" in capsys.readouterr().out


def test_tisserand_missing_args():
    assert main(["tisserand"]) == 2


def test_cli_survives_legacy_windows_encoding(monkeypatch):
    # GitHub's Windows runners (and redirected output on Windows) use cp1252,
    # which cannot encode the ʻokina in "Kaʻepaokaʻawela".
    buffer = io.BytesIO()
    legacy = io.TextIOWrapper(buffer, encoding="cp1252")
    monkeypatch.setattr(sys, "stdout", legacy)
    assert main(["tisserand", "--examples"]) == 0
    legacy.flush()
    assert b"2015 BZ509" in buffer.getvalue()
