sentence=raw_input("sentence:")

screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2

print
print ' '*left_margin+'+'+'-'*(box_width-2)+'+'
print ' '*left_margin+'|'+' '*(text_width+4)+'|'
print ' '*left_margin+'|'+' '*2+sentence+' '*2+'|'
print ' '*left_margin+'|'+' '*(text_width+4)+'|'
print ' '*left_margin+'+'+'-'*(box_width-2)+'+'
print
raw_input('press any key')
