#   Este programa concatena archivos.pdf y permite establecer en que orden lo hace
#   Copyright (C) 2022 Cristian Tocci
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   Contacto : toccicristian@hotmail.com / toccicristian@protonmail.ch

licencias=dict()
licencias['gplv3']="""
    pdfdog.py  Copyright (C) 2022  Cristian Tocci
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; See COPYING.odt file for further details.
    """
licencias['gplv3logo']="""
+----------------------------------------------------------------------------------------------------+
|oooooooo+~~~+~~~~~~+~~~~~+~~~~+~~~~~~+~~~~+~~~~~~+~~+~~~~+~~~~~+~~~~+~~~~~~++~~+~~+~~~~~~:  ::::::~+|
|oooooooo :::::::::::::::::::::::::::::::::::::::::::~::::::::::::::::::::::::::::::::. ~~~++ooooo+:.|
|ooooooo~::::::~:::::::::::::::::::::::::::::::::::::+::::::::::::::::::::::::~~.~:~:~+oooooooooooo:.|
|ooooooo :~:~~~~~~~~~~+~::: +~~~~~~~~~~~~~::++ :::::~+~:::::::::::::::::::~...~:::~ooooooooooooooo~.+|
|oooooo~~:~oo~~~~~~~~~oo~:~+oo ~~~~~~.ooo.~oo+~::::.+o ::::::::::::::::~  .~::::+oo+~:   +ooooooo::+o|
|oooooo::.+o+~::::::~+oo : oo~::::::::oo~:~oo~::::: oo~:::::::::::::: ~ ~::::.++~ ~:::::.+oooo+~ ~ooo|
|ooooo+~:~oo~:::::::::::::~oo::::::::+oo :+oo~:::::~oo+.::::::::::.:~ ~:::::: .:::::::~~oooo+:~ +oooo|
|ooooo::~+o+.:::::::::::: oo+~:::::: oo~~:oo~::::::~ooo~::::::::.~~.::::::::::::::::~~+oooooo+~::oooo|
|oooo+~::oo~:::~:~:~~::::~oo~       ~oo::+oo.::::::~ooo+~::::: ~~.:::::::::::::::: ~+oooooooooo~~oooo|
|oooo~::+oo :::~   +oo::.ooo~~~~~~~~~:.: oo+:::::::~oooo~:::~~+:::::::::::::::: ~+++~~~~oooooo+.~oooo|
|ooo+.: oo~:::::::.oo+.:~oo~::::::::::::~oo:::::::::oooo+~::++~::::::::::::::~   .::::::ooooo~.~ooooo|
|ooo~::~oo::::::::~oo~:~+o+~::::::::::: oo+~:::::::.+ooo~.~o+:::::::::::::::::::::::: +oooo+: +oooooo|
|ooo.: oo+.~~~~~~ +oo.::oo~::::::::::::~oo~~~~~~~:::+oo~ +oo ::::::::::::::::::::.:~ooooo+: ~oooooooo|
|oo~::.~~~~~~~~~~~~~ ::~+~.::::::::::::~+~~~~~~~~~:::o~ +ooo:::::::::::::::::: ~+oooooo~::~oooooooooo|
|o+ :~   ~::::::::::::.  ~::::: ..:::::::::::::::::::~ ~oooo~~::::::::::~. ~~+oooooo+~::+oooooooooooo|
|o~~:~~: ~ :~~. ~~.::~~~~. ::.~~~~::~:: :~~.~::~~ ::::.oooooo+~~::::~~~~ooooooooo+~::~+oooooooooooooo|
|o::~~~~:::~~~ ~~~.:: ::~.~:~.~~~: ~~~ :~~~: ~~~~~:::: oooooooooooooooooooooo++~::~+ooooooooooooooooo|
|+:::~::::::~~::::::::~~:::~::~:::::::::::~::::~:::::::~ooooooooooooooooo++~::~~+oooooooooooooooooooo|
|::::::::::::::::::::::::::::::::::::::::::::::::::::::: ~oooooooooo+~~~::~~+oooooooooooooooooooooooo|
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:~~~~~:    ::::::::~~~ooooooooooooooooooooooooooooo|
+----------------------------------------------------------------------------------------------------+
"""
licencias['textow']=""" 
    15. Disclaimer of Warranty.
    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY 
    APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT 
    HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT 
    WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT 
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A 
    PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE 
    OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU 
    ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
    
    16. Limitation of Liability.
    IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING 
    WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR 
    CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR 
    DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL 
    DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM 
    (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED 
    INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF 
    THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER 
    OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

    17. Interpretation of Sections 15 and 16.
    If the disclaimer of warranty and limitation of liability provided above 
    cannot be given local legal effect according to their terms, 
    reviewing courts shall apply local law that most closely approximates 
    an absolute waiver of all civil liability in connection with the Program, 
    unless a warranty or assumption of liability accompanies a copy of 
    the Program in return for a fee.
    """


