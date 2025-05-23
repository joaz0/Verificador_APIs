import customtkinter as CTk
import requests


# Configurações da janela

CTk.set_appearance_mode("Dark")
CTk.set_default_color_theme("blue")

janela_principal = CTk.CTk()
janela_principal.geometry("800x400")
janela_principal.resizable(False, False)
janela_principal.title("Verificador de API")
janela_principal.iconbitmap("C:/Users/joazr/Downloads/icone_api_129131.ico")

titulo = CTk.CTkLabel(janela_principal, text="Verificador de API", text_color="#a9c8ff", font=("Arial", 25))
titulo.pack(pady=5)
titulo.place(relx=0.5, rely=0.1, anchor="center")

apresentacao = CTk.CTkLabel(janela_principal, text="Olá eu sou o Verificador de APIs seja bem-vindo, ao meu programa! \n Esse programa verifica se a API está funcionando corretamente.", text_color="#a9c8ff", font=("Arial", 16))
apresentacao.pack(pady=5)
apresentacao.place(relx=0.5, rely=0.3, anchor="center")

info = CTk.CTkLabel(janela_principal, text="Para verificar a API, digite a URL dela e clique no botão abaixo.", text_color="#a9c8ff", font=("Arial", 16))
info.pack(pady=5)
info.place(relx=0.5, rely=0.5, anchor="center")

puxador_urls = CTk.CTkEntry(janela_principal, placeholder_text="Digite a URL da API que deseja verificar: ", placeholder_text_color="#a9c8ff", width=250, text_color="#a9c8ff", font=("Arial", 13), border_color="#a9c8ff")
puxador_urls.pack(pady=10)
puxador_urls.place(relx=0.5, rely=0.6, anchor="center")

botao_verificar = CTk.CTkButton(janela_principal, text="Verificar", command=lambda: verificar_api(), width=100, border_color="#a9c8ff", text_color="#a9c8ff", hover_color="#a9c8ff", font=("Arial", 13))
botao_verificar.pack(pady=10)
botao_verificar.place(relx=0.5, rely=0.7, anchor="center")




# Função para verificar a API
def verificar_api():
    url = puxador_urls.get().strip()

    resposta = requests.get(url, timeout=10)
    print(resposta)
    
    ERROS_API = {
        200: ("✅ API funcionando corretamente", "#00FF00"),
        400: ("❌ Erro 400: Requisição inválida", "#FF0000"),
        401: ("❌ Erro 401: Não autorizado", "#FF0000"),
        403: ("❌ Erro 403: Acesso proibido", "#FF0000"),
        404: ("❌ Erro 404: Endpoint não encontrado", "#FF0000"),
        500: ("❌ Erro 500: Erro interno do servidor", "#FF0000"),
        503: ("❌ Erro 503: Serviço indisponível", "#FF0000"),
        "SCHEMA": ("⚠️ URL deve começar com http:// ou https://", "#FFA500"),
        "CONNECTION": ("⚠️ Falha na conexão com o servidor", "#FF0000"),
        "TIMEOUT": ("⚠️ Tempo de espera excedido", "#FFA500"),
        "SSL": ("⚠️ Problema com certificado SSL", "#FF0000"),
        "JSON": ("⚠️ Resposta não é um JSON válido", "#FFA500"),
        "GENERICO": ("⚠️ Erro desconhecido", "#FF0000")
    }

    # Verificação inicial da URL
    if not url:
        mostrar_resultado("⚠️ Por favor, digite uma URL válida!", "#FF0000")
        return
        
    if not url.startswith(("http://", "https://")):
        mostrar_resultado(ERROS_API["SCHEMA"][0], ERROS_API["SCHEMA"][1])
        return

    try:
        resposta = requests.get(url, timeout=10)
        
        if resposta.status_code in ERROS_API:
            mensagem, cor = ERROS_API[resposta.status_code]
            mostrar_resultado(mensagem, cor)
            
            if resposta.status_code == 200:
                try:
                    resposta.json()
                except ValueError:
                    mostrar_resultado("⚠️ API respondeu, mas o JSON é inválido", "#FFA500")
        else:
            mostrar_resultado(f"⚠️ Erro HTTP não catalogado: {resposta.status_code}", "#FF0000")

    except requests.exceptions.RequestException as erro:
        tipo_erro = type(erro).__name__
        codigos_erro = {
            "ConnectionError": "CONNECTION",
            "Timeout": "TIMEOUT",
            "SSLError": "SSL",
            "MissingSchema": "SCHEMA"
        }
        
        erro_key = codigos_erro.get(tipo_erro, "GENERICO")
        mensagem, cor = ERROS_API[erro_key]
        mostrar_resultado(mensagem, cor)

    except Exception as erro:
        mostrar_resultado(ERROS_API["GENERICO"][0], ERROS_API["GENERICO"][1])

def mostrar_resultado(mensagem, color="#a9c8ff"):
    resultado = CTk.CTkLabel(janela_principal, text=mensagem, text_color="#a9c8ff", font=("Arial", 16))
    resultado.pack(pady=5)
    resultado.place(relx=0.5, rely=0.8, anchor="center")
    resultado.after(5000, resultado.destroy)

janela_principal.mainloop()