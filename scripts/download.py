import requests
import requests_cache
from utils import root

cache = root / '.cache'
requests_cache.install_cache(str(cache))

url = 'https://www.kba.de/SharedDocs/Publikationen/DE/Statistik/Fahrzeuge/FZ/2019/fz1_2019_xlsx.xlsx?__blob=publicationFile&v=10'
response = requests.get(url)
response.raise_for_status()

with open(root / 'files' / 'fz1_2019_xlsx.xlsx', 'wb') as f:
    f.write(response.content)
