# -*- coding: utf-8 -*-
import os

import bs4


def write():
    with open("./index.html") as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    div = soup.find("div", {"id": "target"})
    div.clear()
    section = soup.new_tag("section")
    section.string = "start"
    div.append(section)

    count = 0
    with open(os.path.expanduser("~/repos/math-exam/src/expressions.js")) as fp:
        lines = fp.read().splitlines()
        for line in lines[1:-1]:
            if "====================" in line:
                continue
            count += 1
            section = soup.new_tag("section")
            if "$" in line:
                section.string = "({}) {}".format(count, line.strip())
            else:
                section.string = "({}) ${}$".format(count, line.strip())
            div.append(section)

    # save the file again
    with open("./index.html", "w") as outf:
        outf.write(str(soup.prettify()))


def main():
    write()


if __name__ == "__main__":
    main()
