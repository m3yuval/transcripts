# S&P 500 companies and their official GitHub organizations

Built 2026-09-28 as Step 1 of the "Green isn't proof" research: which big US public companies run
public GitHub organizations. **184 of the 500 S&P 500 companies** have at least one confirmed official
GitHub org (**441 orgs** in total); **172 of them are headquartered in the US**. 53 more have a lead
that could not be confirmed, and 263 have no public GitHub org that could be found.

## How it was built

- **Universe:** the 500 S&P 500 constituents (Wikipedia list, share classes merged), with GICS sector
  and headquarters. 24 index members are headquartered outside the US (Ireland, UK, Switzerland,
  Bermuda, Netherlands, Canada); they are kept but flagged `us_hq = False`.
- **Search:** 50 agents (10 companies each), then a second pass of 33 agents on every company without
  a confirmed org (the first pass had run out of web searches), plus 2 agents re-sourcing weak evidence.
- **Evidence rule:** every org must be named on a **non-GitHub page** the company controls or that is
  authoritative: the company's own site, docs or engineering blog, Wikidata (P2037), Wikipedia, or an
  official package the company publishes on npm / PyPI / Maven Central / NuGet / CocoaPods whose
  repository link points to the org. GitHub itself was not queried from this session (its GitHub
  access is limited to the transcripts repo).
- **Verification:** every evidence page was re-fetched by script and checked to contain
  `github.com/<handle>` (`verify_evidence.py`; registry JSON APIs used for npm/PyPI/Maven). 440 of 441
  orgs passed; 1 was checked by hand. Orgs whose evidence could not be re-fetched were moved to
  "uncertain".

## Files

| file | what |
|---|---|
| `sp500-github-orgs.csv` | one row per confirmed org: company, ticker, sector, HQ, US flag, handle, primary, relation (company / subsidiary / product brand / open-source program / research lab), evidence URL, quote |
| `sp500-all-companies-status.csv` | all 500 companies with status (found / uncertain / none_found) and notes |
| `sp500-github-raw.json` | full agent output, including what was checked for every company |
| `github_side_check.py` | **run on your own machine** with `GITHUB_TOKEN`: confirms each org on GitHub (verified-domain badge, website, repo count) and lists every public, non-fork repo |
| `verify_evidence.py` | the evidence re-check script |

Next step on your machine:

    export GITHUB_TOKEN=...
    python3 github_side_check.py sp500-github-orgs.csv out_orgs.csv out_repos.csv

## Caveats

- **"Found" means the company publicly claims the org**, not that the org holds production services.
  Many are SDK, sample or open-source-project orgs. Repo-level filtering is Step 2.
- **"None found" is not proof of absence.** Several company sites block automated access; a company
  may run an org it never links from a public page. `sp500-all-companies-status.csv` lists what was
  checked.
- Orgs of acquired subsidiaries are included with `relation = subsidiary` (e.g. Habana for Intel,
  Flipkart incubator for Walmart); check before attributing their repos to the parent.

## Confirmed companies (184)

