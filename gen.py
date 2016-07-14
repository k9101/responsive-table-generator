
column = int(input("Enter the number of table columns: "))

# Enter the table headings
headings = [""] * column
print "Enter the table headings:"
for i in range(column):
    heading = str(raw_input("Heading " + str(i+1) + ": "))
    headings[i] = heading

row = int(input("Enter the number of table rows: "))

table = "<table class='responsive-table'>\n   <thead>\n      <tr>"

for heading in headings:
    table += "\n         <th>" + heading + "</th>"

table += "\n      </tr>\n   </thead>\n   <tbody>"

for i in range(row):
    table += "\n      <tr>"
    for heading in headings:
        table += "\n         <td data-label='%s'></td>" % heading
    table += "      </tr>"

table += "\n   </tbody>\n</table>"

print table
