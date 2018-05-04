import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


# This is a number of classes that extend the GTK.Widget classes.
# Proper syntax and method naming were added, as well as more functionality.


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class FixedVBox(Gtk.Fixed):
    """
    A VBox of fixed size with added event listeners.
    """

    vbox = Gtk.VBox
    mainBox = Gtk.EventBox

    onClickId = 0
    onEnterId = 0
    onLeaveId = 0

    def __init__(self):
        Gtk.Fixed.__init__(self)
        self.mainBox = Gtk.EventBox()

        self.setSize(100, 200)
        self.mainBox.set_size_request(100, 200)
        self.vbox = Gtk.VBox(100, 200)

        self.mainBox.add(self.vbox)
        self.add(self.mainBox)
        self.show_all()

    def setBackgroundColorRGB(self, red, green, blue):
        # Use proper RGB
        r = translate(red, 0, 255, 0, 65535)
        g = translate(green, 0, 255, 0, 65535)
        b = translate(blue, 0, 255, 0, 65535)

        self.mainBox.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(r, g, b))

    def setBackgroundColor(self, hexademical):
        self.mainBox.modify_bg(Gtk.StateType.NORMAL,
                               Gdk.color_parse(hexademical))

    def setSize(self, width, height):
        self.set_size_request(width, height)
        self.mainBox.set_size_request(width, height)

    # Event handlers

    def setOnClickHandler(self, handler):
        self.onClickId = self.connect("button-press-event", handler)

    def setOnMouseEnterHandler(self, handler):
        self.onEnterId = self.mainBox.connect("enter-notify-event", handler)

    def setOnMouseLeaveHandler(self, handler):
        self.onLeaveId = self.mainBox.connect("leave-notify-event", handler)

    def removeOnClickHandler(self):
        self.disconnect(self.onClickId)

    def removeOnMouseEnterHandler(self):
        self.mainBox.disconnect(self.onEnterId)

    def removeOnMouseLeaveHandler(self):
        self.mainBox.disconnect(self.onLeaveId)

    def addChild(self, widget=Gtk.Widget):
        self.vbox.add(widget)
