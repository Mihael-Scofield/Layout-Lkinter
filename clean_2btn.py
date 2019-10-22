import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image

fields = (
'Info no. 1',
'Info no. 2',
'Info no. 3',
'Info no. 4',
'Info no. 5',
'Info no. 6' )

ent_cells = []

###################################
##### Tratamento de Interação #####
###################################

# Busca os valores que foram digitados
def Calculate(entries, result, result_row):
    inp = fetch(entries, result) # Busca os valores nas entry e os transforma em array
    ###################################
    #####     Zona do cálculo     #####
    ###################################
    
    result.pack_forget() # Exclui a resposta atual, caso exista
    if Resposta <= 7:
        resultado = 'Contexto 1 ' + 'Contexto 2: ' + str(resultado)
        result.config(text = resultado, bg = '#FFD782') # Resultado ok, devido a cor
        #tkinter.messagebox.showinfo("Resultado", Resposta)
    elif Resposta <= 10:
        resultado = 'Contexto 1 ' + 'Contexto 3: ' + str(resultado)
        result.config(text = resultado, bg = '#E8B876') # Resultado preocupante, devido a cor
        #tkinter.messagebox.showwarning("Resultado", Resposta)
    elif Resposta >= 11:
        resultado = 'Contexto 1. ' + 'Contexto 4: ' + str(resultado)
        result.config(text = resultado, bg = '#E89776') # Resultado crítico, devido a cor
        #tkinter.messagebox.showerror("Resultado", Resposta)

    # Posicionamento da resposta
    result.pack(side = tk.LEFT, expand = True)

    #Clear()

# Busca os valores que foram digitados
def fetch(entries, result):
    numbers = [] # Numeros escritos, vetor de retorno
    numbers_s = [] # Vetor auxiliar com os numeros em tipo string
    i = 0

    for entry in entries:
        try: 
            numbers_s.append(str(entry[1].get())) # Pega a entrada atual.
            if (numbers_s[i].find(',') != -1): # Verifica se existe a vírgula.
                numbers_s[i] = numbers_s[i].replace(",", ".") # Substitui a vírgula.
                numbers.append(float(numbers_s[i])) # Acrescenta a entrada atual na final.
            else:
                numbers.append(float(entry[1].get())) # Caso nao exista, eh possivel acrescentar diretamente no vetor de retorno
            i += 1
        except: 
            error_treat(result, 0)

    return numbers

# Faz o tratamento de erro para conversar com o usuario
def error_treat(result, call):
    # Chamada de Interação
    if call == 0:
        result.config(text = 'Valor de entrada inválido! Por favor, digite um valor do tipo "inteiro" ou "real."', bg = '#E8B876')      
        result.pack(side = tk.LEFT, expand = True)


# Limpa as celulas e remove o resultado
def Clear(result):
    # Limpa as entry
    for entry in ent_cells:
        entry.delete(0, tk.END)
        entry.insert(0, 0)

    # Exclui a Label de resultado
    result.pack_forget()


###################################
##### Tratamento de Interface #####
###################################

# Função responsável por criar a janela raiz
def CreateWindow():
    window = tk.Tk() # Cria a janela
    window.title("Clean Interface")
    window.resizable(0, 0)
    window.geometry("740x509")
    window.configure(background = '#FFFFFF')

    return window

def LoadImages(images):
    # Abertura de imagens
    ## Imagem do topo
    path = "Imagem 1.png" # Define o caminho da Imagem
    images.insert(0, Image.open(path)) # Abre ela
    #img = img.resize((137, 63), Image.ANTIALIAS)
    images.insert(0, ImageTk.PhotoImage(images[0])) # Converte para tratamento Tk

    ## Imagens dos botoes
    path = "Imagem 2.png"
    images.insert(1, Image.open(path))
    images.insert(1, ImageTk.PhotoImage(images[1]))

    path = "Imagem 3.png"
    images.insert(2, Image.open(path))
    images.insert(2, ImageTk.PhotoImage(images[2]))

