# Usage

`py3html` has very simple usage simple as html.

### Getting Starting

After installing now import `py3html`.

```python
import py3html as ph
```

### Basic usage

```python
code = ph.P("Test")
assert code.html() == "<p>Test</p>\n"
```

### More complex usage

```python
code = ph.P(
    "This is a ",
    ph.A("test", attrs={"href": "test.com"}),
    " code.",
)
assert code.html() == textwrap.dedent('''\
<p>This is a <a href="test.com">test</a>
 code.</p>
 ''')
```

### Html escape usage

```python
code = ph.P(
    '<small>Escape "it"!</small>',
)
assert code.html() == textwrap.dedent("""\
<p>&lt;small&gt;Escape &quot;it&quot;!&lt;/small&gt;</p>
""")
```

### Attributes usage

```python
code = ph.Div(
    ph.P("Test", attrs={"style": "color: red;"}),
    attrs={"class": "test"},
)
assert code.html() == textwrap.dedent('''\
<div class="test"><p style="color: red;">Test</p>
</div>
''')
```

### Usage for `add` method, to create dynamic content

```python
table = ph.Table()
thead = ph.Thead()
tbody = ph.Tbody()

thead.add(
    ph.Tr(
        ph.Th("Id"),
        ph.Th("Name"),
    )
)
for i in range(3):
    tbody.add(
        ph.Tr(
            ph.Td(i),
            ph.Td(f"Test {i}"),
        )
    )
table.add(thead)
table.add(tbody)
assert (
    table.html()
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
class TestElement(ph.Element):
    tag = "test"
    attrs = {"class": "test"}

code = TestElement("New element!")
assert code.html(), textwrap.dedent('''\
<test class="test">New element!</test>
''')
```

### Create new element and update its html process methods

#### Preprocess

Runs at first

```python
class TestElement(ph.Element):
    tag = "test"

    def pre_process(self):
        return f"<{self.tag}_test>"

code = TestElement("Pre process")
assert code.html(), "<test_test>Pre process</test>"
```

#### On process

Runs when its element processed

```python
class TestElement(ph.Element):
    tag = "test"

    def on_process(self):
        return "..."

code = TestElement("On process (This will not be shown)", ph.P("This will not be shown, too."))
assert code.html(), "<test>...</test>"
```

#### Post process

Runs when last tag appended

```python
class TestElement(ph.Element):
    tag = "test"

    def post_process(self):
        return f"<{self.tag}_test>"

code = TestElement("Post process")
assert code.html() == "<test>Post process<test_test>\n"
```

### Sample new element usage

This is a new element sample

```python
class TestElement(ph.Element):
    tag = "test"

    def pre_process(self):
        return f"<{self.tag}{self.attributes}/>"

    def on_process(self):
        return

    def post_process(self):
        return

code = TestElement("All process method", attrs={"class": "test"})
assert code.html() == '<test class="test"/>\n'
```
