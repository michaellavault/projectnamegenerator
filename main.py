# Générateur avancé de noms de projet (inspiré NSA / agences)

import random
import string
import argparse

PREFIXES = [
    "AERO","CYBER","NANO","PROTO","ULTRA","QUANT","TRANS","META","NEO","ELECTRO",
    "SPECTRA","HYDRO","MAGNO","CRYPTO","PHOTO","ASTRO","HYBRID","VIRTUAL","THERMO","PSEUDO"
]
RACINES = [
    "NET","CORE","BRIDGE","LINK","SCOPE","WATCH","MIND","BEAM","FORGE","SOURCE",
    "TRACE","SENTRY","VECTOR","NODE","BLADE","CIPHER","VAULT","GATE","SHIELD","MATRIX"
]
SUFFIXES = [
    "X","ONE","9000","OPS","SYS","NET","LAB","ZONE","PRO","SIGMA","OMEGA","XEN","BYTE","ARC","ZERO"
]
LATIN = [
    "IGNIS","AURUM","LUX","UMBRA","SAPIENS","NOX","CAELUM","TERRA","VITA","MORS","SILVA","TEMPUS"
]
ADJECTIFS = [
    "SILENT","BLACK","INFINITE","OBSIDIAN","TITAN","PHANTOM","STELLAR","IRON","VOID","ALPHA","GHOST","ONYX","STORM","VORTEX","EPIC"
]
SYLLABLES = [
    "ar","en","ex","ion","tek","sys","com","dat","sec","crypt","man","form","gen","sil","volt"
]
GREEK = ["ALPHA","BETA","DELTA","OMEGA","SIGMA","EPSILON","THETA","XI","PHI","PSI","ZETA"]

def make_code(prefix=True, suffix=True):
    p = random.choice(PREFIXES) if prefix else ""
    r = random.choice(RACINES)
    s = random.choice(SUFFIXES) if suffix else ""
    sep = random.choice(["","-","_"])
    return f"{p}{sep}{r}{sep}{s}".strip(sep)

def make_latinate():
    w1 = random.choice(LATIN)
    w2 = random.choice(ADJECTIFS)
    return f"{w1}-{w2}"

def make_numeric():
    base = make_code()
    num = str(random.randint(10,999))
    return f"{base}-{num}"

def make_syllabic(length=3):
    return "".join(random.choice(SYLLABLES).upper() for _ in range(length))

def make_acronym():
    parts = random.sample(ADJECTIFS + PREFIXES + RACINES, k=random.randint(2,3))
    acronym = "".join(p[0] for p in parts)
    return f"{'-'.join(parts)} ({acronym})"

def make_codename():
    return f"{random.choice(ADJECTIFS)}_{random.choice(RACINES)}_{random.choice(GREEK)}"

def make_random():
    funcs = [make_code, make_latinate, make_numeric, make_syllabic, make_acronym, make_codename]
    return random.choice(funcs)()

def generate(style="mixed", count=1000):
    out = set()
    while len(out) < count:
        if style == "code":
            out.add(make_code())
        elif style == "latin":
            out.add(make_latinate())
        elif style == "numeric":
            out.add(make_numeric())
        elif style == "syllabic":
            out.add(make_syllabic(random.randint(2,3)))
        elif style == "acronym":
            out.add(make_acronym())
        elif style == "codename":
            out.add(make_codename())
        else:
            out.add(make_random())
    return sorted(out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur avancé de noms de projet")
    parser.add_argument("-s","--style", choices=["mixed","code","latin","numeric","syllabic","acronym","codename"],
                        default="mixed", help="Style de génération")
    parser.add_argument("-n","--number", type=int, default=10, help="Nombre de noms à générer")
    args = parser.parse_args()

    for name in generate(style=args.style, count=args.number):
        print(name)
