import mechanize
brows = mechanize.Browser()


url = 'https://www.linkedin.com/'

brows.set_handle_robots(False)
response = brows.open(url)


for form in brows.forms():
    print "Form name: ", form.name
    print '\n'
    print form
    print '\n'
    print '\n'


list(brows.forms())

brows.choosen_form = list(brows.forms())[0]


for control in brows.choosen_form.controls:
    print control.name
    print '\n'
    print control.value


form_names = [form.name for form in brows.forms()]


brows.controls[0].value = 'joshvoss90@outlook.com'
brows.controls[1].value = 'Jobpassword1!'

brows.submit()

brows.geturl()

brows.open('https://www.linkedin.com/feed/')

brows.geturl()

