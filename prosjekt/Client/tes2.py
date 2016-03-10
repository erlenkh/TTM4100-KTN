#tes2

"""
import re



test = {"ost":"ekake"}

print test['ost']

import json

print type(json.dumps(test))


def test(a):

	if a == "ost":
		return

	print "kake"

print test("ost")

"""

import re

inn_tekst = "logout"

#regex = re.compile(r'(.*)\w?(.*)',re.M | re.I)

regex2 = re.compile(r'\S+ ?(\S+)')
regex3 = re.compile(r'\s{1,} ?(.*)')
regex3 = re.compile(r'(\w+)?(\s)?(.*)')

kommando = regex3.search(inn_tekst).group(3)

print kommando == ""

from time import asctime

print type(asctime())