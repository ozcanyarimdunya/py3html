from html import escape as html_escape


class Element:
    tag = None
    attrs = None

    def __init__(self, *elements, attrs=None):
        self._elements = elements
        self._attrs = attrs or dict()
        assert self.tag is not None, "'tag' property cannot be None!"

    def add(self, *element):
        self._elements = self._elements + element

    @property
    def attributes(self):
        attrs = self._attrs.copy()
        attrs.update(self.attrs or dict())
        return "".join([f' {k}="{v}"' for k, v in attrs.items()])

    def pre_process(self):
        return f"<{self.tag}{self.attributes}>"

    def on_process(self):
        html = ""
        for element in self._elements:
            if isinstance(element, Element):
                html += element.html()
            else:
                html += html_escape(str(element))
        return html

    def post_process(self):
        return f"</{self.tag}>"

    def html(self):
        html = self.pre_process() or ""
        html += self.on_process() or ""
        html += self.post_process() or ""
        return html

    def __str__(self):
        return self.html()


class A(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a"""

    tag = "a"


class Abbr(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr"""

    tag = "abbr"


class Acronym(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/acronym"""

    tag = "acronym"


class Address(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address"""

    tag = "address"


class Applet(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/applet"""

    tag = "applet"


class Area(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area"""

    tag = "area"


class Article(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article"""

    tag = "article"


class Aside(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside"""

    tag = "aside"


class Audio(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio"""

    tag = "audio"


class B(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b"""

    tag = "b"


class Base(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base"""

    tag = "base"

    def pre_process(self):
        return f"<{self.tag}{self.attributes}/>"

    def on_process(self):
        return

    def post_process(self):
        return


class Basefont(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/basefont"""

    tag = "basefont"


class Bdi(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi"""

    tag = "bdi"


class Bdo(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo"""

    tag = "bdo"


class Bgsound(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bgsound"""

    tag = "bgsound"


class Big(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/big"""

    tag = "big"


class Blink(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blink"""

    tag = "blink"


class Blockquote(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote"""

    tag = "blockquote"


class Body(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body"""

    tag = "body"


class Br(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br"""

    tag = "br"

    def pre_process(self):
        return f"<{self.tag}{self.attributes}/>"

    def on_process(self):
        return

    def post_process(self):
        return


class Button(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button"""

    tag = "button"


class Canvas(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas"""

    tag = "canvas"


class Caption(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption"""

    tag = "caption"


class Center(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center"""

    tag = "center"


class Cite(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite"""

    tag = "cite"


class Code(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code"""

    tag = "code"


class Col(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col"""

    tag = "col"


class Colgroup(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup"""

    tag = "colgroup"


class Content(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/content"""

    tag = "content"


class Data(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data"""

    tag = "data"


class Datalist(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist"""

    tag = "datalist"


class Dd(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd"""

    tag = "dd"


class Del(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del"""

    tag = "del"


class Details(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details"""

    tag = "details"


class Dfn(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn"""

    tag = "dfn"


class Dialog(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog"""

    tag = "dialog"


class Dir(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dir"""

    tag = "dir"


class Div(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div"""

    tag = "div"


class Dl(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl"""

    tag = "dl"


class Dt(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt"""

    tag = "dt"


class Em(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em"""

    tag = "em"


class Embed(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed"""

    tag = "embed"


class Fieldset(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset"""

    tag = "fieldset"


class Figcaption(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption"""

    tag = "figcaption"


class Figure(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure"""

    tag = "figure"


class Font(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/font"""

    tag = "font"


class Footer(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer"""

    tag = "footer"


class Form(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form"""

    tag = "form"


class Frame(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/frame"""

    tag = "frame"


class Frameset(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/frameset"""

    tag = "frameset"


class Head(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head"""

    tag = "head"


class Header(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header"""

    tag = "header"


class H1(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h1"


class H2(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h2"


class H3(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h3"


class H4(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h4"


class H5(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h5"


class H6(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements"""

    tag = "h6"


class Hgroup(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup"""

    tag = "hgroup"


class Hr(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr"""

    tag = "hr"

    def pre_process(self):
        return f"<{self.tag}{self.attributes}/>"

    def on_process(self):
        return

    def post_process(self):
        return


class Html(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html"""

    tag = "html"


class I(Element):  # noqa E742
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i"""

    tag = "i"


class Iframe(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe"""

    tag = "iframe"


class Image(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/image"""

    tag = "image"


class Img(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img"""

    tag = "img"


class Input(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input"""

    tag = "input"

    def on_process(self):
        return

    def post_process(self):
        return


class Ins(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins"""

    tag = "ins"


class Kbd(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd"""

    tag = "kbd"


class Keygen(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/keygen"""

    tag = "keygen"


class Label(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label"""

    tag = "label"


class Legend(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend"""

    tag = "legend"


class Li(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li"""

    tag = "li"


class Link(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link"""

    tag = "link"

    def on_process(self):
        return

    def post_process(self):
        return


class Main(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main"""

    tag = "main"


class Map(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map"""

    tag = "map"


class Mark(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark"""

    tag = "mark"


class Marquee(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee"""

    tag = "marquee"


class Menu(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu"""

    tag = "menu"


class Menuitem(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menuitem"""

    tag = "menuitem"


class Meta(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta"""

    tag = "meta"

    def on_process(self):
        return

    def post_process(self):
        return


class Meter(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter"""

    tag = "meter"


class Nav(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav"""

    tag = "nav"


class Nobr(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nobr"""

    tag = "nobr"


class Noembed(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noembed"""

    tag = "noembed"


class Noframes(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noframes"""

    tag = "noframes"


class Noscript(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript"""

    tag = "noscript"


class Object(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object"""

    tag = "object"


class Ol(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol"""

    tag = "ol"


class Optgroup(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup"""

    tag = "optgroup"


class Option(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option"""

    tag = "option"


class Output(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output"""

    tag = "output"


class P(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p"""

    tag = "p"


class Param(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/param"""

    tag = "param"


class Picture(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture"""

    tag = "picture"


class Plaintext(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/plaintext"""

    tag = "plaintext"


class Portal(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal"""

    tag = "portal"


class Pre(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre"""

    tag = "pre"


class Progress(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress"""

    tag = "progress"


class Q(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q"""

    tag = "q"


class Rb(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rb"""

    tag = "rb"


class Rp(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp"""

    tag = "rp"


class Rt(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt"""

    tag = "rt"


class Rtc(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rtc"""

    tag = "rtc"


class Ruby(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby"""

    tag = "ruby"


class S(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s"""

    tag = "s"


class Samp(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp"""

    tag = "samp"


class Script(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script"""

    tag = "script"


class Section(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section"""

    tag = "section"


class Select(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select"""

    tag = "select"


class Shadow(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/shadow"""

    tag = "shadow"


class Slot(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot"""

    tag = "slot"


class Small(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small"""

    tag = "small"


class Source(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source"""

    tag = "source"


class Spacer(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/spacer"""

    tag = "spacer"


class Span(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span"""

    tag = "span"


class Strike(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strike"""

    tag = "strike"


class Strong(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong"""

    tag = "strong"


class Style(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style"""

    tag = "style"


class Sub(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub"""

    tag = "sub"


class Summary(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary"""

    tag = "summary"


class Sup(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup"""

    tag = "sup"


class Table(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table"""

    tag = "table"


class Tbody(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody"""

    tag = "tbody"


class Td(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td"""

    tag = "td"


class Template(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template"""

    tag = "template"


class Textarea(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea"""

    tag = "textarea"


class Tfoot(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot"""

    tag = "tfoot"


class Th(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th"""

    tag = "th"


class Thead(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead"""

    tag = "thead"


class Time(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time"""

    tag = "time"


class Title(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title"""

    tag = "title"


class Tr(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr"""

    tag = "tr"


class Track(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track"""

    tag = "track"


class Tt(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tt"""

    tag = "tt"


class U(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u"""

    tag = "u"


class Ul(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul"""

    tag = "ul"


class Var(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var"""

    tag = "var"


class Video(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video"""

    tag = "video"


class Wbr(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr"""

    tag = "wbr"


class Xmp(Element):
    """https://developer.mozilla.org/en-US/docs/Web/HTML/Element/xmp"""

    tag = "xmp"
