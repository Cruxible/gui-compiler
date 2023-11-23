import gi
import subprocess
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MySexyVariables:
    x = os.listdir()
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    home_dir = os.path.join(os.path.expanduser("~"))

class TextBoxWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="TextBox Input")
        self.set_default_size(400, 400)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.entry = Gtk.Entry()
        self.entry.set_text("Enter the filename here")
        self.box.pack_start(self.entry, False, True, 0)

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, False, True, 0)
        self.set_default()  # Set the button as the default widget

        self.label = Gtk.Label()
        self.label.set_margin_top(10)  # Add a top margin
        self.label.set_margin_bottom(10)  # Add a bottom margin
        self.label.set_margin_start(10)  # Add a left margin
        self.label.set_margin_end(10)  # Add a right margin
        self.box.pack_start(self.label, True, True, 0)

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
        elif filename.endswith('.exe'):
            self.compile_executable(filename, filepath)

    def compile_c_lang(self, filename, filepath):
        output_file = filename.replace('.c', '')
        subprocess.run(['gcc', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete. {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_c_plusplus(self, filename, filepath):
        output_file = filename.replace('.cpp', '')
        subprocess.run(['g++', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_py(self, filename, filepath):
        subprocess.run(['python3', filename], check=True)
        print(f' {filename} execution/compilation complete.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_pyw(self, filename, filepath):
        subprocess.run(['python3', filename], check=True)
        print(f' {filename} execution/compilation complete.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_assembly(self, filename, filepath):
        subprocess.run(['nasm', '-f', 'win32', filename], check=True)
        output_file = filename.replace('.asm', '.obj')
        output_file2 = output_file.replace('.obj', '.exe')
        time.sleep(3)
        subprocess.run(['gcc', output_file, '-o', output_file2], check=True)
        print(f' {filename} compilation and execution complete.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_object_file(self, filename, filepath):
        output_file = filename.replace('.obj', '')
        subprocess.run(['gcc', filename, '-o', output_file], check=True)
        print(f' {filename} compilation complete.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

    def compile_executable(self, filename, filepath):
        subprocess.run(['chmod', '+x', filename], check=True)
        subprocess.run(['./'+filename], check=True)
        print(f' {filename} execution.\n {filepath}')
        self.label.set_text(f'{filename} compilation complete.\n{filepath}')

win = TextBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

