from datapackage import Package
from utils import root, datadir
from download import source_url

package = Package()
package.infer(str(datadir / '*.csv'))

# add metadata
package.descriptor['name'] = 'pkw-bestand-nach-bezirk'
package.descriptor['title'] = 'FZ1.2 Personenkraftwagen am 1. Januar 2019 nach Zulassungsbezirken, Kraftstoffarten und Emissionsgruppen'
package.descriptor['homepage'] = 'https://www.kba.de/DE/Statistik/Fahrzeuge/Bestand/Umwelt/umwelt_node.html'
package.descriptor['description'] = 'https://www.kba.de/DE/Statistik/Fahrzeuge/fz_methodische_erlaueterungen_201901_pdf.pdf?__blob=publicationFile&v=7'
package.descriptor['contributors'] = [{
    'title': 'Kraftfahrt-Bundesamt, Flensburg',
    'path': 'https://www.kba.de',
    'role': 'publisher'
}]
package.descriptor['sources'] = [{
    'title': 'Kraftfahrt-Bundesamt, Flensburg',
    'path': source_url
}]
package.descriptor['licenses'] = [{
    'name': 'other-at',
    'path': 'https://www.kba.de/EN/Service_en/Hinweise_en/urheberrechtliche_inhalt_en.html?nn=644206'
}]

# fix schema
# the 'KS' field is a key made of numbers and should be treated as string
package.descriptor['resources'][0]['schema']['fields'][0]['type'] = 'string'

package.commit()
package.save(str(root / 'datapackage.json'))
