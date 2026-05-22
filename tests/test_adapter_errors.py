import pytest

from shoptalk.adapter_errors import SendNotApprovedError, require_send_approval


def test_require_send_approval_blocks_unapproved_send() -> None:
    with pytest.raises(SendNotApprovedError):
        require_send_approval(False)
