import os
from random import uniform

RANDOM_SLEEP = round(uniform(6, 8), 1)

SITE_NAME = os.environ.get('SITE_NAME')

URLS_USA = {    # 444 unique locations
     "AK": [
      f"https://anchorage.{SITE_NAME}.org",
      f"https://fairbanks.{SITE_NAME}.org",
      f"https://kenai.{SITE_NAME}.org",
      f"https://juneau.{SITE_NAME}.org"
     ],
     "AL": [
      f"https://auburn.{SITE_NAME}.org",
      f"https://bham.{SITE_NAME}.org",
      f"https://columbusga.{SITE_NAME}.org",
      f"https://dothan.{SITE_NAME}.org",
      f"https://shoals.{SITE_NAME}.org",
      f"https://gadsden.{SITE_NAME}.org",
      f"https://huntsville.{SITE_NAME}.org",
      f"https://mobile.{SITE_NAME}.org",
      f"https://montgomery.{SITE_NAME}.org",
      f"https://tuscaloosa.{SITE_NAME}.org"
     ],
     "AR": [
      f"https://fayar.{SITE_NAME}.org",
      f"https://fortsmith.{SITE_NAME}.org",
      f"https://jonesboro.{SITE_NAME}.org",
      f"https://littlerock.{SITE_NAME}.org",
      f"https://memphis.{SITE_NAME}.org",
      f"https://texarkana.{SITE_NAME}.org"
     ],
     "AZ": [
      f"https://flagstaff.{SITE_NAME}.org",
      f"https://mohave.{SITE_NAME}.org",
      f"https://phoenix.{SITE_NAME}.org",
      f"https://prescott.{SITE_NAME}.org",
      f"https://showlow.{SITE_NAME}.org",
      f"https://sierravista.{SITE_NAME}.org",
      f"https://tucson.{SITE_NAME}.org",
      f"https://yuma.{SITE_NAME}.org"
     ],
     "CA": [
      f"https://bakersfield.{SITE_NAME}.org",
      f"https://chico.{SITE_NAME}.org",
      f"https://fresno.{SITE_NAME}.org",
      f"https://goldcountry.{SITE_NAME}.org",
      f"https://hanford.{SITE_NAME}.org",
      f"https://humboldt.{SITE_NAME}.org",
      f"https://imperial.{SITE_NAME}.org",
      f"https://inlandempire.{SITE_NAME}.org",
      f"https://losangeles.{SITE_NAME}.org",
      f"https://mendocino.{SITE_NAME}.org",
      f"https://merced.{SITE_NAME}.org",
      f"https://modesto.{SITE_NAME}.org",
      f"https://monterey.{SITE_NAME}.org",
      f"https://orangecounty.{SITE_NAME}.org",
      f"https://palmsprings.{SITE_NAME}.org",
      f"https://redding.{SITE_NAME}.org",
      f"https://reno.{SITE_NAME}.org",
      f"https://sacramento.{SITE_NAME}.org",
      f"https://sandiego.{SITE_NAME}.org",
      f"https://slo.{SITE_NAME}.org",
      f"https://santabarbara.{SITE_NAME}.org",
      f"https://santamaria.{SITE_NAME}.org",
      f"https://sfbay.{SITE_NAME}.org",
      f"https://siskiyou.{SITE_NAME}.org",
      f"https://stockton.{SITE_NAME}.org",
      f"https://susanville.{SITE_NAME}.org",
      f"https://ventura.{SITE_NAME}.org",
      f"https://visalia.{SITE_NAME}.org",
      f"https://yubasutter.{SITE_NAME}.org"
     ],
     "CO": [
      f"https://boulder.{SITE_NAME}.org",
      f"https://cosprings.{SITE_NAME}.org",
      f"https://denver.{SITE_NAME}.org",
      f"https://eastco.{SITE_NAME}.org",
      f"https://fortcollins.{SITE_NAME}.org",
      f"https://rockies.{SITE_NAME}.org",
      f"https://pueblo.{SITE_NAME}.org",
      f"https://westslope.{SITE_NAME}.org"
     ],
     "CT": [
      f"https://newlondon.{SITE_NAME}.org",
      f"https://hartford.{SITE_NAME}.org",
      f"https://newhaven.{SITE_NAME}.org",
      f"https://nwct.{SITE_NAME}.org",
      f"https://newyork.{SITE_NAME}.org/fct/"
     ],
     "DE": [
      f"https://delaware.{SITE_NAME}.org/"
     ],
     "FL": [
      f"https://daytona.{SITE_NAME}.org",
      f"https://keys.{SITE_NAME}.org",
      f"https://fortmyers.{SITE_NAME}.org",
      f"https://gainesville.{SITE_NAME}.org",
      f"https://cfl.{SITE_NAME}.org",
      f"https://jacksonville.{SITE_NAME}.org",
      f"https://lakeland.{SITE_NAME}.org",
      f"https://lakecity.{SITE_NAME}.org",
      f"https://ocala.{SITE_NAME}.org",
      f"https://okaloosa.{SITE_NAME}.org",
      f"https://orlando.{SITE_NAME}.org",
      f"https://panamacity.{SITE_NAME}.org",
      f"https://pensacola.{SITE_NAME}.org",
      f"https://sarasota.{SITE_NAME}.org",
      f"https://miami.{SITE_NAME}.org",
      f"https://spacecoast.{SITE_NAME}.org",
      f"https://staugustine.{SITE_NAME}.org",
      f"https://tallahassee.{SITE_NAME}.org",
      f"https://tampa.{SITE_NAME}.org",
      f"https://treasure.{SITE_NAME}.org"
     ],
     "GA": [
      f"https://albanyga.{SITE_NAME}.org",
      f"https://athensga.{SITE_NAME}.org",
      f"https://atlanta.{SITE_NAME}.org",
      f"https://augusta.{SITE_NAME}.org",
      f"https://brunswick.{SITE_NAME}.org",
      f"https://columbusga.{SITE_NAME}.org",
      f"https://macon.{SITE_NAME}.org",
      f"https://nwga.{SITE_NAME}.org",
      f"https://savannah.{SITE_NAME}.org",
      f"https://statesboro.{SITE_NAME}.org",
      f"https://valdosta.{SITE_NAME}.org"
     ],
     "HI": [
      f"https://honolulu.{SITE_NAME}.org/"
     ],
     "IA": [
      f"https://ames.{SITE_NAME}.org",
      f"https://cedarrapids.{SITE_NAME}.org",
      f"https://desmoines.{SITE_NAME}.org",
      f"https://dubuque.{SITE_NAME}.org",
      f"https://fortdodge.{SITE_NAME}.org",
      f"https://iowacity.{SITE_NAME}.org",
      f"https://masoncity.{SITE_NAME}.org",
      f"https://omaha.{SITE_NAME}.org",
      f"https://quadcities.{SITE_NAME}.org",
      f"https://siouxcity.{SITE_NAME}.org",
      f"https://ottumwa.{SITE_NAME}.org",
      f"https://waterloo.{SITE_NAME}.org"
     ],
     "ID": [
      f"https://boise.{SITE_NAME}.org",
      f"https://eastidaho.{SITE_NAME}.org",
      f"https://lewiston.{SITE_NAME}.org",
      f"https://pullman.{SITE_NAME}.org",
      f"https://spokane.{SITE_NAME}.org",
      f"https://twinfalls.{SITE_NAME}.org"
     ],
     "IL": [
      f"https://bn.{SITE_NAME}.org",
      f"https://chambana.{SITE_NAME}.org",
      f"https://chicago.{SITE_NAME}.org",
      f"https://decatur.{SITE_NAME}.org",
      f"https://lasalle.{SITE_NAME}.org",
      f"https://mattoon.{SITE_NAME}.org",
      f"https://peoria.{SITE_NAME}.org",
      f"https://quadcities.{SITE_NAME}.org",
      f"https://rockford.{SITE_NAME}.org",
      f"https://carbondale.{SITE_NAME}.org",
      f"https://springfieldil.{SITE_NAME}.org",
      f"https://stlouis.{SITE_NAME}.org",
      f"https://quincy.{SITE_NAME}.org"
     ],
     "IN": [
      f"https://bloomington.{SITE_NAME}.org",
      f"https://evansville.{SITE_NAME}.org",
      f"https://fortwayne.{SITE_NAME}.org",
      f"https://indianapolis.{SITE_NAME}.org",
      f"https://kokomo.{SITE_NAME}.org",
      f"https://tippecanoe.{SITE_NAME}.org",
      f"https://muncie.{SITE_NAME}.org",
      f"https://richmondin.{SITE_NAME}.org",
      f"https://southbend.{SITE_NAME}.org",
      f"https://terrehaute.{SITE_NAME}.org",
      f"https://chicago.{SITE_NAME}.org/nwi/"
     ],
     "KS": [
      f"https://kansascity.{SITE_NAME}.org",
      f"https://lawrence.{SITE_NAME}.org",
      f"https://ksu.{SITE_NAME}.org",
      f"https://nwks.{SITE_NAME}.org",
      f"https://salina.{SITE_NAME}.org",
      f"https://seks.{SITE_NAME}.org",
      f"https://swks.{SITE_NAME}.org",
      f"https://topeka.{SITE_NAME}.org",
      f"https://wichita.{SITE_NAME}.org"
     ],
     "KY": [
      f"https://bgky.{SITE_NAME}.org",
      f"https://cincinnati.{SITE_NAME}.org",
      f"https://eastky.{SITE_NAME}.org",
      f"https://huntington.{SITE_NAME}.org",
      f"https://lexington.{SITE_NAME}.org",
      f"https://louisville.{SITE_NAME}.org",
      f"https://owensboro.{SITE_NAME}.org",
      f"https://westky.{SITE_NAME}.org"
     ],
     "LA": [
      f"https://batonrouge.{SITE_NAME}.org",
      f"https://cenla.{SITE_NAME}.org",
      f"https://houma.{SITE_NAME}.org",
      f"https://lafayette.{SITE_NAME}.org",
      f"https://lakecharles.{SITE_NAME}.org",
      f"https://monroe.{SITE_NAME}.org",
      f"https://neworleans.{SITE_NAME}.org",
      f"https://shreveport.{SITE_NAME}.org"
     ],
     "MA": [
      f"https://boston.{SITE_NAME}.org",
      f"https://capecod.{SITE_NAME}.org",
      f"https://southcoast.{SITE_NAME}.org",
      f"https://westernmass.{SITE_NAME}.org",
      f"https://worcester.{SITE_NAME}.org"
     ],
     "MD": [
      f"https://annapolis.{SITE_NAME}.org",
      f"https://baltimore.{SITE_NAME}.org",
      f"https://chambersburg.{SITE_NAME}.org",
      f"https://easternshore.{SITE_NAME}.org",
      f"https://frederick.{SITE_NAME}.org",
      f"https://smd.{SITE_NAME}.org",
      f"https://westmd.{SITE_NAME}.org",
      f"https://washingtondc.{SITE_NAME}.org/mld/"
     ],
     "ME": [
      f"https://maine.{SITE_NAME}.org/"
     ],
     "MI": [
      f"https://annarbor.{SITE_NAME}.org",
      f"https://battlecreek.{SITE_NAME}.org",
      f"https://centralmich.{SITE_NAME}.org",
      f"https://detroit.{SITE_NAME}.org",
      f"https://flint.{SITE_NAME}.org",
      f"https://grandrapids.{SITE_NAME}.org",
      f"https://holland.{SITE_NAME}.org",
      f"https://jxn.{SITE_NAME}.org",
      f"https://kalamazoo.{SITE_NAME}.org",
      f"https://lansing.{SITE_NAME}.org",
      f"https://monroemi.{SITE_NAME}.org",
      f"https://muskegon.{SITE_NAME}.org",
      f"https://nmi.{SITE_NAME}.org",
      f"https://porthuron.{SITE_NAME}.org",
      f"https://saginaw.{SITE_NAME}.org",
      f"https://southbend.{SITE_NAME}.org",
      f"https://swmi.{SITE_NAME}.org",
      f"https://thumb.{SITE_NAME}.org",
      f"https://up.{SITE_NAME}.org"
     ],
     "MN": [
      f"https://bemidji.{SITE_NAME}.org",
      f"https://brainerd.{SITE_NAME}.org",
      f"https://duluth.{SITE_NAME}.org",
      f"https://fargo.{SITE_NAME}.org",
      f"https://mankato.{SITE_NAME}.org",
      f"https://minneapolis.{SITE_NAME}.org",
      f"https://rmn.{SITE_NAME}.org",
      f"https://marshall.{SITE_NAME}.org",
      f"https://stcloud.{SITE_NAME}.org"
     ],
     "MO": [
      f"https://columbiamo.{SITE_NAME}.org",
      f"https://joplin.{SITE_NAME}.org",
      f"https://kansascity.{SITE_NAME}.org",
      f"https://kirksville.{SITE_NAME}.org",
      f"https://loz.{SITE_NAME}.org",
      f"https://semo.{SITE_NAME}.org",
      f"https://springfield.{SITE_NAME}.org",
      f"https://stjoseph.{SITE_NAME}.org",
      f"https://stlouis.{SITE_NAME}.org"
     ],
     "MS": [
      f"https://gulfport.{SITE_NAME}.org",
      f"https://hattiesburg.{SITE_NAME}.org",
      f"https://jackson.{SITE_NAME}.org",
      f"https://memphis.{SITE_NAME}.org",
      f"https://meridian.{SITE_NAME}.org",
      f"https://northmiss.{SITE_NAME}.org",
      f"https://natchez.{SITE_NAME}.org"
     ],
     "MT": [
      f"https://billings.{SITE_NAME}.org",
      f"https://bozeman.{SITE_NAME}.org",
      f"https://butte.{SITE_NAME}.org",
      f"https://montana.{SITE_NAME}.org",
      f"https://greatfalls.{SITE_NAME}.org",
      f"https://helena.{SITE_NAME}.org",
      f"https://kalispell.{SITE_NAME}.org",
      f"https://missoula.{SITE_NAME}.org"
     ],
     "NC": [
      f"https://asheville.{SITE_NAME}.org",
      f"https://boone.{SITE_NAME}.org",
      f"https://charlotte.{SITE_NAME}.org",
      f"https://eastnc.{SITE_NAME}.org",
      f"https://fayetteville.{SITE_NAME}.org",
      f"https://greensboro.{SITE_NAME}.org",
      f"https://hickory.{SITE_NAME}.org",
      f"https://onslow.{SITE_NAME}.org",
      f"https://outerbanks.{SITE_NAME}.org",
      f"https://raleigh.{SITE_NAME}.org",
      f"https://wilmington.{SITE_NAME}.org",
      f"https://winstonsalem.{SITE_NAME}.org"
     ],
     "ND": [
      f"https://bismarck.{SITE_NAME}.org",
      f"https://fargo.{SITE_NAME}.org",
      f"https://grandforks.{SITE_NAME}.org",
      f"https://nd.{SITE_NAME}.org"
     ],
     "NE": [
      f"https://grandisland.{SITE_NAME}.org",
      f"https://lincoln.{SITE_NAME}.org",
      f"https://northplatte.{SITE_NAME}.org",
      f"https://omaha.{SITE_NAME}.org",
      f"https://scottsbluff.{SITE_NAME}.org",
      f"https://siouxcity.{SITE_NAME}.org"
     ],
     "NH": [
      f"https://nh.{SITE_NAME}.org/"
     ],
     "NJ": [
      f"https://cnj.{SITE_NAME}.org",
      f"https://jerseyshore.{SITE_NAME}.org",
      f"https://newjersey.{SITE_NAME}.org",
      f"https://southjersey.{SITE_NAME}.org",
      f"https://newyork.{SITE_NAME}.org/jsy/"
     ],
     "NM": [
      f"https://albuquerque.{SITE_NAME}.org",
      f"https://clovis.{SITE_NAME}.org",
      f"https://farmington.{SITE_NAME}.org",
      f"https://lascruces.{SITE_NAME}.org",
      f"https://roswell.{SITE_NAME}.org",
      f"https://santafe.{SITE_NAME}.org"
     ],
     "NV": [
      f"https://elko.{SITE_NAME}.org",
      f"https://lasvegas.{SITE_NAME}.org",
      f"https://reno.{SITE_NAME}.org"
     ],
     "NY": [
      f"https://albany.{SITE_NAME}.org",
      f"https://binghamton.{SITE_NAME}.org",
      f"https://buffalo.{SITE_NAME}.org",
      f"https://catskills.{SITE_NAME}.org",
      f"https://chautauqua.{SITE_NAME}.org",
      f"https://elmira.{SITE_NAME}.org",
      f"https://fingerlakes.{SITE_NAME}.org",
      f"https://glensfalls.{SITE_NAME}.org",
      f"https://hudsonvalley.{SITE_NAME}.org",
      f"https://ithaca.{SITE_NAME}.org",
      f"https://longisland.{SITE_NAME}.org",
      f"https://newyork.{SITE_NAME}.org",
      f"https://oneonta.{SITE_NAME}.org",
      f"https://plattsburgh.{SITE_NAME}.org",
      f"https://potsdam.{SITE_NAME}.org",
      f"https://rochester.{SITE_NAME}.org",
      f"https://syracuse.{SITE_NAME}.org",
      f"https://twintiers.{SITE_NAME}.org",
      f"https://utica.{SITE_NAME}.org",
      f"https://watertown.{SITE_NAME}.org"
     ],
     "OH": [
      f"https://akroncanton.{SITE_NAME}.org",
      f"https://ashtabula.{SITE_NAME}.org",
      f"https://athensohio.{SITE_NAME}.org",
      f"https://chillicothe.{SITE_NAME}.org",
      f"https://cincinnati.{SITE_NAME}.org",
      f"https://cleveland.{SITE_NAME}.org",
      f"https://columbus.{SITE_NAME}.org",
      f"https://dayton.{SITE_NAME}.org",
      f"https://huntington.{SITE_NAME}.org",
      f"https://limaohio.{SITE_NAME}.org",
      f"https://mansfield.{SITE_NAME}.org",
      f"https://wheeling.{SITE_NAME}.org",
      f"https://parkersburg.{SITE_NAME}.org",
      f"https://sandusky.{SITE_NAME}.org",
      f"https://toledo.{SITE_NAME}.org",
      f"https://tuscarawas.{SITE_NAME}.org",
      f"https://youngstown.{SITE_NAME}.org",
      f"https://zanesville.{SITE_NAME}.org"
     ],
     "OK": [
      f"https://fortsmith.{SITE_NAME}.org",
      f"https://lawton.{SITE_NAME}.org",
      f"https://enid.{SITE_NAME}.org",
      f"https://oklahomacity.{SITE_NAME}.org",
      f"https://stillwater.{SITE_NAME}.org",
      f"https://texoma.{SITE_NAME}.org",
      f"https://tulsa.{SITE_NAME}.org"
     ],
     "OR": [
      f"https://bend.{SITE_NAME}.org",
      f"https://corvallis.{SITE_NAME}.org",
      f"https://eastoregon.{SITE_NAME}.org",
      f"https://eugene.{SITE_NAME}.org",
      f"https://klamath.{SITE_NAME}.org",
      f"https://medford.{SITE_NAME}.org",
      f"https://oregoncoast.{SITE_NAME}.org",
      f"https://portland.{SITE_NAME}.org",
      f"https://roseburg.{SITE_NAME}.org",
      f"https://salem.{SITE_NAME}.org"
     ],
     "PA": [
      f"https://altoona.{SITE_NAME}.org",
      f"https://chambersburg.{SITE_NAME}.org",
      f"https://erie.{SITE_NAME}.org",
      f"https://harrisburg.{SITE_NAME}.org",
      f"https://lancaster.{SITE_NAME}.org",
      f"https://allentown.{SITE_NAME}.org",
      f"https://meadville.{SITE_NAME}.org",
      f"https://philadelphia.{SITE_NAME}.org",
      f"https://pittsburgh.{SITE_NAME}.org",
      f"https://poconos.{SITE_NAME}.org",
      f"https://reading.{SITE_NAME}.org",
      f"https://scranton.{SITE_NAME}.org",
      f"https://pennstate.{SITE_NAME}.org",
      f"https://twintiers.{SITE_NAME}.org",
      f"https://williamsport.{SITE_NAME}.org",
      f"https://york.{SITE_NAME}.org"
     ],
     "RI": [
      f"https://providence.{SITE_NAME}.org/"
     ],
     "SC": [
      f"https://charleston.{SITE_NAME}.org",
      f"https://columbia.{SITE_NAME}.org",
      f"https://florencesc.{SITE_NAME}.org",
      f"https://greenville.{SITE_NAME}.org",
      f"https://hiltonhead.{SITE_NAME}.org",
      f"https://myrtlebeach.{SITE_NAME}.org"
     ],
     "SD": [
      f"https://nesd.{SITE_NAME}.org",
      f"https://csd.{SITE_NAME}.org",
      f"https://rapidcity.{SITE_NAME}.org",
      f"https://siouxfalls.{SITE_NAME}.org",
      f"https://sd.{SITE_NAME}.org"
     ],
     "TN": [
      f"https://chattanooga.{SITE_NAME}.org",
      f"https://clarksville.{SITE_NAME}.org",
      f"https://cookeville.{SITE_NAME}.org",
      f"https://jacksontn.{SITE_NAME}.org",
      f"https://knoxville.{SITE_NAME}.org",
      f"https://memphis.{SITE_NAME}.org",
      f"https://nashville.{SITE_NAME}.org",
      f"https://tricities.{SITE_NAME}.org"
     ],
     "TX": [
      f"https://abilene.{SITE_NAME}.org",
      f"https://amarillo.{SITE_NAME}.org",
      f"https://austin.{SITE_NAME}.org",
      f"https://beaumont.{SITE_NAME}.org",
      f"https://brownsville.{SITE_NAME}.org",
      f"https://collegestation.{SITE_NAME}.org",
      f"https://corpuschristi.{SITE_NAME}.org",
      f"https://dallas.{SITE_NAME}.org",
      f"https://nacogdoches.{SITE_NAME}.org",
      f"https://delrio.{SITE_NAME}.org",
      f"https://elpaso.{SITE_NAME}.org",
      f"https://galveston.{SITE_NAME}.org",
      f"https://houston.{SITE_NAME}.org",
      f"https://killeen.{SITE_NAME}.org",
      f"https://laredo.{SITE_NAME}.org",
      f"https://lubbock.{SITE_NAME}.org",
      f"https://mcallen.{SITE_NAME}.org",
      f"https://odessa.{SITE_NAME}.org",
      f"https://sanangelo.{SITE_NAME}.org",
      f"https://sanantonio.{SITE_NAME}.org",
      f"https://sanmarcos.{SITE_NAME}.org",
      f"https://bigbend.{SITE_NAME}.org",
      f"https://texarkana.{SITE_NAME}.org",
      f"https://texoma.{SITE_NAME}.org",
      f"https://easttexas.{SITE_NAME}.org",
      f"https://victoriatx.{SITE_NAME}.org",
      f"https://waco.{SITE_NAME}.org",
      f"https://wichitafalls.{SITE_NAME}.org"
     ],
     "UT": [
      f"https://logan.{SITE_NAME}.org",
      f"https://ogden.{SITE_NAME}.org",
      f"https://provo.{SITE_NAME}.org",
      f"https://saltlakecity.{SITE_NAME}.org",
      f"https://stgeorge.{SITE_NAME}.org"
     ],
     "VA": [
      f"https://charlottesville.{SITE_NAME}.org",
      f"https://danville.{SITE_NAME}.org",
      f"https://easternshore.{SITE_NAME}.org",
      f"https://fredericksburg.{SITE_NAME}.org",
      f"https://harrisonburg.{SITE_NAME}.org",
      f"https://lynchburg.{SITE_NAME}.org",
      f"https://blacksburg.{SITE_NAME}.org",
      f"https://norfolk.{SITE_NAME}.org",
      f"https://richmond.{SITE_NAME}.org",
      f"https://roanoke.{SITE_NAME}.org",
      f"https://swva.{SITE_NAME}.org",
      f"https://winchester.{SITE_NAME}.org",
      f"https://washingtondc.{SITE_NAME}.org/nva/"
     ],
     "VT": [
      f"https://vermont.{SITE_NAME}.org/"
     ],
     "WA": [
      f"https://bellingham.{SITE_NAME}.org",
      f"https://kpr.{SITE_NAME}.org",
      f"https://lewiston.{SITE_NAME}.org",
      f"https://moseslake.{SITE_NAME}.org",
      f"https://olympic.{SITE_NAME}.org",
      f"https://pullman.{SITE_NAME}.org",
      f"https://seattle.{SITE_NAME}.org",
      f"https://skagit.{SITE_NAME}.org",
      f"https://spokane.{SITE_NAME}.org",
      f"https://wenatchee.{SITE_NAME}.org",
      f"https://yakima.{SITE_NAME}.org",
      f"https://portland.{SITE_NAME}.org/clk/"
     ],
     "WI": [
      f"https://appleton.{SITE_NAME}.org",
      f"https://duluth.{SITE_NAME}.org",
      f"https://eauclaire.{SITE_NAME}.org",
      f"https://greenbay.{SITE_NAME}.org",
      f"https://janesville.{SITE_NAME}.org",
      f"https://racine.{SITE_NAME}.org",
      f"https://lacrosse.{SITE_NAME}.org",
      f"https://madison.{SITE_NAME}.org",
      f"https://milwaukee.{SITE_NAME}.org",
      f"https://northernwi.{SITE_NAME}.org",
      f"https://sheboygan.{SITE_NAME}.org",
      f"https://wausau.{SITE_NAME}.org"
     ],
     "WV": [
      f"https://charlestonwv.{SITE_NAME}.org",
      f"https://martinsburg.{SITE_NAME}.org",
      f"https://huntington.{SITE_NAME}.org",
      f"https://morgantown.{SITE_NAME}.org",
      f"https://wheeling.{SITE_NAME}.org",
      f"https://parkersburg.{SITE_NAME}.org",
      f"https://swv.{SITE_NAME}.org",
      f"https://wv.{SITE_NAME}.org"
     ],
     "WY": [
      f"https://wyoming.{SITE_NAME}.org/"
     ]
}

