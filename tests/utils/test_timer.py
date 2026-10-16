"""Tests for hive.utils.timer.Timer status lines on a coarse clock."""

from hive.utils import timer as timer_module
from hive.utils.timer import Timer


def _frozen_timer(monkeypatch, total, done):
    """A timer whose clock never advances, as two back-to-back reads of a Xen clocksource can."""
    monkeypatch.setattr(timer_module, 'perf', lambda: 100.0)
    t = Timer(total, entity='block', laps=['rps', 'wps'])
    t.batch_start()
    t.batch_lap()
    t.batch_finish(done)
    return t


def test_finished_batch_with_zero_elapsed_time(monkeypatch):
    t = _frozen_timer(monkeypatch, 1000, 1000)
    assert t.batch_status('[MASSIVE-SQL] Got block 1000') == (
        '[MASSIVE-SQL] Got block 1000 (0/s, 0rps, 0wps) -- done in 00s, avg rate: 0.0/s'
    )


def test_unfinished_batch_with_zero_elapsed_time(monkeypatch):
    t = _frozen_timer(monkeypatch, 1000, 10)
    assert t.batch_status() == ' -- block 10 of 1000 (0/s, 0rps, 0wps) -- eta unknown'


def test_rates_and_eta_on_a_moving_clock(monkeypatch):
    clock = iter([0.0, 1.0, 3.0, 4.0])
    monkeypatch.setattr(timer_module, 'perf', lambda: next(clock))
    t = Timer(100, entity='block', laps=['rps', 'wps'])
    t.batch_start()
    t.batch_lap()
    t.batch_finish(10)
    # 10 items: 3 s for the batch, 2 s for the first lap, 1 s for the second.
    assert t.batch_status() == ' -- block 10 of 100 (3/s, 5rps, 10wps) -- eta 27s'
