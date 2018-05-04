import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry
from genume.exports.terminal import print_enumeration

from genume.view.event_panels import FixedVBox


def main():
    MainWindow()
    Gtk.main()


# Define colors -> subject to change
# TODO: Add CSS support
primary_color_light = "#FFFFFF"
accent_color = "#673AB7"
accent_color_light = "#9575CD"

LOGO = "data/images/logo.png"  # The logo image must be 200X100 px


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="genume")
        self.set_default_size(750, 500)

        reg = Registry()
        reg.update()
        print_enumeration(reg.root)  # TODO remove, here for debugging

        # setup the layout
        self.set_titlebar(self.generate_header_bar())
        self.add(self.generate_main_view(reg))

        # handle events
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

        # store state
        self.reg = reg

    def refresh(self):
        """Updates the registry and refreshes the view"""
        # TODO improve
        self.reg.update()
        current_page = self.subtrees_container.get_current_page()
        self.remove(self.get_child())
        self.add(self.generate_main_view(self.reg))
        self.show_all()
        self.subtrees_container.set_current_page(current_page)

    def generate_header_bar(self):

        bar = Gtk.HeaderBar(
            title="genume",
            show_close_button=True
        )

        menu_button = Gtk.MenuButton()
        menu_button.add(Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.BUTTON))
        menu_button.set_popup(self.generate_header_bar_menu())
        bar.pack_end(menu_button)

        refresh_button = Gtk.Button()
        refresh_button.add(Gtk.Image(stock=Gtk.STOCK_REFRESH))
        refresh_button.connect("clicked", self.request_refresh)
        bar.pack_start(refresh_button)

        return bar

    def generate_header_bar_menu(self):
        """Generates and returns a menu for the header bar menu button"""

        menu = Gtk.Menu(halign=Gtk.Align.END)

        def add(name, func):
            item = Gtk.MenuItem(name)
            item.connect("activate", func)
            menu.append(item)

        def add_separator():
            menu.append(Gtk.SeparatorMenuItem())

        add("Refresh", self.request_refresh)
        add_separator()
        add("About", self.request_about)
        add("Close", self.request_close)

        # TODO extend the menu

        menu.show_all()
        return menu

    def generate_main_view(self, reg):
        """Generate and return the content of the window"""

        def srcoll_wrap(container, vertical=False):
            s = Gtk.ScrolledWindow()
            s.set_policy(
                Gtk.PolicyType.AUTOMATIC if vertical else Gtk.PolicyType.NEVER,
                Gtk.PolicyType.AUTOMATIC)
            s.add(container)
            return s

        grid = Gtk.Box()
        roots_container = self.generate_roots_container()

        # The inner container is used so that the only content that is
        # scrollable is the tabs and not the logo
        inner_container = Gtk.VBox()
        inner_container.pack_end(srcoll_wrap(roots_container), True, True, 0)

        grid.pack_start(inner_container, False, False, 0)

        subtrees_container = self.generate_subtrees_container()

        grid.pack_start(srcoll_wrap(subtrees_container, True), True, True, 0)

        # fill the layout

        # Add logo
        logo = Item()
        logo.setImage(LOGO)
        logo.setBackgroundColor(primary_color_light)
        logo.noEventListeners()
        inner_container.pack_start(logo, False, False, 0)

        # TODO improve, covert Registry to a signleton
        reg = Registry()
        reg.update()
        # TODO remove, here for debugging
        print_enumeration(reg.root)

        for name, entry in reg.root.items():
            if isinstance(entry, CategoryEntry):

                self.generate_root_and_subtree(name, entry, roots_container, subtrees_container)
            else:
                print("Scripts on the root scripts folder are not supported, yet")  # TODO implement

        self.subtrees_container = subtrees_container
        return grid

    def generate_root_and_subtree(self, name, entry: CategoryEntry, roots_container, subtrees_container):
        """Generate a root tab and the corresponding subtree view"""

        root = self.generate_root(name, entry)
        roots_container.pack_start(root, False, False, 0)

        subtree = self.generate_subtree(name, entry)
        subtrees_container.append_page(subtree, Gtk.Label(label=name))

        # setup the events
        root.page_index = subtrees_container.get_n_pages() - 1
        root.parent = self

    def generate_roots_container(self):
        mainBox = Gtk.VBox()
        mainBox.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(accent_color))

        return mainBox

    def generate_root(self, name, entry: CategoryEntry):
        """Generate the tab like button that correspond to the given entry"""

        item = Item()
        item.setBackgroundColor(accent_color)
        item.setTitle(name)

        return item

    def generate_subtrees_container(self):
        backBox = Gtk.Notebook(show_tabs=False)
        # backBox.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(primary_color_light))

        return backBox

    def generate_subtree(self, name, entry: CategoryEntry):
        """Generate the list like view that correspond to the given entry"""

        # create the store

        store = Gtk.ListStore(str, str)
        for name, entry in entry.items():
            if isinstance(entry, CategoryEntry):
                print("Scripts on the sub root folders are not supported, yet")  # TODO implement
            else:
                store.append([self.format_name(name), repr(entry)])

        # create the tree view

        tree = Gtk.TreeView(store)
        # Enable this if the show_tabs value is set to True
        # tree.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(primary_color_light))

        # TODO: find a way to set this background
        for i, column_title in enumerate(["Name", "Value"]):

            tree.append_column(Gtk.TreeViewColumn(
                column_title,
                Gtk.CellRendererText(),
                text=i
            ))
        return tree

    def format_name(self, name):
        # TODO extend
        return name.replace("_", " ")

    def show_root(self, button):
        """Changes to the tab given by the page_index value of the button"""
        self.subtrees_container.set_current_page(button.page_index)

    def request_refresh(self, _):
        self.refresh()

    def request_about(self, _):
        # TODO show about dialog
        pass

    def request_close(self, _):
        self.close()

    def show_root(self, page_index):
        self.subtrees_container.set_current_page(page_index)


class Item(FixedVBox):
    """
    This class represents a root element.
    """

    title = ""
    page_index = ""
    parent = MainWindow

    def __init__(self):
        FixedVBox.__init__(self)

        self.setSize(200, 50)

        self.setOnClickHandler(self.on_click)
        self.setOnMouseEnterHandler(self.on_mouse_enter)
        self.setOnMouseLeaveHandler(self.on_mouse_leave)

    def setTitle(self, title=""):
        label = Gtk.Label(title)
        label.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse(primary_color_light))
        self.addChild(label)
        self.title = title

    def setImage(self, path):
        image = Gtk.Image()
        image.set_from_file(path)
        self.addChild(image)

    def noEventListeners(self):
        self.removeOnClickHandler()
        self.removeOnMouseEnterHandler()
        self.removeOnMouseLeaveHandler()

    # Event handlers

    def on_click(self, widget, event):
        self.parent.show_root(self.page_index)

    def on_mouse_enter(self, widget, event):
        self.setBackgroundColor(accent_color_light)
        self.parent.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))

    def on_mouse_leave(self, widget, event):
        self.setBackgroundColor(accent_color)
        self.parent.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))

# class ScrollingItem:
    
