from dragonfly import Key, Text, Dictation
from castervoice.lib import control
from castervoice.lib.context import AppContext
from castervoice.lib.actions import Key
from castervoice.lib.dfplus.merge.mergerule import MergeRule
from castervoice.lib.dfplus.state.short import R
from castervoice.lib import settings

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
            R(Text("<a href=''></a>") + Key("left/10:6"), rdescript="HTML: Make Link"),
        "table macro":
            R(Text("<table>") + Key("enter") + Text("<tr>") + Key("enter") +
            Text("<td></td>") + Key("enter") + Text("</tr>") + Key("enter") +
            Text("</table>"), rdescript="HTML: Table Macro"),
        "checkbox":
            R(Text("<input type=\"checkbox\">"), rdescript="HTML: Checkbox"),
        # HTML elements
        # Basic or Root elements
        "HTML":
            R(Text("<html>") + Key("enter") + Text("</html>") + Key("up"), rdescript="HTML: HTML"),
        "doc type":
            R(Text("<!DOCTYPE html>") + Key("enter"), rdescript="HTML: Doc Type"),
        # Document metadata
        "base":
            R(Text("<base >") + Key("left/10:1"), rdescript="HTML: Base"),
        "head":
            R(Text("<head>") + Key("enter") + Text("</head>") + Key("up"), rdescript="HTML: Head"),
        "link":
            R(Text("<link  />") + Key("left/10:3"), rdescript="HTML: Link"),
        "meta":
            R(Text("<meta  />") + Key("left/10:3"), rdescript="HTML: Meta"),
        "style":
            R(Text("<style >") + Key("left/10:1"), rdescript="HTML: Style"),
        "style close":
            R(Text("</style>"), rdescript="HTML: Style Close"),
        "title":
            R(Text("<title></title>") + Key("left/10:8"), rdescript="HTML: Title"),
        # Content sectioning
        "address ":
            R(Text("<address>") + Key("enter") + Text("</address>") + Key("up"), rdescript="HTML: Address"),
        "article ":
            R(Text("<article >"), rdescript="HTML: Article"),
        "close article":
            R(Text("</article>"), rdescript="HTML: Close Article"),
        "body":
            R(Text("<body>") + Key("enter") + Text("</body>") + Key("up"), rdescript="HTML: Body"),
        "footer":
            R(Text("<footer>") + Key("enter") + Text("</footer>") + Key("up"), rdescript="HTML: Footer"),
        "header":
            R(Text("<header>") + Key("enter") + Text("</header>") + Key("up"), rdescript="HTML: Header"),
        "H 1 | heading one":
            R(Text("<h1></h1>") + Key("left/10:5"), rdescript="HTML: Heading 1"),
        "H 2 | heading to":
            R(Text("<h2></h2>") + Key("left/10:5"), rdescript="HTML: Heading 2"),
        "H 3 | heading three":
            R(Text("<h3></h3>") + Key("left/10:5"), rdescript="HTML: Heading 3"),
        "H 4 | heading for":
            R(Text("<h4></h4>") + Key("left/10:5"), rdescript="HTML: Heading 4"),
        "H 5 | heading five":
            R(Text("<h5></h5>") + Key("left/10:5"), rdescript="HTML: Heading 5"),
        "H 6 | heading six":
            R(Text("<h6></h6>") + Key("left/10:5"), rdescript="HTML: Heading 6"),
        "H group | headings group":
            R(Text("<hgroup></hgroup>") + Key("left/10:9"), rdescript="HTML: Group"),
        "navigation | navigate":
            R(Text("<nav>") + Key("enter") + Text("</nav>") + Key("up"), rdescript="HTML: Navigate"),
        "section":
            R(Text("<section>") + Key("enter") + Text("</section>") + Key("up"), rdescript="HTML: Section"),
        # Text content
        "description | DD":
            R(Text("<dd>"), rdescript="HTML: Description"),
        "division":
            R(Text("<div></div>") + Key("left/10:6"), rdescript="HTML: Division"),
        "list element | DL":
            R(Text("<dl>"), rdescript="HTML: List Element"),
        "fig caption":
            R(Text("<figcaption>"), rdescript="HTML: Fig Caption"),
        "figure":
            R(Text("<figure>"), rdescript="HTML: Figure"),
        "H are | HR":
            R(Text("<hr>"), rdescript="HTML: HR"),
        "list item | LI":
            R(Text("<li></li>") + Key("left/10:5"), rdescript="HTML: List Item"),
        "main":
            R(Text("<main>") + Key("enter") + Text("</main>") + Key("up"), rdescript="HTML: Main"),
        "ordered list | OL":
            R(Text("<ol>") + Key("enter") + Text("</ol>") + Key("up"), rdescript="HTML: Ordered List"),
        "paragraph":
            R(Text("<p>") + Key("enter") + Text("</p>") + Key("up"), rdescript="HTML: Paragraph"),
        "pre-format":
            R(Text("<pre>") + Key("enter") + Text("</pre>") + Key("up"), rdescript="HTML: Pre-format"),
        "unordered list | UL":
            R(Text("<ul>") + Key("enter") + Text("</ul>") + Key("up"), rdescript="HTML: Unordered List"),
        # Inline text semantics
        "anchor":
            R(Text("<a></a>") + Key("left/10:4"), rdescript="HTML: Anchor"),
        "abbreviation":
            R(Text("<abbr></abbr>") + Key("left/10:7"), rdescript="HTML: Abbreviation"),
        "bold":
            R(Text("<b></b>") + Key("left/10:4"), rdescript="HTML: Bold"),
        "override":
            R(Text("<bdo></bdo>") + Key("left/10:6"), rdescript="HTML: Override"),
        "isolate | bi-directional isolation":
            R(Text("<bdi></bdi>") + Key("left/10:6"), rdescript="HTML: Bi-directional Isolation"),
        "break | be are | BR":
            R(Text("<br>") + Key("enter"), rdescript="HTML: Break"),
        "code":
            R(Text("<code></code>") + Key("left/10:7"), rdescript="HTML: Code"),
        "data":
            R(Text("<data></data>") + Key("left/10:7"), rdescript="HTML: Data"),
        "defining instance":
            R(Text("<dfn></dfn>") + Key("left/10:6"), rdescript="HTML: Defining Instance"),
        "emphasis | EM":
            R(Text("<em></em>") + Key("left/10:5"), rdescript="HTML: Emphasis"),
        "semantics | italics":
            R(Text("<i></i>") + Key("left/10:4"), rdescript="HTML: Semantics | Italics"),
        "keyboard input":
            R(Text("<kbd></kbd>") + Key("left/10:6"), rdescript="HTML: Keyboard Input"),
        "mark | highlight":
            R(Text("<mark></mark>") + Key("left/10:7"), rdescript="HTML: Mark | Highlight"),
        "quote":
            R(Text("<q></q>") + Key("left/10:4"), rdescript="HTML: Quote"),
        "fall-back parenthesis | RP":
            R(Text("<rp></rp>") + Key("left/10:5"), rdescript="HTML: Fall-back Parentheses"),
        "embraces pronunciation | RT":
            R(Text("<rt></rt>") + Key("left/10:5"), rdescript="HTML: Embrace Pronunciation"),
        "ruby | pronounce asian":
            R(Text("<ruby></ruby>") + Key("left/10:7"), rdescript="HTML: Ruby | Pronounce Asian"),
        # #"strike through | strike":    Text("<s></s>")+  Key("left/10:4"), rdescript="HTML: Strike Through | Strike"),
        "deleted text | deleted | replaced":
            R(Text("<del></del>") + Key("left/10:6"), rdescript="HTML: Deleted Text | Deleted | Replaced"),
        "sample output":
            R(Text("<samp></samp>") + Key("left/10:7"), rdescript="HTML: Sample Output"),
        "small":
            R(Text("<small></small>") + Key("left/10:8"), rdescript="HTML: Small"),
        "span":
            R(Text("<span></span>") + Key("left/10:7"), rdescript="HTML: Span"),
        "strong":
            R(Text("<strong></strong>") + Key("left/10:9"), rdescript="HTML: Strong"),
        "subscript":
            R(Text("<sub></sub>") + Key("left/10:6"), rdescript="HTML: Subscript"),
        "superscript":
            R(Text("<sup></sup>") + Key("left/10:6"), rdescript="HTML: Superscript"),
        "time":
            R(Text("<time></time>") + Key("left/10:7"), rdescript="HTML: Time"),
        "underline":
            R(Text("<u></u>") + Key("left/10:4"), rdescript="HTML: Underline"),
        "variable":
            R(Text("<var></var>") + Key("left/10:6"), rdescript="HTML: Variable"),
        "optional break":
            R(Text("<wbr></wbr>") + Key("left/10:6"), rdescript="HTML: Optional Break"),
        # Image & multimedia
        "area":
            R(Text("<area />") + Key("left/10:2"), rdescript="HTML: Area"),
        "audio":
            R(Text("<audio>") + Key("enter") + Text("</audio>") + Key("up"), rdescript="HTML: Audio"),
        "image ":
            R(Text("<img></img>") + Key("left/10:6"), rdescript="HTML: Image"),
        "map":
            R(Text("<map>") + Key("enter") + Text("</map>") + Key("up"), rdescript="HTML: Map"),
        "track":
            R(Text("<track >") + Key("left/10:1"), rdescript="HTML: Track"),
        "video":
            R(Text("<video >") + Key("left/10:1"), rdescript="HTML: Video"),
        "video close":
            R(Text("</video>"), rdescript="HTML: Video Close"),
        # embedded content
        "embedded":
            R(Text("<embed >") + Key("left/10:1"), rdescript="HTML: Embedded"),
        "inline frame":
            R(Text("<iframe >") + Key("left/10:1"), rdescript="HTML: Inline Frame"),
        "inline frame close":
            R(Text("</iframe>") + Key("left/10:1"), rdescript="HTML: In-line Frame Close"),
        "object | embedded object":
            R(Text("<object >") + Key("left/10:1"), rdescript="HTML: Object | Embedded Object"),
        "parameter ":
            R(Text("<param >") + Key("left/10:1"), rdescript="HTML: Parameter"),
        "tag source":
            R(Text("<source >") + Key("left/10:1"), rdescript="HTML: Source"),
        # Scripting
        "canvas":
            R(Text("<canvas >") + Key("left/10:1"), rdescript="HTML: Canvas"),
        "canvas close":
            R(Text("</canvas>"), rdescript="HTML: Canvas Close"),
        "noscript":
            R(Text("<noscript>") + Key("enter") + Text("</noscript>") + Key("up"), rdescript="HTML: NoScript"),
        "script":
            R(Text("<script></script>") + Key("left/10:9"), rdescript="HTML: Script"),
        # Edits
        "deleted text | deleted":
            Text("<del>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "inserted text | inserted":
            R(Text("<ins></ins>") + Key("left/10:6"), rdescript="HTML: Inserted Text | Inserted"),
        # Table content
        "table caption | tee caption":
            R(Text("<caption>"), rdescript="HTML: Table Caption"),
        "table column | tee column":
            R(Text("<col>"), rdescript="HTML: Table Column"),
        "table column group | tee group":
            R(Text("<colgroup>"), rdescript="HTML: Table Column Group"),
        "table":
            R(Text("<table>"), rdescript="HTML: Table"),
        "table body":
            R(Text("<tbody>"), rdescript="HTML: Table Body"),
        "table cell | TD | tee D":
            R(Text("<td></td>") + Key("left/10:5"), rdescript="HTML: Table Body Cell"),
        "table foot":
            R(Text("<tfoot>"), rdescript="HTML: Table Foot"),
        "table header | TH":
            R(Text("<th>"), rdescript="HTML: Table Header"),
        "table head | thead":
            R(Text("<thead>"), rdescript="HTML: Table Head"),
        "table row | tee are":
            R(Text("<tr></tr>") + Key("left/10:5"), rdescript="HTML: Table Row"),
        # Forms
        "button":
            R(Text("<button></button>") + Key("left/10:9"), rdescript="HTML: Button"),
        "data list":
            R(Text("<datalist>") + Key("enter") + Text("</datalist>") + Key("up"), rdescript="HTML: Data List"),
        "field set":
            R(Text("<fieldset>") + Key("enter") + Text("</fieldset>") + Key("up"), rdescript="HTML: Field Set"),
        "field set close":
            R(Text("</fieldset>"), rdescript="HTML: Field Set Close"),
        "form":
            R(Text("<form>") + Key("enter") + Text("</form>") + Key("up"), rdescript="HTML: Form"),
        "input":
            R(Text("<input >") + Key("left/10:1"), rdescript="HTML: Input"),
        "keygen":
            R(Text("<keygen >") + Key("left/10:1"), rdescript="HTML: Keygen"),
        "label":
            R(Text("<label>"), rdescript="HTML: Label"),
        "label close":
            R(Text("</label>"), rdescript="HTML: Label Close"),
        "legend":
            R(Text("<legend>"), rdescript="HTML: Legend"),
        "meter":
            R(Text("<meter >") + Key("left/10:1"), rdescript="HTML: Meter"),
        "meter close":
            R(Text("</meter>"), rdescript="HTML: Meter Close"),
        "opt group":
            R(Text("<optgroup>") + Key("enter") + Text("</optgroup>") + Key("up"), rdescript="HTML: Opt Group"),
        "option":
            R(Text("<option >") + Key("left/10:1"), rdescript="HTML: Option"),
        "option close":
            R(Text("</option>"), rdescript="HTML: Option Close"),
        "output":
            R(Text("<output >") + Key("left/10:1"), rdescript="HTML: Output"),
        "output close":
            R(Text("</output>"), rdescript="HTML: Output Close"),
        "progress":
            R(Text("<progress >") + Key("left/10:1"), rdescript="HTML: Progress"),
        "select":
            R(Text("<select>") + Key("enter") + Text("</select>") + Key("up"), rdescript="HTML: Select"),
        "text area":
            R(Text("<textarea >") + Key("left/10:1"), rdescript="HTML: Text Area"),
        "text area close":
            R(Text("</textarea>"), rdescript="HTML: Text Area Close"),
        # Interactive elements
        "details":
            R(Text("<details>"), rdescript="HTML: Details"),
        "dialog":
            R(Text("<dialog>"), rdescript="HTML: Dialogue"),
        "menu":
            R(Text("<menu>"), rdescript="HTML: Menu"),
        "menu item":
            R(Text("<menuitem>"), rdescript="HTML: Menu Item"),
        "summary":
            R(Text("<summary>"), rdescript="HTML: Summary"),
        # Web Components: As defined in (W3C)
        "content":
            R(Text("<content>"), rdescript="HTML: Context"),
        "decorator":
            R(Text("<decorator>"), rdescript="HTML: Decorator"),
        "element":
            R(Text("<element>"), rdescript="HTML: Element"),
        "shadow":
            R(Text("<shadow>"), rdescript="HTML: Shadow"),
        "template":
            R(Text("<template>"), rdescript="HTML: Template"),
        # my own commands
        "attribute [I] accept":
            R(Text('accept=""') + Key("left:1"), rdescript="HTML: attribute accept"),
        "attribute access key":
            R(Text('accesskey=""') + Key("left:1"), rdescript="HTML: attribute access key"),
        "attribute action":
            R(Text('action=""') + Key("left:1"), rdescript="HTML: attribute action"),
        "attribute a line":
            R(Text('align=""') + Key("left:1"), rdescript="HTML: attribute align"),
        "attribute alternative":
            R(Text('alt=""') + Key("left:1"), rdescript="HTML: attribute alternative"),
        "attribute asynchronous":
            R(Text('async=""') + Key("left:1"), rdescript="HTML: attribute asynchronous"),
        "attribute auto complete":
            R(Text('autocomplete=""') + Key("left:1"), rdescript="HTML: attribute auto complete"),
        "attribute autofocus":
            R(Text('autofocus=""') + Key("left:1"), rdescript="HTML: attribute autofocus"),
        "attribute autoplay":
            R(Text('autoplay=""') + Key("left:1"), rdescript="HTML: attribute autoplay"),
        "attribute autosave":
            R(Text('autosave=""') + Key("left:1"), rdescript="HTML: attribute autosave"),
        "attributes buffered":
            R(Text('buffered=""') + Key("left:1"), rdescript="HTML: attribute buffered"),
        "attribute challenge":
            R(Text('challenge=""') + Key("left:1"), rdescript="HTML: attribute challenge"),
        "attribute character set":
            R(Text('charset=""') + Key("left:1"), rdescript="HTML: attribute character set"),
        "attributes checked":
            R(Text('checked=""') + Key("left:1"), rdescript="HTML: attribute checked"),
        "attribute site":
            R(Text('cite=""') + Key("left:1"), rdescript="HTML: attribute cite"),
        "attribute class":
            R(Text('class=""') + Key("left:1"), rdescript="HTML: attribute class"),
        "attribute code":
            R(Text('code=""') + Key("left:1"), rdescript="HTML: attribute code"),
        "attribute code base":
            R(Text('codebase=""') + Key("left:1"), rdescript="HTML: attribute code base"),
        "attribute columns":
            R(Text('cols=""') + Key("left:1"), rdescript="HTML: attribute "),
        "attribute columns span":
            R(Text('colspan=""') + Key("left:1"), rdescript="HTML: attribute columns span"),
        "attribute content":
            R(Text('content=""') + Key("left:1"), rdescript="HTML: attribute content"),
        "attribute content edit":
            R(Text('contenteditable=""') + Key("left:1"), rdescript="HTML: attribute content editable"),
        "attribute context menu":
            R(Text('contextmenu=""') + Key("left:1"), rdescript="HTML: attribute context menu"),
        "attribute controls":
            R(Text('controls=""') + Key("left:1"), rdescript="HTML: attribute controls"),
        "attribute coordinates":
            R(Text('coords=""') + Key("left:1"), rdescript="HTML: attribute coordinates"),
        "attribute across origin":
            R(Text('crossorigin=""') + Key("left:1"), rdescript="HTML: attribute across origin"),
        "attribute data":
            R(Text('data=""') + Key("left:1"), rdescript="HTML: attribute data"),
        "attribute data global":
            R(Text('data-*=""') + Key("left:1"), rdescript="HTML: attribute data global"),
        "attribute date":
            R(Text('datetime=""') + Key("left:1"), rdescript="HTML: attribute date"),
        "attribute default":
            R(Text('default=""') + Key("left:1"), rdescript="HTML: attribute default"),
        "attribute [to] defer":
            R(Text('defer=""') + Key("left:1"), rdescript="HTML: attribute defer"),
        "attribute direction":
            R(Text('dir=""') + Key("left:1"), rdescript="HTML: attribute direction"),
        "attribute direction name":
            R(Text('dirname=""') + Key("left:1"), rdescript="HTML: attribute direction name"),
        "attribute [a] disabled":
            R(Text('disabled'), rdescript="HTML: attribute disabled"),
        "attribute download":
            R(Text('download=""') + Key("left:1"), rdescript="HTML: attribute download"),
        "attribute draggable":
            R(Text('draggable=""') + Key("left:1"), rdescript="HTML: attribute draggable"),
        "attribute drops on":
            R(Text('dropzone=""') + Key("left:1"), rdescript="HTML: attribute dropzone"),
        "attribute form type":
            R(Text('enctype=""') + Key("left:1"), rdescript="HTML: attribute form type"),
        "attribute for":
            R(Text('for=""') + Key("left:1"), rdescript="HTML: attribute for"),
        "attribute form":
            R(Text('form=""') + Key("left:1"), rdescript="HTML: attribute form"),
        "attribute form action":
            R(Text('formaction=""') + Key("left:1"), rdescript="HTML: attribute form action"),
        "attribute headers":
            R(Text('headers=""') + Key("left:1"), rdescript="HTML: attribute headers"),
        "attribute height":
            R(Text('height=""') + Key("left:1"), rdescript="HTML: attribute height"),
        "attribute hidden":
            Text('hidden=""') + Key("left:1"),
        "attribute high":
            Text('high=""') + Key("left:1"),
        "attribute hyperlink":
            Text('href=""') + Key("left:1"),
        "attribute hyperlink language":
            Text('hreflang=""') + Key("left:1"),
        "attribute hyperlink equivalent":
            Text('http-equivalent=""') + Key("left:1"),
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
    extras = [
        Dictation("text"),
    ]
    defaults = {
        "text": "",
    }


control.nexus().merger.add_global_rule(HTML())
