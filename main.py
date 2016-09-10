
from pptx import Presentation

textBlob = list()
prs = Presentation("pitch.pptx")
prs.save('temp.pptx')

slide = prs.slides[2]

for shape in slide.shapes:
    try:
        textBlob.append(shape.text)
    except AttributeError:
        print "not a valid attribute"

textBlob = filter(None, textBlob)  # fastest

print textBlob
