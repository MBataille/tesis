from scholarly import scholarly, ProxyGenerator
from alive_progress import alive_bar, alive_it

def get_bibtex(pub_str):
    print(f'Trying for {pub_str}')
    try:
        query = scholarly.search_pubs(pub_str)
        pub = next(query)
    except:
        print(f'Could not find ref for {pub_str}')
        return ''
    return scholarly.bibtex(pub)

def parse_ref(ref_str: str):
    start = ref_str.find('[')
    stop = ref_str.find(']')
    if start == -1 or stop == -1:
        return ref_str

    return ref_str.replace(ref_str[start:stop+2], '')

def main():
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    scholarly.use_proxy(pg)

    print(success)

    filename = 'refs.txt'
    bibtexs = []
    with open(filename) as f:
        bar = alive_it(f)
        for line in bar:
            ref = parse_ref(line)
            bar.text(f'Searching citation for: {ref}')
            bibtexs.append(get_bibtex(ref))

    for bibtex in bibtexs:
        print(bibtex + '\n\n')

if __name__ == '__main__':
    main()
