<map version="freeplane 1.8.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Pizzacats" FOLDED="false" ID="ID_1710282600" CREATED="1587226137498" MODIFIED="1587226200275" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle" background="#3c3f41">
    <properties fit_to_viewport="false" show_note_icons="true" edgeColorConfiguration="#808080ff,#00ddddff,#dddd00ff,#dd0000ff,#00dd00ff,#dd0000ff,#7cddddff,#dddd7cff,#dd7cddff,#7cdd7cff,#dd7c7cff,#7c7cddff"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#cccccc" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#cccccc" BACKGROUND_COLOR="#3c3f41" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#dddddd" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#ff3300">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#ffb439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#99ffff">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#bbbbbb">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="5" RULE="ON_BRANCH_CREATION"/>
<node TEXT="Was?" POSITION="right" ID="ID_1198125582" CREATED="1587226142028" MODIFIED="1587226214217">
<edge COLOR="#00dddd"/>
<node TEXT="Webanwendung: Pizzacats" ID="ID_183835034" CREATED="1587226273480" MODIFIED="1587226299381"/>
<node TEXT="Bestellvorgang" ID="ID_929884456" CREATED="1587226300829" MODIFIED="1587226313675">
<node TEXT="Auswahl ohne/mit Bestellung" ID="ID_629647292" CREATED="1587226358956" MODIFIED="1587226452646"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Nur ohne Anmeldung gemacht
    </p>
  </body>
