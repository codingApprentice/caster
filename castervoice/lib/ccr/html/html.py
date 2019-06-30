from castervoice.lib.imports import *

# HTML auto complete workaround for Jetbrains Products
# If more applications have issues with auto complete may be moved to actions.py
context = AppContext(executable=["idea", "idea64", "studio64", "pycharm", "webstorm64", "webstorm"])

if context:
    from dragonfly.actions.action_paste import Paste as Text
    if settings.SETTINGS["miscellaneous"]["use_aenea"]:
        try:
            from aenea import Paste as Text
        except ImportError:
            print("Unable to import aenea Paste actions. Dragonfly actions will be used "
            "instead.")
else:
    from castervoice.lib.actions import Text


class HTML(MergeRule):
    mapping = {

        # A macro with ## is depreciated HTML.
        # Macros
        "make link":
            R(Text("<a href=''></a>") + Key("left/10:6")),
        "table macro":
            R(Text("<table>") + Key("enter") + Text("<tr>") + Key("enter") +
            Text("<td></td>") + Key("enter") + Text("</tr>") + Key("enter") +
            Text("</table>")),
        "checkbox":
            R(Text("<input type=\"checkbox\">")),
        # HTML elements
        # Basic or Root elements
        "HTML":
            R(Text("<html>") + Key("enter") + Text("</html>") + Key("up")),
        "doc type":
            R(Text("<!DOCTYPE html>") + Key("enter")),
        # Document metadata
        "base":
            R(Text("<base >") + Key("left/10:1")),
        "head":
            R(Text("<head>") + Key("enter") + Text("</head>") + Key("up")),
        "link":
            R(Text("<link  />") + Key("left/10:1")),
        "meta":
            R(Text("<meta  />") + Key("left/10:1")),
        "style":
            R(Text("<style >") + Key("left/10:1")),
        "style close":
            R(Text("</style>")),
        "title":
            R(Text("<title></title>") + Key("left/10:8")),
        # Content sectioning
        "address ":
            R(Text("<address>") + Key("enter") + Text("</address>") + Key("up")),
        "article ":
            R(Text("<article >")),
        "close article":
            R(Text("</article>")),
        "body":
            R(Text("<body>") + Key("enter") + Text("</body>") + Key("up")),
        "footer":
            R(Text("<footer>") + Key("enter") + Text("</footer>") + Key("up")),
        "header":
            R(Text("<header>") + Key("enter") + Text("</header>") + Key("up")),
        "H 1 | heading one":
            R(Text("<h1></h1>") + Key("left/10:5")),
        "H 2 | heading to":
            R(Text("<h2></h2>") + Key("left/10:5")),
        "H 3 | heading three":
            R(Text("<h3></h3>") + Key("left/10:5")),
        "H 4 | heading for":
            R(Text("<h4></h4>") + Key("left/10:5")),
        "H 5 | heading five":
            R(Text("<h5></h5>") + Key("left/10:5")),
        "H 6 | heading six":
            R(Text("<h6></h6>") + Key("left/10:5")),
        "H group | headings group":
            R(Text("<hgroup></hgroup>") + Key("left/10:9")),
        "navigation | navigate":
            R(Text("<nav>") + Key("enter") + Text("</nav>") + Key("up")),
        "section":
            R(Text("<section>") + Key("enter") + Text("</section>") + Key("up")),
        # Text content
        "description | DD":
            R(Text("<dd>")),
        "division":
            R(Text("<div></div>") + Key("left/10:6")),
        "list element | DL":
            R(Text("<dl>")),
        "fig caption":
            R(Text("<figcaption>")),
        "figure":
            R(Text("<figure>")),
        "H are | HR":
            R(Text("<hr>")),
        "list item | LI":
            R(Text("<li></li>") + Key("left/10:5")),
        "main":
            R(Text("<main>") + Key("enter") + Text("</main>") + Key("up")),
        "ordered list | OL":
            R(Text("<ol>") + Key("enter") + Text("</ol>") + Key("up")),
        "paragraph":
            R(Text("<p>") + Key("enter") + Text("</p>") + Key("up")),
        "pre-format":
            R(Text("<pre>") + Key("enter") + Text("</pre>") + Key("up")),
        "unordered list | UL":
            R(Text("<ul>") + Key("enter") + Text("</ul>") + Key("up")),
        # Inline text semantics
        "anchor":
            R(Text("<a></a>") + Key("left/10:4")),
        "abbreviation":
            R(Text("<abbr></abbr>") + Key("left/10:7")),
        "bold":
            R(Text("<b></b>") + Key("left/10:4")),
        "override":
            R(Text("<bdo></bdo>") + Key("left/10:6")),
        "isolate | bi-directional isolation":
            R(Text("<bdi></bdi>") + Key("left/10:6")),
        "break | be are | BR":
            R(Text("<br>") + Key("enter")),
        "code":
            R(Text("<code></code>") + Key("left/10:7")),
        "data":
            R(Text("<data></data>") + Key("left/10:7")),
        "defining instance":
            R(Text("<dfn></dfn>") + Key("left/10:6")),
        "emphasis | EM":
            R(Text("<em></em>") + Key("left/10:5")),
        "semantics | italics":
            R(Text("<i></i>") + Key("left/10:4")),
        "keyboard input":
            R(Text("<kbd></kbd>") + Key("left/10:6")),
        "mark | highlight":
            R(Text("<mark></mark>") + Key("left/10:7")),
        "quote":
            R(Text("<q></q>") + Key("left/10:4")),
        "fall-back parenthesis | RP":
            R(Text("<rp></rp>") + Key("left/10:5")),
        "embraces pronunciation | RT":
            R(Text("<rt></rt>") + Key("left/10:5")),
        "ruby | pronounce asian":
            R(Text("<ruby></ruby>") + Key("left/10:7")),
        # #"strike through | strike":    Text("<s></s>")+  Key("left/10:4"), rdescript="HTML: Strike Through | Strike"),
        "deleted text | deleted | replaced":
            R(Text("<del></del>") + Key("left/10:6")),
        "sample output":
            R(Text("<samp></samp>") + Key("left/10:7")),
        "small":
            R(Text("<small></small>") + Key("left/10:8")),
        "span":
            R(Text("<span></span>") + Key("left/10:7")),
        "strong":
            R(Text("<strong></strong>") + Key("left/10:9")),
        "subscript":
            R(Text("<sub></sub>") + Key("left/10:6")),
        "superscript":
            R(Text("<sup></sup>") + Key("left/10:6")),
        "time":
            R(Text("<time></time>") + Key("left/10:7")),
        "underline":
            R(Text("<u></u>") + Key("left/10:4")),
        "variable":
            R(Text("<var></var>") + Key("left/10:6")),
        "optional break":
            R(Text("<wbr></wbr>") + Key("left/10:6")),
        # Image & multimedia
        "area":
            R(Text("<area />") + Key("left/10:2")),
        "audio":
            R(Text("<audio>") + Key("enter") + Text("</audio>") + Key("up")),
        "image ":
            R(Text("<img></img>") + Key("left/10:6")),
        "map":
            R(Text("<map>") + Key("enter") + Text("</map>") + Key("up")),
        "track":
            R(Text("<track >") + Key("left/10:1")),
        "video":
            R(Text("<video >") + Key("left/10:1")),
        "video close":
            R(Text("</video>")),
        # embedded content
        "embedded":
            R(Text("<embed >") + Key("left/10:1")),
        "inline frame":
            R(Text("<iframe >") + Key("left/10:1")),
        "inline frame close":
            R(Text("</iframe>") + Key("left/10:1")),
        "object | embedded object":
            R(Text("<object >") + Key("left/10:1")),
        "parameter ":
            R(Text("<param >") + Key("left/10:1")),
        "tag source":
            R(Text("<source >") + Key("left/10:1")),
        # Scripting
        "canvas":
            R(Text("<canvas >") + Key("left/10:1")),
        "canvas close":
            R(Text("</canvas>")),
        "noscript":
            R(Text("<noscript>") + Key("enter") + Text("</noscript>") + Key("up")),
        "script":
            R(Text("<script></script>") + Key("left/10:9")),
        # Edits
        "deleted text | deleted":
            Text("<del>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "inserted text | inserted":
            R(Text("<ins></ins>") + Key("left/10:6")),
        # Table content
        "table caption | tee caption":
            R(Text("<caption>")),
        "table column | tee column":
            R(Text("<col>")),
        "table column group | tee group":
            R(Text("<colgroup>")),
        "table":
            R(Text("<table>")),
        "table body":
            R(Text("<tbody>")),
        "table cell | TD | tee D":
            R(Text("<td></td>") + Key("left/10:5")),
        "table foot":
            R(Text("<tfoot>")),
        "table header | TH":
            R(Text("<th>")),
        "table head | thead":
            R(Text("<thead>")),
        "table row | tee are":
            R(Text("<tr></tr>") + Key("left/10:5")),
        # Forms
        "button":
            R(Text("<button></button>") + Key("left/10:9")),
        "data list":
            R(Text("<datalist>") + Key("enter") + Text("</datalist>") + Key("up")),
        "field set":
            R(Text("<fieldset>") + Key("enter") + Text("</fieldset>") + Key("up")),
        "field set close":
            R(Text("</fieldset>")),
        "form":
            R(Text("<form>") + Key("enter") + Text("</form>") + Key("up")),
        "input":
            R(Text("<input >") + Key("left/10:1")),
        "keygen":
            R(Text("<keygen >") + Key("left/10:1")),
        "label":
            R(Text("<label>")),
        "label close":
            R(Text("</label>")),
        "legend":
            R(Text("<legend>")),
        "meter":
            R(Text("<meter >") + Key("left/10:1")),
        "meter close":
            R(Text("</meter>")),
        "opt group":
            R(Text("<optgroup>") + Key("enter") + Text("</optgroup>") + Key("up")),
        "option":
            R(Text("<option >") + Key("left/10:1")),
        "option close":
            R(Text("</option>")),
        "output":
            R(Text("<output >") + Key("left/10:1")),
        "output close":
            R(Text("</output>")),
        "progress":
            R(Text("<progress >") + Key("left/10:1")),
        "select":
            R(Text("<select>") + Key("enter") + Text("</select>") + Key("up")),
        "text area":
            R(Text("<textarea >") + Key("left/10:1")),
        "text area close":
            R(Text("</textarea>")),
        # Interactive elements
        "details":
            R(Text("<details>")),
        "dialog":
            R(Text("<dialog>")),
        "menu":
            R(Text("<menu>")),
        "menu item":
            R(Text("<menuitem>")),
        "summary":
            R(Text("<summary>")),
        # Web Components: As defined in (W3C)
        "content":
            R(Text("<content>")),
        "decorator":
            R(Text("<decorator>")),
        "element":
            R(Text("<element>")),
        "shadow":
            R(Text("<shadow>")),
        "template":
            R(Text("<template>")),
        # my own commands
        "attribute [I] accept":
            R(Text('accept=""') + Key("left:1")),
        "attribute access key":
            R(Text('accesskey=""') + Key("left:1")),
        "attribute action":
            R(Text('action=""') + Key("left:1")),
        "attribute a line":
            R(Text('align=""') + Key("left:1")),
        "attribute alternative":
            R(Text('alt=""') + Key("left:1")),
        "attribute asynchronous":
            R(Text('async=""') + Key("left:1")),
        "attribute auto complete":
            R(Text('autocomplete=""') + Key("left:1")),
        "attribute autofocus":
            R(Text('autofocus=""') + Key("left:1")),
        "attribute autoplay":
            R(Text('autoplay=""') + Key("left:1")),
        "attribute autosave":
            R(Text('autosave=""') + Key("left:1")),
        "attributes buffered":
            R(Text('buffered=""') + Key("left:1")),
        "attribute challenge":
            R(Text('challenge=""') + Key("left:1")),
        "attribute character set":
            R(Text('charset=""') + Key("left:1")),
        "attributes checked":
            R(Text('checked=""') + Key("left:1")),
        "attribute site":
            R(Text('cite=""') + Key("left:1")),
        "attribute class":
            R(Text('class=""') + Key("left:1")),
        "attribute code":
            R(Text('code=""') + Key("left:1")),
        "attribute code base":
            R(Text('codebase=""') + Key("left:1")),
        "attribute columns":
            R(Text('cols=""') + Key("left:1")),
        "attribute columns span":
            R(Text('colspan=""') + Key("left:1")),
        "attribute content":
            R(Text('content=""') + Key("left:1")),
        "attribute content edit":
            R(Text('contenteditable=""') + Key("left:1")),
        "attribute context menu":
            R(Text('contextmenu=""') + Key("left:1")),
        "attribute controls":
            R(Text('controls=""') + Key("left:1")),
        "attribute coordinates":
            R(Text('coords=""') + Key("left:1")),
        "attribute across origin":
            R(Text('crossorigin=""') + Key("left:1")),
        "attribute data":
            R(Text('data=""') + Key("left:1")),
        "attribute data global":
            R(Text('data-*=""') + Key("left:1")),
        "attribute date":
            R(Text('datetime=""') + Key("left:1")),
        "attribute default":
            R(Text('default=""') + Key("left:1")),
        "attribute [to] defer":
            R(Text('defer=""') + Key("left:1")),
        "attribute direction":
            R(Text('dir=""') + Key("left:1")),
        "attribute direction name":
            R(Text('dirname=""') + Key("left:1")),
        "attribute [a] disabled":
            R(Text('disabled')),
        "attribute download":
            R(Text('download=""') + Key("left:1")),
        "attribute draggable":
            R(Text('draggable=""') + Key("left:1")),
        "attribute drops on":
            R(Text('dropzone=""') + Key("left:1")),
        "attribute form type":
            R(Text('enctype=""') + Key("left:1")),
        "attribute for":
            R(Text('for=""') + Key("left:1")),
        "attribute form":
            R(Text('form=""') + Key("left:1")),
        "attribute form action":
            R(Text('formaction=""') + Key("left:1")),
        "attribute headers":
            R(Text('headers=""') + Key("left:1")),
        "attribute height":
            R(Text('height=""') + Key("left:1")),
        "attribute hidden":
            Text('hidden=""') + Key("left:1"),
        "attribute high":
            Text('high=""') + Key("left:1"),
        "attribute hyperlink":
            Text('href=""') + Key("left:1"),
        "attribute hyperlink language":
            Text('hreflang=""') + Key("left:1"),
        "attribute hyperlink equivalent":
            Text('http-equiv=""') + Key("left:1"),
        "attribute icon":
            Text('icon=""') + Key("left:1"),
        "attribute identity":
            Text('id=""') + Key("left:1"),
        "attribute integrity":
            Text('integrity=""') + Key("left:1"),
        "attribute map":
            Text('ismap=""') + Key("left:1"),
        "attribute item property":
            Text('itemprop=""') + Key("left:1"),
        "attribute [a] key type":
            Text('keytype=""') + Key("left:1"),
        "attribute kind":
            Text('kind=""') + Key("left:1"),
        "attribute label":
            Text('label=""') + Key("left:1"),
        "attribute language":
            Text('lang=""') + Key("left:1"),
        "attribute list":
            Text('list=""') + Key("left:1"),
        "attribute loop":
            Text('loop=""') + Key("left:1"),
        "attribute [a] low":
            Text('low=""') + Key("left:1"),
        "attribute manifest":
            Text('manifest=""') + Key("left:1"),
        "attribute Max":
            Text('max=""') + Key("left:1"),
        "attribute max length":
            Text('maxlength=""') + Key("left:1"),
        "attribute [a] minimum length":
            Text('minlength=""') + Key("left:1"),
        "attribute media":
            Text('media=""') + Key("left:1"),
        "attribute method":
            Text('method=""') + Key("left:1"),
        "attribute minimum":
            Text('min=""') + Key("left:1"),
        "attribute multiple":
            Text('multiple=""') + Key("left:1"),
        "attribute muted":
            Text('muted=""') + Key("left:1"),
        "attribute name":
            Text('name=""') + Key("left:1"),
        "attribute no validation":
            Text('novalidate=""') + Key("left:1"),
        "attribute open":
            Text('open=""') + Key("left:1"),
        "attribute optimum":
            Text('optimum=""') + Key("left:1"),
        "attribute pattern":
            Text('pattern=""') + Key("left:1"),
        "attribute paying":
            Text('ping=""') + Key("left:1"),
        "attribute placeholder":
            Text('placeholder=""') + Key("left:1"),
        "attribute poster":
            Text('poster=""') + Key("left:1"),
        "attributes preload":
            Text('preload=""') + Key("left:1"),
        "attributes radio group":
            Text('radiogroup=""') + Key("left:1"),
        "attribute read-only":
            Text('readonly=""') + Key("left:1"),
        "attribute relationship":
            Text('rel=""') + Key("left:1"),
        "attribute required":
            Text('required=""') + Key("left:1"),
        "attribute reversed":
            Text('reversed=""') + Key("left:1"),
        "attribute rose":
            Text('rows=""') + Key("left:1"),
        "attribute row span":
            Text('rowspan=""') + Key("left:1"),
        "attribute sandbox":
            Text('sandbox=""') + Key("left:1"),
        "attribute scope":
            Text('scope=""') + Key("left:1"),
        "attributes scoped":
            Text('scoped=""') + Key("left:1"),
        "attribute seamless":
            Text('seamless=""') + Key("left:1"),
        "attributes selected":
            Text('selected=""') + Key("left:1"),
        "attribute shape":
            Text('shape=""') + Key("left:1"),
        "attribute size":
            Text('size=""') + Key("left:1"),
        "attribute sizes":
            Text('sizes=""') + Key("left:1"),
        "attribute slot":
            Text('slot=""') + Key("left:1"),
        "attribute span":
            Text('span=""') + Key("left:1"),
        "attribute spellcheck":
            Text('spellcheck=""') + Key("left:1"),
        "attribute [a] source":
            Text('src=""') + Key("left:1"),
        "attribute source document":
            Text('srcdoc=""') + Key("left:1"),
        "attribute source language":
            Text('srclang=""') + Key("left:1"),
        "attribute source set":
            Text('srcset=""') + Key("left:1"),
        "attributes start":
            Text('start=""') + Key("left:1"),
        "attributes step":
            Text('step=""') + Key("left:1"),
        "attribute summary":
            Text('summary=""') + Key("left:1"),
        "attribute index":
            Text('tabindex=""') + Key("left:1"),
        "attribute target":
            Text('target=""') + Key("left:1"),
        "attributes title":
            Text('title=""') + Key("left:1"),
        "attribute type":
            Text('type=""') + Key("left:1"),
        "attributes use map":
            Text('usemap=""') + Key("left:1"),
        "attribute value":
            Text('value=""') + Key("left:1"),
        "attribute with":
            Text('width=""') + Key("left:1"),
    }




control.global_rule(HTML())
