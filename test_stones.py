"""
Tests for stones.py.

Each step is only checked once the program shows at least some trace of
its implementation (e.g. the output 'Tag=' for step 2). Until then, the
corresponding test is skipped (SKIPPED) instead of being marked as
failed. This way, only the tests matching the step currently being
worked on actually run.
"""
import pytest

from test_helpers import expected_numbers, expected_stones, run_main, square_count_up_to

# Step 0: Check the setup of this project
def test_setup(monkeypatch, capsys):
    assert True

# Step 1: Create list

def test_list_1(monkeypatch, capsys):
    result, _ = run_main(monkeypatch, capsys, 1, 5)
    if not result:
        pytest.skip('Step 1 (Liste erstellen) noch nicht umgesetzt')
    assert isinstance(result, list)
    assert len(result) == 5


def test_list_2(monkeypatch, capsys):
    result, _ = run_main(monkeypatch, capsys, 1, 8)
    if not result:
        pytest.skip('Step 1 (Liste erstellen) noch nicht umgesetzt')
    assert len(result) == 8
    assert all(stone in ('green', 'blue') for stone in result)


# Step 2: Output all days

def test_days_1(monkeypatch, capsys):
    upper_limit = 5
    _, output = run_main(monkeypatch, capsys, 1, upper_limit)
    if 'Tag' not in output:
        pytest.skip('Step 2 (Ausgabe aller Tage) noch nicht umgesetzt')
    expected = [f'Tag={day}' for day in range(1, upper_limit + 1)]
    found = [line for line in output.splitlines() if line.startswith('Tag=')]
    assert found == expected


def test_days_2(monkeypatch, capsys):
    upper_limit = 3
    _, output = run_main(monkeypatch, capsys, 1, upper_limit)
    if 'Tag' not in output:
        pytest.skip('Step 2 (Ausgabe aller Tage) noch nicht umgesetzt')
    expected = [f'Tag={day}' for day in range(1, upper_limit + 1)]
    found = [line for line in output.splitlines() if line.startswith('Tag=')]
    assert found == expected

def test_days_3(monkeypatch, capsys):
    upper_limit = 9
    _, output = run_main(monkeypatch, capsys, 1, upper_limit)
    if 'Wochen' not in output:
        pytest.skip('SKIPPED wird aktuell erwartet')
    expected = [f'Wochen={int(upper_limit/7)}']
    found = [line for line in output.splitlines() if line.startswith('Wochen=')]
    assert found == expected

# Step 3: Process numbers

def test_number_1(monkeypatch, capsys):
    upper_limit = 6
    _, output = run_main(monkeypatch, capsys, 1, upper_limit)
    if 'Nummer' not in output:
        pytest.skip('Step 3 (Nummer verarbeiten) noch nicht umgesetzt')
    found = [int(line.split('=')[1]) for line in output.splitlines() if line.startswith('Nummer=')]
    assert found == expected_numbers(upper_limit)


def test_number_2(monkeypatch, capsys):
    upper_limit = 10
    _, output = run_main(monkeypatch, capsys, 1, upper_limit)
    if 'Nummer' not in output:
        pytest.skip('Step 3 (Nummer verarbeiten) noch nicht umgesetzt')
    found = [int(line.split('=')[1]) for line in output.splitlines() if line.startswith('Nummer=')]
    assert found == expected_numbers(upper_limit)


# Step 4: Turn stones

def test_stones_1(monkeypatch, capsys):
    upper_limit = 10
    result, _ = run_main(monkeypatch, capsys, 1, upper_limit)
    if not result or 'blue' not in result:
        pytest.skip('Step 4 (Steine umdrehen) noch nicht umgesetzt')
    assert result == expected_stones(upper_limit)


def test_stones_2(monkeypatch, capsys):
    upper_limit = 20
    result, _ = run_main(monkeypatch, capsys, 1, upper_limit)
    if not result or 'blue' not in result:
        pytest.skip('Step 4 (Steine umdrehen) noch nicht umgesetzt')
    assert result == expected_stones(upper_limit)

def test_stones_3(monkeypatch, capsys):
    upper_limit = 17
    result, _ = run_main(monkeypatch, capsys, 1, upper_limit)
    if not result or result[0] != 'blank' :
        pytest.skip('SKIPPED wird aktuell erwartet')
    assert result[0] == 'blank'
# Step 5: Count stones

def test_count_1(monkeypatch, capsys):
    lower_limit, upper_limit = 1, 20
    _, output = run_main(monkeypatch, capsys, lower_limit, upper_limit)
    if 'blaue Steine' not in output:
        pytest.skip('Step 5 (Steine zählen) noch nicht umgesetzt')
    expected_count = square_count_up_to(upper_limit - 1) - square_count_up_to(lower_limit - 1)
    assert f'{expected_count} blaue Steine' in output


def test_count_2(monkeypatch, capsys):
    lower_limit, upper_limit = 5, 30
    _, output = run_main(monkeypatch, capsys, lower_limit, upper_limit)
    if 'blaue Steine' not in output:
        pytest.skip('Step 5 (Steine zählen) noch nicht umgesetzt')
    expected_count = square_count_up_to(upper_limit - 1) - square_count_up_to(lower_limit - 1)
    assert f'{expected_count} blaue Steine' in output
