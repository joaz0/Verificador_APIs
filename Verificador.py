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
    
    mensagem_funcionando = "✅API funcionando corretamente"
    mensagem_scheme = "SCHEMA URL deve começar com http:// ou https://"
    ERROS_API = {
    400: "Requisição inválida",
    401: "Não autorizado",
    403: "Acesso proibido",
    404: "Endpoint não encontrado",
    500: "Erro interno do servidor",
    503: "Serviço indisponível",
    "CONNECTION": "Falha na conexão com o servidor",
    "TIMEOUT": "Tempo de espera excedido",
    "SSL": "Problema com certificado SSL",
    "JSON": "Resposta não é um JSON válido",
    "GENERICO": "Erro desconhecido"}


    if not url.startswith(("http://", "https://")):
       mostrar_resultado(f"⚠️ {mensagem_scheme}", "#a9c8ff")

        
    try:
        if resposta.status_code == 200:
                mostrar_resultado(f"{mensagem_funcionando}", "#a9c8ff")            
    
    except requests.exceptions.ConnectionError:
        mostrar_resultado(f"⚠️ {ERROS_API['CONNECTION']}", "#a9c8ff")
    
    except requests.exceptions.Timeout:
        mostrar_resultado(f"⚠️ {ERROS_API['TIMEOUT']}", "#a9c8ff")
    
    except requests.exceptions.SSLError:
        mostrar_resultado(f"⚠️ {ERROS_API['SSL']}")



def mostrar_resultado(mensagem, color="#a9c8ff"):
    resultado = CTk.CTkLabel(janela_principal, text=mensagem, text_color="#a9c8ff", font=("Arial", 16))
    resultado.pack(pady=5)
    resultado.place(relx=0.5, rely=0.8, anchor="center")
    resultado.after(5000, resultado.destroy)

janela_principal.mainloop()