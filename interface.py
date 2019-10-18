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

# Funcao definida para que o auto-py-to-exe possa utilizar as imagens
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Busca os valores que foram digitados
def Calculate(entries, result, result_row):
    inp = fetch(entries, result) # Busca os valores nas entry e os transforma em array
    ###################################
    #####     Zona do cálculo     #####
    ################################### 


    ###################################
    #####  Interação da Resposta  #####
    ################################### 
    result.pack_forget() # Exclui a resposta atual, caso exista
    if resultado <= 3: # Faz o tratamento do resultado gerado na zona de cálculo
        resultado = 'Contexto 1 ' + 'Contexto 2: ' + str(resultado)
        result.config(text = resultado, bg = '#FFD782') # Resultado ok, devido a cor
        #tkinter.messagebox.showinfo("Resultado", resultado)
    elif resultado <= 5:
        resultado = 'Contexto 1 ' + 'Contexto 3: ' + str(resultado)
        result.config(text = resultado, bg = '#E8B876') # Resultado preocupante, devido a cor
        #tkinter.messagebox.showwarning("Resultado", resultado)
    elif resultado >= 7:
        resultado = 'Contexto 1. ' + 'Contexto 4: ' + str(resultado)
        result.config(text = resultado, bg = '#E89776') # Resultado crítico, devido a cor
        #tkinter.messagebox.showerror("Resultado", resultado)


    # Posicionamento da resposta
    result.pack(side = tk.LEFT, expand = True)

    #Clear()

# Busca os valores que foram digitados
def fetch(entries, result):
    numbers = [] # Numeros escritos, vetor de retorno
    numbers_s = [] # Vetor auxiliar com os numeros em tipo string
    i = 0

    # Tratamento para ler numeros reais tanto com ',' quanto com '.'
    for entry in entries:
        try: 
        	numbers_s.append(str(entry[1].get())) # Pega a entrada atual.
        	if (numbers_s[i].find(',') != -1): # Verifica se existe a vírgula.
        		numbers_s[i] = numbers_s[i].replace(",", ".") # Substitui a vírgula.
	        	numbers.append(float(numbers_s[i])) # Acrescenta a entrada atual na final.
	        else:
	        	numbers.append(float(entry[1].get())) # Caso nao exista, eh possivel acrescentar diretamente, sem trata-lo, no vetor de retorno
        	i += 1
        except: 
        	error_treat(result, 0) # Chama tratamento de erro

    return numbers

# Faz o tratamento de erro para conversar com o usuario
def error_treat(result, call):
	# Chamada de Interação
	if call == 0:
		result.config(text = 'Valor de entrada inválido! Por favor, digite um valor do tipo "inteiro" ou "real."', bg = '#E8B876')		
		result.pack(side = tk.LEFT, expand = True)

	# Eh possivel adicionar mais tratamentos diferentes, basta utilizar a call para saber de onde ela vem

# Limpa as celulas e remove o resultado
def Clear(result):
    # Limpa as entry
    for entry in ent_cells:
        entry.delete(0, tk.END)

    # Exclui a Label de resultado
    result.pack_forget()


# Funcao que gera estrutura do layout
def makeform(window, fields):
    entries = []
    i = 1

    # Criação das linhas descritas no "field", acrescentando elas as entradas para futuros tratamentos
    for field in fields:
        row = tk.Frame(window, bg = '#FFFFFF') # Cria o frame da linha atual
        lab = tk.Label(row, bd = 3, relief = 'flat', width = 50, text = field, anchor = 'w', fg = 'black', bg = '#ebebeb', font = 'helvetica') # informacao ancorada
        ent = tk.Entry(row, bd = 2, relief = 'flat', bg = '#ebebeb', fg = 'black', justify = 'center', font = 'helvetica') # Entry
        lab_um1 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'um1', anchor = 'sw', fg = 'black', bg = '#ebebeb', font = ('helvetica', 13)) # Unidade de medida 1
        lab_um2 = tk.Label(row, bd = 3, width = 4, relief = 'flat', text = 'um2', anchor = 'sw', fg = 'black', bg = '#ebebeb', font = ('helvetica', 13)) # Unidade de medida 2

        row.pack(side = tk.TOP, fill = tk.X, pady = 5) # Posiciona os frames e os preenche, deixando espaçamento        
        lab.pack(side = tk.LEFT, expand = tk.YES) # Posiciona Info no. n
        ent.pack(side = tk.LEFT, expand = False) # Posiciona campo de entrada.
        if i <= 2: # Verifica qual unidade de medida deve ser utilizada
            lab_um1.pack(side = tk.RIGHT, expand = True)
        else:
            lab_um2.pack(side = tk.RIGHT, expand = True)

        i += 1 # Incrementa verificador 
        entries.append((field, ent)) # Atualiza a lista de entradas, para ler depois.
        ent_cells.append(ent) # Atualiza lista de células presentes, para apaga-las depois.

    return entries

