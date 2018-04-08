# -*- coding: utf-8 -*-
"""

initial author: K.Draziotis
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import  Gtk, Pango
from genume_basic_script import *
""" improve basic_info.py and add suitable buttons  """

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Enumeration Script")
        self.set_default_size(500, 350)
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textview()
        self.create_buttons()
        #self.create_toolbar()
        
    def create_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 50, 1)
        self.textview = Gtk.TextView()
        scrolledwindow.add(self.textview)
        self.textbuffer = self.textview.get_buffer()
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)
        self.textview.override_font(Pango.font_description_from_string('DejaVu Sans Mono 12'))
       

    def create_buttons(self):
        self.button1 = Gtk.Button(label="Linux distro")   
        self.button1.connect("clicked", self.on_button1_clicked)
        self.grid.attach(self.button1, 0,  0, 1, 1)      
        
        self.button2 = Gtk.Button(label="kernel")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.grid.attach_next_to(self.button2,self.button1,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        self.button3 = Gtk.Button(label="users")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.grid.attach_next_to(self.button3,self.button2,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        self.button4 = Gtk.Button(label="CPU")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.grid.attach_next_to(self.button4,self.button3,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        self.button5 = Gtk.Button(label="Memory")
        self.button5.connect("clicked", self.on_button5_clicked)
        self.grid.attach_next_to(self.button5,self.button4,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        self.button6 = Gtk.Button(label="disks")
        self.button6.connect("clicked", self.on_button6_clicked)
        self.grid.attach_next_to(self.button6,self.button5,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        self.button7 = Gtk.Button(label="Desktop enviroment")
        self.button7.connect("clicked", self.on_button7_clicked)
        self.grid.attach_next_to(self.button7,self.button6,\
        Gtk.PositionType.RIGHT, 1, 1)
        
        #### network buttons
        self.button8 = Gtk.Button(label="Local ip")
        self.button8.connect("clicked", self.on_button8_clicked)
        self.grid.attach(self.button8, 0, 2, 1, 1)
        
        
        self.button9 = Gtk.Button(label="Public ip")
        self.button9.connect("clicked", self.on_button9_clicked)
        self.grid.attach_next_to(self.button9,self.button8,\
        Gtk.PositionType.RIGHT, 1, 1)
    

    def on_button1_clicked(self, widget):
        self.textbuffer.set_text(find_distro())

    def on_button7_clicked(self, widget):
        self.textbuffer.set_text(find_desktop_enviroment())

    def on_button2_clicked(self, widget):
        self.textbuffer.set_text(find_version())
    
    def on_button3_clicked(self, widget):
        self.textbuffer.set_text(users())
        
    def on_button4_clicked(self, widget):
        self.textbuffer.set_text(find_cpu('True'))
        
    def on_button5_clicked(self, widget):
        self.textbuffer.set_text(find_mem('True'))
        
    def on_button6_clicked(self, widget):
        self.textbuffer.set_text(disks())
        
    def on_button8_clicked(self, widget):
        self.textbuffer.set_text(local_ip())
        
    def on_button9_clicked(self, widget):
        self.textbuffer.set_text(public_ip())
        
        
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()