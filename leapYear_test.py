import pytest
import leapYear
import io

def test_leapYear(capsys, monkeypatch):
    assert True == leapYear.isLeapYear(2024), "2024 ist ein Schaltjahr"
    assert True == leapYear.isLeapYear(2000), "2000 ist ein Schaltjahr"
    assert False == leapYear.isLeapYear(2100), "2100 ist KEIN Schaltjahr"
    assert False == leapYear.isLeapYear(2025), "2025 ist KEIN Schaltjahr"
