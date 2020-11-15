class Constants:
	BOT_EXEC = 'BlackMarket.py'
	MAIN_DIR = ''
	TOKEN = ''
	APP_DESC = 'BlackMarket is a custom economical management bot by Dvlsh::Sftwr'
	PREFIX = '--'
	GAME = 'with your mother\'s clit :stuck_out_tongue:'
	WAL = 'wallet'
	BNK ='bank'
	LATENCY = '```py\nLatency : {0.latency}```'
	
	
	class BotAuthor:
		AUTHOR = 'Fluffykins Allmighty'
		DISCORD = "`5P4{3 |_0RD |V|07|-|3RF|_|{K3R#7797`"
		E_MAIL = "`DvlshSftwr@protonmail.com`"
	
	class EMJ:
		FOOD_EMOJI = [
			"cookie", 
			"pizza", 
			"hamburger", 
			"fries", 
			"pie", 
			"cake", 
			"cupcake", 
			"moon_cake", 
			"fish_cake", 
			"poultry_leg", 
			"cut_of_meat", 
			"waffle", 
			"pancakes", 
			"ramen", 
			"icecream", 
			"taco", 
			"burrito", 
			"rice_ball", 
			"sushi", 
			"falafel", 
			"sandwich", 
			"pretzel", 
			"ice_cream", 
			"oden", 
			"dango", 
			"coffee", 
			"tea", 
			"lolipop", 
			"candy", 
			"chocolate_bar", 
			"popcorn", 
			"doughnut", 
			"bubble_tea", 
			"beverage_box", 
			"sake", "beer", 
			"wine_glass", 
			"whisky", 
			"cocktail", 
			"curry"
		]
	
	class Field:
		STORE_NAMES = [
			"`Temporary Ability Boosting Items`",
			":syringe:\nTestosterone Shot\n${0}",
			":muscle:\nMuscle Shirt \n${0}",
			"<:drink_can:776774403404726282>\nCan Of Redbull\n${0}",
			":eyeglasses:\nGlasses \n${0}",
			"<:binoculars:776776363305861130>\nBinoculars\n${0}",
			":athletic_shoe:\nFresh Kicks\n${0}",
			"`Temporary Talent Boosting Items`'",
			"<:tablet2:776789955833233419>\nE-Cyclopedia\n${0}",
			"<:bluepotion:776510405153390623>\nSpecial Cologne\n${0}",
			"<:camo:776783595170824213>\nCamouflage Suit\n${0}",
			":levitate:\nSharp Suit\n${0}",
			":notepad_spiral:\nInformant Tip\n${0}",
			":notebook_with_decorative_cover:\nInstruction Manual\n${0}",
			":school_satchel:\nSurvivalist's Kit\n${0}",
			":medical_symbol:\nFirst Aid Kit\n${0}",
			"<:voice:776788298902274048>\nVoice Modifier\n${0}",
			":microscope:\nScience Kit\n${0}",
			":satellite:\nJammer\n${0}",
			"<:tablet:776787306816339968>\nDiagnostics Pad\n${0}",
			":goggles:\nSpy Goggles\n${0}"
			]
		
		INVENTORY_NAMES = [
			"`Temporary Ability Boosting Items`",
			":syringe:\nTestosterone Shot\n{0}/5",
			":muscle:\nMuscle Shirt \n{0}/5",
			"<:drink_can:776774403404726282>\nCan Of Redbull\n{0}/5",
			":eyeglasses:\nGlasses \n{0}/5",
			"<:binoculars:776776363305861130>\nBinoculars\n${0}/5",
			":athletic_shoe:\nFresh Kicks\n{0}/5",
			"`Temporary Talent Boosting Items`'",
			"<:tablet2:776789955833233419>\nE-Cyclopedia\n${0}/15",
			"<:bluepotion:776510405153390623>\nSpecial Cologne\n{0}/15",
			"<:camo:776783595170824213>\nCamouflage Suit\n{0}/15",
			":levitate:\nSharp Suit\n{0}/15",
			":notepad_spiral:\nInformant Tip\n{0}/15",
			":notebook_with_decorative_cover:\nInstruction Manual\n{0}/15",
			":school_satchel:\nSurvivalist's Kit\n{0}/15",
			":medical_symbol:\nFirst Aid Kit\n{0}/15",
			"<:voice:776788298902274048>\nVoice Modifier\n{0}/15",
			":microscope:\nScience Kit\n{0}/15",
			":satellite:\nJammer\n{0}/15",
			"<:tablet:776787306816339968>\nDiagnostics Pad\n{0}/15",
			":goggles:\nSpy Goggles\n{0}"
			]
		
		STORE_VALUES = [
			"```css\nYou may have up to 5 of each```",
			"A steroid shot to give you that extra OOMPH!\n\n+1d #MIGHT    \n\noption : steroids",
			"Feel a little tougher with this bad-ass tank top!\n\n+1d #TOUGH    \n\noption : muscle-shirt",
			"Need a little boost to get you through the day?\n\n+1d #WILL     \n\noption : redbull",
			"Feel a little smarter with these snazzy specs!        \n\n\n+1d #INTEL      \n\noption : glasses",
			"Need a better look at the milf next door? PFFT. Sure, ok. Whatever you say...\n\n+1d #PERC      \n\noption : binoculars",
			"A fresh new set of sneakers! Better than...whatever you call those\n\n+1d #AGIL\n\noption : fresh-kicks",
			"```css\nYou may have up to 15 of each```",
			"A digital encyclopedia for all your 'on the go' informational needs\n\n\n\n\n\n\n+1 #ACAD\n\noption : e-cyclopedia",
			"That stinky crap Mark and Cass wear that apperently has some kind of charming quality to others...\nShit just gives me a fucking headache, I swear... -,..,-\"\n\n+1d #CHARM\n\noption : cologne",
			"My personal choice in attire for covert operations, very effective ^,..,^\n\n\n\n\n\n\n+1d #COVRT\n\noption : camouflage",
			"Wanna seem a little more profesh? This snazzy suit'll get you there.\n\n\n\n+1d #PROF\n\noption : sharp-suit",
			"Boy, do Ihave some juice for you...can't tell you who passed it on though. Client confidentiality, you know the drill.\n\n+1d #STRT\n\noption : info-tip",
			"What, you don't know how to drive that thing?! All good, homie, I gotchu. Peep this.\n\n\n+1d #VEHIC\noption : \ninstruction-manual",
			"Roughing it? I've go t just what you need, all the tools you need to make it through...if you're not a total dumbass, that is...\n\n+1d #SURV\n\noption : survival-kit",
			"Always good to have some med supplies on you, fights can get rough!\n\n\n\n+1d #MEDIC\n\noption : med-kit",
			"Sound a little more 'in command' with this little dohicky\n\n\n\n\n+1 #CMND\n\noption : voice-mod",
			"A little prtable kit for all your scientific needs...if you're smart enough to use it, that is\n\n+1d #SCINC\n\noption : science-kit",
			"A signal jammer. Built it myself. It...should work...I think. ^,..,^\"\n\n\n+1d #TECH\n\noption : jammer",
			"A diagnostics pad for system analytics.\n\n\n\n\n+1d #TECH\noption : \ndiagnotsic-pad",
			"Need to do some PI work? These suckers magnify, hide your eyes, and have optical display tech built in. Built em myself.\n\n+1d #INVS\n\noption : goggles"
			]
	
	
	class Prompt:
		HOE1 = '```css\nSometimes, shit just doesnt go your way. You decided "\Ehhh, I know my way arround a dick, why not use my sensational skills to earn some cash?\" Well, you made $120 for sucking some sweaty fat dudes knob! Gross...worse yet, on your way home, you get your ass kicked and lose the whole haul in the mugging! Fuckin A...```'
		HOE2 = '```css\nYou decided to go work the corner your mom used to and made $120 for a blowjob! Too bad you contracted syphilis. Antibiotics are expensive so youre left with ${} bucks. Bummer```'
		HOE3 = '```css\nHard up for cash, you decide to degrade yourself and sell your mouth. Unfortunately you fucking suck at oral and used too much teeth. You made ${} for you to stop and get your skilless mouth off their prick. Good job, loser.```'
		HOE4 = '```css\nWorking the night, you managed to make a good $100. Unfortunately, you got busted by an officer. Devious bitch lets you off, but only after forcing you to get her off and confiscating most of your earnings, leaving you with {} to show for your work. Twatting cunt! At least she was sexy...```'
		HOE5 = '```css\nYou worked as a slut at a bar and the guys loved your thicc thighs with stockings. You received ${ammount} from the men. AND THE WOMEN. Whos bad? {usr}s bad, baby!```'
		HOE6 = '```css\nYou tried to have sex with an officer cause you were horny, the officer liked it and had sex with you, the officer paid ${}. Skills~~```'
		HOE7 = '```css\nYou and your significant other decided to make some amateur furry porn. Well recieved, you earned ${}. Niiiice ```'
		HOE8 = '```css\nYou fell from the pole and embarrassed yourself. Pay {} to fix your leg.```'
		HOE9 = '```css\nYou took a banana up the ass whilst streaming and earned ${} through donations. Puttin in work, baby.```'
		HOE10 = '```css\nYou used your salacious oral skills to deepthroat a thicc cucumber on stream and earned ${} in donations. What a throat bulge that was! >;3```'
		HOE11 = ''
		HOE12 = ''
		
		MUG1 = "```css\nyou scared some rich old {0} into giving you their wallet and took home ${1}\nDick move man. But hey, phat paid, right. e,..,e```"
		MUG2 = "```css\nyou beat some fat {0} on a scooter with a riding crop and took ${1} off them for calling you a faget. Nice >;3.```"
		MUG3 = "```css\nyou shoved some drunk {0} in a dumpster and took ${1} for grabbing your ass. ```"
		MUG4 = "```css\nyou mugged someone but they gave you a rough time. You got $100, but gotta go buy some bandages...\nand maybe some candy...${} is your payout```"
		MUG5 = "```css\nou scared some stoner kids out of ${} and a bag of kush. Good job.```"
		MUG6 = "```css\nyou tried to mug someone and got your ass kicked and ${} thrown at you```"
		MUG = "```css\nyou tried to mug a cop and got arrested. Your fine is ${}```"
		MUG8 = "```css\nyou mugged a cop's son and got arrested. Your fine is ${}```"
		MUG9 = "```css\nyou tried to mug someone and got arrested. Your fine is ${}```"
		MUG10 = "```css\nyou tried to mug someone and got mugged. You lost ${}```"
		MUG11 = "```css\nyou tried to mug someone and got mugged. You lost ${}```"
		MUG12 = "```css\nyou tried to mug someone and got mugged. You loose ${}```"
		
	
	
	class F:
		JSON_FILE_1 = 'cog/Bank.json'
		JSON_FILE_2 = 'cog/Store.json'
		JSON_FILE_3 = 'cog/Inventory.json'
	
	
	class Login:
		LOGGED_IN = '\nClient         : Logged in as\nUSER           : {0}\nID             : {1} '
					 
		LOADING = 'Loading        : {0}'
		OPEN = '{0}    : open for business! ^,..,^'
	
	
	class Logout:
		INIT_SHUTDOWN = '```CSS\nShutdown process initiated!\nLogging out and shutting down now...\nexit : {0}```'
		END_SHUTDOWN = '\n{0} has meen shut down\nIt\'s been fun, have a nice day ^,..,^'
		INIT_RESET = '```CSS\nReset process initiated!\nLogging out and shutting down now...\nexit : {0}```'
	
	
	class ERR:
		ERR_STR = "```CSS\n{0}yooooou're NOT my FUCKING father! E,..,E\nFuck right off with that shit!\n I'm telling on you!```"
		WARN_STR = 'User : {0}\nID : {1}\n This user just tried to activate : {2}\nWith value : {3}\nOperation aborted, warning sent to dad'
	
	
	class URL:
		BOT_PORTAL = "https://discord.com/oauth2/authorize?client_id=767825670394871879&scope=bot"
		DEF_WALLET_IMG = 'https://image.freepik.com/free-photo/dirty-hands-homeless-poor-man-with-empty-wallet-modern-capitalism-society_140289-3.jpg'
		WALLET_IMG_1 = 'https://dayair.org/wp-content/uploads/2017/04/money-wallet.jpg'
		WALLET_IMG_2 = 'http://www.todayifoundout.com/wp-content/uploads/2017/10/wallet-full-of-money.png'
		WALLET_IMG_3 = 'https://www.star991.com/images/blog/old-wallet-with-useless-papers-picture-id139671232.jpg'
		WALLET_IMG_4 = 'https://www.catster.com/wp-content/uploads/2015/06/cash-cat-1.jpg'
		WALLET_IMG_5 = 'https://cdn.ebaumsworld.com/mediaFiles/picture/910655/80810319.jpg'
		WALLET_IMG_6 = 'http://brucemctague.com/wp-content/uploads/2014/08/money-stack-of.jpg'
		AUTHOR_GITHUB = 'https://github.com/DvlshSftwr'
		AUTHOR_ICON = 'https://avatars3.githubusercontent.com/u/71295247?s=400&u=591ad97be84b88ab9d59d47653d0dd6af6c60561&v=4'
		E = 'https://i.imgur.com/x3PSV9Y.jpg'
		F = 'https://img.pixers.pics/pho_wat(s3:700/FO/38/21/09/85/700_FO38210985_76f532408a9bb431aed242a945e56cc9.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/wall-murals-fire-alphabet-letter-f.jpg.jpg'
		COOKIE = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Femojis.wiki%2Femoji-pics%2Fwhatsapp%2Fcookie-whatsapp.png&f=1&nofb=1'
		BURGER = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Femojis.wiki%2Femoji-pics%2Ffacebook%2Fhamburger-facebook.png&f=1&nofb=1'
		FRIES = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Femojis.wiki%2Femoji-pics%2Ffacebook%2Ffrench-fries-facebook.png&f=1&nofb=1'
		TWINKIE_HOUSES = [
			'https://i.imgur.com/lkkAuOB.jpg',
			'https://i0.kym-cdn.com/photos/images/original/000/022/614/3JJN4VJA7USJQLD5WKCLFJBLC6LJFG5P.png'
			'https://i0.kym-cdn.com/photos/images/original/000/896/675/78e.jpg',
			'https://external-preview.redd.it/tj_19XlsUL8TUe2RFyWumq7dznJ3ZwNcaFwO0B84mJg.jpg?auto=webp&s=d786b8b0839e7b965bad3761e6d434f11bc9474c',
			'https://t04.deviantart.net/LbJTfltaaqNm5Hp0GuJZPuNXi1g=/fit-in/700x350/filters:fixed_height(100,100):origin()/pre11/dbf4/th/pre/f/2009/274/4/2/twinkie_house_by_nekoninja12.png',
			'https://64.media.tumblr.com/196fda28bb30dde26ebbddb0c089ecce/tumblr_p0luyz0CQr1vheqneo1_500.png' 
		]
	
	class COL:
		LIME = 0x40FF00
		VERMILION = 0xFF4D00
		EGG_PLANT = 0x390042
		GOLD = 0xFFD700
		FUCHA = 0xFF0040
	
	class CMD:
		BAL = 'atm'
		EXT = 'e'
		PING = 'ping='
		RST = 'r'
		HLP = 'h'
		SEND = 'send='
		SHOP = 'shop'
		INV = 'inventory'
		CHCK = 'check='
		USE = 'use='
		BUY = 'buy='
		TRAN = 'atm='
		USE = 'use='
		INV = 'inventory'
		RNG = 'rng='
		DAD = 'papi'
		PROS = 'hoe'
		WORK = 'work'
		MUG = 'mug'
		FGT = 'street-fight'
		E = 'E'
		F = 'F'
		FOOD = 'food='
		TWH = 'twinkie-house='
		MTL_BENDING = 'gat-bending'
def MY_ID():
	return ''

Const = Constants()
