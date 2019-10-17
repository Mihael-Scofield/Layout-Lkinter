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

# Busca os valores que foram digitados
def Calculate(entries, result, result_row):
    ###################################
    #####     Zona do cálculo     #####
    ################################### 
    
    
    ###################################
    #####  Interação da Resposta  #####
    ################################### 
    result.pack_forget()
    if classe <= 3:
        classe = 'Contexto 1 ' + 'Contexto 2 ' + str(classe)
        result.config(text = classe, bg = '#FFD782')
        #tkinter.messagebox.showinfo("Resultado", classe)
    elif classe <= 7:
        classe = 'Contexto 1 ' + 'Contexto 2 ' + str(classe)
        result.config(text = classe, bg = '#E8B876')
        #tkinter.messagebox.showwarning("Resultado", classe)
    elif classe >= 8:
        classe = 'Contexto 1 ' + 'Contexto 2 ' + str(classe)
        result.config(text = classe, bg = '#E89776')
        #tkinter.messagebox.showerror("Resultado", classe)

    # Posicionamento da resposta
    result.pack(side = tk.LEFT, expand = True)

    #Clear()

# Busca os valores que foram digitados
def fetch(entries):
    numbers = []
    for entry in entries:
        numbers.append(float(entry[1].get()))
    return numbers

# Faz a limpeza do Layout
def Clear(result):
    # Limpa as entry
    for entry in ent_cells:
        entry.delete(0, tk.END)

    # Exclui a Label de resultado
    result.pack_forget()


# Funcao que gera estrutura do layout e retorna as entries para alteracao
def makeform(window, fields):
    entries = []
    i = 1

    for field in fields:
        row = tk.Frame(window, bg = '#FFFFFF') # Cria o frame da linha atual
        lab = tk.Label(row, bd = 3, relief = 'flat', width = 50, text = field, anchor = 'center', fg = 'black', bg = '#ebebeb', font = 'helvetica') # informacao ancorada
        ent = tk.Entry(row, bd = 2, relief = 'flat', bg = '#ebebeb', fg = 'black', justify = 'center', font = 'helvetica') # Entry
        lab_UM1 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'UM1', anchor = 'sw', fg = 'black', bg = '#ebebeb', font = ('helvetica', 13)) # Unidade de medida
        lab_UM2 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'UM2', anchor = 'sw', fg = 'black', bg = '#ebebeb', font = ('helvetica', 13)) # Unidade de medida

        row.pack(side = tk.TOP, fill = tk.X, pady = 5) # Posiciona os frames e os preenche
        lab.pack(side = tk.LEFT, expand = tk.YES)
        ent.pack(side = tk.LEFT, expand = False)
        if i <= 2: # Verifica qual unidade de medida deve ser utilizada
            lab_UM1.pack(side = tk.RIGHT, expand = True)
        else:
            lab_UM2.pack(side = tk.RIGHT, expand = True)

        i += 1 # Incrementa verificador 
        entries.append((field, ent)) # Atualiza a lista de entradas.
        ent_cells.append(ent)

    return entries

if __name__ == '__main__':
    # Tratamento de tela    
    window = tk.Tk() # Cria a janela
    window.title("Try")
    window.resizable(0, 0) # Impede redimensionamento
    window.geometry("740x509")
    window.configure(background = '#FFFFFF')

    ###################################
    ##### Tratamento de Cabeçalho #####
    ###################################
    path = "Imagem 1.png" # Define o caminho da Imagem
    img = Image.open(path) # Abre ela
    #img = img.resize((137, 63), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img) # Converte para tratamento Tk]

    ## Criacao da linha das imagens
    row = tk.Frame(window, bg = '#FFFFFF')    
    panel = tk.Label(row, image = img, bg = '#FFFFFF') # Define o label onde a imagem sera presa
    banner = tk.Label(row, bg = '#7988A2', text = '', font = ('helvetica', 1))

    ### Posicionamento da linha das imagens
    row.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'center') # Posiciona imagem
    panel.pack(side = tk.TOP, fill = 'none', expand = True, anchor = 'center') 
    banner.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'n') 

    ## Criacao da Linha header
    row2 = tk.Frame(window, bg = '#FFFFFF')
    calc_label = tk.Label(row2, bd = 3, width = 50, relief = 'flat', text = '  Título', fg = 'black', bg = '#FFFFFF', font = ('helvetica', 13, 'bold'), anchor = 'w') # ancora 
    ### Posicionamento da linha header
    row2.pack(side = tk.TOP, fill = tk.X, pady = 5) # Posiciona header  
    calc_label.pack(side = tk.LEFT, fill = tk.X, expand = True, anchor = "w")

    
    ###################################
    ##### Tratamento de Interação #####
    ###################################
    ents = makeform(window, fields) # Recebe as entidades passadas pelos campos

    ## Interacao das respostas
    result_row = tk.Frame(window, bg = '#FFFFFF') # Linha contendo o resultado
    result = tk.Label(result_row, bd = 2, relief = 'flat', width = 79, bg = '#ebebeb', fg = 'black', justify = 'center', font = 'helvetica', text = '') # Label com o resultado
    result_row.pack(side = tk.TOP, fill = tk.X, expand = True)
    # A linha é posicionada para garantir o espaçamento inicial, entretanto, a label só deve ser posicionada
    # ou removida após os cálculos, portanto, isso fica a cargo de Calculate() e Clear()

    ## Botão de interação
    window.bind('<Return>', (lambda event, e = ents: fetch(e))) # Declara a ligacao com o evento de busca
    row = tk.Frame(window, bg = '#FFFFFF')
    b1 = tk.Button(row, width = 10, relief = 'flat', highlightbackground = '#444444', bd = 3, text = ' Limpar ', font = ('helvetica', '12'), bg = '#CAC8C8', command = (lambda: Clear(result))) # Seta a funcao e aparencia dos botoes
    b2 = tk.Button(row, width = 10, bd = 3, relief = 'flat', highlightbackground ='#444444', text = 'Calcular', font = ('helvetica', '12', 'bold'), fg = 'white', bg = '#010f64', command = (lambda e = ents: Calculate(e, result, result_row)))
    row.pack(side = tk.BOTTOM, fill = 'none', expand = False)
    b1.pack(side = tk.LEFT, padx = 5, pady = 10)
    b2.pack(side = tk.LEFT, padx = 5, pady = 10)

    window.mainloop()