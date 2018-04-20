
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry


def main():
    MainWindow()


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="genume")
        self.set_default_size(500, 350)

        grid = Gtk.Box()
        self.add(grid)

        # setup the layout

        roots_container = self.generate_roots_container()
        grid.add(roots_container)
        subtrees_container = self.generate_subtrees_container()
        grid.add(subtrees_container)

        # fill the layout

        reg = Registry()
        reg.update()

        for name, entry in reg.root.items():
            if isinstance(entry, CategoryEntry):

                root = self.generate_root(name, entry)
                roots_container.add(root)

                # subtree = self.generate_subtree(name, entry)
                # subtrees_container.add(subtree)
            else:
                print("Scripts on the root scripts folder are not supported, yet") # TODO implement

        # handle events

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def generate_roots_container(self):
        
        return Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=6,
            border_width=6
        )

    def generate_root(self, name, entry: CategoryEntry):
        """Generate the tab like button that correspond to the given entry"""

        return Gtk.Button(
            label=name
        )

    def generate_subtrees_container(self):

        pass

    def generate_subtree(self, name, entry: CategoryEntry):
        """Generate the list like view that correspond to the given entry"""

        pass

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
