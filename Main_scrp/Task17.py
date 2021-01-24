from xml.dom import minidom


def main():
    filepath = r'Res/generic.xml'
    xmldoc = minidom.parse(filepath)

    born = xmldoc.createElement("born")
    born.setAttribute("val", "05.04.1909")
    xmldoc.firstChild.appendChild(born)

    xmldoc.getElementsByTagName("lastName")[0].childNodes[0].nodeValue = "Depczyński"

    with open("Res/modified_generic.xml", "w") as fs:
        fs.write(xmldoc.toxml())
        fs.close()


if __name__ == '__main__':
    main()