</html>
</richcontent>
<node TEXT="index.html" ID="ID_1961643816" CREATED="1587226402919" MODIFIED="1587226406454"/>
</node>
<node TEXT="Name + Adresse erfassen" ID="ID_1874063540" CREATED="1587226395217" MODIFIED="1587226423933">
<node TEXT="bestellung_keineanmeldung.html" ID="ID_1543742549" CREATED="1587226491098" MODIFIED="1587226511004">
<node TEXT="kunde_anlegen.py" ID="ID_623506544" CREATED="1587226517336" MODIFIED="1587226531834"/>
</node>
</node>
<node TEXT="Pizzen auswählen" ID="ID_789193590" CREATED="1587226463532" MODIFIED="1587226475086">
<node TEXT="pizzaliste.py" ID="ID_125398932" CREATED="1587226561884" MODIFIED="1587226565741"/>
</node>
<node TEXT="Bestellung anzeigen" ID="ID_695945707" CREATED="1587226475964" MODIFIED="1587226486587">
<node TEXT="bestellung_keineanmeldung.py" ID="ID_1951720939" CREATED="1587226607924" MODIFIED="1587226613430"/>
</node>
</node>
<node TEXT="Pizzen anlegen" ID="ID_450476355" CREATED="1587227390363" MODIFIED="1587227402883">
<node TEXT="pizzaanlage.html" ID="ID_336797817" CREATED="1587227404707" MODIFIED="1587227432556">
<node TEXT="pizzaanlage.py" ID="ID_504302146" CREATED="1587227432562" MODIFIED="1587227438921"/>
</node>
</node>
</node>
<node TEXT="Wie?" POSITION="left" ID="ID_6275547" CREATED="1587226218268" MODIFIED="1587226221937">
<edge COLOR="#dddd00"/>
<node TEXT="Datenbank" ID="ID_1524651751" CREATED="1587226618186" MODIFIED="1587226621688">
<node TEXT="MySQL" ID="ID_835781451" CREATED="1587226621694" MODIFIED="1587226626660">
<node TEXT="XAMPP" ID="ID_459933758" CREATED="1587226626665" MODIFIED="1587226633803"/>
</node>
<node TEXT="DDL" ID="ID_23423638" CREATED="1587227102274" MODIFIED="1587227104961">
<node TEXT="Erstellen von Datenbank und Tabellen" ID="ID_1537018895" CREATED="1587227108729" MODIFIED="1587227120806"/>
</node>
<node TEXT="SQL" ID="ID_405161111" CREATED="1587227452548" MODIFIED="1587227483803">
<node TEXT="SELECT" ID="ID_1859078730" CREATED="1587227483812" MODIFIED="1587227486578"/>
<node TEXT="INSERT" ID="ID_440186789" CREATED="1587227497288" MODIFIED="1587227500051"/>
</node>
</node>
<node TEXT="Python" ID="ID_961698903" CREATED="1587226636519" MODIFIED="1587226639564">
<node TEXT="3.8.2 32bit" ID="ID_538222247" CREATED="1587226639567" MODIFIED="1587226682847"/>
</node>
<node TEXT="HTTP-Server" ID="ID_1233986378" CREATED="1587226690907" MODIFIED="1587226698925">
<node TEXT="Apache httpd" ID="ID_1012595947" CREATED="1587226698931" MODIFIED="1587226708864">
<node TEXT="XAMPP" ID="ID_929774662" CREATED="1587226708867" MODIFIED="1587226717476"/>
<node TEXT="für .html-Seiten" ID="ID_855122872" CREATED="1587226724151" MODIFIED="1587226731822"/>
<node TEXT="Port: 80" ID="ID_1343566305" CREATED="1587226764864" MODIFIED="1587226770970"/>
</node>
<node TEXT="Python HTTP-Server" ID="ID_140605086" CREATED="1587226742030" MODIFIED="1587226754131">
<node TEXT="für .py-Dateien" ID="ID_1098198391" CREATED="1587226754135" MODIFIED="1587226761057"/>
<node TEXT="Port: 8888" ID="ID_1516753710" CREATED="1587226772384" MODIFIED="1587226778252"/>
<node TEXT="cgi-bin/cgiserver.py" ID="ID_1428821516" CREATED="1587226779436" MODIFIED="1587226807530"/>
</node>
</node>
<node TEXT="IDE" ID="ID_16132490" CREATED="1587226812163" MODIFIED="1587226814648">
<node TEXT="Integrated Development Environment" ID="ID_1352671199" CREATED="1587226814659" MODIFIED="1587226833424"/>
<node TEXT="Visual Studio Code" ID="ID_988301173" CREATED="1587226836412" MODIFIED="1587226853980">
<node TEXT="Extension für Python" ID="ID_1270085466" CREATED="1587226872621" MODIFIED="1587226886488">
<node TEXT="Debugging" ID="ID_1585666007" CREATED="1587226890944" MODIFIED="1587226895125">
<node TEXT="Breakpoint" ID="ID_1566286625" CREATED="1587226895128" MODIFIED="1587226903024"/>
</node>
<node TEXT="CGI-Server starten" ID="ID_1451902507" CREATED="1587226904466" MODIFIED="1587226911723"/>
</node>
<node TEXT="Shortcuts" ID="ID_1448251539" CREATED="1587226921146" MODIFIED="1587226925711">
<node TEXT="Shift+P" ID="ID_1309698586" CREATED="1587226925716" MODIFIED="1587226932523">
<node TEXT="Dateien finden" ID="ID_658871381" CREATED="1587227021568" MODIFIED="1587227029050"/>
</node>
<node TEXT="Strg+Shift+P" ID="ID_412993798" CREATED="1587226933613" MODIFIED="1587226945889">
<node TEXT="Befehle, z.B. Open in default browser" ID="ID_1310224421" CREATED="1587227031951" MODIFIED="1587227052025"/>
</node>
<node TEXT="Strg+Shift+K" ID="ID_1387589811" CREATED="1587226947060" MODIFIED="1587226959741">
<node TEXT="Zeile löschen" ID="ID_1048565968" CREATED="1587227056260" MODIFIED="1587227061217"/>
</node>
<node TEXT="F5" ID="ID_139511073" CREATED="1587226960399" MODIFIED="1587226962185">
<node TEXT="Debuggen ausgewählte Datei" ID="ID_1926973117" CREATED="1587227063722" MODIFIED="1587227076666"/>
</node>
<node TEXT="Strg+F5" ID="ID_1817406962" CREATED="1587227079360" MODIFIED="1587227084648">
<node TEXT="Ausführen ausgewählte Datei" ID="ID_42924888" CREATED="1587227086051" MODIFIED="1587227099974"/>
</node>
</node>
</node>
</node>
<node TEXT="Testen" ID="ID_1547885582" CREATED="1587227125422" MODIFIED="1587227130131">
<node TEXT="Unit Tests zum Ausprobieren" ID="ID_1775979979" CREATED="1587227130134" MODIFIED="1587227142399"/>
</node>
<node TEXT="Deployen" ID="ID_1317485392" CREATED="1587227158925" MODIFIED="1587227171754">
<node TEXT="Installieren/Ausführen außerhalb IDE" ID="ID_987378519" CREATED="1587227171756" MODIFIED="1587227181126"/>
<node TEXT=".html-Seiten nach htdoc" ID="ID_833381253" CREATED="1587227186401" MODIFIED="1587227197779"/>
<node TEXT="Python-Seiten nach cgi-bin" ID="ID_1644459765" CREATED="1587227198533" MODIFIED="1587227217010"/>
</node>
<node TEXT="Quellcode/Sourcecode" ID="ID_883524335" CREATED="1587227275275" MODIFIED="1587227287560">
<node TEXT="Versionskontrolle" ID="ID_270394584" CREATED="1587227287568" MODIFIED="1587227294381">
<node TEXT="Git" ID="ID_1769344186" CREATED="1587227294387" MODIFIED="1587227299099">
<node TEXT="git commit" ID="ID_1581847135" CREATED="1587227315002" MODIFIED="1587227318523"/>
</node>
<node TEXT="GitHub" ID="ID_695592640" CREATED="1587227302221" MODIFIED="1587227305891">
<node TEXT="git push" ID="ID_1341230786" CREATED="1587227323085" MODIFIED="1587227325335"/>
</node>
</node>
</node>
<node TEXT="Reproduzierbar machen" ID="ID_963891961" CREATED="1587227364213" MODIFIED="1587227371336">
<node TEXT="Datenbank mit Pizzen erstellen" ID="ID_1758519063" CREATED="1587227371347" MODIFIED="1587227383283"/>
<node TEXT="html-Seiten nach xampp/htdocs kopieren" ID="ID_798804052" CREATED="1587227589016" MODIFIED="1587227624692"/>
<node TEXT=".py-Dateien nach xampp/cgi-bin/cgi-bin" ID="ID_506954705" CREATED="1587227601430" MODIFIED="1587234702007">
<node TEXT="! cgiserver.py mit Python starten" ID="ID_700284391" CREATED="1587227770361" MODIFIED="1587227789960">
<node TEXT="C:\Users\juerg\AppData\Local\Programs\Python\Python38-32^\python.exe" ID="ID_332403451" CREATED="1587227885909" MODIFIED="1587227897278"/>
<node TEXT="Rechtsklick auf Datei" ID="ID_469198531" CREATED="1587227967183" MODIFIED="1587227982504">
<node TEXT="Terminal mit Strg+C schließen" ID="ID_982052911" CREATED="1587227985430" MODIFIED="1587227996971"/>
</node>
<node TEXT="start_server.bat - ggf. Pfad anpassen für python.exe/xampp" ID="ID_1265567516" CREATED="1587234663327" MODIFIED="1587234685124"/>
</node>
</node>
<node TEXT="xampp" ID="ID_1185587132" CREATED="1587227724411" MODIFIED="1587227734709">
<node TEXT="Apache httpd starten" ID="ID_1703644748" CREATED="1587227738479" MODIFIED="1587227751037"/>
<node TEXT="MySQL starten" ID="ID_1633697223" CREATED="1587227753846" MODIFIED="1587227758026">
<node TEXT="sql/setup_pizzastars_db.sql in phpMyAdmin SQL ausführen" ID="ID_1999257791" CREATED="1587229126573" MODIFIED="1587231098587"/>
</node>
</node>
</node>
<node TEXT="Herausforderungen" ID="ID_142442719" CREATED="1587227517485" MODIFIED="1587227531173">
<node TEXT="Datentypen aus Datenbank" ID="ID_1117928538" CREATED="1587227532587" MODIFIED="1587227540753"/>
<node TEXT="SQL&quot;dynamisch&quot; machen" ID="ID_150009137" CREATED="1587227542777" MODIFIED="1587227554399"/>
<node TEXT="Übersicht behalten über Dateienwust" ID="ID_135223206" CREATED="1587227561801" MODIFIED="1587227572354"/>
</node>
</node>
</node>
</map>
