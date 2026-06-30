def clean_customer_name(name):
    return " ".join(str(name).strip().split()).title()
