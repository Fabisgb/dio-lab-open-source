import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso
if __name__ == "__main__":
    print("Gerador de Senhas")
    tamanho = int(input("Informe o tamanho da senha: "))
    senha = gerar_senha(
        tamanho=tamanho,
        usar_maiusculas=True,
        usar_minusculas=True,
        usar_numeros=True,
        usar_simbolos=True
    )
    print("Senha gerada:", senha)
