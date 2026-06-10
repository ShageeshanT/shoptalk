from shoptalk.whatsapp_optin_label import whatsapp_optin_label

def test_whatsapp_optin_label_known_values():
    assert whatsapp_optin_label('opted_in') == 'WhatsApp opted in'
    assert whatsapp_optin_label('pending') == 'WhatsApp pending'
    assert whatsapp_optin_label('opted_out') == 'WhatsApp opted out'

def test_whatsapp_optin_label_unknown_value():
    assert whatsapp_optin_label("") == 'WhatsApp unknown'
