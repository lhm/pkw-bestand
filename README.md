# German passenger car fleet by district, fuel type and emission group

Reference date: 1. January 2019

Source: [fz1_2019_xlsx.xlsx](https://www.kba.de/SharedDocs/Publikationen/DE/Statistik/Fahrzeuge/FZ/2019/fz1_2019_xlsx.xlsx?__blob=publicationFile&v=10)

Publisher [Kraftfahrt-Bundesamt, Flensburg](https://www.kba.de)

## Preparation

```
make data/pkw-bestand-20190101.csv
```

This will download the excel, extract and do some minor cleanup, putting the results in the data directory.

## Notes

The source dataset includes a number of subsets for various categories, such as the number of plug-ins within hybrids, breakdown of emission groups for diesel etc. These are omitted for brevity. If needed, please refer to the source excel table.

## Requirements

Python3 is used, all dependencies are installed automatically into a Virtualenv
when using the `Makefile`.

## License

The Python files in `scripts` are released under an
[CC0 Public Dedication License](https://creativecommons.org/publicdomain/zero/1.0/).

Data is [© Kraftfahrt-Bundesamt, Flensburg](https://www.kba.de) and subject to [their terms of use](https://www.kba.de/EN/Service_en/Hinweise_en/urheberrechtliche_inhalt_en.html?nn=644206):
```
Duplication and dissemination of this publication, even in part or in digitalised form,
is permitted provided the Kraftfahrt-Bundesamt (KBA - Federal Motor Transport Authority)
is acknowledged as source. This also applies if contents of this publication are
disseminated which were not obtained directly.
```