import tkinter
from tkinter import filedialog
import os


browser_dir_inicial='~'


def loguea(logbox,linea=str()):
        logbox.insert(tkinter.END, linea)
        logbox.see(tkinter.END)


def file_browser():
        tipos=(
                ('archivos pdf','*.pdf'),
                ('Todos los archivos','*.*')
        )
        archivo_url = filedialog.askopenfilenames(
                #initialdir = os.path.expanduser(os.path.normpath(browser_dir_inicial)), #esto inicia en '~' pero olvida ultimo directorio
                title='Agregar PDF...',
                filetypes=(tipos)
        )
        return archivo_url


def agregarpdf(listbox_pdfs,logbox):
        archivo_urls=file_browser()
        for archivo_url in archivo_urls:
                listbox_pdfs.insert(tkinter.END, archivo_url)
                listbox_pdfs.see(tkinter.END)
#                listbox_pdfs.selection_clear(0,tkinter.END)
#                listbox_pdfs.selection_set(tkinter.END)
                loguea(logbox,'Archivo agregado: '+str(archivo_url)+'\n')
        #indice_insercion=tkinter.END                           # TODO : INICIO DE VOLAR ESTO A LA MIERDA
        #print(len(listbox_pdfs.curselection()))
        #if len(listbox_pdfs.curselection())>0:
        #        indice_insercion=listbox_pdfs.curselection()[0]+1
        #if archivo_url:
        #        listbox_pdfs.insert(indice_insercion, archivo_url)
        #        listbox_pdfs.see(indice_insercion)
        #        listbox_pdfs.selection_clear(0,tkinter.END)
        #        listbox_pdfs.selection_set(listbox_pdfs.curselection()[0])
        #        if str(indice_seleccion) != tkinter.END:
        #                listbox_pdfs.see(indice_seleccion)
        #                listbox_pdfs.selection_clear(0,tkinter.END)
        #                listbox_pdfs.selection_set(indice_seleccion)
        #        loguea(logbox,'Archivo agregado: '+str(archivo_url))      #FIN DE VOLAR A LA MIERDA


def quitarpdf(listbox_pdfs,logbox):
        for i in listbox_pdfs.curselection()[::-1]:
                loguea(logbox,'Quitar :'+str(listbox_pdfs.get(i))+'\n')
                listbox_pdfs.delete(i)


#####################################################################################
#			GUI :
#####################################################################################
ventana=tkinter.Tk()
ventana.title("PDF DOG")
ventana.geometry("800x600")

