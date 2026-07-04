
#1: Why extract_data(self) needs self

extract_data is defined inside a class, which makes it a method, not a plain function. Every method in Python automatically receives the object it's being called on as its first argument — by convention we name that parameter self

#2: 
"1.0" means line 1, column 0 → the very start of the text, even if there's only one line
"end-1c" means "the end of the content, minus 1 character" — the -1c trims off the automatic trailing newline that Text widgets always add