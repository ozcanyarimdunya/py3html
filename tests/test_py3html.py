import unittest

import py3html as ph


class TestPy3Html(unittest.TestCase):
    def test_basic(self):
        code = ph.Div(
            ph.P("Test"),
        )
        self.assertEqual(
            code.html(),
            '<div><p>Test</p></div>',
        )

    def test_complex(self):
        code = ph.P(
            "This is a ",
            ph.A("test", attrs={"href": "test.com"}),
            " code.",
        )
        self.assertEqual(
            code.html(),
            '<p>This is a <a href="test.com">test</a> code.</p>',
        )

    def test_html_escape(self):
        code = ph.P(
            '<small>Escape "it"!</small>',
        )
        self.assertEqual(
            code.html(),
            '<p>&lt;small&gt;Escape &quot;it&quot;!&lt;/small&gt;</p>',
        )

    def test_attributes(self):
        code = ph.Div(
            ph.P("Test", attrs={"style": "color: red;"}),
            attrs={"class": "test"},
        )
        self.assertEqual(
            code.html(),
            '<div class="test"><p style="color: red;">Test</p></div>',
        )

    def test_add(self):
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
        self.assertEqual(
            table.html(),
            (
                '<table>'
                '<thead>'
                '<tr><th>Id</th><th>Name</th></tr>'
                '</thead>'
                '<tbody>'
                '<tr><td>0</td><td>Test 0</td></tr>'
                '<tr><td>1</td><td>Test 1</td></tr>'
                '<tr><td>2</td><td>Test 2</td></tr>'
                '</tbody>'
                '</table>'
            ),
        )

    def test_str(self):
        code = ph.P("test")
        self.assertEqual(
            code.html(),
            str(code),
        )

    def test_new_element(self):
        class TestElement(ph.Element):
            tag = "test"
            attrs = {"class": "test"}

        code = TestElement("New element!")
        self.assertEqual(
            code.html(),
            '<test class="test">New element!</test>'
        )

    def test_pre_process(self):
        class TestElement(ph.Element):
            tag = "test"

            def pre_process(self):
                return f"<{self.tag}_test>"

        code = TestElement("Pre process")
        self.assertEqual(
            code.html(),
            '<test_test>Pre process</test>'
        )

    def test_on_process(self):
        class TestElement(ph.Element):
            tag = "test"

            def on_process(self):
                return "..."

        code = TestElement(
            "On process (This will not be shown)",
            ph.P("This will not be shown, too.")
        )
        self.assertEqual(
            code.html(),
            "<test>...</test>"
        )

    def test_post_process(self):
        class TestElement(ph.Element):
            tag = "test"

            def post_process(self):
                return f"<{self.tag}_test>"

        code = TestElement("Post process")
        self.assertEqual(
            code.html(),
            '<test>Post process<test_test>',
        )

    def test_all_process_methods(self):
        class TestElement(ph.Element):
            tag = "test"

            def pre_process(self):
                return f"<{self.tag}{self.attributes}/>"

            def on_process(self):
                return

            def post_process(self):
                return

        code = TestElement("All process method", attrs={"class": "test"})
        self.assertEqual(
            code.html(),
            '<test class="test"/>',
        )


if __name__ == '__main__':
    unittest.main()
