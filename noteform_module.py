# PROJECT 4 IMPROVEMENT # 1
# MakeNote module
# imports
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import datetime # one module for working with dates and times
import json #this solution saves and opens json files. You may use a different file type and change the import accordingly


# the NoteForm() class creates a Toplevel window that is a note form containing fields for
# data entry for title, text, link, and tags. It also calculates a meta field with date, time, and timezone
# the Noteform class has an __init__() method, and a submit() method that is called by a submit button
# the class may contain additional methods to perform tasks like calculating the metadata, for example

# PROJECT 03 MODIFICATIONS
# ADD NOTE_ID, AUTHOR, AND SNIPPET FIELDS TO NoteForm

class NoteForm(tk.Toplevel):
    
    def __init__(self, master, notebook, notes): # initialize the new object
        super().__init__(master) # initialize it as a toplevel window
        # set the new window's default parameters
        # PROJECT 4 IMPROVEMENT # 2
        # - improve overall display (made window larger)
        self.geometry("900x600") 
        self.title('New Note')
        
        # create a frame in the new window that covers the entire window
        self.frame_main = tk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)
        self.frame_main.config(bg='light gray')

        #PROJECT 03 EDIT
        # moved the definition of self.notebook above the default note
        
        #define self.notebook as the notebook passed from the main window
        self.notebook = notebook
        #self.notes = notes (not necessary)
        
        # PROJECT 03 EDIT: ADD note_id
        self.last_id = len(self.notebook)
        

        
        #define default dummy text (for development purposes only)
        default_note = {"title":"new note title",
                     "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sit amet suscipit mi, non porttitor mauris. Aliquam in lorem risus. Proin mauris mauris, varius ac vulputate sed, tempor nec lacus. Morbi sodales turpis in placerat semper. Donec bibendum blandit ante sit amet hendrerit.", 
                    "link":"If there is a link with this note enter it here.",
                    "tags":"enter hashtags here",
                    "id":self.last_id + 1,
                    "author":"Scott Dempwolf",
                    "snippet":"# enter executable code snippet here \nprint('Hello World')",
                    "meta":"metadata added at submission"}
                    
        note = default_note # provided in anticipation of note editing functionality
        
        
        # create some labels and put them in the grid
        # we are using the grid layout. Notice the sticky='e' attribute. 
        # this causes the label to 'stick' to the 'east' side of the grid cell
        title_label = tk.Label(self.frame_main, bg='light gray', text='Note Title:')
        title_label.grid(padx=10, pady=10, row=1, column=0, sticky='e')

        text_label = tk.Label(self.frame_main, bg='light gray', text='Note Text:')
        text_label.grid(padx=10, pady=10, row=2, column=0, sticky='e')

        link_label = tk.Label(self.frame_main, bg='light gray', text='Note Link:')
        link_label.grid(padx=10, pady=10, row=3, column=0, sticky='e')

        tag_label = tk.Label(self.frame_main, bg='light gray', text='Note Tags:')
        tag_label.grid(padx=10, pady=10, row=4, column=0, sticky='e')
        
        tag_label = tk.Label(self.frame_main, bg='light gray', text='Note ID:')
        tag_label.grid(padx=10, pady=10, row=5, column=0, sticky='e')
        
        tag_label = tk.Label(self.frame_main, bg='light gray', text='Note Author:')
        tag_label.grid(padx=10, pady=10, row=6, column=0, sticky='e')
        
        tag_label = tk.Label(self.frame_main, bg='light gray', text='Snippet:')
        tag_label.grid(padx=10, pady=10, row=7, column=0, sticky='e')

        # create our note title entry field
        self.note_title = tk.Entry(self.frame_main, width=80)
        self.note_title.grid(padx=10, pady=10, row=1, column=1, sticky='w')
#         self.note_title.insert(0, note["title"]) # adds default text (useful during development)

        # create our note text field
        self.note_text = tk.Text(self.frame_main, height=10, width=60)
        self.note_text.grid(padx=10, pady=10, row=2, column=1)
        self.note_text.insert('1.0', note["text"]) # adds default text (useful during development)

        # create our note link entry field
        self.note_link = tk.Entry(self.frame_main, width=80)
        self.note_link.grid(padx=10, pady=10, row=3, column=1, sticky='w')
        self.note_link.insert(0, note["link"]) # adds default text (useful during development)

        # create our note tags entry field
        self.note_tags = tk.Entry(self.frame_main, width=80)
        self.note_tags.grid(padx=10, pady=10, row=4, column=1, sticky='w')
        self.note_tags.insert(0, note["tags"]) # adds default text (useful during development)

        # create our note id entry field
        self.note_id = tk.Entry(self.frame_main, width=80)
        self.note_id.grid(padx=10, pady=10, row=5, column=1, sticky='w')
        self.note_id.insert(0, note["id"]) # adds default text (useful during development)

        # create our note author entry field
        self.note_author = tk.Entry(self.frame_main, width=80)
        self.note_author.grid(padx=10, pady=10, row=6, column=1, sticky='w')
        self.note_author.insert(0, note["author"]) # adds default text (useful during development)

        # create our note snippet field
        self.snippet = tk.Text(self.frame_main, height=10, width=60)
        self.snippet.grid(padx=10, pady=10, row=7, column=1)
        self.snippet.insert('1.0', note["snippet"]) # adds default text (useful during development)        
        
        # create our note meta field if you want to add edit functionality
#         self.note_meta = tk.Entry(self.frame_main, width=80)
#         self.note_meta.grid(padx=10, pady=10, row=5, column=1, sticky='w')
#         self.note_meta.insert(0, note["meta"]) # adds default text (useful during development)
        

        # note that the parameters for the Entry box and Text box are slightly different.
        # The user can create multiple notes with the same note form. Each time the 'submit'
        # button is pressed, a new note is added to the notebook.

        b1 = tk.Button(self.frame_main, text='submit', command=self.submit)
        b1.grid(padx=10, pady=10, row=9, column=1, sticky='w')

        b5 = tk.Button(self.frame_main, text='close', command=self.destroy)
        b5.grid(padx=10, pady=10, row=9, column=0) 
       

    
    def submit(self):
        # calculate the date and time information for the meta field
        now = datetime.datetime.now() # gets the current date and time
        local_now = now.astimezone() # shows the local time and the GMT offset
        local_tz = local_now.tzinfo 
        created = datetime.datetime.now()
        
        # get all the input values and put them into a dictionary along with the metadata
        title = self.note_title.get()
        text = self.note_text.get('1.0', 'end').strip('\n')
        link = self.note_link.get()
        tags = self.note_tags.get()
        note_id = self.note_id.get()
        author = self.note_author.get()
        snippet = self.snippet.get('1.0', 'end').strip('\n')
        meta = f'note_id {note_id} created {created}, {local_tz} by {author}'
        note_dict = {'title':title, 'text':text, 'link':link, 'tags':tags, 'note_id':note_id, 'author':author, 'snippet':snippet, 'meta':meta}
        
        # add the dictionary to the notebook
        self.notebook.append(note_dict)
        self.last_id = self.last_id + 1
        self.note_id.delete(0, tk.END)
        self.note_id.insert(0, self.last_id + 1)
        
        return None
    

