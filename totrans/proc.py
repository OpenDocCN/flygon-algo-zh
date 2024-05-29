import os, re, yaml

def proc_yaml(trans):
    for it in trans:
        if 'zh' in it: continue
        if 'answer' not in it: continue
        ans = it['answer']
        ms = re.findall(r'^\-   (.+?)$', ans, flags=re.M)
        if len(ms) != 1: 
            del it['answer']
        else:
            it['zh'] = ms[0]
    

fnames = [f for f in os.listdir() if f.endswith('.yaml')]

for f in fnames:
    print(f)
    trans =  yaml.safe_load(open(f, encoding='utf8').read())
    proc_yaml(trans)
    open(f, 'w', encoding='utf8').write(yaml.safe_dump(trans, allow_unicode=True))

