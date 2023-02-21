import textwrap

import py3html as ph


def test_basic():
    code = ph.P("Test")
    assert code.html() == "<p>Test</p>\n"


def test_complex():
    code = ph.P(
        "This is a ",
        ph.A("test", attrs={"href": "test.com"}),
        " code.",
    )
    assert code.html() == textwrap.dedent('''\
    <p>This is a <a href="test.com">test</a>
     code.</p>
     ''')


def test_html_escape():
    code = ph.P(
        '<small>Escape "it"!</small>',
    )
    assert code.html() == textwrap.dedent("""\
    <p>&lt;small&gt;Escape &quot;it&quot;!&lt;/small&gt;</p>
    """)


def test_attributes():
    code = ph.Div(
        ph.P("Test", attrs={"style": "color: red;"}),
        attrs={"class": "test"},
    )
    assert code.html() == textwrap.dedent('''\
    <div class="test"><p style="color: red;">Test</p>
    </div>
    ''')


def test_add():
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


def test_str():
    code = ph.P("test")
    assert code.html() == str(code)


def test_new_element():
    class TestElement(ph.Element):
        tag = "test"
        attrs = {"class": "test"}

    code = TestElement("New element!")
    assert code.html(), textwrap.dedent('''\
    <test class="test">New element!</test>
    ''')


def test_pre_process():
    class TestElement(ph.Element):
        tag = "test"

        def pre_process(self):
            return f"<{self.tag}_test>"

    code = TestElement("Pre process")
    assert code.html(), "<test_test>Pre process</test>"


def test_on_process():
    class TestElement(ph.Element):
        tag = "test"

        def on_process(self):
            return "..."

    code = TestElement("On process (This will not be shown)", ph.P("This will not be shown, too."))
    assert code.html(), "<test>...</test>"


def test_post_process():
    class TestElement(ph.Element):
        tag = "test"

        def post_process(self):
            return f"<{self.tag}_test>"

    code = TestElement("Post process")
    assert code.html() == "<test>Post process<test_test>\n"


def test_all_process_methods():
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
