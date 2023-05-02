# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->
This project analyzes the radio signal distribution at stations of DB RegioNetz Infrastruktur GmbH and DB Station&Service AG. The aim is to identify the stations where the radio signal reception should be improved in order to offer an enhanced travel experience to passengers of public transport. With possible further available data sets, the radio signal availability on the most important railroad lines can also be analyzed and thus, in times of mobile work, weak points in the network availability in connection with railroad lines can be uncovered.

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
The analysis helps to identify weak points in network availability and thus facilitate travel by public transport

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: List of stations to be operated by DB Station&Service AG
* Metadata URL: https://mobilithek.info/offers/573361342675562496
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

Stations DB S+S List of stations to be operated by DB Station&Service AG

### Datasource2: List of stations to be operated by DB RegioNetz Infrastruktur GmbH
* Metadata URL: https://mobilithek.info/offers/573361314154344448
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

Stations RNI List of stations to be operated by DB RegioNetz Infrastruktur GmbH.

### Datasource3: Mobile radio signal strength & signal quality for GSM, UMTS and LTE
* Metadata URL: https://mobilithek.info/offers/577101012068614144
* Data URL: https://raw.githubusercontent.com/od-ms/radverkehr-zaehlstellen/main/100035541/2019-01.csv
* Data Type: CSV

The data set provides signal strength and signal quality for mobile communications connections of the most widespread mobile network operators in Germany by means of various parameters. Data is provided for the mobile communications technologies GSM, UMTS and LTE.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Batch Data and data Ingestion [#1][i1]
2. Data Cleansing & Transformation [#2] [i2]
3. Automation of Testing [#3][i3]
4. Data Analysis [#4][i4]
5. Data Interpretation [#5][i5]
6. Project Publication [#6][i6]

[i1]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/1
[i2]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/2
[i3]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/3
[i4]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/4
[i5]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/5
[i6]: https://github.com/Magnus-schn/2023-amse-template_magnus/issues/6
