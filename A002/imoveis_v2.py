# %%
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time
# %%
url = 'https://glue-api.vivareal.com/v2/listings?addressCity=Curitiba&addressLocationId=BR%3EParana%3ENULL%3ECuritiba&addressNeighborhood=&addressState=Paran%C3%A1&addressCountry=Brasil&addressStreet=&addressZone=&addressPointLat=-25.437238&addressPointLon=-49.269973&business=SALE&facets=amenities&unitTypes=APARTMENT&unitSubTypes=UnitSubType_NONE%2CDUPLEX%2CLOFT%2CSTUDIO%2CTRIPLEX&unitTypesV3=APARTMENT&usageTypes=RESIDENTIAL&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount)%2Cpage%2CseasonalCampaigns%2CfullUriFragments%2Cnearby(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Cexpansion(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones%2Cphones)%2Cdevelopments(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Cowners(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))&size=300&from={}&q=&developmentsSize=5&__vt=&levels=CITY%2CUNIT_TYPE&ref=&pointRadius=&isPOIQuery='

headerList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "x-domain": "www.vivareal.com.br"
}

payload = ""

# %%
def get_json(url, i, headerList, payload):
    ret = requests.request("GET", url.format(i), data=payload, headers=headerList)
    soup = bs(ret.text, "html.parser")
    return json.loads(soup.text)
# %%
df = pd.DataFrame(
    columns=['descricao',
             'endereco',
             'area',
             'quartos',
             'wc',
             'vagas',
             'valor',
             'condominio',
             'wlink']
)
# %%
imovel_id = 0
json_data = get_json(url, imovel_id, headerList, payload)
# %%
while len(json_data['search']['result']['listings']) > 0:
    qtd = len(json_data['search']['result']['listings'])
    print(f"Qtd imóveis: {qtd} | total {imovel_id}")
    for i in range(0, qtd):
        try:
            descricao = json_data['search']['result']['listings'][i]['listing']['title']
        except:
            descricao = '-'
        try:
            endereco = json_data['search']['result']['listings'][i]['listing']['address']['street'] + ", " + json_data['search']['result']['listings'][i]['listing']['address']['streetNumber']
        except:
            #endereco = json_data['search']['result']['listings'][i]['listing']['address']['street']
            endereco = '-'
        try:
            area = json_data['search']['result']['listings'][i]['listing']['totalAreas'][0]
        except:
            area = '-'
        try:
            quartos = json_data['search']['result']['listings'][i]['listing']['bedrooms'][0]
        except:
            quartos = '-'
        try:
            suites = json_data['search']['result']['listings'][i]['listing']['suites'][0]
        except:
            suites = '-'
        try:
            wc = json_data['search']['result']['listings'][i]['listing']['bathrooms'][0]
        except:
            wc = '-'
        try:
            valor = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['price']
        except:
            valor = '-'
        try:
            vagas = json_data['search']['result']['listings'][i]['listing']['parkingSpaces'][0]
        except:
            vagas = '-'
        try:
            condominio = json_data['search']['result']['listings'][i]['listing']['pricingInfos'][0]['monthlyCondoFee']
        except:
            condominio = '-'
        try:
            wlink = 'https://www.vivareal.com.br' + json_data['search']['result']['listings'][i]['link']['href']
        except:
            wlink = '-'

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink
        ]
        imovel_id = imovel_id + qtd
        if imovel_id > 1000:
            break

        time.sleep(1) # para evitar o erro 429
        json_data = get_json(url, imovel_id, headerList, payload)

# %%
df

# %%
df.to_csv('banco_de_imoveis.csv', sep=';', index=False)
# %%
