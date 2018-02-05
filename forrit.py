import os
from bottle import route, run, template, static_file, error

frettir = [
    {
        "fyrirsögn": "Lenti á grasflöt við Eiðisgranda",
        "texti": " Þyrla Land­helg­is­gæsl­unn­ar var nú fyr­ir stundu kölluð út vegna um­ferðaró­happs á Suður­landi en aðstoð henn­ar var svo aft­ur­kölluð. Þegar þyrl­an ætlaði að lenda aft­ur hafði skyggni við Reykja­vík­ur­flug­völl spillst svo mikið vegna dimmra élja að ekki reynd­ist unnt að lenda þar.",
        "mynd": "frett1.jpg",
        "email": "þyrla@gmail.com"
    },
    {
        "fyrirsögn": "Margir vilja vera á lista Sjálfstæðiflokksins",
        "texti": "Mik­ill áhugi er á að taka sæti á fram­boðslista Sjálf­stæðis­flokks­ins í Reykja­vík vegna borg­ar­stjórn­ar­kosn­ing­anna í vor að sögn Sveins H. Skúla­son­ar, for­manns kjör­nefnd­ar. Leiðtoga­kjör fór fram hjá sjálf­stæðismönn­um í Reykja­vík í lok síðasta mánaðar þar sem Eyþór Lax­dal Arn­alds bar sig­ur úr být­um með rúm­lega 60% greiddra at­kvæða.",
        "mynd": "frett2.jpg",
        "email": "sus@gmail.com"
    },
    {
        "fyrirsögn": "Einar aðstoðar Dómsmálaráðherra",
        "texti": "Ein­ar Hann­es­son lögmaður hef­ur verið ráðinn aðstoðarmaður Sig­ríðar Á. And­er­sen dóms­málaráðherra. Ein­ar hef­ur störf á næstu vik­um og mun starfa með Lauf­eyju Rún Ket­ils­dótt­ur sem hef­ur verið aðstoðarmaður ráðherra und­an­farið eitt ár. ",
        "mynd": "frett3.jpg",
        "email": "einsikaldi@gmail.com"
    },
    {
        "fyrirsögn": "'Ertu að grínast?'",
        "texti": "Nokkr­ir leik­manna NFL-meist­araliðs Phila­delp­hia Eag­les hafa nú þegar greint frá því að þeir ætli ekki að heim­sækja Don­ald Trump Banda­ríkja­for­seta. Hefð er fyr­ir því að sig­ur­veg­ur­um í stærstu íþrótt­un­um vest­an­hafs sé boðið í Hvíta húsið.",
        "mynd": "frett4.jpg",
        "email": "nfl@gmail.com"
    }
]

@route("/")
def index():
    return template("verk3")

@route("/a")
def lidura():
    return template("lidura")

@route("/b")
def lidurb():
    return template("index", frettir=frettir)

@route("/frett/1")
def frett():
    return template("frett1", frettir=frettir)

@route("/frett/2")
def frett():
    return template("frett2", frettir=frettir)

@route("/frett/3")
def frett():
    return template("frett3", frettir=frettir)

@route("/frett/4")
def frett():
    return template("frett4", frettir=frettir)

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="./myfiles")

@route("/kt/<kennitala>")
def kt(kennitala):
    return template("kt", kennitala=kennitala)

@error(404)
def error404(error):
    return "Þessi síða er ekki til"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
