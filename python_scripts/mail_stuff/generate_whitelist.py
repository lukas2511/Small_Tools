#!/usr/bin/env python2.7

from AddressBook import *
import sys

whitelist_contacts=[]

sys.stdout.write('require ["fileinto"]\n')

sys.stdout.write('\n')

ab = ABAddressBook.sharedAddressBook()
people = ab.people()

for person in people:
    props=person.allProperties()
    if person.valueForProperty_("ABPersonFlags") == 1:
        name = person.valueForProperty_("Organization")
    else:
        name = "%s %s" % (person.valueForProperty_("First"),person.valueForProperty_("Last"))

    emails = person.valueForProperty_("Email")

    if emails:
        for mailIndex in range(0,emails.count()):
            whitelist_contacts.append([name,emails.valueAtIndex_(mailIndex)])

sys.stdout.write('# Mail Whitelist\n')

sys.stdout.write('if not anyof (\n')

for entry in whitelist_contacts:
    sys.stdout.write('    # Mails from ')
    sys.stdout.write(entry[0])
    sys.stdout.write('\n')
    sys.stdout.write('    header :contains "From" "')
    sys.stdout.write(entry[1])
    sys.stdout.write('"\n')

sys.stdout.write('){\n')
sys.stdout.write('    fileinto "Not Important";\n')
sys.stdout.write('    stop;\n')
sys.stdout.write('}\n')