URLS_CAN = {    # 55 unique locations

     "barrie, ON": [
      f"https://barrie.{SITE_NAME}.ca"
     ],
     "belleville, ON": [
      f"https://belleville.{SITE_NAME}.ca"
     ],
     "brantford-woodstock": [
      f"https://brantford.{SITE_NAME}.ca"
     ],
     "calgary, AB": [
      f"https://calgary.{SITE_NAME}.ca"
     ],
     "cariboo, BC": [
      f"https://cariboo.{SITE_NAME}.ca"
     ],
     "chatham-kent, ON": [
      f"https://chatham.{SITE_NAME}.ca"
     ],
     "comox valley, BC": [
      f"https://comoxvalley.{SITE_NAME}.ca"
     ],
     "cornwall, ON": [
      f"https://cornwall.{SITE_NAME}.ca"
     ],
     "edmonton, AB": [
      f"https://edmonton.{SITE_NAME}.ca"
     ],
     "fraser valley, BC": [
      f"https://abbotsford.{SITE_NAME}.ca"
     ],
     "ft mcmurray, AB": [
      f"https://ftmcmurray.{SITE_NAME}.ca"
     ],
     "guelph, ON": [
      f"https://guelph.{SITE_NAME}.ca"
     ],
     "halifax, NS": [
      f"https://halifax.{SITE_NAME}.ca"
     ],
     "hamilton-burlington": [
      f"https://hamilton.{SITE_NAME}.ca"
     ],
     "kamloops, BC": [
      f"https://kamloops.{SITE_NAME}.ca"
     ],
     "kelowna / okanagan": [
      f"https://kelowna.{SITE_NAME}.ca"
     ],
     "kingston, ON": [
      f"https://kingston.{SITE_NAME}.ca"
     ],
     "kitchener-waterloo-cambridge": [
      f"https://kitchener.{SITE_NAME}.ca"
     ],
     "kootenays, BC": [
      f"https://kootenays.{SITE_NAME}.ca"
     ],
     "lethbridge, AB": [
      f"https://lethbridge.{SITE_NAME}.ca"
     ],
     "london, ON": [
      f"https://londonon.{SITE_NAME}.ca"
     ],
     "medicine hat, AB": [
      f"https://hat.{SITE_NAME}.ca"
     ],
     "montreal, QC": [
      f"https://montreal.{SITE_NAME}.ca"
     ],
     "nanaimo, BC": [
      f"https://nanaimo.{SITE_NAME}.ca"
     ],
     "new brunswick": [
      f"https://newbrunswick.{SITE_NAME}.ca"
     ],
     "niagara region": [
      f"https://niagara.{SITE_NAME}.ca"
     ],
     "ottawa-hull-gatineau": [
      f"https://ottawa.{SITE_NAME}.ca"
     ],
     "owen sound, ON": [
      f"https://owensound.{SITE_NAME}.ca"
     ],
     "peace river country": [
      f"https://peace.{SITE_NAME}.ca"
     ],
     "peterborough, ON": [
      f"https://peterborough.{SITE_NAME}.ca"
     ],
     "prince edward island": [
      f"https://pei.{SITE_NAME}.ca"
     ],
     "prince george, BC": [
      f"https://princegeorge.{SITE_NAME}.ca"
     ],
     "quebec city": [
      f"https://quebec.{SITE_NAME}.ca"
     ],
     "red deer, AB": [
      f"https://reddeer.{SITE_NAME}.ca"
     ],
     "regina, SK": [
      f"https://regina.{SITE_NAME}.ca"
     ],
     "saguenay, QC": [
      f"https://saguenay.{SITE_NAME}.ca"
     ],
     "sarnia, ON": [
      f"https://sarnia.{SITE_NAME}.ca"
     ],
     "saskatoon, SK": [
      f"https://saskatoon.{SITE_NAME}.ca"
     ],
     "sault ste marie, ON": [
      f"https://soo.{SITE_NAME}.ca"
     ],
     "sherbrooke, QC": [
      f"https://sherbrooke.{SITE_NAME}.ca"
     ],
     "skeena-bulkley": [
      f"https://skeena.{SITE_NAME}.ca"
     ],
     "st john's, NL": [
      f"https://newfoundland.{SITE_NAME}.ca"
     ],
     "sudbury, ON": [
      f"https://sudbury.{SITE_NAME}.ca"
     ],
     "sunshine coast, BC": [
      f"https://sunshine.{SITE_NAME}.ca"
     ],
     "territories": [
      f"https://territories.{SITE_NAME}.ca"
     ],
     "thunder bay, ON": [
      f"https://thunderbay.{SITE_NAME}.ca"
     ],
     "toronto": [
      f"https://toronto.{SITE_NAME}.ca"
     ],
     "trois-rivieres, QC": [
      f"https://troisrivieres.{SITE_NAME}.ca"
     ],
     "vancouver, BC": [
      f"https://vancouver.{SITE_NAME}.ca"
     ],
     "victoria, BC": [
      f"https://victoria.{SITE_NAME}.ca"
     ],
     "whistler / squamish": [
      f"https://whistler.{SITE_NAME}.ca"
     ],
     "whitehorse, YT": [
      f"https://whitehorse.{SITE_NAME}.ca"
     ],
     "windsor, ON": [
      f"https://windsor.{SITE_NAME}.ca"
     ],
     "winnipeg, MB": [
      f"https://winnipeg.{SITE_NAME}.ca"
     ],
     "yellowknife, NT": [
      f"https://yellowknife.{SITE_NAME}.ca"
     ]
}

