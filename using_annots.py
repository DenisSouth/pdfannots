from pdfannots import process_file, PrettyPrinter
from colr import color as term_color
from collections import Counter

input_path = r"tests\hotos17.pdf"
# input_path = r"tests\issue9.pdf"
# input_path = r"tests\issue13.pdf"
# input_path = r"tests\pr24.pdf"

annots, outlines = process_file(open(input_path, 'rb'), emit_progress=True)

pp = PrettyPrinter(outlines, wrapcol=None, condense=True)
data = pp.return_all(annots)

all_ct = list(tuple([item.tagname] + item.selection_colour) for item in data)

classes = {}
for index, data_ in enumerate(Counter(all_ct).most_common()):
    rgb = data_[0][1:]
    class_n = data_[0]
    cnt = data_[1]
    classes[class_n] = index
    print("class:", index, "count:", cnt, term_color(class_n, fore=(0, 0, 0), back=rgb))
print()

for d in data:
    key = tuple([d.tagname] + d.selection_colour)
    to_print = f"class:     :  {classes[key]}" \
           f"\ntext       :{d.text}" \
           f"\ncomment    :{d.comment}" \
           f"\ntagname    :{d.tagname}" \
           f"\nsel_colour :{d.selection_colour}" \
           f"\nrect       :{d.rect}" \
           f"\npage_number:{d.page_number}" \
           f"\nchap_title :{d.chap_title}\n"

    print(term_color(to_print, fore=(0, 0, 0), back=d.selection_colour))
