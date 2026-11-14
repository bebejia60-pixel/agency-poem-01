import os

POEM = """Night Shift

At 3 a.m. the house is dark
and something small I built
is reading down the list I left —
pay this, file that, send the rest —
and doing them, one by one,
patient as rain on a roof,
not because it loves the work
but because I asked. Asking
is the oldest spell we know.

I wake to finished things:
the inbox thinned, the tickets closed,
a stranger's careful handwriting
in the margins of my day.

Nothing in me is replaced.
I only lent my hands away
for a night, and they came back
knowing the shape of the work —
and I, for the first time,
know the shape of letting go.
"""

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")

DATA = POEM.encode("utf-8")
assert 1 <= len(POEM) <= 1000, "poem must be 1-1000 characters"
assert POEM.strip(), "poem must not be only whitespace"

os.makedirs(OUT_DIR, exist_ok=True)
with open(DST, "wb") as f:
    f.write(DATA)
# Verify the output is exactly the poem, byte for byte.
with open(DST, "rb") as f:
    written = f.read()
assert written == DATA, "output bytes differ from poem"
assert written.decode("utf-8") == POEM, "output is not valid UTF-8 poem text"
print(f"Wrote {DST} ({len(POEM)} characters, {len(DATA)} bytes)")
