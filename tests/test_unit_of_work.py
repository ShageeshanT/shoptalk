from shoptalk.unit_of_work import SqlUnitOfWork


class FakeSession:
    def __init__(self):
        self.events = []
    def commit(self): self.events.append("commit")
    def rollback(self): self.events.append("rollback")
    def close(self): self.events.append("close")


def test_unit_of_work_commits_and_closes_on_success():
    session = FakeSession()
    with SqlUnitOfWork(session):
        pass
    assert session.events == ["commit", "close"]


def test_unit_of_work_rolls_back_and_closes_on_error():
    session = FakeSession()
    try:
        with SqlUnitOfWork(session):
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    assert session.events == ["rollback", "close"]