if __name__ == '__main__':
    # Tratamento de tela    
    window = tk.Tk() # Cria a janela
    window.title("Interface")
    window.resizable(0, 0) # Impede o redimencionamento
    window.geometry("740x509")
    window.configure(background = '#FFFFFF')

    ###################################
    ##### Tratamento de Cabeçalho #####
    ###################################
    
    # Abertura de imagens
    ## Imagem do topo
    path = "Imagem 1.png" # Define o caminho da imagem.
    #path = resource_path('Imagem 1.png') # Define o caminho da imagem, para o auto-py-to-exe
    img = Image.open(path) # Abre ela
    #img = img.resize((137, 63), Image.ANTIALIAS) # Redimenciona a imagem
    img = ImageTk.PhotoImage(img) # Converte para tratamento Tk

    ## Criacao da linha das imagens
    row = tk.Frame(window, bg = '#FFFFFF')    
    panel = tk.Label(row, image = img, bg = '#FFFFFF') # Define o label onde a imagem sera presa
    banner = tk.Label(row, bg = '#7988A2', text = '', font = ('helvetica', 1)) # Cria uma faixa sem utilizar imagem

    ## Imagens dos botoes
    path2 = "Imagem 2.png" # Define o caminho da imagem. 
    #path2 = resource_path('Imagem 2.png')
    btn_limp = Image.open(path2)
    btn_limp = ImageTk.PhotoImage(btn_limp)

    path3 = "Imagem 3.png" # Define o caminho da imagem.
    #path3 = resource_path('Imagem 3.png')
    btn_calc = Image.open(path3)
    btn_calc = ImageTk.PhotoImage(btn_calc)

    ### Posicionamento da linha das imagens
    row.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'center') # Posiciona Frame onde elas estão presentes
    panel.pack(side = tk.TOP, fill = 'none', expand = True, anchor = 'center') # Posiciona imagem
    banner.pack(side = tk.TOP, fill = tk.X, expand = False, anchor = 'n') # Posiciona faixa

    ## Criacao da Linha header
    row2 = tk.Frame(window, bg = '#FFFFFF')
    calc_label = tk.Label(row2, bd = 3, width = 50, relief = 'flat', text = '  CALCULADORA', fg = 'black', bg = '#FFFFFF', font = ('helvetica', 13, 'bold'), anchor = 'w') # ancora 
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

    ## Botoes de interacao
    window.bind('<Return>', (lambda event, e = ents: fetch(e))) # Declara a ligacao com o evento de busca
    row = tk.Frame(window, bg = '#FFFFFF')
    b1 = tk.Button(row, image = btn_limp, relief = 'flat', highlightbackground = '#FFFFFF', bd = 1, text = ' Limpar ', font = ('helvetica', '12'), bg = '#FFFFFF', command = (lambda: Clear(result))) # Seta a funcao e aparencia dos botoes
    b2 = tk.Button(row, image = btn_calc, bd = 1, relief = 'flat', highlightbackground ='#FFFFFF', text = 'Calcular', font = ('helvetica', '12', 'bold'), fg = 'white', bg = '#FFFFFF', command = (lambda e = ents: Calculate(e, result, result_row)))
    row.pack(side = tk.BOTTOM, fill = 'none', expand = False)
    b1.pack(side = tk.LEFT, padx = 5, pady = 10, expand = True, fill = 'none')
    b2.pack(side = tk.LEFT, padx = 5, pady = 10, expand = True, fill = 'none')

    window.mainloop()
