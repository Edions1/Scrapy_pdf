import os
import fitz  # PyMuPDF

def listar_pdfs(caminho):
    """Lista todos os arquivos PDFs em um diretório."""
    pdfs = [arquivo for arquivo in os.listdir(caminho) if arquivo.endswith('.pdf')]
    return pdfs

def buscar_palavra_chave(pdf_path, palavra_chave):
    """Busca uma palavra-chave em um PDF e retorna as linhas que a contêm."""
    linhas_encontradas = []
    doc = fitz.open(pdf_path)
    for pagina in doc:
        texto = pagina.get_text()
        for linha in texto.split('\n'):
            if palavra_chave.lower() in linha.lower():
                linhas_encontradas.append(linha)
    doc.close()
    return linhas_encontradas

if __name__ == "__main__":
    print("Inicio do programa.\n")

    # Leitura dos PDFs da pasta
    pasta = "/home/seu/diretorio/busca_pdf"
    print("PDFs cadastrados:")
    pdfs_disponiveis = listar_pdfs(pasta)
    for pdf in pdfs_disponiveis:
        print(pdf)
    
    # Seleção do PDF pelo usuário
    pdf_escolhido = input("\nSelecione um PDF: ")
    if pdf_escolhido not in pdfs_disponiveis:
        print("PDF selecionado não encontrado. Saindo do programa.")
        exit()
    
    # Inserção da palavra-chave pelo usuário
    palavra_chave = input("\nInsira a palavra-chave para busca: ")

    # Busca pela palavra-chave no PDF selecionado
    resultados = buscar_palavra_chave(os.path.join(pasta, pdf_escolhido), palavra_chave)

    # Exibição dos resultados
    print("\nExemplos de linhas encontradas:")
    for linha in resultados:
        print(linha)
