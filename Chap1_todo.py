



#todo 1
from lorem_text import lorem
L = lorem.paragraphs(3)
with open('C:/Users/850/Documents/example1.txt', 'a+') as f:
    f.write(L) 
    
#todo 2
import json


dict_papers = {"paper_1": {"title": "Deep learning", 
                    "authors": {"Yann LeCun": {"affiliations": ["Facebook AI Research, 770 Broadway, New York, New York 10003 USA.", "New York University, 715 Broadway, New York, New York 10003, USA."]}, 
                                "Yoshua Bengio": {"affiliations": ["Department of Computer Science and Operations Research Universite de Montreal, Pavillon Andre-Aisenstadt, PO Box 6128  Centre-Ville STN Montreal, Quebec H3C 3J7, Canada."]},
                                "Geoffrey Hinton": {"affiliations": ["Google, 1600 Amphitheatre Parkway, Mountain View, California 94043, USA.", "Department of Computer Science, University of Toronto"]}}}, 
               "paper_2": {"title": "Deep learning", 
                    "authors": {"Ian J. Goodfellow": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Jean Pouget-Abadie": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Mehdi Mirza": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Bing Xu": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "David Warde-Farley": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Sherjil Ozair": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]},
                                "Aaron Courville": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}, 
                                "Yoshua Bengio": {"affiliations": ["Departement d'informatique et de recherche operationnelle Universite de Montreal"]}}}}    


#todo 3
with open('C:/Users/850/Documents/paper_data.json', 'w') as fp:
    json.dump(dict_papers, fp)



with open('C:/Users/850/Documents/paper_data.json', 'r') as fp:
    loaded = json.load(fp)

print(loaded)


#todo 4
import lxml.etree


xml_file = "C:/Users/850/Documents/data.xml"
root = lxml.etree.parse(xml_file)


date = root.xpath("//note/date/text()")
hour = root.xpath("//note/hour/text()")
to= root.xpath("//note/to/text()")
fromm = root.xpath("//note/from/text()")
body = root.xpath("//note/body/text()")

Dict = {"date" : date,
        "hour" : hour,
        "to" : to,
        "from" : fromm,
        "body" : body}

with open('C:/Users/850/Documents/xml_data.json', 'w') as fp:
    json.dump(Dict, fp)
    
with open('C:/Users/850/Documents/xml_data.json', 'r') as fp:
    to_load= json.load(fp)
print(to_load)