#               DEFINICIONES 
print('cargando marcos')
marco_superior=tkinter.Frame(ventana)
marco_inferior=tkinter.Frame(ventana)
marco_fondo=tkinter.Frame(ventana)
marco_izquierdo= tkinter.Frame(marco_superior)
marco_derecho= tkinter.Frame(marco_superior)
marco_inferior_izquierdo=tkinter.Frame(marco_inferior)
marco_inferior_derecho=tkinter.Frame(marco_inferior)
print("cargando listbox y scrollbar")
listbox_pdfs = tkinter.Listbox(marco_izquierdo, selectmode="multiple")
scrollbar_pdfs = tkinter.Scrollbar(marco_izquierdo)
print("cargando cargando logbox")
etiqueta_logbox=tkinter.Label(marco_fondo,text="Log:")
logbox=tkinter.Text(marco_fondo,height=5,width = 95)
scrollbar_logbox = tkinter.Scrollbar(marco_fondo)
print("cargando imagenes")
imagen_boton_agregar=tkinter.PhotoImage(file=os.path.normpath('./res/pdfadd-64x64.png'))
imagen_boton_quitar=tkinter.PhotoImage(file=os.path.normpath('./res/pdfremove-64x64.png'))
imagen_boton_subir=tkinter.PhotoImage(file=os.path.normpath('./res/arrow_up.png'))
imagen_boton_bajar=tkinter.PhotoImage(file=os.path.normpath('./res/arrow_down.png'))
imagen_boton_dog=tkinter.PhotoImage(file=os.path.normpath('./res/olicara-64x64.png'))
print("cargando botones")
boton_agregar=tkinter.Button(marco_derecho,image=imagen_boton_agregar,command=lambda : agregarpdf(listbox_pdfs,logbox))
boton_quitar=tkinter.Button(marco_derecho,image=imagen_boton_quitar, command=lambda : quitarpdf(listbox_pdfs,logbox))
boton_subir=tkinter.Button(marco_derecho, image=imagen_boton_subir)
boton_bajar=tkinter.Button(marco_derecho,image=imagen_boton_bajar)
boton_dog=tkinter.Button(marco_derecho,image=imagen_boton_dog)
boton_examinar=tkinter.Button(marco_inferior_derecho,text="Examinar...")
print("cargando el resto")
etiqueta_entry_url=tkinter.Label(marco_inferior_izquierdo,text="Ruta y nombre del pdf a generar:")
entry_url=tkinter.Entry(marco_inferior_izquierdo, width=95)
print('cargadas las definiciones; Presentando objetos...')

#               PACKS
marco_superior.pack (side = tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES, pady=(10,10),padx=(10,10))
marco_inferior.pack (side = tkinter.TOP, fill = tkinter.BOTH, expand=tkinter.YES, pady=(10,0),padx=(10,10))
marco_fondo.pack (side = tkinter.BOTTOM, fill = tkinter.BOTH, expand=tkinter.YES, pady=(0,10), padx=(10,10))
#		                     lado izquierdo
marco_izquierdo.pack ( side = tkinter.LEFT , fill=tkinter.BOTH, expand=tkinter.YES, pady=(10,10))
#				                   LISTBOX CON SCROLLBAR
listbox_pdfs.pack(side = tkinter.LEFT, fill = tkinter.BOTH, expand=tkinter.YES)
scrollbar_pdfs.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
listbox_pdfs.config(yscrollcommand = scrollbar_pdfs.set)
scrollbar_pdfs.config(command = listbox_pdfs.yview)
#		lado derecho
marco_derecho.pack( side = tkinter.RIGHT, fill=tkinter.BOTH, anchor=tkinter.N)
#				botones:
boton_agregar.pack( side = tkinter.TOP, anchor=tkinter.E, pady=(10,0),padx=(20,10))
boton_quitar.pack( side = tkinter.TOP, anchor=tkinter.E,padx=(0,10))
boton_subir.pack( side = tkinter.TOP, anchor=tkinter.E, pady=(40,0), padx=(0,10))
boton_bajar.pack( side = tkinter.TOP, anchor=tkinter.E, padx=(0,10))
boton_dog.pack( side = tkinter.BOTTOM, anchor=tkinter.E, pady=(40,10), padx=(0,10))
#		abajo
marco_inferior_izquierdo.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
marco_inferior_derecho.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=tkinter.YES)
etiqueta_entry_url.pack( side = tkinter.TOP, anchor=tkinter.W, pady=(0,0))
entry_url.pack( side = tkinter.TOP, anchor=tkinter.W)
boton_examinar.pack(side = tkinter.TOP, anchor=tkinter.E, pady=(15,0), padx=(0,10))
#		fondo	(log y scrollbar)
etiqueta_logbox.pack( side = tkinter.TOP, anchor=tkinter.W)
logbox.pack(side =tkinter.LEFT, fill = tkinter.BOTH, expand=tkinter.YES)
scrollbar_logbox.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)
logbox.config(yscrollcommand = scrollbar_logbox.set)
scrollbar_logbox.config(command = logbox.yview)


#####################################################################################
#				EL PROGRAMA:
#####################################################################################


logbox.insert(tkinter.END, licencias['gplv3'])
ventana.mainloop()

# TODO : trabajar sobre el show w de los argumentos