| company | ticker | sector | note | GitHub orgs |
|---|---|---|---|---|
| 3M | MMM | Industrials |  | [3mcloud](https://github.com/3mcloud) *(primary)* |
| AbbVie | ABBV | Health Care |  | [abbvie-external](https://github.com/abbvie-external) *(primary)*, [AbbVie-ComputationalGenomics](https://github.com/AbbVie-ComputationalGenomics) |
| Adobe Inc. | ADBE | Information Technology |  | [adobe](https://github.com/adobe) *(primary)*, [AdobeDocs](https://github.com/AdobeDocs), [magento](https://github.com/magento), [adobe-fonts](https://github.com/adobe-fonts), [adobe-research](https://github.com/adobe-research), [adobe-type-tools](https://github.com/adobe-type-tools), [Frameio](https://github.com/Frameio) |
| Advanced Micro Devices | AMD | Information Technology |  | [amd](https://github.com/amd) *(primary)*, [ROCm](https://github.com/ROCm), [GPUOpen-LibrariesAndSDKs](https://github.com/GPUOpen-LibrariesAndSDKs), [GPUOpen-Tools](https://github.com/GPUOpen-Tools), [GPUOpen-Drivers](https://github.com/GPUOpen-Drivers), [GPUOpen-Effects](https://github.com/GPUOpen-Effects), [Xilinx](https://github.com/Xilinx) |
| Agilent Technologies | A | Health Care |  | [Agilent](https://github.com/Agilent) *(primary)* |
| Airbnb | ABNB | Consumer Discretionary |  | [airbnb](https://github.com/airbnb) *(primary)* |
| Akamai Technologies | AKAM | Information Technology |  | [akamai](https://github.com/akamai) *(primary)*, [linode](https://github.com/linode), [akamai-developers](https://github.com/akamai-developers) |
| Alphabet Inc. (Class A) | GOOGL | Communication Services |  | [google](https://github.com/google) *(primary)*, [GoogleCloudPlatform](https://github.com/GoogleCloudPlatform), [google-research](https://github.com/google-research), [google-deepmind](https://github.com/google-deepmind), [tensorflow](https://github.com/tensorflow), [googleapis](https://github.com/googleapis), [android](https://github.com/android), [flutter](https://github.com/flutter), [golang](https://github.com/golang), [firebase](https://github.com/firebase) |
| Amazon | AMZN | Consumer Discretionary |  | [amzn](https://github.com/amzn) *(primary)*, [aws](https://github.com/aws), [awslabs](https://github.com/awslabs), [amazon-science](https://github.com/amazon-science), [aws-amplify](https://github.com/aws-amplify), [aws-powertools](https://github.com/aws-powertools), [smithy-lang](https://github.com/smithy-lang), [awsdocs](https://github.com/awsdocs), [twitchdev](https://github.com/twitchdev), [AmazonAppDev](https://github.com/AmazonAppDev) |
| American Express | AXP | Financials |  | [americanexpress](https://github.com/americanexpress) *(primary)* |
| Ametek | AME | Industrials |  | [CrankSoftware](https://github.com/CrankSoftware) |
| Amgen | AMGN | Health Care |  | [DecodeGenetics](https://github.com/DecodeGenetics) |
| Analog Devices | ADI | Information Technology |  | [analogdevicesinc](https://github.com/analogdevicesinc) *(primary)*, [analogdevicesinc](https://github.com/analogdevicesinc) |
| Apple Inc. | AAPL | Information Technology |  | [apple](https://github.com/apple) *(primary)*, [apple-oss-distributions](https://github.com/apple-oss-distributions), [swiftlang](https://github.com/swiftlang), [ml-explore](https://github.com/ml-explore), [webkit](https://github.com/webkit) |
| AppLovin | APP | Communication Services |  | [AppLovin](https://github.com/AppLovin) *(primary)* |
| Arista Networks | ANET | Information Technology |  | [aristanetworks](https://github.com/aristanetworks) *(primary)*, [arista-eosplus](https://github.com/arista-eosplus), [awakesecurity](https://github.com/awakesecurity) |
| AT&T | T | Communication Services |  | [att](https://github.com/att) *(primary)*, [attm2x](https://github.com/attm2x) |
| Autodesk | ADSK | Information Technology |  | [Autodesk](https://github.com/Autodesk) *(primary)*, [autodesk-platform-services](https://github.com/autodesk-platform-services), [Autodesk-Forge](https://github.com/Autodesk-Forge), [shotgunsoftware](https://github.com/shotgunsoftware) |
| Automatic Data Processing | ADP | Industrials |  | [adplabs](https://github.com/adplabs) *(primary)* |
| Best Buy | BBY | Consumer Discretionary |  | [BestBuyAPIs](https://github.com/BestBuyAPIs) *(primary)* |
| Biogen | BIIB | Health Care |  | [Biogen-Inc](https://github.com/Biogen-Inc) *(primary)* |
| BlackRock | BLK | Financials |  | [blackrock](https://github.com/blackrock) *(primary)* |
| Block, Inc. | XYZ | Financials |  | [block](https://github.com/block) *(primary)*, [square](https://github.com/square), [cashapp](https://github.com/cashapp), [afterpay](https://github.com/afterpay), [Square-Developers](https://github.com/Square-Developers), [tidal-music](https://github.com/tidal-music), [weebly](https://github.com/weebly), [proto-at-block](https://github.com/proto-at-block), [cequals](https://github.com/cequals) |
| BNY Mellon | BNY | Financials |  | [BNYMellon](https://github.com/BNYMellon) *(primary)* |
| Booking Holdings | BKNG | Consumer Discretionary |  | [bookingcom](https://github.com/bookingcom) *(primary)*, [opentable](https://github.com/opentable), [priceline](https://github.com/priceline), [agoda-com](https://github.com/agoda-com) |
| Boston Scientific | BSX | Health Care |  | [bos-sci](https://github.com/bos-sci) *(primary)* |
| Broadcom | AVGO | Information Technology |  | [vmware](https://github.com/vmware) *(primary)*, [vmware-tanzu](https://github.com/vmware-tanzu), [spring-projects](https://github.com/spring-projects), [spring-cloud](https://github.com/spring-cloud), [bitnami](https://github.com/bitnami), [rabbitmq](https://github.com/rabbitmq), [saltstack](https://github.com/saltstack), [carbonblack](https://github.com/carbonblack), [BroadcomMFD](https://github.com/BroadcomMFD), [CAAPIM](https://github.com/CAAPIM) |
| Broadridge Financial Solutions | BR | Industrials |  | [Ullink](https://github.com/Ullink) |
| C.H. Robinson | CHRW | Industrials |  | [ch-robinson](https://github.com/ch-robinson) *(primary)* |
| Cadence Design Systems | CDNS | Information Technology |  | [pointwise](https://github.com/pointwise) |
| Capital One | COF | Financials |  | [capitalone](https://github.com/capitalone) *(primary)*, [Hygieia](https://github.com/Hygieia) |
| Caterpillar Inc. | CAT | Industrials |  | [caterpillar-inc](https://github.com/caterpillar-inc) *(primary)* |
| CBRE Group | CBRE | Real Estate |  | [cbre](https://github.com/cbre) *(primary)*, [floored](https://github.com/floored) |
| Ciena | CIEN | Information Technology |  | [ciena-blueplanet](https://github.com/ciena-blueplanet) *(primary)*, [ciena-frost](https://github.com/ciena-frost) |
| Cigna | CI | Health Care |  | [Evernorth](https://github.com/Evernorth) *(primary)* |
| Cisco | CSCO | Information Technology |  | [cisco](https://github.com/cisco) *(primary)*, [CiscoDevNet](https://github.com/CiscoDevNet), [cisco-open](https://github.com/cisco-open), [cisco-developer](https://github.com/cisco-developer), [CiscoTestAutomation](https://github.com/CiscoTestAutomation), [Cisco-Talos](https://github.com/Cisco-Talos), [splunk](https://github.com/splunk), [duosecurity](https://github.com/duosecurity) |
| CME Group | CME | Financials |  | [CMEGroupPublic](https://github.com/CMEGroupPublic) *(primary)* |
| Coca-Cola Company (The) | KO | Consumer Staples |  | [The-Coca-Cola-Company](https://github.com/The-Coca-Cola-Company) *(primary)* |
| Cognizant | CTSH | Information Technology |  | [cognizant-ai-lab](https://github.com/cognizant-ai-lab) *(primary)*, [leaf-ai](https://github.com/leaf-ai) |
| Coinbase | COIN | Financials |  | [coinbase](https://github.com/coinbase) *(primary)*, [base](https://github.com/base), [base-org](https://github.com/base-org) |
| Comcast | CMCSA | Communication Services |  | [Comcast](https://github.com/Comcast) *(primary)*, [sky-uk](https://github.com/sky-uk), [lightning-js](https://github.com/lightning-js) |
| Copart | CPRT | Industrials |  | [copartit](https://github.com/copartit) *(primary)* |
| Corteva | CTVA | Materials |  | [corteva](https://github.com/corteva) *(primary)* |
| CoStar Group | CSGP | Real Estate |  | [matterport](https://github.com/matterport) |
| Costco | COST | Consumer Staples |  | [nxt-costco-com](https://github.com/nxt-costco-com) *(primary)* |
| CrowdStrike | CRWD | Information Technology |  | [CrowdStrike](https://github.com/CrowdStrike) *(primary)*, [humio](https://github.com/humio), [pangeacyber](https://github.com/pangeacyber) |
| CVS Health | CVS | Health Care |  | [cvs-health](https://github.com/cvs-health) *(primary)* |
| Datadog | DDOG | Information Technology |  | [DataDog](https://github.com/DataDog) *(primary)*, [vectordotdev](https://github.com/vectordotdev), [quickwit-oss](https://github.com/quickwit-oss) |
| Deere & Company | DE | Industrials |  | [JohnDeere](https://github.com/JohnDeere) *(primary)* |
| Dell Technologies | DELL | Information Technology |  | [dell](https://github.com/dell) *(primary)*, [dell](https://github.com/dell) |
| DoorDash | DASH | Consumer Discretionary |  | [doordash](https://github.com/doordash) *(primary)* |
| eBay Inc. | EBAY | Consumer Discretionary |  | [eBay](https://github.com/eBay) *(primary)* |
| EchoStar | ECHO | Communication Services |  | [DISHDevEx](https://github.com/DISHDevEx) |
| Elevance Health | ELV | Health Care |  | [openanthem](https://github.com/openanthem) *(primary)*, [anthem-projects](https://github.com/anthem-projects) |
| Emerson Electric | EMR | Industrials |  | [ni](https://github.com/ni), [emerson-eps](https://github.com/emerson-eps) |
| Equifax | EFX | Industrials |  | [Kount](https://github.com/Kount) |
| Equinix | EQIX | Real Estate |  | [equinix](https://github.com/equinix) *(primary)*, [equinix-labs](https://github.com/equinix-labs), [packethost](https://github.com/packethost) |
| Everpure | P | Information Technology |  | [PureStorage-OpenConnect](https://github.com/PureStorage-OpenConnect) *(primary)*, [purestorage](https://github.com/purestorage), [PureStorage-Connect](https://github.com/PureStorage-Connect), [Everpure-Ansible](https://github.com/Everpure-Ansible) |
| Expedia Group | EXPE | Consumer Discretionary |  | [ExpediaGroup](https://github.com/ExpediaGroup) *(primary)*, [HotelsDotCom](https://github.com/HotelsDotCom), [ExpediaDotCom](https://github.com/ExpediaDotCom), [trivago](https://github.com/trivago) |
| F5, Inc. | FFIV | Information Technology |  | [F5Networks](https://github.com/F5Networks) *(primary)*, [nginx](https://github.com/nginx), [f5devcentral](https://github.com/f5devcentral), [nginxinc](https://github.com/nginxinc), [shapesecurity](https://github.com/shapesecurity) |
| FactSet | FDS | Financials |  | [factset](https://github.com/factset) *(primary)* |
| Fair Isaac | FICO | Information Technology |  | [fico-xpress](https://github.com/fico-xpress) |
| FedEx | FDX | Industrials |  | [ShopRunner](https://github.com/ShopRunner) |
| Ferguson Enterprises | FERG | Industrials |  | [FergusonUX](https://github.com/FergusonUX) |
| Fifth Third Bancorp | FITB | Financials |  | [newline53](https://github.com/newline53) |
| Fiserv | FISV | Financials |  | [Fiserv](https://github.com/Fiserv) *(primary)*, [clover](https://github.com/clover) |
| Ford Motor Company | F | Consumer Discretionary |  | [Ford](https://github.com/Ford) *(primary)*, [openxc](https://github.com/openxc) |
| Fortinet | FTNT | Information Technology |  | [fortinet](https://github.com/fortinet) *(primary)*, [fortinetdev](https://github.com/fortinetdev), [fortinet-ansible-dev](https://github.com/fortinet-ansible-dev), [fortinet-solutions-cse](https://github.com/fortinet-solutions-cse) |
| Fortive | FTV | Industrials |  | [Accruent](https://github.com/Accruent), [servicechannel](https://github.com/servicechannel) |
| Fox Corporation (Class A) | FOXA | Communication Services |  | [foxcorp](https://github.com/foxcorp) *(primary)*, [Tubitv](https://github.com/Tubitv) |
| GE Aerospace | GE | Industrials |  | [ge-high-assurance](https://github.com/ge-high-assurance), [ge-flight-analytics](https://github.com/ge-flight-analytics), [ge-semtk](https://github.com/ge-semtk) |
| GE Vernova | GEV | Industrials |  | [alteia-ai](https://github.com/alteia-ai) |
| Gen Digital | GEN | Information Technology |  | [gendigitalinc](https://github.com/gendigitalinc) *(primary)*, [avast](https://github.com/avast) |
| Generac | GNRC | Industrials |  | [neurio](https://github.com/neurio) *(primary)* |
| General Motors | GM | Consumer Discretionary |  | [cruise-automation](https://github.com/cruise-automation) |
| Global Payments | GPN | Financials |  | [globalpayments](https://github.com/globalpayments) *(primary)*, [Worldpay](https://github.com/Worldpay), [hps](https://github.com/hps), [heartlandpayments](https://github.com/heartlandpayments) |
| GoDaddy | GDDY | Information Technology |  | [godaddy](https://github.com/godaddy) *(primary)*, [godaddy-wordpress](https://github.com/godaddy-wordpress), [poynt](https://github.com/poynt) |
| Goldman Sachs | GS | Financials |  | [goldmansachs](https://github.com/goldmansachs) *(primary)* |
| Hewlett Packard Enterprise | HPE | Information Technology |  | [HewlettPackard](https://github.com/HewlettPackard) *(primary)*, [Juniper](https://github.com/Juniper), [aruba](https://github.com/aruba), [determined-ai](https://github.com/determined-ai), [CrayLabs](https://github.com/CrayLabs), [grommet](https://github.com/grommet), [DragonHPC](https://github.com/DragonHPC), [bluek8s](https://github.com/bluek8s), [hpe-dev-incubator](https://github.com/hpe-dev-incubator) |
| Home Depot (The) | HD | Consumer Discretionary |  | [homedepot](https://github.com/homedepot) *(primary)* |
| Honeywell Technologies | HON | Industrials |  | [quantinuum](https://github.com/quantinuum), [CQCL](https://github.com/CQCL) |
| HP Inc. | HPQ | Information Technology |  | [HPInc](https://github.com/HPInc) *(primary)* |
| Huntington Ingalls Industries | HII | Industrials |  | [hii-mdis](https://github.com/hii-mdis) |
| IBM | IBM | Information Technology |  | [IBM](https://github.com/IBM) *(primary)*, [Qiskit](https://github.com/Qiskit), [IBM-Cloud](https://github.com/IBM-Cloud), [carbon-design-system](https://github.com/carbon-design-system), [watson-developer-cloud](https://github.com/watson-developer-cloud), [instana](https://github.com/instana), [DS4SD](https://github.com/DS4SD), [ibm-granite-community](https://github.com/ibm-granite-community), [RedHatOfficial](https://github.com/RedHatOfficial), [hashicorp](https://github.com/hashicorp) |
| Illumina, Inc. | ILMN | Health Care |  | [Illumina](https://github.com/Illumina) *(primary)* |
| Intel | INTC | Information Technology |  | [intel](https://github.com/intel) *(primary)*, [IntelLabs](https://github.com/IntelLabs), [openvinotoolkit](https://github.com/openvinotoolkit), [IntelPython](https://github.com/IntelPython), [HabanaAI](https://github.com/HabanaAI), [NervanaSystems](https://github.com/NervanaSystems) |
| Intercontinental Exchange | ICE | Financials |  | [intercontinentalexchange](https://github.com/intercontinentalexchange) *(primary)*, [ICEMortgageTechnology](https://github.com/ICEMortgageTechnology), [intcx](https://github.com/intcx) |
| Intuit | INTU | Information Technology |  | [intuit](https://github.com/intuit) *(primary)*, [numaproj](https://github.com/numaproj), [mailchimp](https://github.com/mailchimp), [creditkarma](https://github.com/creditkarma) |
| Jack Henry & Associates | JKHY | Financials |  | [Banno](https://github.com/Banno) *(primary)* |
| Jacobs Solutions | J | Industrials |  | [People-Places-Solutions](https://github.com/People-Places-Solutions) |
| Johnson & Johnson | JNJ | Health Care |  | [johnsonandjohnson](https://github.com/johnsonandjohnson) *(primary)*, [csats](https://github.com/csats) |
| JPMorgan Chase | JPM | Financials |  | [jpmorganchase](https://github.com/jpmorganchase) *(primary)*, [jpmorgan-payments](https://github.com/jpmorgan-payments) |
| Keysight Technologies | KEYS | Information Technology |  | [OpenIxia](https://github.com/OpenIxia), [open-traffic-generator](https://github.com/open-traffic-generator), [opentap](https://github.com/opentap) |
| Kroger | KR | Consumer Staples |  | [krogerco](https://github.com/krogerco) *(primary)* |
| Lilly (Eli) | LLY | Health Care |  | [EliLillyCo](https://github.com/EliLillyCo) *(primary)* |
| Live Nation Entertainment | LYV | Communication Services |  | [ticketmaster](https://github.com/ticketmaster) *(primary)*, [twotoasters](https://github.com/twotoasters) |
| Lockheed Martin | LMT | Industrials |  | [lmco](https://github.com/lmco) *(primary)* |
| Marvell Technology | MRVL | Information Technology |  | [MarvellEmbeddedProcessors](https://github.com/MarvellEmbeddedProcessors) *(primary)*, [kinoma](https://github.com/kinoma) |
| Mastercard | MA | Financials |  | [Mastercard](https://github.com/Mastercard) *(primary)*, [Mastercard-Gateway](https://github.com/Mastercard-Gateway), [recordedfuture](https://github.com/recordedfuture) |
| McDonald's | MCD | Consumer Discretionary |  | [mcdcorp](https://github.com/mcdcorp) *(primary)* |
| McKesson Corporation | MCK | Health Care |  | [covermymeds](https://github.com/covermymeds) |
| Merck & Co. | MRK | Health Care |  | [Merck](https://github.com/Merck) *(primary)*, [MSDLLCpapers](https://github.com/MSDLLCpapers) |
| Meta Platforms | META | Communication Services |  | [facebook](https://github.com/facebook) *(primary)*, [facebookresearch](https://github.com/facebookresearch), [facebookincubator](https://github.com/facebookincubator), [meta-llama](https://github.com/meta-llama), [meta-pytorch](https://github.com/meta-pytorch), [facebookarchive](https://github.com/facebookarchive), [oculus-samples](https://github.com/oculus-samples), [Instagram](https://github.com/Instagram), [WhatsApp](https://github.com/WhatsApp), [OculusVR](https://github.com/OculusVR), [meta-models](https://github.com/meta-models) |
| Microchip Technology | MCHP | Information Technology |  | [MicrochipTech](https://github.com/MicrochipTech) *(primary)*, [microchip-pic-avr-tools](https://github.com/microchip-pic-avr-tools) |
| Micron Technology | MU | Information Technology |  | [FWDNXT](https://github.com/FWDNXT) |
| Microsoft | MSFT | Information Technology |  | [microsoft](https://github.com/microsoft) *(primary)*, [Azure](https://github.com/Azure), [dotnet](https://github.com/dotnet), [MicrosoftDocs](https://github.com/MicrosoftDocs), [Azure-Samples](https://github.com/Azure-Samples), [microsoftgraph](https://github.com/microsoftgraph), [PowerShell](https://github.com/PowerShell), [OfficeDev](https://github.com/OfficeDev), [github](https://github.com/github), [linkedin](https://github.com/linkedin), [citusdata](https://github.com/citusdata) |
| Monolithic Power Systems | MPWR | Information Technology |  | [monolithicpower](https://github.com/monolithicpower) *(primary)* |
| Moody's Corporation | MCO | Financials |  | [RMS](https://github.com/RMS) |
| Morgan Stanley | MS | Financials |  | [morganstanley](https://github.com/morganstanley) *(primary)* |
| Motorola Solutions | MSI | Information Technology |  | [pelcointegrations](https://github.com/pelcointegrations) |
| Nasdaq, Inc. | NDAQ | Financials |  | [Nasdaq](https://github.com/Nasdaq) *(primary)*, [quandl](https://github.com/quandl) |
| NetApp | NTAP | Information Technology |  | [NetApp](https://github.com/NetApp) *(primary)*, [NetAppDocs](https://github.com/NetAppDocs), [instaclustr](https://github.com/instaclustr) |
| Netflix | NFLX | Communication Services |  | [Netflix](https://github.com/Netflix) *(primary)*, [Netflix-Skunkworks](https://github.com/Netflix-Skunkworks) |
| News Corp (Class A) | NWSA | Communication Services |  | [dowjones](https://github.com/dowjones), [newscorp-ghfb](https://github.com/newscorp-ghfb) |
| Nike, Inc. | NKE | Consumer Discretionary |  | [Nike-Inc](https://github.com/Nike-Inc) *(primary)* |
| NRG Energy | NRG | Utilities |  | [vivint](https://github.com/vivint), [vivint-smarthome](https://github.com/vivint-smarthome) |
| Nvidia | NVDA | Information Technology |  | [NVIDIA](https://github.com/NVIDIA) *(primary)*, [NVlabs](https://github.com/NVlabs), [rapidsai](https://github.com/rapidsai), [NVIDIA-Omniverse](https://github.com/NVIDIA-Omniverse), [NVIDIAGameWorks](https://github.com/NVIDIAGameWorks), [NVIDIA-NeMo](https://github.com/NVIDIA-NeMo), [triton-inference-server](https://github.com/triton-inference-server), [NVIDIA-AI-IOT](https://github.com/NVIDIA-AI-IOT), [isaac-sim](https://github.com/isaac-sim), [NVIDIA-ISAAC-ROS](https://github.com/NVIDIA-ISAAC-ROS), [NVIDIA-Merlin](https://github.com/NVIDIA-Merlin) |
| Omnicom Group | OMC | Communication Services |  | [Acxiom](https://github.com/Acxiom) |
| ON Semiconductor | ON | Information Technology |  | [ONSemiconductor](https://github.com/ONSemiconductor) *(primary)* |
| Oracle Corporation | ORCL | Information Technology |  | [oracle](https://github.com/oracle) *(primary)*, [mysql](https://github.com/mysql), [oracle-devrel](https://github.com/oracle-devrel), [oracle-quickstart](https://github.com/oracle-quickstart), [oracle-terraform-modules](https://github.com/oracle-terraform-modules), [graalvm](https://github.com/graalvm), [helidon-io](https://github.com/helidon-io), [cerner](https://github.com/cerner) |
| Otis Worldwide | OTIS | Industrials |  | [OtisElevatorCompany](https://github.com/OtisElevatorCompany) *(primary)* |
| Palantir Technologies | PLTR | Information Technology |  | [palantir](https://github.com/palantir) *(primary)* |
| Palo Alto Networks | PANW | Information Technology |  | [PaloAltoNetworks](https://github.com/PaloAltoNetworks) *(primary)*, [demisto](https://github.com/demisto), [pan-unit42](https://github.com/pan-unit42), [bridgecrewio](https://github.com/bridgecrewio), [cyberark](https://github.com/cyberark), [chronosphereio](https://github.com/chronosphereio), [protectai](https://github.com/protectai) |
| Paramount Skydance Corporation | PSKY | Communication Services |  | [Pluto-tv](https://github.com/Pluto-tv) |
| Paychex | PAYX | Industrials |  | [paychex](https://github.com/paychex) *(primary)* |
| PayPal | PYPL | Financials |  | [paypal](https://github.com/paypal) *(primary)*, [braintree](https://github.com/braintree), [venmo](https://github.com/venmo), [krakenjs](https://github.com/krakenjs), [hyperwallet](https://github.com/hyperwallet) |
| PepsiCo | PEP | Consumer Staples |  | [pepsico-ecommerce](https://github.com/pepsico-ecommerce) |
| Pfizer | PFE | Health Care |  | [pfizer-opensource](https://github.com/pfizer-opensource) *(primary)* |
| Philip Morris International | PM | Consumer Staples |  | [philipmorrisintl](https://github.com/philipmorrisintl) *(primary)* |
| Principal Financial Group | PFG | Financials |  | [principalfinancialgroup-emu](https://github.com/principalfinancialgroup-emu) *(primary)*, [principalinformationservices-emu](https://github.com/principalinformationservices-emu) |
| PTC Inc. | PTC | Information Technology |  | [onshape-public](https://github.com/onshape-public), [onshape](https://github.com/onshape) |
| Qualcomm | QCOM | Information Technology |  | [qualcomm](https://github.com/qualcomm) *(primary)*, [quic](https://github.com/quic), [arduino](https://github.com/arduino), [edgeimpulse](https://github.com/edgeimpulse) |
| Reddit | RDDT | Communication Services |  | [reddit](https://github.com/reddit) *(primary)* |
| Regeneron Pharmaceuticals | REGN | Health Care |  | [rgcgithub](https://github.com/rgcgithub) *(primary)* |
| Republic Services | RSG | Industrials |  | [RepublicServicesRepository](https://github.com/RepublicServicesRepository) *(primary)* |
| Revvity | RVTY | Health Care |  | [Revvity](https://github.com/Revvity) *(primary)* |
| Robinhood Markets | HOOD | Financials |  | [robinhood](https://github.com/robinhood) *(primary)* |
| Rockwell Automation | ROK | Industrials |  | [FactoryTalk-Optix](https://github.com/FactoryTalk-Optix) *(primary)*, [clearpathrobotics](https://github.com/clearpathrobotics) |
| Roper Technologies | ROP | Information Technology |  | [TheFoundryVisionmongers](https://github.com/TheFoundryVisionmongers), [replicon](https://github.com/replicon), [dltkengineering](https://github.com/dltkengineering) |
| RTX Corporation | RTX | Industrials |  | [raytheonbbn](https://github.com/raytheonbbn) |
| S&P Global | SPGI | Financials |  | [kensho-technologies](https://github.com/kensho-technologies), [spgi-ci](https://github.com/spgi-ci) |
| Salesforce | CRM | Information Technology |  | [salesforce](https://github.com/salesforce) *(primary)*, [forcedotcom](https://github.com/forcedotcom), [salesforcecli](https://github.com/salesforcecli), [slackapi](https://github.com/slackapi), [heroku](https://github.com/heroku), [tableau](https://github.com/tableau), [SFDO-Tooling](https://github.com/SFDO-Tooling) |
| Schlumberger | SLB | Energy |  | [Schlumberger](https://github.com/Schlumberger) *(primary)* |
| ServiceNow | NOW | Information Technology |  | [ServiceNow](https://github.com/ServiceNow) *(primary)*, [ServiceNowDevProgram](https://github.com/ServiceNowDevProgram), [ServiceNowNextExperience](https://github.com/ServiceNowNextExperience), [lightstep](https://github.com/lightstep) |
| Synopsys | SNPS | Information Technology |  | [ansys](https://github.com/ansys), [AnalyticalGraphicsInc](https://github.com/AnalyticalGraphicsInc) |
| Sysco | SYY | Consumer Staples |  | [syscolabs](https://github.com/syscolabs) *(primary)* |
| T-Mobile US | TMUS | Communication Services |  | [tmobile](https://github.com/tmobile) *(primary)* |
| Take-Two Interactive | TTWO | Communication Services |  | [zynga](https://github.com/zynga) |
| Target Corporation | TGT | Consumer Staples |  | [target](https://github.com/target) *(primary)* |
| Teledyne Technologies | TDY | Information Technology |  | [Photometrics](https://github.com/Photometrics) |
| Teradyne | TER | Information Technology |  | [UniversalRobots](https://github.com/UniversalRobots) |
| Tesla, Inc. | TSLA | Consumer Discretionary |  | [teslamotors](https://github.com/teslamotors) *(primary)* |
| Texas Instruments | TXN | Information Technology |  | [TexasInstruments](https://github.com/TexasInstruments) *(primary)* |
| Thermo Fisher Scientific | TMO | Health Care |  | [Olink-Proteomics](https://github.com/Olink-Proteomics) |
| Travelers Companies (The) | TRV | Financials |  | [simplybusiness](https://github.com/simplybusiness) |
| Trimble Inc. | TRMB | Information Technology |  | [trimble-oss](https://github.com/trimble-oss) *(primary)*, [SketchUp](https://github.com/SketchUp) |
| Tyler Technologies | TYL | Information Technology |  | [tyler-technologies-oss](https://github.com/tyler-technologies-oss) *(primary)*, [socrata](https://github.com/socrata) |
| Uber | UBER | Industrials |  | [uber](https://github.com/uber) *(primary)*, [uber-go](https://github.com/uber-go), [uber-research](https://github.com/uber-research), [uber-common](https://github.com/uber-common), [uber-archive](https://github.com/uber-archive) |
| UnitedHealth Group | UNH | Health Care |  | [Optum](https://github.com/Optum) *(primary)*, [rallyhealth](https://github.com/rallyhealth) |
| Veeva Systems | VEEV | Health Care |  | [veeva](https://github.com/veeva) *(primary)* |
| Veralto | VLTO | Industrials |  | [AquaticInformatics](https://github.com/AquaticInformatics), [Sea-BirdScientific](https://github.com/Sea-BirdScientific) |
| Verisign | VRSN | Information Technology |  | [verisign](https://github.com/verisign) *(primary)* |
| Verizon | VZ | Communication Services |  | [Verizon](https://github.com/Verizon) *(primary)* |
| Visa Inc. | V | Financials |  | [visa](https://github.com/visa) *(primary)*, [cybersource](https://github.com/cybersource), [AuthorizeNet](https://github.com/AuthorizeNet) |
| W. W. Grainger | GWW | Industrials |  | [monotaro](https://github.com/monotaro) |
| Walmart | WMT | Consumer Staples |  | [walmartlabs](https://github.com/walmartlabs) *(primary)*, [electrode-io](https://github.com/electrode-io), [oneops](https://github.com/oneops), [flipkart-incubator](https://github.com/flipkart-incubator) |
| Walt Disney Company (The) | DIS | Communication Services |  | [disneystreaming](https://github.com/disneystreaming), [PixarAnimationStudios](https://github.com/PixarAnimationStudios), [wdas](https://github.com/wdas), [hulu](https://github.com/hulu), [munki](https://github.com/munki) |
| Warner Bros. Discovery | WBD | Communication Services |  | [wbd-open-source](https://github.com/wbd-open-source) *(primary)*, [HBOCodeLabs](https://github.com/HBOCodeLabs), [bleacherreport](https://github.com/bleacherreport), [cnnlabs](https://github.com/cnnlabs), [EurosportDigital](https://github.com/EurosportDigital), [turnerlabs](https://github.com/turnerlabs) |
| Western Digital | WDC | Information Technology |  | [westerndigitalcorporation](https://github.com/westerndigitalcorporation) *(primary)* |
| Workday, Inc. | WDAY | Information Technology |  | [Workday](https://github.com/Workday) *(primary)*, [FlowiseAI](https://github.com/FlowiseAI), [PipedreamHQ](https://github.com/PipedreamHQ) |
| Zebra Technologies | ZBRA | Information Technology |  | [ZebraDevs](https://github.com/ZebraDevs) *(primary)*, [Zebra](https://github.com/Zebra), [developer-zebra](https://github.com/developer-zebra), [Zebra-Techdocs](https://github.com/Zebra-Techdocs), [zebratechnologies](https://github.com/zebratechnologies) |
| Zoetis | ZTS | Health Care |  | [ZoetisDenmark](https://github.com/ZoetisDenmark) |
| Accenture | ACN | Information Technology | non-US HQ | [Accenture](https://github.com/Accenture) *(primary)* |
| Allegion | ALLE | Industrials | non-US HQ | [Yonomi](https://github.com/Yonomi) |
| Aon plc | AON | Financials | non-US HQ | [Aon-Cyber-Solutions](https://github.com/Aon-Cyber-Solutions), [coverwallet](https://github.com/coverwallet) |
| Aptiv | APTV | Consumer Discretionary | non-US HQ | [Wind-River](https://github.com/Wind-River) |
| Eaton Corporation | ETN | Industrials | non-US HQ | [etn-ccis](https://github.com/etn-ccis) *(primary)*, [brightlayer-ui](https://github.com/brightlayer-ui) |
| Garmin | GRMN | Consumer Discretionary | non-US HQ | [garmin](https://github.com/garmin) *(primary)* |
| Johnson Controls | JCI | Industrials | non-US HQ | [jci-public](https://github.com/jci-public) *(primary)*, [metasys-server](https://github.com/metasys-server), [jci-metasys](https://github.com/jci-metasys) |
| Lululemon Athletica | LULU | Consumer Discretionary | non-US HQ | [Lululemon](https://github.com/Lululemon) *(primary)* |
| NXP Semiconductors | NXPI | Information Technology | non-US HQ | [nxp](https://github.com/nxp) *(primary)*, [nxp-mcuxpresso](https://github.com/nxp-mcuxpresso), [NXPmicro](https://github.com/NXPmicro) |
| Seagate Technology | STX | Information Technology | non-US HQ | [Seagate](https://github.com/Seagate) *(primary)* |
| TE Connectivity | TEL | Information Technology | non-US HQ | [TEConnectivity](https://github.com/TEConnectivity) *(primary)* |
| Willis Towers Watson | WTW | Financials | non-US HQ | [WTW-IM](https://github.com/WTW-IM) |

## Uncertain: a lead exists but no non-GitHub page confirms it (53)

Check these on GitHub itself (verified-domain badge) with `github_side_check.py`.

| company | ticker | lead / notes |
|---|---|---|
| Abbott Laboratories | ABT | Lead still unconfirmed: github.com/Abbott-Labs ('Abbott Navica', the BinaxNOW/NAVICA app; archived Oct 2024). No company or registry page names it. github.com/AbbottPlatform belongs to CI&T and github.com/open-abbott is  |
| Aflac | AFL | Best lead: github.com/Aflac-SCM (Columbus, GA, about 123 followers, a 'devX On-boarding Guide' repo). A web-search snippet says it has verified the aflac.com domain on GitHub, but that is visible only on GitHub. Other le |
| Applied Materials | AMAT | A search result shows a GitHub org github.com/applied-materials ('GitHub is where applied-materials builds software... This organization has no public members'), but no non-GitHub page (company site, careers, registry, W |
| AutoZone | AZO | Lead still unconfirmed: github.com/autozone ('AutoZone, Inc'), which has no public members and no visible public repos. No non-GitHub page links to it. The founder can check it for a verified-domain badge. |
| Avery Dennison | AVY | Leads still unconfirmed: github.com/AveryDennison ('Avery Dennison') and github.com/Avery-Dennison-AI (repo ad-smartsheet). No company-controlled or registry page links to either. |
| Axon Enterprise | AXON | Lead still unconfirmed: github.com/OpenAxon ('Axon'; repos webhooks-sample-consumer, terraform-provider-identitynow, terraform-provider-azurekvca, azure-key-vault-to-kubernetes, constrained-nn; a repo carries 'Copyright  |
| Baker Hughes | BKR | Lead: github.com/BakerHughes. The search snippet reads 'Baker Hughes Company' with 8 followers and links bakerhughes.com. The company's own sites block automated fetches or name no org, so no non-GitHub page confirming t |
| Bank of America | BAC | Lead only: github.com/bankofamerica. Search snippets say its website field is bankofamerica.com and it has no public members or repos. No non-GitHub page links to it: not the developer portal, Wikipedia or FINOS pages. T |
| Becton Dickinson | BDX | Lead only: github.com/FlowJo ('FlowJoExchange', hosts FlowJo.github.io, described as housing scripts and plugins for FlowJo). FlowJo LLC is a BD business (the plugin docs give [email redacted] as the contact). No flowjo.com |
| Berkshire Hathaway | BRK.B | The holding company itself runs no GitHub presence. Strong subsidiary lead: github.com/geico (GEICO, a wholly owned subsidiary), with about 23 repos including TuxTape, a Rust Linux-kernel livepatching toolkit that GEICO  |
| Boeing | BA | Lead only, not confirmed: github.com/Boeing (config-file-validator). No Boeing-controlled or authoritative non-GitHub page, press release or registry entry published by Boeing links to it. The founder should check the or |
| Bristol Myers Squibb | BMY | No official BMS org confirmed. The only GitHub links found for BMS-affiliated packages point to personal (ronammar) or consortium (PhUSE) repos, which do not count. Left as uncertain because a large pharma may have a dat |
| Carrier Global | CARR | No Carrier corporate GitHub org found. The only lead is github.com/viessmann, from an official 2019 Viessmann PyPI package (author 'Viessmann', @viessmann.com email). Carrier bought Viessmann Climate Solutions (closed Ja |
| Carvana | CVNA | The only lead is still github.com/carvana, recalled from memory and never seen on any Carvana-owned or authoritative page. It cannot be listed without evidence; the founder could check it on GitHub by hand. WebSearch bud |
| Charter Communications | CHTR | No org was found for Charter or Spectrum themselves. The only lead is still the legacy Time Warner Cable org TWCable (TWC merged into Charter in 2016; twcable.com was TWC's domain). The string was confirmed on the Gradle |
| Citigroup | C | Strong but unconfirmed lead: github.com/Citi. It hosts Citi/citi-ospo ('guidelines and resources from Citi's Open Source Program Office') and Citi/.github, which gives [email redacted] as its contact. Every search hit |
| Citizens Financial Group | CFG | github.com/citizensbanking is still the only lead, and no non-GitHub page confirms it. Search results show only the third-party api-evangelist/citizens-financial-group profile, which does not count, and unrelated 'Citize |
| Corpay | CPAY | I found no Corpay-branded GitHub org. Corpay's own developer portal, api.corpay.com, embeds a Mintlify deploy config showing that its docs are built from a private GitHub repo, plugsurfing/corpay-api. plugsurfing.com con |
| Dexcom | DXCM | No official GitHub org confirmed on any Dexcom-controlled page, registry package or Wikidata. Every Dexcom client library found is third-party. Left uncertain rather than none_found only because Dexcom runs a real develo |
| Domino's | DPZ | Lead still unconfirmed: github.com/dominos-pizza. Search snippets say it has verified the domains www.dominos.com and dominos.com, but no non-GitHub page links to it. tech.dominos.co.uk belongs to Domino's Pizza Group (U |
| Dow Inc. | DOW | Lead: github.com/Dow. The search snippet reads 'GitHub is where Dow builds software' and says the profile links https://www.dow.com/. dow.com is WAF-blocked, and no registry, Wikipedia or Wikidata page confirms the handl |
| DTE Energy | DTE | Lead only: github.com/dteenergy, an org whose website field is dteenergy.com (per search snippet), with 103 followers and no public repos or members. No DTE-controlled page links to it. The founder can verify on GitHub. |
| Duke Energy | DUK | Lead only: github.com/mthollylab ('Duke Energy ETO - Mt Holly Lab', Mount Holly Microgrid Lab and Research Center). The lab also has a GitLab group (gitlab.com/mthollylab: openfmb-cpp-sample-code, darksky). Its own domai |
| DuPont | DD | No official org confirmed. The earlier name-matching leads (github.com/dupont, dupont-tech, DuPont-Research-Group, DuPont-OrderAutomation, DuPont-myAccess) did not surface on any non-GitHub page, and a web search returns |
| Fidelity National Information Services | FIS | Large fintech, so an official org may exist, but it could not be confirmed: the main site is bot-walled and no search engine was usable. Worldpay is excluded (fully divested). Worth a retry once web search is available. |
| GE HealthCare | GEHC | Two likely-official leads are still unconfirmed on non-GitHub pages. github.com/GEHealthcare ('GE HealthCare') hosts apiserver.gehealthcare.com, the Centricity FHIR API server docs. github.com/GEUltrasound ('GE HealthCar |
| Gilead Sciences | GILD | Lead only, not confirmed: github.com/Gilead-BioStats, home of the gsm (Good Statistical Monitoring) R packages. No non-GitHub, Gilead-controlled or authoritative page naming it was found, and the gsm packages are still n |
| Halliburton | HAL | Landmark/OSDU work sits on the Open Group's GitLab, not on a Halliburton GitHub org. No official org confirmed. Left uncertain because a web search for a Landmark developer org could not be run. |
| Interactive Brokers | IBKR | IBKR's own site sends users to 'GitHub' at interactivebrokers.github.io. That is the GitHub Pages site of the 'interactivebrokers' account, which search shows as github.com/InteractiveBrokers (tws-api-public). The eviden |
| Invesco | IVZ | Two unconfirmed leads. (1) github.com/Invesco: an API Evangelist summary describes it as the Invesco org with a single inactive repo last updated in 2017. (2) github.com/jemstep ('Jemstep by Invesco', 19 repos, Scala, Jo |
| Invitation Homes | INVH | Strong but unconfirmed lead: github.com/invitation-homes, named 'Invitation Homes'. It holds 4 public repos (career-progression-framework, career-progression-framework-theme, heroku-buildpack-static, unt-git-good) and ha |
| IQVIA | IQV | No IQVIA-controlled or authoritative page links any GitHub org. Leads found only on GitHub or in search results: github.com/IQVIA-ML (TreeParzen.jl and LightGBM.jl Julia packages, registered in Julia General since 2020,  |
| Leidos | LDOS | There's no Leidos corporate GitHub org. kudu-dynamics belongs to Kudu Dynamics, which Leidos acquired on May 28, 2025. The evidence is an archived copy (May 2024) of Kudu's own site kududyn.com. The live site now redirec |
| Loews Corporation | L | Holding company; no GitHub org found for parent or subsidiaries, but loews.com and cna.com could not be fetched (403) and web search was unavailable, so CNA Financial in particular is unverified. Likely none. |
| Lowe's | LOW | There is evidence of an open-source program (npm scope @lowes-tech published by [email redacted], author 'Backyard Design System') and an official 'Lowe's Engineering' Medium publication (medium.com/lowes-engine |
| Medtronic | MDT | Medtronic plc is domiciled in Ireland; its operational HQ is in Minneapolis. The only company-adjacent org is github.com/Medtronic-LABS, confirmed on spice.docs.medtroniclabs.org. Sources describe Medtronic LABS as an in |
| MetLife | MET | No org confirmed by a non-GitHub page. github.com/MetLife (display name 'ML', repos such as awesome-abiogenesis, awesome-evolution and dune-weaver) does not look like MetLife Inc. and is probably a personal or unrelated  |
| Moderna | MRNA | The evidence is a peer-reviewed paper by Moderna, Inc. authors (Frontiers in Immunology 2022, doi 10.3389/fimmu.2022.948335), not a Moderna-owned domain. It calls github.com/modernatx 'the Moderna GitHub repository'. Fiv |
| Northrop Grumman | NOC | Unverified lead from memory only: a 'northropgrumman' GitHub org hosting JellyFish MBSE tooling. No non-GitHub page confirming the handle was found, so nothing is listed. The founder could check github.com/northropgrumma |
| Norwegian Cruise Line Holdings | NCLH | Lead: github.com/norwegian-cruise-line. The npm package bxslider-ncl (a fork of bxslider for NCL) points its repository to github.com/norwegian-cruise-line/bxslider-4, but it was published by an individual account (gmail |
| Paccar | PCAR | Leads still unconfirmed: github.com/PACCAR ('PACCAR, Inc.', repos opencpu, DataScience_ProjectTemplate, DataScience_PkgPattern, webster_py) and github.com/PACCAR-SAP. Only GitHub itself and rdrr.io (a GitHub mirror) show |
| Parker Hannifin | PH | Leads only: github.com/ParkerMSGIoT ('Parker Hannifin - Motion Systems', one TestRepo) and github.com/parkerhannifin. Parker's own sites block automated fetches (403), and no fetchable Parker page links to either org. Th |
| Procter & Gamble | PG | procter-gamble-vdp is P&G's official GitHub org for its vulnerability disclosure program: P&G's own security.txt names vdp.pg.com as the contact, and that domain redirects to the org. The evidence string is in the HTTP L |
| Progressive Corporation | PGR | No official org confirmed. developer.progressive.com is a real Progressive API portal but shows no GitHub link. Left uncertain because a web search could not be run. |
| Sandisk | SNDK | Confirmed from Sandisk's own (archived) open-source page, which calls it 'an official GitHub repo for our own projects'. The live page now redirects to about-us, so the evidence is the archived copy. The same page also l |
| Sherwin-Williams | SHW | Leads still unconfirmed: github.com/sherwin-williams-co ('The Sherwin Williams Company', SSO-enforced, about 460 followers) and github.com/sherwin-williams ('The Sherwin-Williams Company [OLD]'). They are probably the re |
| Stryker Corporation | SYK | github.com/stryker-mutator is an unrelated mutation-testing project, not the company. Subsidiaries (Vocera, care.ai and others) were not confirmable without search. Left uncertain. |
| Supermicro | SMCI | No official GitHub org could be confirmed on any readable Supermicro page. The status stays uncertain rather than none_found because a hardware and firmware company plausibly runs one, while supermicro.com blocks all aut |
| TJX Companies | TJX | No official GitHub org found; tjx.com itself remains unreachable (403) and web search was unavailable, so not fully ruled out. Likely none. |
| Trane Technologies | TT | No corporate Trane org found. github.com/nexiahome is probably the engineering org of Nexia, the smart-home brand Trane got from Ingersoll Rand; nexiahome.com now redirects to trane.com. It stays uncertain: the only evid |
| U.S. Bancorp | USB | Lead still unconfirmed: github.com/usbank ('U.S. Bank'), which holds the Yackety Hack hackathon repos (Event-Info, Test-Data-Sets, Technical-Resources, FAQ-Tips). Its hackathon portal hacktotrack-innovation.usbank.com ha |
| Ulta Beauty | ULTA | Lead: github.com/ultabeauty ('Ulta Beauty', 9 repos, mostly ML/CV forks such as tensorflow, opencv, mediapipe, clearml and face-occlusion-generation, plus Deep-Link-Generator and Intercept-Generator). No non-GitHub page  |
| United Parcel Service | UPS | Strong lead, still unconfirmed: github.com/UPS-API, which holds UPS-SDKs, Widgets-SDK, api-documentation and ups-mcp, and whose SDKs point to the UPS Developer Portal. It is very likely official, but every UPS page that  |
