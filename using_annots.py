from pdfannots import process_file, PrettyPrinter
from colr import color

input_path = r"tests\hotos17.pdf"
# input_path = r"tests\issue9.pdf"
# input_path = r"tests\issue13.pdf"
# input_path = r"tests\pr24.pdf"

annots, outlines = process_file(open(input_path, 'rb'), emit_progress=True)

pp = PrettyPrinter(outlines, wrapcol=None, condense=True)
data = pp.return_all(annots)

for d in data:
    prnt = f"text:{d.text}" \
           f"\ncomment:{d.comment}" \
           f"\ntagname:{d.tagname}" \
           f"\nrect_colour:{d.selection_colour}" \
           f"\nrect:{d.rect}" \
           f"\nP_number:{d.P_number}" \
           f"\nP_title:{d.P_title}\n"

    print(color(prnt, fore=(0, 0, 0), back=d.selection_colour))
