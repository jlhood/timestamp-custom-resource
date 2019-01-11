import pytest
import generatetimestamp


def test_create(mocker):
    generatetimestamp.create({}, None)
