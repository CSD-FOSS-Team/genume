import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import math

from genume.registry.registry import Registry
from genume.registry.category import CategoryEntry
from genume.exports.terminal import print_enumeration

from genume.view.event_panels import FixedVBox


def main():
    MainWindow()
    Gtk.main()


LOGO = "data/images/logo.png"  # The logo image must be 200X100 px
CSS = "genume/view/styles.css"
REFRESH_ICON = "data/icons/refresh.png"

# Sizes
WIDTH = 400
HEIGHT = 350

class MainWindow(Gtk.Window):
    selected_tab = None

    def __init__(self):
        Gtk.Window.__init__(self, title="genume")
        self.set_default_size(WIDTH, HEIGHT)

        reg = Registry()
        reg.update()
        # print_enumeration(reg.root)  # TODO remove, here for debugging

        # Load css once
        self.load_css()

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

        add_separator()
        add("About", self.request_about)
        add("Close", self.request_close)

        # TODO extend the menu

        menu.show_all()
        return menu

    def generate_main_view(self, reg):
        """Generate and return the content of the window"""
        
        main_view = Gtk.Overlay()

        def srcoll_wrap(container, vertical=False):
            s = Gtk.ScrolledWindow()
            s.set_policy(
                Gtk.PolicyType.AUTOMATIC if vertical else Gtk.PolicyType.NEVER,
                Gtk.PolicyType.AUTOMATIC)
            s.add(container)
            return s

        def set_button_location(s, b, allocation):
            allocation.x = 200 - 25
            allocation.y = HEIGHT - 100
            allocation.width = 50
            allocation.height = 50
            return allocation

        grid = Gtk.Box()
        grid.set_size_request(WIDTH, HEIGHT)
        main_view.add(grid)

        refresh_button = self.generate_refresh_button()
        main_view.add_overlay(refresh_button)
        main_view.set_overlay_pass_through(refresh_button, True)
        main_view.connect("get-child-position", set_button_location)


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
        inner_container.pack_start(self.load_logo(), False, False, 0)

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
        return main_view

    def load_css(self):
        style_provider = Gtk.CssProvider()

        css = open(CSS, 'rb')
        css_data = css.read()
        css.close()

        style_provider.load_from_data(css_data)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,     
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def load_logo(self):
        logo = Item()
        logo.setImage(LOGO)
        logo.noEventListeners()
        logo.addClass("logo")

        return logo

    def generate_refresh_button(self):
        container = Gtk.Fixed()
        container.set_size_request(40, 40)
        event = Gtk.EventBox()
        event.set_size_request(40,40)
        button = Gtk.Box()
        icon = Gtk.Image()
        icon.set_from_file(REFRESH_ICON)
        icon.set_opacity(0.9)
        button.pack_start(icon, True, True, 0)
        button.get_style_context().add_class("refresh-button")

        def on_mouse_enter(w, e):
            self.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))
            button.get_style_context().add_class("refresh-button-hover")

        def on_mouse_leave(w, e):
            self.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
            button.get_style_context().remove_class("refresh-button-hover")

        def refresh(w, e):
            self.request_refresh(self)

        event.connect("button-press-event", refresh)
        event.connect("enter-notify-event", on_mouse_enter)

        event.connect("leave-notify-event", on_mouse_leave)

        event.add(button)
        container.add(event)

        return container
        

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
        # mainBox.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse(accent_color))
        mainBox.set_name("tab-holder")

        return mainBox

    def generate_root(self, name, entry: CategoryEntry):
        """Generate the tab like button that correspond to the given entry"""

        item = Item()
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
        label.get_style_context().add_class("label")
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
        self.addClass("tab-clicked")
        if(self.parent.selected_tab != None):
            self.parent.selected_tab.removeClass("tab-clicked")
        self.parent.selected_tab = self

    # TODO: Find a way for pseudoclasses to work
    def on_mouse_enter(self, widget, event):
        self.addClass("tab-hover")
        self.parent.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.HAND2))

    def on_mouse_leave(self, widget, event):
        self.removeClass("tab-hover")
        self.parent.get_window().set_cursor(Gdk.Cursor(Gdk.CursorType.ARROW))
