import pytest

from valid_number import Solution

s = Solution()


def test_sign_behavior():
    assert s.isNumber("+1")
    assert s.isNumber("-1")
    assert s.isNumber("++1") == False
    assert s.isNumber("--1") == False
    assert s.isNumber("+-1") == False
    assert s.isNumber("+-1.391e-99") == False
    assert s.isNumber("++1.391e-99") == False
    assert s.isNumber("-+1.391e-99") == False
    assert s.isNumber("--1.391e-99") == False
    assert s.isNumber("+1.391e-+99") == False
    assert s.isNumber("+1.391e--99") == False
    assert s.isNumber("+1.391e++99") == False
    assert s.isNumber("+1.391e+-99") == False


def test_decimals():
    assert s.isNumber("1.1")
    assert s.isNumber(".1")
    assert s.isNumber("1.")
    assert s.isNumber(".") == False


def test_complex():
    assert s.isNumber("1e99")
    assert s.isNumber("1.391e99")
    assert s.isNumber("-1.391e99")
    assert s.isNumber("1.391e+99")
    assert s.isNumber("-1.391e+99")
    assert s.isNumber("+1.391e-99")


def test_malformed():
    assert s.isNumber(".e9") == False
    assert s.isNumber("1.e") == False
    assert s.isNumber("1.e9")
