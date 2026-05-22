from shoptalk.schemas import MessageAnalysis


def title_from_analysis(analysis: MessageAnalysis) -> str:
    details = analysis.order_details
    product = details.product or 'Customer request'
    quantity = f"{details.quantity}x " if details.quantity else ''
    size = f" {details.size}" if details.size else ''
    return f"{quantity}{product}{size}".strip().title()
