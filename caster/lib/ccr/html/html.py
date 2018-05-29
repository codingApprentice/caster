from dragonfly import Key, Text, Dictation

from caster.lib import control
from caster.lib.dfplus.merge.mergerule import MergeRule


class HTML(MergeRule):
    mapping = {

        # A macro with ## is depreciated HTML.
        #Macros
        "make link [<text>]":
            Text("<a href='%(text)s'>") + Key("enter") + Key("up") + Key("end") +
            Key("enter"),
        "table macro":
            Text("<table>") + Key("enter") + Text("<tr>") + Key("enter") +
            Text("<td></td>") + Key("enter") + Text("</tr>") + Key("enter") +
            Text("</table>"),
        "close tag":
            Key("c-left/10:2"),
        "checkbox":
            Text("<input type=\"checkbox\">"),

        #HTML elements
        #Basic or Root elements
        "HTML":
            Text("<html>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "DOC TYPE":
            Text("<!DOCTYPE html>") + Key("enter"),
        #Document metadata
        "base":
            Text("<base >") + Key("left/10:1"),
        "head":
            Text("<head>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "link":
            Text("<link  />") + Key("left/10:3"),
        "meta":
            Text("<meta />") + Key("left/10:3"),
        "style":
            Text("<style >") + Key("left/10:1"),
        "style close":
            Text("</style>"),
        "tag title":
            Text("<title>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Content sectioning
        "address ":
            Text("<address>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "article ":
            Text("<article>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "close article":
            Text("</article>"),
        "body":
            Text("<body>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "footer":
            Text("<footer>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "header":
            Text("<header>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 1 | heading one":
            Text("<h1>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 2 | heading to":
            Text("<h2>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 3 | heading three":
            Text("<h3>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 4 | heading for":
            Text("<h4>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 5 | heading five":
            Text("<h5>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H 6 | heading six":
            Text("<h6>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "isolate ":
            Text("<bdi>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H group | headings group":
            Text("<hgroup>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "navigation | navigate":
            Text("<nav>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "section":
            Text("<section>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Text content
        "description | DD":
            Text("<dd>"),
        "division":
            Text("<div>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "list element | DL":
            Text("<dl>"),
        "fig caption":
            Text("<figcaption>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "figure":
            Text("<figure>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "H are | HR":
            Text("<hr>"),
        "list item | LI":
            Text("<li>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "main":
            Text("<main>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "ordered list | OL":
            Text("<ol>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "paragraph":
            Text("<p>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "pre-format":
            Text("<pre>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "unordered list | UL":
            Text("<ul>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Inline text semantics
        "anchor":
            Text("<a>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "abbreviation":
            Text("<abbr>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "bold":
            Text("<b>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "override":
            Text("<bdo>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "isolate | bi-directional isolation":
            Text("<bdi>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "break | be are | BR":
            Text("<br>") + Key("enter"),
        "code":
            Text("<code>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "data":
            Text("<data>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "definine instance":
            Text("<dfn>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "emphasis | EM":
            Text("<em>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "semantics | italics":
            Text("<i>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "keyboard input":
            Text("<kbd>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "mark | highlight":
            Text("<mark>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "quote":
            Text("<q>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "fall-back parenthesis | RP":
            Text("<rp>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "embraces pronunciation | RT":
            Text("<rt>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "ruby | pronounce asian":
            Text("<ruby>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        ##"strike through | strike":    Text("<s></s>")+  Key("left/10:4"),
        "deleted | replaced":
            Text("<del>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "sample output":
            Text("<samp>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "small":
            Text("<small>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "span":
            Text("<span>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "strong":
            Text("<strong>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "subscript":
            Text("<sub>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "superscript":
            Text("<sup>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "time":
            Text("<time>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "underline":
            Text("<u>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "variable":
            Text("<var>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "optional break":
            Text("<wbr>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Image & multimedia
        "area":
            Text("<area />") + Key("left/10:3"),
        "audio":
            Text("<audio>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "image ":
            Text("<img />") + Key("left/10:3"),
        "map":
            Text("<map>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "track":
            Text("<track >") + Key("left/10:1"),
        "video":
            Text("<video>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #embedded content
        "embedded":
            Text("<embed >") + Key("left/10:1"),
        "inline frame":
            Text("<iframe >") + Key("left/10:1"),
        "inline frame close":
            Text("</iframe>") + Key("left/10:1"),
        "object| embedded object":
            Text("<object >") + Key("left/10:1"),
        "parameter ":
            Text("<param >") + Key("left/10:1"),
        "source":
            Text("<source >") + Key("left/10:1"),
        #Scripting
        "canvas":
            Text("<canvas>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "canvas close":
            Text("</canvas>"),
        "noscript":
            Text("<noscript>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "script":
            Text("<script>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Edits
        "deleted text | deleted":
            Text("<del>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "inserted text | inserted":
            Text("<ins>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Table content
        "table caption | tee caption":
            Text("<caption>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table column | tee column":
            Text("<col>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table column group | tee group":
            Text("<colgroup>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table":
            Text("<table>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table body":
            Text("<tbody>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table cell | TD | tee D":
            Text("<td>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table foot":
            Text("<tfoot>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table header | TH":
            Text("<th>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table head | thead":
            Text("<thead>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "table row | tee are":
            Text("<tr>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        #Forms
        "button":
            Text("<button>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "data list":
            Text("<datalist>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "field set":
            Text("<fieldset>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "field set close":
            Text("</fieldset>"),
        "form":
            Text("<form>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "input":
            Text("<input />") + Key("left/10:3"),
        "keygen":
            Text("<keygen />") + Key("left/10:3"),
        "label":
            Text("<label>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "label close":
            Text("</label>"),
        "legend":
            Text("<legend>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "meter":
            Text("<meter>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "meter close":
            Text("</meter>"),
        "opt group":
            Text("<optgroup>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "option":
            Text("<option>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "option close":
            Text("</option>"),
        "output":
            Text("<output>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "output close":
            Text("</output>"),
        "progress":
            Text("<progress>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "select":
            Text("<select>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "text area":
            Text("<textarea>") + Key("enter") + Key("up") + Key("end") + Key("enter"),
        "text area close":
            Text("</textarea>"),
        #Interactive elements
        "details":
            Text("<details>"),
        "dialog":
            Text("<dialog>"),
        "menu":
            Text("<menu>"),
        "menu item":
            Text("<menuitem>"),
        "summary":
            Text("<summary>"),
        #Web Components: As defined in (W3C)
        "content":
            Text("<content>"),
        "decorator":
            Text("<decorator>"),
        "element":
            Text("<element>"),
        "shadow":
            Text("<shadow>"),
        "template":
            Text("<template>"),

        #my own commands
        "attribute [I] accept":
            Text('accept=""') + Key("left:1"),
        "attribute access key":
            Text('accesskey=""') + Key("left:1"),
        "attribute action":
            Text('action=""') + Key("left:1"),
        "attribute a line":
            Text('align=""') + Key("left:1"),
        "attribute alternative":
            Text('alt=""') + Key("left:1"),
        "attribute asynchronous":
            Text('async=""') + Key("left:1"),
        "attribute auto complete":
            Text('autocomplete=""') + Key("left:1"),
        "attribute autofocus":
            Text('autofocus=""') + Key("left:1"),
        "attribute autoplay":
            Text('autoplay=""') + Key("left:1"),
        "attribute autosave":
            Text('autosave=""') + Key("left:1"),
        "attributes buffered":
            Text('buffered=""') + Key("left:1"),
        "attribute challenge":
            Text('challenge=""') + Key("left:1"),
        "attribute character set":
            Text('charset=""') + Key("left:1"),
        "attributes checked":
            Text('checked=""') + Key("left:1"),
        "attribute site":
            Text('cite=""') + Key("left:1"),
        "attribute class":
            Text('class=""') + Key("left:1"),
        "attribute code":
            Text('code=""') + Key("left:1"),
        "attribute code base":
            Text('codebase=""') + Key("left:1"),
        "attribute columns":
            Text('cols=""') + Key("left:1"),
        "attribute columns span":
            Text('colspan=""') + Key("left:1"),
        "attribute content":
            Text('content=""') + Key("left:1"),
        "attribute content edit":
            Text('contenteditable=""') + Key("left:1"),
        "attribute context menu":
            Text('contextmenu=""') + Key("left:1"),
        "attribute controls":
            Text('controls=""') + Key("left:1"),
        "attribute coordinates":
            Text('coords=""') + Key("left:1"),
        "attribute across origin":
            Text('crossorigin=""') + Key("left:1"),
        "attribute data":
            Text('data=""') + Key("left:1"),
        "attribute data global":
            Text('data-*=""') + Key("left:1"),
        "attribute date":
            Text('datetime=""') + Key("left:1"),
        "attribute default":
            Text('default=""') + Key("left:1"),
        "attribute [to] defer":
            Text('defer=""') + Key("left:1"),
        "attribute direction":
            Text('dir=""') + Key("left:1"),
        "attribute direction name":
            Text('dirname=""') + Key("left:1"),
        "attribute [a] disabled":
            Text('disabled'),
        "attribute download":
            Text('download=""') + Key("left:1"),
        "attribute draggable":
            Text('draggable=""') + Key("left:1"),
        "attribute drops on":
            Text('dropzone=""') + Key("left:1"),
        "attribute form type":
            Text('enctype=""') + Key("left:1"),
        "attribute for":
            Text('for=""') + Key("left:1"),
        "attribute form":
            Text('form=""') + Key("left:1"),
        "attribute form action":
            Text('formaction=""') + Key("left:1"),
        "attribute headers":
            Text('headers=""') + Key("left:1"),
        "attribute height":
            Text('height=""') + Key("left:1"),
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
