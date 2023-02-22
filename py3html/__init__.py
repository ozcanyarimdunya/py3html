from collections import namedtuple
from html import escape


class Html(namedtuple("Html", ["html"])):
    __slots__ = ()

    def __str__(self):
        return self.html


def element(tag, self_closing=False, **default_attributes):
    def wrapper(*content_or_elements, **attributes):
        string = f"<{tag}"
        for k, v in {**default_attributes, **attributes}.items():
            if k == "class_":
                k = "class"
            if v is None:
                string += f" {k}"
            elif isinstance(v, (int, float)):
                string += f" {k}={v}"
            else:
                string += f" {k}=\"{v}\""

        if not self_closing:
            string += ">"

        for each in content_or_elements:
            if isinstance(each, Html):
                string += each.html
            else:
                string += escape(str(each))

        if self_closing:
            string += " />"
        else:
            string += f"</{tag}>"

        string += "\n"

        return Html(string)

    return wrapper


a = element(tag="a")
abbr = element(tag="abbr")
acronym = element(tag="acronym")
address = element(tag="address")
applet = element(tag="applet")
area = element(tag="area", self_closing=True)
article = element(tag="article")
aside = element(tag="aside")
audio = element(tag="audio")
b = element(tag="b")
base = element(tag="base", self_closing=True)
basefont = element(tag="basefont")
bdi = element(tag="bdi")
bdo = element(tag="bdo")
bgsound = element(tag="bgsound")
big = element(tag="big")
blink = element(tag="blink")
blockquote = element(tag="blockquote")
body = element(tag="body")
br = element(tag="br", self_closing=True)
button = element(tag="button")
canvas = element(tag="canvas")
caption = element(tag="caption")
center = element(tag="center")
cite = element(tag="cite")
code = element(tag="code")
col = element(tag="col", self_closing=True)
colgroup = element(tag="colgroup")
command = element(tag="command", self_closing=True)
content = element(tag="content")
data = element(tag="data")
datalist = element(tag="datalist")
dd = element(tag="dd")
del_ = element(tag="del")
details = element(tag="details")
dfn = element(tag="dfn")
dialog = element(tag="dialog")
dir = element(tag="dir")
div = element(tag="div")
dl = element(tag="dl")
dt = element(tag="dt")
em = element(tag="em")
embed = element(tag="embed", self_closing=True)
fieldset = element(tag="fieldset")
figcaption = element(tag="figcaption")
figure = element(tag="figure")
font = element(tag="font")
footer = element(tag="footer")
form = element(tag="form")
frame = element(tag="frame")
frameset = element(tag="frameset")
head = element(tag="head")
header = element(tag="header")
h1 = element(tag="h1")
h2 = element(tag="h2")
h3 = element(tag="h3")
h4 = element(tag="h4")
h5 = element(tag="h5")
h6 = element(tag="h6")
hgroup = element(tag="hgroup")
hr = element(tag="hr", self_closing=True)
html = element(tag="html")
i = element(tag="i")
iframe = element(tag="iframe")
image = element(tag="image")
img = element(tag="img", self_closing=True)
input = element(tag="input", self_closing=True)
ins = element(tag="ins")
kbd = element(tag="kbd")
keygen = element(tag="keygen", self_closing=True)
label = element(tag="label")
legend = element(tag="legend")
li = element(tag="li")
link = element(tag="link", self_closing=True)
main = element(tag="main")
map = element(tag="map")
mark = element(tag="mark")
marquee = element(tag="marquee")
menu = element(tag="menu")
menuitem = element(tag="menuitem")
meta = element(tag="meta", self_closing=True)
meter = element(tag="meter")
nav = element(tag="nav")
nobr = element(tag="nobr")
noembed = element(tag="noembed")
noframes = element(tag="noframes")
noscript = element(tag="noscript")
object = element(tag="object")
ol = element(tag="ol")
optgroup = element(tag="optgroup")
option = element(tag="option")
output = element(tag="output")
p = element(tag="p")
param = element(tag="param", self_closing=True)
picture = element(tag="picture")
plaintext = element(tag="plaintext")
portal = element(tag="portal")
pre = element(tag="pre")
progress = element(tag="progress")
q = element(tag="q")
rb = element(tag="rb")
rp = element(tag="rp")
rt = element(tag="rt")
rtc = element(tag="rtc")
ruby = element(tag="ruby")
s = element(tag="s")
samp = element(tag="samp")
script = element(tag="script")
section = element(tag="section")
select = element(tag="select")
shadow = element(tag="shadow")
slot = element(tag="slot")
small = element(tag="small")
source = element(tag="source", self_closing=True)
spacer = element(tag="spacer")
span = element(tag="span")
strike = element(tag="strike")
strong = element(tag="strong")
style = element(tag="style")
sub = element(tag="sub")
summary = element(tag="summary")
sup = element(tag="sup")
table = element(tag="table")
tbody = element(tag="tbody")
td = element(tag="td")
template = element(tag="template")
textarea = element(tag="textarea")
tfoot = element(tag="tfoot")
th = element(tag="th")
thead = element(tag="thead")
time = element(tag="time")
title = element(tag="title")
tr = element(tag="tr")
track = element(tag="track", self_closing=True)
tt = element(tag="tt")
u = element(tag="u")
ul = element(tag="ul")
var = element(tag="var")
video = element(tag="video")
wbr = element(tag="wbr", self_closing=True)
xmp = element(tag="xmp")
