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
licencias['gplv3']="""    pdfdog.py  Copyright (C) 2022  Cristian Tocci
    This program comes with ABSOLUTELY NO WARRANTY; for details press 'w'.
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
import pikepdf

pdf_salida_defaultdir='~'
pdf_salida_default='output.pdf'


def loguea(logbox,linea=str()):
        logbox.configure(state='normal')
        logbox.insert(tkinter.END, linea)
        logbox.see(tkinter.END)
        logbox.configure(state='disabled')

def file_browser():
        tipos=(
                ('archivos pdf','*.pdf'),
                ('Todos los archivos','*.*')
        )
        archivo_url = filedialog.askopenfilenames(
                title='Agregar PDF...',
                filetypes=(tipos)
        )
        return archivo_url


def directory_browser(titulo=str(),defaultdir=str()):
        if not titulo:
                titulo='Seleccione directorio destino...'
        directorio=filedialog.askdirectory(title=titulo)
        if not directorio:
               directorio=defaultdir
        return os.path.expanduser(os.path.normpath(directorio))


def agregarpdf(listbox_pdfs,logbox):
        archivo_urls=file_browser()
        for archivo_url in archivo_urls:
                listbox_pdfs.insert(tkinter.END, archivo_url)
                listbox_pdfs.see(tkinter.END)
                loguea(logbox,'Archivo agregado: '+str(archivo_url)+'\n')


def quitarpdf(listbox_pdfs,logbox):
        for i in listbox_pdfs.curselection()[::-1]:
                loguea(logbox,'Quitar :'+str(listbox_pdfs.get(i))+'\n')
                listbox_pdfs.delete(i)


def moverarriba(listbox_pdfs,logbox):
        indices_seleccion=listbox_pdfs.curselection()
        if not indices_seleccion:
                return
        for posicion in indices_seleccion:
                if posicion == 0:
                        return
                contenido=listbox_pdfs.get(posicion)
                listbox_pdfs.delete(posicion)
                listbox_pdfs.insert(posicion-1,contenido)
        listbox_pdfs.selection_clear(0,tkinter.END)
        for indice in indices_seleccion:
                listbox_pdfs.selection_set(indice-1)
        listbox_pdfs.see(indices_seleccion[0]-1)


def moverabajo(listbox_pdfs,logbox):
        indices_seleccion=listbox_pdfs.curselection()
        if not indices_seleccion:
                return
        if indices_seleccion[-1] == listbox_pdfs.size()-1:
                return
        for posicion in indices_seleccion[::-1]:
                contenido = listbox_pdfs.get(posicion)
                listbox_pdfs.delete(posicion)
                listbox_pdfs.insert(posicion+1,contenido)
        listbox_pdfs.selection_clear(0,tkinter.END)
        for indice in indices_seleccion:
                listbox_pdfs.selection_set(indice+1)
        listbox_pdfs.see(indices_seleccion[-1]+1)


def examinar(entry_url,logbox):
        head_url=os.path.expanduser(os.path.normpath(pdf_salida_defaultdir))
        tail_url=os.path.expanduser(os.path.normpath(pdf_salida_default))
        if len(entry_url.get()) != 0:
                head_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[0]
                tail_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[1]
        directorio_seleccionado=directory_browser('Seleccione directorio para '+tail_url,head_url)
        entry_url.delete(0,tkinter.END)
        if not directorio_seleccionado:
                directorio_seleccionado = head_url
        entry_url.insert(tkinter.END, os.path.join(directorio_seleccionado,tail_url))
        return


def pdfdog (listbox_pdf,entry_url,logbox):
        head_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[0]
        tail_url=os.path.split(os.path.expanduser(os.path.normpath(entry_url.get())))[1]
        if (not head_url) or (not tail_url) or (not os.path.isdir(os.path.expanduser(os.path.normpath(head_url)))):
                loguea(logbox,'***No se ha generado ningún pdf: Ruta de destino no válida.\n')
                return
        lista_pdfs=[]
        for i in range (0,listbox_pdfs.size()):
                lista_pdfs.append(listbox_pdfs.get(i))
        if len(lista_pdfs)>0:
                loguea(logbox,'Concatenando ('+str(len(lista_pdfs))+') PDFS:\n')
                pdf = pikepdf.Pdf.new()
                for archivo_pdf in lista_pdfs:
                        src=pikepdf.Pdf.open(archivo_pdf)
                        pdf.pages.extend(src.pages)
                        loguea(logbox,'['+str(lista_pdfs.index(archivo_pdf)+1)+'] :'+str(os.path.split(archivo_pdf)[1])+'\n')
                pdf.save(os.path.join(head_url,tail_url))
                loguea(logbox,'...[LISTO]\n')
                return
        loguea(logbox,'***No se ha generado ningún pdf: Lista vacía.\n')


def show_w(ventana_principal,textow):
        ventana_w = tkinter.Toplevel(ventana_principal)
        ventana_w.title('This program comes with ABSOLUTELY NO WARRANTY')
        ventana_w.geometry('800x600')
        tkinter.Label(ventana_w,text=textow).pack()
        ventana_w.focus_set()
        ventana_w.bind('<Escape>', lambda event : ventana_w.destroy())


def ayuda(ventana_principal):
        texto_ayuda="""
        F1 : Esta ayuda.
        w : Más acerca de la licencia
        z : Agrega PDF
        x : Quita PDF
        u : Mueve hacia arriba los PDF seleccionados.
        j : Mueve hacia abajo los PDF seleccionados.
        Enter : Concatena los pdf en la lista.
        Esc : Cierra la aplicación / Cierra esta ventana
        """
        ventana_ayuda = tkinter.Toplevel(ventana_principal)
        ventana_ayuda.title(' Atajos y ayuda')
        tkinter.Label(ventana_ayuda,text=texto_ayuda,justify='left').pack(side=tkinter.LEFT,padx=(0,30), pady=(10,10))
        ventana_ayuda.focus_set()
        ventana_ayuda.bind('<Escape>', lambda event : ventana_ayuda.destroy())


#####################################################################################
#			GUI :
#####################################################################################
ventana=tkinter.Tk()
ventana.title("PDF DOG")
ventana.geometry("800x600")

#               DEFINICIONES
marco_superior=tkinter.Frame(ventana)
marco_inferior=tkinter.Frame(ventana)
marco_fondo=tkinter.Frame(ventana)
marco_izquierdo= tkinter.Frame(marco_superior)
marco_derecho= tkinter.Frame(marco_superior)
marco_inferior_izquierdo=tkinter.Frame(marco_inferior)
marco_inferior_derecho=tkinter.Frame(marco_inferior)
listbox_pdfs = tkinter.Listbox(marco_izquierdo, selectmode="multiple")
scrollbar_pdfs = tkinter.Scrollbar(marco_izquierdo)
etiqueta_logbox=tkinter.Label(marco_fondo,text="Log:")
logbox=tkinter.Text(marco_fondo,height=5,width = 95, state='disabled')
scrollbar_logbox = tkinter.Scrollbar(marco_fondo)
imagen_boton_agregar=tkinter.PhotoImage(file=os.path.normpath('./res/PDF_mas-64x64.png'))
imagen_boton_quitar=tkinter.PhotoImage(file=os.path.normpath('./res/PDF_menos-64x64.png'))
imagen_boton_subir=tkinter.PhotoImage(file=os.path.normpath('./res/arrow_up-32x32.png'),height=32,width=32)
imagen_boton_bajar=tkinter.PhotoImage(file=os.path.normpath('./res/arrow_down-32x32.png'),height=32,width=32)
imagen_boton_dog=tkinter.PhotoImage(file=os.path.normpath('./res/olicara-64x64.png'))
boton_agregar=tkinter.Button(marco_derecho,image=imagen_boton_agregar,command = lambda : agregarpdf(listbox_pdfs,logbox))
boton_quitar=tkinter.Button(marco_derecho,image=imagen_boton_quitar, command = lambda : quitarpdf(listbox_pdfs,logbox))
boton_subir=tkinter.Button(marco_derecho, image=imagen_boton_subir, command = lambda : moverarriba(listbox_pdfs,logbox))
boton_bajar=tkinter.Button(marco_derecho,image=imagen_boton_bajar, command = lambda : moverabajo(listbox_pdfs,logbox))
boton_dog=tkinter.Button(marco_derecho,image=imagen_boton_dog, command = lambda : pdfdog (listbox_pdfs,entry_url,logbox))
etiqueta_entry_url=tkinter.Label(marco_inferior_izquierdo,text="Ruta y nombre del pdf a generar:")
entry_url=tkinter.Entry(marco_inferior_izquierdo, width=95)
boton_examinar=tkinter.Button(marco_inferior_derecho,text="Examinar...", command = lambda : examinar(entry_url,logbox))

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
#				BINDEOS:
#####################################################################################


ventana.bind('<F1>', lambda event : ayuda(ventana))
ventana.bind('<w>', lambda event : show_w(ventana,licencias['textow']))
ventana.bind('<z>', lambda event : agregarpdf(listbox_pdfs,logbox))
ventana.bind('<x>', lambda event : quitarpdf(listbox_pdfs,logbox))
ventana.bind('<u>', lambda event : moverarriba(listbox_pdfs,logbox))
ventana.bind('<j>', lambda event : moverabajo(listbox_pdfs,logbox))
ventana.bind('<Return>', lambda event : pdfdog (listbox_pdfs,entry_url,logbox))
ventana.bind('<Escape>', lambda event : ventana.destroy())
#####################################################################################
#				EL PROGRAMA:
#####################################################################################


loguea(logbox,licencias['gplv3'])
loguea(logbox,'Presione <F1> para ayuda.\n')
logbox.see(0.0)
entry_url.insert(tkinter.END,os.path.expanduser(os.path.normpath(os.path.join(pdf_salida_defaultdir,pdf_salida_default))))


ventana.mainloop()
