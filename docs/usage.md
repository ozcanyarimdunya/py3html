# Usage

`py3html` has very simple usage simple as html.

### Getting Starting

After installing now import `py3html`.

```python
import py3html as ph
```

### Basic usage

```python
code = ph.p("Test")
assert code.html == "<p>Test</p>\n"


code = ph.br()
assert code.html == "<br />\n"


code = ph.p("test")
assert str(code) == "<p>test</p>\n"
```

### More complex usage

```python
code = ph.p(
"This is a ",
ph.a("test", href="test.com"),
" code.",
)
assert code.html == textwrap.dedent('''\
<p>This is a <a href="test.com">test</a>
code.</p>
''')
```

### Html escape usage

```python
code = ph.p(
'<small>Escape "it"!</small>',
)
assert code.html == textwrap.dedent("""\
<p>&lt;small&gt;Escape &quot;it&quot;!&lt;/small&gt;</p>
""")
```

### Attributes usage

```python
code = ph.div(
    ph.p("Test", style="color: red;"),
    class_="test",
)
assert code.html == textwrap.dedent('''\
<div class="test"><p style="color: red;">Test</p>
</div>
''')
```

### Usage for `add` method, to create dynamic content

```python
table = ph.table(
    ph.thead(
        ph.tr(
            ph.th("Id"),
            ph.th("Name"),
        )
    ),
    ph.tbody(
        *[
            ph.tr(
                ph.td(i),
                ph.td(f"Test {i}")
            )
            for i in range(3)
        ]
    )
)

assert (
    table.html
    == textwrap.dedent("""\
    <table><thead><tr><th>Id</th>
    <th>Name</th>
    </tr>
    </thead>
    <tbody><tr><td>0</td>
    <td>Test 0</td>
    </tr>
    <tr><td>1</td>
    <td>Test 1</td>
    </tr>
    <tr><td>2</td>
    <td>Test 2</td>
    </tr>
    </tbody>
    </table>
""")
)
```

### Create new element

```python
test = ph.element(tag="test")
code = test("New element!", class_="test")
assert code.html == textwrap.dedent('''\
<test class="test">New element!</test>
''')
```

### Create new element with default attributes

```python
test = ph.element(tag="test", class_="test", style="background: red;")
assert test("Element 1!").html == '<test class="test" style="background: red;">Element 1!</test>\n'
assert test("Element 2!", class_="new").html == '<test class="new" style="background: red;">Element 2!</test>\n'
assert test("Element 3!", class_=None).html == '<test class style="background: red;">Element 3!</test>\n'
```
