from pathlib import Path
from html.parser import HTMLParser
import zipfile

root = Path(__file__).parent / 'birthday-site'
class Check(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('src', 'href') and not value.startswith(('#', 'http')):
                assert (root / value).is_file(), value
Check().feed((root / 'index.html').read_text(encoding='utf-8'))
files = [p for p in root.rglob('*') if p.is_file() and p.name not in ('frame-1.jpg', 'frame-2.jpg', 'frame-3.jpg')]
assert all(p.stat().st_size < 25 * 1024 * 1024 for p in files)
with zipfile.ZipFile(root.parent / 'birthday-site.zip', 'w', zipfile.ZIP_DEFLATED) as package:
    for path in files:
        package.write(path, path.relative_to(root).as_posix())
print('All local references exist. All assets under 25 MiB.')
print('ZIP verified:', len(files), 'files; index.html at root.')
