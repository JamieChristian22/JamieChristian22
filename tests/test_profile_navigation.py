"""Local, network-free regression tests for profile navigation checks."""
import tempfile
import unittest
from pathlib import Path

from tools.check_profile_navigation import check_local_links, local_targets


class ProfileLinkTests(unittest.TestCase):
    def test_local_targets_exclude_http_and_fragment(self):
        content = '[internal](README.md#intro) [web](https://github.com/) [same](#start) [mail](mailto:x@y.com)'
        self.assertEqual(list(local_targets(content)), ['README.md'])

    def test_encoded_file_name(self):
        self.assertEqual(list(local_targets('[a](<Folder%20Name/file.md>)')), ['Folder Name/file.md'])

    def test_broken_file_is_detected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'README.md').write_text('[missing](NOT_THERE.md)', encoding='utf-8')
            errors = check_local_links(root, [Path('README.md')])
            self.assertEqual(len(errors), 1)
            self.assertIn('Broken local link', errors[0])

    def test_existing_file_is_accepted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'README.md').write_text('[guide](guide.md)', encoding='utf-8')
            (root / 'guide.md').write_text('# Guide\n', encoding='utf-8')
            self.assertEqual(check_local_links(root, [Path('README.md')]), [])

    def test_escape_outside_checkout_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'README.md').write_text('[escape](../private.txt)', encoding='utf-8')
            errors = check_local_links(root, [Path('README.md')])
            self.assertTrue(errors and 'Outside repository' in errors[0])


if __name__ == '__main__':
    unittest.main()
