#!/usr/bin/python3

import re

def check_postcode(code):
	# Permitted letters depend upon their position in the postcode.
	alpha1 = "[abcdefghijklmnoprstuwyz]"
	alpha2 = "[abcdefghklmnopqrstuvwxy]"
	alpha3 = "[abcdefghjkpmnrstuvwxy]"
	alpha4 = "[abehmnprvwxy]"
	alpha5 = "[abdefghjlnpqrstuwxyz]"
	BFPOa5 = "[abdefghjlnpqrst]"
	BFPOa6 = "[abdefghjlnpqrstuwzyz]"

	# Array holds the regular expressions for the valid postcodes
	patt_list = []

	# BFPO postcode
	patt_list.append(r'^(bf1)(\s*)([0-6]{1}'+BFPOa5+'{1}'+BFPOa6+'{1})$')

	# Expression for postcodes: AN NAA, ANN NAA, AAN NAA, and AANN NAA
	patt_list.append(r'^(' + alpha1 + '{1}' + alpha2 + '?[0-9]{1,2})(\\s*)([0-9]{1}' + alpha5 + '{2})$')

	# Expression for postcodes: ANA NAA
	patt_list.append(r'^(' + alpha1 + '{1}[0-9]{1}' + alpha3 + '{1})(\\s*)([0-9]{1}' + alpha5 + '{2})$')

	# Expression for postcodes: AANA  NAA
	patt_list.append(r'^(' + alpha1 + '{1}' + alpha2 + '{1}' + '?[0-9]{1}' + alpha4 +'{1})(\\s*)([0-9]{1}' + alpha5 + '{2})$')

	# Exception for the special postcode GIR 0AA
	patt_list.append(r'^(GIR)(\s*)(0AA)$')

    # Exception for the DLVA postcodes
	patt_list.append(r'^(SA99)(\s*)(.*)$')

	# Standard BFPO numbers
	patt_list.append(r'^(bfpo)(\s*)([0-9]{1,4})$')

	# c/o BFPO numbers
	patt_list.append(r'^(bfpo)(\s*)(c\/o\s*[0-9]{1,3})$')

	# Overseas Territories
	patt_list.append(r'^([A-Z]{4})(\s*)(1ZZ)$')

	# Anguilla
	patt_list.append(r'^(ai-2640)$')

	valid = False
	post_code = code

	for p in patt_list:
		matches = re.search(p, post_code, re.I)

		if matches:
			# Copy it back into the original string, converting it to uppercase and inserting a space
			# between the inward and outward codes
			if len(matches.groups()) > 1:
				post_code = matches.group(1).upper() + ' ' + matches.group(3).upper()

			# If it is a BFPO c/o type postcode, tidy up the "c/o" part
			if re.search(r'c/o', post_code, re.I):
				post_code = post_code.sub(r'C\/O\s*', "c/o ")

			# If it is the Anguilla overseas territory postcode, we need to treat it specially
			if code.upper() == 'AI-2640':
				post_code = 'AI-2640'

			valid = True

			break

	if valid:
		return post_code

	return False


if __name__ == '__main__':
    print(check_postcode('AI-2640'))
    print(check_postcode('GIR 0AA'))
    print(check_postcode('gir 0qq'))
    print(check_postcode('ASCN 1ZZ'))
    print(check_postcode('BS98 1TL'))
    print(check_postcode('SA99 1BU'))

