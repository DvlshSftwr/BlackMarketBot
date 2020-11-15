import discord
import random
import json

from discord.ext import commands
from Constants import *
from math import ceil

class DankBank(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	
	@commands.command(name = Const.CMD.BAL)
	async def check_balance(self, ctx : commands.Context, colour = Const.COL.LIME):
		"""Check your funds!"""
		
		id_num = f"{ctx.author.id}"
		usr = ctx.author
		MM = "<:money_mouth_master:776800199287767050>"
		MW = "<:winged_money:776800201091579906>"
		MB = "<:money_bag:776800201309552670>"
		
		await self.open_account(usr)
		
		usrs = await self.get_bank_data()
		footer_text = ""
		funds1 = int(usrs[id_num]["bank"])
		funds2 = int(usrs[id_num]["wallet"])
		wallet_img = Const.URL.DEF_WALLET_IMG
		
		
		if funds1 >= 1000000:
			footer_text = f'...{usr.mention}, are you a fucking Rothschild? e,..,0'
			wallet_img = Const.URL.WALLET_IMG_6
		
		elif funds1 >= 100000:
			footer_text = 'Filthy. Ass. Stinking. RRRRICH BICH O,..,O'
			wallet_img = Const.URL.WALLET_IMG_5
		
		elif funds1 >= 10000:
			footer_text = f'{usr.mention}\'s GOT MAD PAPEEEER...or...coins...or something ^,..,^\"'
			wallet_img = Const.URL.WALLET_IMG_4
		
		elif funds1 >= 1000:
			footer_text = f'ROLLIN HARD o,..,<'
			wallet_img = Const.URL.WALLET_IMG_3
		
		elif funds1 >= 500:
			footer_text = f'500+ bones, get at {usr.mention}! >,..,>'
			wallet_img = Const.URL.WALLET_IMG_2
		
		elif funds1 > 0:
			footer_text = f':Munnies in da BAAANK! ^,..,^'
			wallet_img = Const.URL.WALLET_IMG_1
		
		elif funds1 <= 0:
			footer_text = 'Broke ass nigga x,..,x'
		
		embed1 = discord.Embed(title = f'{MM}{MM}{MM}Dank Bank ATM{MM}{MM}{MM}', description = f'Your Account Information : ', color = colour)
		
		embed1.add_field(name = "Client Name", value = f"<@{id_num}>", inline = False)
		embed1.add_field(name = f"{MW}Wallet Funds{MW}", value = "$" + str(ceil(funds2)), inline = True)
		embed1.add_field(name = f"{MB}Bank Balance{MB}" , value = "$" + str(ceil(funds1)), inline = True)
		embed1.set_image(url = wallet_img)
		embed1.set_thumbnail(url = ctx.author.avatar_url)
		embed1.set_footer(text = f"Status : {footer_text}")
		
		await ctx.send(embed = embed1)
	
	
	@commands.command(name = Const.CMD.SEND)
	async def send_funds(self, ctx : commands.Context, arg, member : discord.Member):
		"""send funds to a person!"""
		
		await self.open_account(member)
		
		id_str = f"{ctx.author.id}"
		usr = ctx.author.name
		usrs = await self.get_bank_data()
		
		if id_str != MY_ID():
			await ctx.send(Const.ERR.ERR_STR.format(usr))
		
		else:
			if arg == "--random":
				funds = random.randint(50, 500)
			
			elif arg.isnumeric() is True:
				funds = int(arg)
			
			else:
				await ctx.send(f'```css\nHOLY FUCK, are you fucking retarded?! e,..,e\n\"{arg}\" is NOT a fucking number, you fucking mouth breather! -,..,-```')
			
			usrs[str(member.id)]["bank"] += funds
			await self.set_bank_data(usrs)
			await ctx.send(f"<@{member.id}> ```py\n{usr} just deposited [{funds}] into your account!\n...Lucky cunt E,..,E```")
	
	
	@commands.command(name = Const.CMD.TRAN)
	async def transfer_funds(self, ctx : commands.Context, arg1 = '0', arg2 = "bank"):
		"""transfer your funds between your bank and wallet! """
		
		id_str = str(ctx.author.id)
		usr = ctx.author.name 
		bank = dict(await self.get_bank_data())
		
		if arg1.isnumeric() is True:
			if bank[id_str][arg2] >= 0:
				if arg2 == "bank":
					if int(arg1) <= bank[id_str]["wallet"]:
						colour = Const.COL.LIME
						bank[id_str][arg2] += int(arg1)
						bank[id_str]["wallet"] -= int(arg1)
				
				elif arg2 == "wallet":
					colour = Const.COL.FUCHA
					
					if int(arg1) <= bank[id_str]["bank"]:
						bank[id_str][arg2] += int(arg1)
						bank[id_str]["bank"] -= int(arg1)
				
				else:
					await ctx.send(f'```css\n{usr}, you have a wallet, and a fucking bank account. Nothing else. Is it that hard to remember?! e,..,e```')
				
				
				await self.set_bank_data(bank)
				await self.check_balance(ctx, colour)
			
			else:
				await ctx.send(f'```css\n{usr}, you have no fucking funds... e,..,e```')
		
		else:
			ctx.send(f'```css\nOh my fucking...[NUMBERS. MONEY IS REPRESENTED BY NUMBERS YOU FUCKING DILL HOLE] e,..,0\nSiva, take me please...```')
	
	
	@classmethod
	async def open_account(self, usr):
		id_num = f"{usr.id}"
		usrs = await self.get_bank_data()
		
		
		if id_num in usrs:
			return False
		
		else:
			usrs.update({id_num : { "wallet" : 0, "bank" : 0}})
		
		await self.set_bank_data(usrs)
		
		return True
	
	
	@classmethod
	async def get_bank_data(self):
		with open(Const.F.JSON_FILE_1, 'r') as ifile:
			usrs = json.load(ifile)
		
		return usrs
	
	
	@classmethod
	async def set_bank_data(self, usrs):
		with open(Const.F.JSON_FILE_1, 'w') as ofile:
			json.dump(usrs, ofile)



def setup(client):
	client.add_cog(DankBank(client))
