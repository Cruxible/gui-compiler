#!/usr/bin/env python3
#Created by: Ioannes Cruxibulum
#Date Created: 11-23-23

import os
import subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from gi.repository import GLib

class MySexyVariables:
    x = os.listdir()
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    home_dir = os.path.join(os.path.expanduser("~"))

class TextBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pyra Compiler")
        self.set_default_size(400, 350)
        self.set_border_width(10)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.entry.set_name('first_entry')
        self.entry.set_text("Enter the filename here")
        self.box.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="Compile/Run File")
        self.button.set_name('first_button')
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        #create the label
        self.note_label = Gtk.Label(label="Notes")
        #sets the css name
        self.note_label.set_name("note_label")
        self.box.pack_start(self.note_label, True, True, 0)

        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.box.pack_start(self.scrollable_treelist, True, True, 0)
        self.textview = Gtk.TextView()
        self.textview.set_name('text_box')
        self.textbuffer = self.textview.get_buffer()
        self.scrollable_treelist.add(self.textview)

        # Create a button
        self.save_button = Gtk.Button(label="Save to File")
        self.save_button.set_name('save_button')
        self.box.pack_start(self.save_button, True, True, 0)
        # Connect the "clicked" signal to the save_to_file method
        self.save_button.connect("clicked", self.save_to_file)

        # Add a scrolled window for displaying messages
        self.scrolled_window = Gtk.ScrolledWindow()
        self.box.pack_start(self.scrolled_window, True, True, 0)
        # Add a label for displaying messages inside the scrolled window
        self.message_label = Gtk.Label()
        self.message_label.set_name('message_label')
        self.scrolled_window.add(self.message_label)
        self.message_label.set_text(f"Welcome Sentient!")

        # Apply CSS
        css_provider = Gtk.CssProvider()
        css = """
        #first_entry {
            font-family: Sans;
            font-size: 20px;
        }
        #first_button {
            font-family: Sans;
            font-size: 20px;
        }
        #note_label {
            font-family: Sans;
            font-size: 20px;
        }
        #text_box {
            font-family: Sans;
            font-size: 20px;
        }
        #save_button {
            font-family: Sans;
            font-size: 20px;
        }
        #message_label {
            font-family: Sans;
            font-size: 20px;
        }
        """
        css_provider.load_from_data(css.encode())
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def on_button_clicked(self, widget):
        filename = self.entry.get_text()
        print("Filename: " + filename)
        # Add your code here
        found = False
        for dirpath, dirnames, filenames in os.walk(MySexyVariables.desktop):
            if filename in filenames:
                filepath = os.path.join(dirpath, filename)
                found = True
                os.chdir(dirpath)
                break
        if not found:
            for dirpath, dirnames, filenames in os.walk(MySexyVariables.home_dir):
                if filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    found = True
                    os.chdir(dirpath)
                    break
        if not found:
            raise FileNotFoundError(f"{filename} not found in Desktop or pyra env")
        # Call your compile functions here based on the file extension
        if filename.endswith('.c'):
            self.compile_c_lang(filename, filepath)
        elif filename.endswith('.cpp'):
            self.compile_c_plusplus(filename, filepath)
        elif filename.endswith('.py'):
            self.compile_py(filename, filepath)
        elif filename.endswith('.pyw'):
            self.compile_pyw(filename, filepath)
        elif filename.endswith('.asm'):
            self.compile_assembly(filename, filepath)
        elif filename.endswith('.obj'):
            self.compile_object_file(filename, filepath)
        elif filename.endswith(''):
            self.compile_executable(filename, filepath)

    def compile_c_lang(self, filename, filepath):
        output_file = filename.replace('.c', '')
        subprocess.run(['gcc', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete. {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_c_plusplus(self, filename, filepath):
        output_file = filename.replace('.cpp', '')
        subprocess.run(['g++', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_py(self, filename, filepath):
        subprocess.run(['python3', filename], check=True)
        print(f' {filename} execution/compilation complete.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_pyw(self, filename, filepath):
        subprocess.run(['python3', filename], check=True)
        print(f' {filename} execution/compilation complete.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_assembly(self, filename, filepath):
        subprocess.run(['nasm', '-f', 'win32', filename], check=True)
        output_file = filename.replace('.asm', '.obj')
        output_file2 = output_file.replace('.obj', '.exe')
        time.sleep(3)
        subprocess.run(['gcc', output_file, '-o', output_file2], check=True)
        print(f' {filename} compilation and execution complete.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_object_file(self, filename, filepath):
        output_file = filename.replace('.obj', '')
        subprocess.run(['gcc', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_executable(self, filename, filepath):
        subprocess.run(['chmod', '+x', filename], check=True)
        subprocess.run(['./'+filename], check=True)
        print(f' {filename} execution.\n {filepath}')
        self.message_label.set_text(f'{filename} compilation complete.\n{filepath}')

    def save_to_file(self, button):
        self.dialog = Gtk.FileChooserDialog(
            title="Please choose a file",
            parent=self,
            action=Gtk.FileChooserAction.SAVE
        )
        self.dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_SAVE,
            Gtk.ResponseType.OK
        )
        # Set the current folder to 'Videos'
        self.dialog.set_current_folder(os.path.expanduser('~/Videos'))
        self.dialog.show_all()  # Ensure the dialog is shown first
        self.dialog.resize(450, 300)
        response = self.dialog.run()
        if response == Gtk.ResponseType.OK:
            filename = self.dialog.get_filename()
            textbuffer = self.textview.get_buffer()
            start_iter = textbuffer.get_start_iter()
            end_iter = textbuffer.get_end_iter()
            text = textbuffer.get_text(start_iter, end_iter, False)
            with open(filename, 'w') as f:
                f.write(text)
                self.message_label.set_text(f"File Saved")
        self.dialog.destroy()


if __name__ == "__main__":
    win = TextBoxWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