# Função que cria o cabeçalho e carrega as imagens
def CreateHeader(images):
    ## Criacao da linha das imagens
    row = tk.Frame(window, bg = '#FFFFFF')    
    panel = tk.Label(row, image = images[0], bg = '#FFFFFF') # Define o label onde a imagem sera presa
    banner = tk.Label(row, bg = '#7988A2', text = '', font = ('helvetica', 1))

    ### Posicionamento da linha das imagens
    row.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'center') # Posiciona imagem
    panel.pack(side = tk.TOP, fill = 'none', expand = True, anchor = 'center') 
    banner.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'n') 

    ## Criacao da Linha header
    row2 = tk.Frame(window, bg = '#FFFFFF')
    calc_label = tk.Label(row2, bd = 3, width = 50, relief = 'flat', text = 'CALCULADORA', fg = 'black', bg = '#FFFFFF',
    font = ('helvetica', 14, 'bold'), anchor = 'w') # ancora 

    ### Posicionamento da linha header
    row2.pack(side = tk.TOP, fill = tk.X, padx = 80, pady = 5) # Posiciona header  
    calc_label.pack(side = tk.LEFT, fill = tk.X, expand = True, anchor = "w")

# Funcao que gera interna do layout e retorna as possíveis entradas
def MakeForm(window, fields):
    entries = []
    i = 1

    for field in fields:
        row = tk.Frame(window, bg = '#FFFFFF') # Cria o frame da linha atual
        lab = tk.Label(row, bd = 3, relief = 'flat', width = 35, text = field, anchor = 'w', fg = 'black',
        bg = '#FFFFFF', font = ('helvetica', 14)) # informacao ancorada
        ent = tk.Entry(row, bd = 0, highlightbackground = 'white', relief = 'flat', width = 10, bg = '#FFFFFF', fg = 'black', justify = 'center', font = ('helvetica', 14)) # Entry
        lab_um1 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'um1', anchor = 'sw', fg = 'black', bg = '#FFFFFF', font = ('helvetica', 12)) # Unidade de medida
        lab_um2 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'um2', anchor = 'sw', fg = 'black', bg = '#FFFFFF', font = ('helvetica', 12)) # Unidade de medida

        row.pack(side = tk.TOP, fill = tk.X, padx = 50, pady = 5) # Posiciona os frames e os preenche
        lab.pack(side = tk.LEFT, padx = 10, expand = True)
        ent.pack(side = tk.LEFT, expand = False)
        ent.insert(0, 0)
        if i <= 2: # Verifica qual unidade de medida deve ser utilizada
            lab_um1.pack(side = tk.LEFT, padx = 10, expand = True)
        else:
            lab_um2.pack(side = tk.LEFT, padx = 10, expand = True)

        i += 1 # Incrementa verificador 
        entries.append((field, ent)) # Atualiza a lista de entradas.
        ent_cells.append(ent)

    return entries

# Faz o tratamento com a interacao do usuario
def InteractionTreatment(ents, images):
    ## Interacao das respostas
    result_row = tk.Frame(window, bg = '#FFFFFF') # Linha contendo o resultado
    result = tk.Label(result_row, bd = 2, relief = 'flat', width = 79, bg = '#ebebeb', fg = 'black', justify = 'center', font = 'helvetica', text = '') # Label com o resultado
    result_row.pack(side = tk.TOP, fill = tk.X, expand = True)
    # A linha é posicionada para garantir o espaçamento inicial, entretanto, a label só deve ser posicionada
    # ou removida após os cálculos, portanto, isso fica a cargo de Calculate() e Clear()

    ## Botoes de interacao
    window.bind('<Return>', (lambda event, e = ents: fetch(e))) # Declara a ligacao com o evento de busca
    row = tk.Frame(window, bg = '#FFFFFF')
    b1 = tk.Button(row, image = images[1], borderwidth = 0, relief = 'sunken', highlightbackground = '#FFFFFF', text = ' Limpar ', font = ('helvetica', '12'), bg = '#FFFFFF', command = (lambda: Clear(result))) # Seta a funcao e aparencia dos botoes
    b2 = tk.Button(row, image = images[2], borderwidth = 0, relief = 'sunken', highlightbackground ='#FFFFFF', text = 'Calcular', font = ('helvetica', '12', 'bold'), fg = 'white', bg = '#FFFFFF', command = (lambda e = ents: Calculate(e, result, result_row)))
    row.pack(side = tk.BOTTOM, fill = 'none', expand = False)
    b1.pack(side = tk.LEFT, padx = 5, pady = 10, expand = True, fill = 'none')
    b2.pack(side = tk.LEFT, padx = 5, pady = 10, expand = True, fill = 'none')

# Main
if __name__ == '__main__':
    # Tratamento de tela
    window = CreateWindow()

    # Tratamento de Cabecalho
    images = []
    LoadImages(images)
    CreateHeader(images)

    # Criacao do Layout
    ents = MakeForm(window, fields) # Recebe as entidades passadas pelos campos

    # Tratamento de interacao
    InteractionTreatment(ents, images)
    
    window.mainloop()