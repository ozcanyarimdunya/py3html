import textwrap

import py3html as ph


def test_basic():
    code = ph.p("Test")
    assert code.html == "<p>Test</p>\n"


def test_self_closing():
    code = ph.br()
    assert code.html == "<br />\n"


def test_str():
    code = ph.p("test")
    assert str(code) == "<p>test</p>\n"


def test_complex():
    code = ph.p(
        "This is a ",
        ph.a("test", href="test.com"),
        " code.",
    )
    assert code.html == textwrap.dedent('''\
    <p>This is a <a href="test.com">test</a>
     code.</p>
     ''')


def test_html_escape():
    code = ph.p(
        '<small>Escape "it"!</small>',
    )
    assert code.html == textwrap.dedent("""\
    <p>&lt;small&gt;Escape &quot;it&quot;!&lt;/small&gt;</p>
    """)


def test_attributes():
    code = ph.div(
        ph.p("Test", style="color: red;"),
        class_="test",
    )
    assert code.html == textwrap.dedent('''\
    <div class="test"><p style="color: red;">Test</p>
    </div>
    ''')


def test_add():
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


def test_new_element():
    test = ph.element(tag="test")
    code = test("New element!", class_="test")
    assert code.html == textwrap.dedent('''\
    <test class="test">New element!</test>
    ''')


def test_new_element_with_attributes():
    test = ph.element(tag="test", class_="test", style="background: red;")
    assert (
        test("Element 1!").html
        == '<test class="test" style="background: red;">Element 1!</test>\n'
    )
    assert (
        test("Element 2!", class_="changed").html
        == '<test class="changed" style="background: red;">Element 2!</test>\n'
    )
    assert (
        test("Element 3!", class_=None).html
        == '<test class style="background: red;">Element 3!</test>\n'
    )
