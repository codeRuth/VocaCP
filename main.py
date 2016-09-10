import sys
from pptx import Presentation

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv[0])

# class VocaCP(object):
#     def __init__(self, Presentation):
#         self.prez = Presentation

#     def getText(self, slideNum):

# # copy the content of the presentation
# str(sys.argv[0])
textBlob = list()
prs = Presentation("pitch.pptx")
prs.save('temp.pptx')

slide = prs.slides[2]
# slide_master = prs.slide_masters[0].slide_layouts[0]
# print(slide_master)
# is equivalent to
# slide_master = prs.slide_master

for shape in slide.shapes:
    try:
        textBlob.append(shape.text)
    except AttributeError:
        print "not a valid attribute"
        # if not shape.has_text_frame:
        #     continue
        # text_frame = shape.text_frame
        # print shape.text

# print text_frame

# for paragraph in text_frame.paragraphs:
# 	print paragraph.text


# p = len(text_frame.paragraphs)
# p1 = text_frame.paragraphs[1]

# print p
# print p1



textBlob = filter(None, textBlob)  # fastest

print textBlob
