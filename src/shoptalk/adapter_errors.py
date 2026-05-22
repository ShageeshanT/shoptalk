class ChannelAdapterError(RuntimeError):
    """Base error for channel adapter failures."""


class SendNotApprovedError(ChannelAdapterError):
    """Raised when code tries to send without human approval."""


def require_send_approval(approved: bool) -> None:
    if not approved:
        raise SendNotApprovedError('Message requires seller approval before sending')