URLS_UK = {     #27 unique locations
     "aberdeen": [
      f"https://aberdeen.{SITE_NAME}.co.uk"
     ],
     "bath, UK": [
      f"https://bath.{SITE_NAME}.co.uk"
     ],
     "belfast": [
      f"https://belfast.{SITE_NAME}.co.uk"
     ],
     "birmingham / west mids": [
      f"https://birmingham.{SITE_NAME}.co.uk"
     ],
     "brighton": [
      f"https://brighton.{SITE_NAME}.co.uk"
     ],
     "bristol": [
      f"https://bristol.{SITE_NAME}.co.uk"
     ],
     "cambridge, UK": [
      f"https://cambridge.{SITE_NAME}.co.uk"
     ],
     "cardiff / wales": [
      f"https://cardiff.{SITE_NAME}.co.uk"
     ],
     "coventry, UK": [
      f"https://coventry.{SITE_NAME}.co.uk"
     ],
     "derby, UK": [
      f"https://derby.{SITE_NAME}.co.uk"
     ],
     "devon & cornwall": [
      f"https://devon.{SITE_NAME}.co.uk"
     ],
     "dundee": [
      f"https://dundee.{SITE_NAME}.co.uk"
     ],
     "east anglia": [
      f"https://norwich.{SITE_NAME}.co.uk"
     ],
     "east midlands": [
      f"https://eastmids.{SITE_NAME}.co.uk"
     ],
     "edinburgh": [
      f"https://edinburgh.{SITE_NAME}.co.uk"
     ],
     "essex, UK": [
      f"https://essex.{SITE_NAME}.co.uk"
     ],
     "glasgow": [
      f"https://glasgow.{SITE_NAME}.co.uk"
     ],
     "hampshire": [
      f"https://hampshire.{SITE_NAME}.co.uk"
     ],
     "kent, UK": [
      f"https://kent.{SITE_NAME}.co.uk"
     ],
     "leeds": [
      f"https://leeds.{SITE_NAME}.co.uk"
     ],
     "liverpool": [
      f"https://liverpool.{SITE_NAME}.co.uk"
     ],
     "london, UK": [
      f"https://london.{SITE_NAME}.co.uk"
     ],
     "manchester, UK": [
      f"https://manchester.{SITE_NAME}.co.uk"
     ],
     "newcastle / NE england": [
      f"https://newcastle.{SITE_NAME}.co.uk"
     ],
     "nottingham, UK": [
      f"https://nottingham.{SITE_NAME}.co.uk"
     ],
     "oxford, UK": [
      f"https://oxford.{SITE_NAME}.co.uk"
     ],
     "sheffield": [
      f"https://sheffield.{SITE_NAME}.co.uk"
     ]
}
