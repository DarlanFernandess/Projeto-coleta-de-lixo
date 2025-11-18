import re

def validar_telefone(telefone):
    """Valida formato de telefone"""
    if not telefone:
        return True
    
    # Remove caracteres não numéricos
    telefone_limpo = re.sub(r'\D', '', telefone)
    
    # Verifica se tem entre 10 e 11 dígitos
    return 10 <= len(telefone_limpo) <= 11

def validar_email(email):
    """Valida formato de email"""
    if not email:
        return True
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None