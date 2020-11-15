import discord
import json

from discord.ext import commands
from Constants import * 
from cog.DankBank import DankBank


class Store(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	
	@commands.command(name = Const.CMD.SHOP)
	async def shop(self, ctx : commands.Context, page = 1):
		"""view the store inventory!"""
		
		shop_inv = await self.get_store_data()
		embed2 = discord.Embed(title = "Welcome to the Black Market!", color = Const.COL.GOLD)
		name1 = "healing"
		name2 = "pharma"
		name3 = "ability"
		name4 = "talent"
		
		heal_keys = list(shop_inv[name1])
		drug_keys = list(shop_inv[name2])
		ability_keys = list(shop_inv[name3])
		talent_keys = list(shop_inv[name4])
		
		cnt = 0
		
		if int(page) == 1:
			img = discord.File("img/store.png", "image.png")
			
			embed2 = discord.Embed(title = "Welcome to Black Market Bazaar!", description = "```css\npage 1/3\nbuy option : bazaar [item option]```", color = Const.COL.GOLD)
			
			
			embed2.add_field(name = Const.Field.STORE_NAMES[0], value = Const.Field.STORE_VALUES[0], inline = False)
			
			for number in range(1, 6):
				embed2.add_field(name = Const.Field.STORE_NAMES[number].format(shop_inv[name3][ability_keys[cnt]]), value = Const.Field.STORE_VALUES[number], inline = True)
				
				cnt += 1
			
			embed2.add_field(name = Const.Field.STORE_NAMES[7], value = Const.Field.STORE_VALUES[7], inline = False)
			
			cnt = 0
			
			for number in range(8, 21):
				embed2.add_field(name = Const.Field.STORE_NAMES[number].format(shop_inv[name4][talent_keys[cnt]]), value = Const.Field.STORE_VALUES[number], inline = True)
				
				cnt += 1
			
			embed2.add_field(name = "`Special Items`", value = "```css\nYou may have 1 of these```", inline = False)
			
			embed2.add_field(name = f":moneybag:\nVanity Role Colour!\n$2500", value = "Good for 1 month and a color of members choice (OTHER than mod blue e,..,e)\nbuy option : --buy-color= [color choice] \ninstead of '--buy= bazaar [item option]'", inline = False)
			
			
		elif int(page) == 2:
			img = discord.File("img/face_bandage.png", "image.png")
			
			embed2 = discord.Embed(title = "Welcome to Black Market Natural Medicines!", description = "```css\npage 1/3\nCannot be used to heal drug induced damages\nbuy option : healing [item option]```", color = Const.COL.GOLD)
			
			embed2.add_field(name = f"Healing Tonic ${shop_inv[name1][heal_keys[0]]}", value = "Standard healing solution made of herbs mixed with tonic water..tastes pretty good!\n+1 HP restored\noption : tonic", inline = False)
			embed2.add_field(name = f"Healing Concauction ${shop_inv[name1][heal_keys[1]]}", value = "A more potent, chemically refined healing solution\n+3 HP restored\noption : potion", inline = False)
			embed2.add_field(name = f"Potent Healing Concauction ${shop_inv[name1][heal_keys[2]]}", value = "A highly concentrated, chemically refined healing solution\n+5 HP restored\noption : hipotion", inline = False)
			embed2.add_field(name = f"Grammy's Secret Elixer ${shop_inv[name1][heal_keys[3]]}", value = "A complex, potent chemical and herbal solution which fully heals the user and removes all stat debilitations\nDoes not work for drug induced debilitations\noption : elixer", inline = False)
			
		
		
		elif int(page) == 3:
			img = discord.File("img/whore_pills.png", "image.png")
			
			embed2 = discord.Embed(title = "Welcome to Black Market Pharmacy!", description = "```css\npage 3/5\nThese items give you a substancial boost, but have adverse side effects.\nUse them sparingly and wisely\nbuy option : pharma [item option]```", color = Const.COL.GOLD)
			
			embed2.add_field(name = f":pill: 0.3mg Epinephrine Pen ${shop_inv[name2][drug_keys[0]]}", value = "Autoinjector for artifical adrenaline\n+2d #MIGHT & #TOUGH\nHealth reduced to 1 for 24h post use if medical attention not sought\noption : epinephrine", inline = False)
			embed2.add_field(name = f":pill: 20mg Dextroamphetamine Caplet ${shop_inv[name2][drug_keys[1]]}", value = "A potent, addictive stimulant\n+2d #AGIL, #TOUGH & #PER\n-1d #AGIL, #TOUGH & #PER for 24h post use\noption : amphetamine", inline = False)
			embed2.add_field(name = f":pill: 10mg Diazepam Tablet ${shop_inv[name2][drug_keys[2]]}", value = "Benzodiazepine traquelizer for quelling your anxiety\n+2d #COV & #CHARM\n-1d #TOUGH & #CHARM for 24hr post use\noption : diazepam", inline = False)
			embed2.add_field(name = f":pill: 12mg Hydromorphone Caplet ${shop_inv[name2][drug_keys[3]]}", value = "A powerful opioid painkiller\n+2d #TOUGH\n-1d #CHARM while in use\n-1d #TOUGH & #MIGHT for 24hr post use\noption : hydromorphone", inline = False)
			embed2.add_field(name = f":pill: 100mg Modafinil Tablet ${shop_inv[name2][drug_keys[4]]}", value = "Highly effective neuroenhancer\n+2d #INT, #ACAD, #INV, #SCI, #TECH & #PER\n-1d to #CHARM during use\n-1d all abilities and talents for 24hr post use\noption : modafinil", inline = False)
			
		
		else:
			await ctx.send(f"```css\nHoly FUCK, there's only 3 fucking pages, how can you be so dumb? -,..,-\"```")
			return 0
		
		embed2.set_thumbnail(url = "attachment://image.png")
		
		await ctx.send(file = img, embed = embed2)
	
	
	@commands.command(name = Const.CMD.BUY)
	async def buy_item(self, ctx : commands.Context, arg1, arg2, arg3 = '1'):
		"""Buy items!"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author
		
		
		await self.open_inventory(ctx.author)
		funds = await DankBank.get_bank_data()
		store = await self.get_store_data()
		inventory = await self.get_inventory_data()
		img = discord.File(f"img/{arg2}.png", "image.png")
		
		if arg3.isnumeric() is False:
			await ctx.send(f'```css\n{arg3} isn\'t a fucking number, you slowtard! -,..,-\"```')
		
		elif arg1 in store:
			if arg2 in store[arg1]:
				if inventory[arg1][arg2] < 15:
					if funds[id_str]["wallet"] >= store[arg1][arg2] * int(arg3):
						price = store[arg1][arg2] * int(arg3)
						inventory[id_str][arg1][arg2] += int(arg3)
						funds[id_str]["wallet"] -= price	
						
						await ctx.send(f'```css\n[{arg3}] of [{arg2}]? That\'ll be [${price}], please and thank you.\nNow get the hell out! e,..,e```')
						
						await DankBank.set_bank_data(funds)
						await self.set_inventory_data(inventory)
					
					else:
						await ctx.send(f'```css\n[...Are you fucking serious {usr.name}?! This look like a fucking charity to you?!]\n[You dont have close to enough funds for that. Get your broke ass outa here!]\n[Come back when youre ready to buy something, asshole!] E,..,E```')
					
		elif arg1 == "bazaar":
			if arg2 in store["ability"]:
				if inventory[id_str]["ability"][arg2] < 5:
					if funds[id_str]["wallet"] >= store["ability"][arg2] * int(arg3):
						price = store["ability"][arg2] * int(arg3)
						inventory[id_str]["ability"][arg2] += int(arg3)
						funds[id_str]["wallet"] -= price
						
						embed8 = discord.Embed(title = f'{usr.name}\n[{arg3}] of [{arg2}]? That\'ll be [${price}], please and thank you.', description = '```css\nNow get the hell out, asshole! e,..,e', color = Const.COL.LIME)
						embed8.set_thumbnail(url = "attachment://image.png")
						
						await ctx.send(file = img, embed = embed8)
						
						await DankBank.set_bank_data(funds)
						await self.set_inventory_data(inventory)
					
					else:
						await ctx.send(f'```css\n[...Are you fucking serious {usr.name}?! This look like a fucking charity to you?!]\n[You dont have close to enough funds for that. Get your broke ass outa here!]\n[Come back when youre ready to buy something, asshole!] E,..,E```')
					
				else:
					await ctx.send(f'```css\n...You\'ve got a little too many of {arg2} already. Don\'t be a greedy lil bitch! e,..,e```')
			
			elif arg2 in store["talent"]:
				if inventory[id_str]["talent"][arg2] < 15:
					if funds[id_str]["wallet"] >= store["talent"][arg2] * int(arg3):
						price = store["talent"][arg2] * int(arg3)
						inventory[id_str]["talent"][arg2] += int(arg3)
						funds[id_str]["wallet"] -= price
						
						embed8 = discord.Embed(title = f'{usr.name}\n[{arg3}] of [{arg2}]? That\'ll be [${price}], please and thank you.```', description = '```css\nNow get the hell out, you slowtard! e,..,e```', color = Const.COL.LIME)
						embed8.set_thumbnail(url = "attachment://image.png")
						
						await ctx.send(f"<@{id_str}>")
						await ctx.send(file = img, embed = embed8)
					
						await DankBank.set_bank_data(funds)
						await self.set_inventory_data(inventory)
				
					else:
						await ctx.send(f'```css\n[...Are you fucking serious {usr.name}?! This look like a fucking charity to you?!]\n[You dont have close to enough funds for that. Get your broke ass outa here!]\n[Come back when youre ready to buy something, asshole!] E,..,E```')
				else:
					await ctx.send(f'```css\n...You\'ve got a little too many of {arg2} already. Don\'t be a greedy lil bitch! e,..,e```')
			
			else:
				await ctx.send(f'```css\nGoddamn it, {usr}, there is no item called {arg2}, you shit! -,..,-\"```')
		
		else:
			await ctx.send(f'```css\nWe don\'t even have a catigory called {arg1}! e,..,0\"```')
	
	
	@commands.command(name = Const.CMD.USE)
	async def use_item(self, ctx : commands.Context, arg):
		"""use an item!"""
		
		await self.open_inventory(ctx.author)
		id_str = str(ctx.author.id)
		usr = ctx.author
		inv = await self.get_inventory_data()
		boost = {
			"ability" : {
				"steroids": "[#MIGHT]",
				"muscle-shirt": "[#TOUGH]",
				"redbull": "[#WILL]",
				"glasses": "[#INTEL]",
				"binoculars": "[#PERC]",
				"fresh-kicks": "[#AGIL]"
			},
			"talent" : {
				"e-cyclopedia": "[#ACAD]",
				"cologne": "[#CHARM]",
				"camouflage": "[#CVRT]",
				"sharp-suit": "[#PROF]",
				"info-tip": "[#STRT]",
				"instruction-manual": "[#VEHIC]",
				"survival-kit": "[#SURV]",
				"med-kit": "[#MEDIC]",
				"voice-mod": "[#CMND]",
				"science-kit": "[#SCINC]",
				"jammer" : "[#TECH]",
				"diagnostic-pad": "[#TECH]",
				"goggles": "[#INVS]"
			},
		}
		
		img = discord.File(f"img/{arg}.png", "image.png")
		
		if arg in inv[id_str]["healing"]:
			if inv[id_str]["healing"][arg] > 0:
				inv[id_str]["healing"][arg] -= 1
				await ctx.send(f'```css\n{usr.mantion} has used a {arg}!\nDon\'t you go and fuck up, now, ya knuckle dragging slowtard! ^,..,^```')
		
		elif arg in inv[id_str]["pharma"]:
			if inv[id_str]["pharma"][arg] > 0:
				inv[id_str]["pharma"][arg] -= 1
				await ctx.send(f'```css\n{usr.mention} has used a {arg}!\nMake it count, you fucking druggie loser! ^,..,^```')
		
		elif arg in inv[id_str]["food"]:
			if inv[id_str]["food"][arg] > 0:
				inv[id_str]["food"][arg] -= 1
				
				embed13 = discord.Embed(title =f'You have eaten a {arg}!', description = f'```css\nEnjoying your munchies, are you?\nYou fucking fatass... ^,..,^````', color = Const.COL.VERMILION)
				embed13.set_thumbnail(url = "attachment://image.png")
				
				
				await ctx.send(f'{usr.mention}')
				await ctx.send(file = img, embed = embed13)
		
		elif arg in inv[id_str]["ability"]:
			if inv[id_str]["ability"][arg] > 0:
				inv[id_str]["ability"][arg] -= 1
				
				embed13 = discord.Embed(title =f'You have used a {arg}!', description = f'```css\nDon\'t you go and fuck up, now, ya knuckle dragging mouth breather! ^,..,^\n[+1d] added to {boost["ability"][arg]}```', color = Const.COL.VERMILION)
				embed13.set_thumbnail(url = "attachment://image.png")
				
				
				await ctx.send(f'{usr.mention}')
				await ctx.send(file = img, embed = embed13)
		
		elif arg in inv[id_str]["talent"]:
			if inv[id_str]["talent"][arg] > 0:
				inv[id_str]["talent"][arg] -= 1
				
				embed13 = discord.Embed(title =f'You have used a {arg}!', description = f'```css\nDon\'t you go and fuck up, now, ya knuckle dragging slowtard! ^,..,^\n[+1d] added to {boost["talent"][arg]}```', color = Const.COL.VERMILION)
				embed13.set_thumbnail(url = "attachment://image.png")
				
				
				await ctx.send(f'{usr.mention}')
				await ctx.send(file = img, embed = embed13)
		
		
		else:
			await ctx.send(f'```css\n{usr} has used a {arg}!\nYou don\'t even have that in your damn inventory, you raging slowtard! e,..,e```')
	
		await self.set_inventory_data(inv)
	
	
	@classmethod
	async def open_inventory(self, usr):
		id_num = f"{usr.id}"
		usrs = await get_inventory_data()
		
		if id_num in usrs:
			return False
		
		else:
			inventory = self.get_inventory_data()
		
		usrs.update({id_num : inventory["default"]})
		
		await self.set_inventory_data(usrs)
		
		return True
	
	
	@classmethod
	async def get_inventory_data(self):
		with open(Const.F.JSON_FILE_3, 'r') as ifile:
			usrs = json.load(ifile)
		
		return usrs
	
	
	@classmethod
	async def set_inventory_data(self, usrs):
		with open(Const.F.JSON_FILE_3, 'w') as ofile:
			json.dump(usrs, ofile)
	
	
	@classmethod
	async def get_store_data(self):
		with open(Const.F.JSON_FILE_2, 'r') as ifile:
			usrs = json.load(ifile)
		
		return usrs
	
	
	@classmethod
	async def set_store_data(self, usrs):
		with open(Const.F.JSON_FILE_2, 'w') as ofile:
			json.dump(usrs, ofile)


def setup(client):
	client.add_cog(Store(client))


