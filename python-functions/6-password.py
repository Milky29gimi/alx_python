def validate_password(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_space = ' ' in password
    if not (has_upper and has_lower and has_digit) or has_space:
        return False
    
    return True

