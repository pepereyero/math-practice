import pep8
import os


def test_pep8_conformance():
    """Test that we conform to PEP8."""

    pep8style = pep8.StyleGuide(quiet=True)
    result = pep8style.check_files([os.path.join(root, fname)
                                    for root, _, fnames in os.walk('.')
                                    for fname in fnames
                                    if (fname != '__init__.py' and
                                        os.path.splitext(fname)[1] == '.py')])
    assert result.total_errors == 0
