import json
from pathlib import Path
from urllib.parse import urlsplit

def check(result):
    expected=json.loads(Path('tests/public-sites/pages.json').read_text())
    assert 'error' not in result, result
    rows=result['pages']
    assert len(rows)==len(expected),len(rows)
    for row,(url,lang) in zip(rows,expected):
        print(url, row, flush=True)
        assert row['lang']==lang and row['heading'] and row['title'] and row['cardTitle'],row
        assert row['url'].rstrip('/')==url.rstrip('/')==row['canonical'].rstrip('/'),row
        assert urlsplit(row['card']).scheme=='https' and row['image']==[1200,630],row
        assert row['client']>200 and row['scroll']<=row['client']+1,row
