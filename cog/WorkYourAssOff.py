import discord
import random

from discord.ext import commands
from Constants import * 
from cog.DankBank import DankBank


class WorkYourAssOff(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	@commands.command(name = Const.CMD.WORK)
	@commands.cooldown(1, 60 * 24, commands.BucketType.user)
	async def go_to_work(self, ctx : commands.Context):
		"""Do some honest work for some honest pay"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author
		bank = await DankBank.get_bank_data()
		ammount = random.randint(5, 25)
		fuckup = random.randint(1, 2) 
		pay = ammount * 8
		option = random.randint(1, 2)
		
		if option == 1:
			if fuckup == 2:
				payment = pay * fuckup
			
				embed10 = discord.Embed(title = "Go To Work: Warehouse", description = f'What. The. FUCK. {usr.mention}!?! WHAT DID I TELL YOU ABOUT FUCKING AROUND ON THE FORKLIFTS?! You\'re so fucking lucky, _so_ lucky no one was killed in that fucking accident! I\'m gonna need {payment} from you asap for the fucking damages. Holy shit, you slowtard, what where you thinking?! E,..,E\nUmbra', color = Const.COL.FUCHA)
				
				await ctx.send(f'```css\n${payment} has been deducted from your bank```')
				await ctx.send(embed = embed10)
				
				bank[id_str]["bank"] -= payment
				await DankBank.set_bank_data(bank)
				
				return
		
			elif fuckup == 1:
				if ammount in range(5, 10):
					embed10 = discord.Embed(title = "Go To Work: Warehouse", description = f'Fucking hell, {usr.mention}, I\'m trying to run a business here, not a circus. Forklift racing is against protocol for a reason, it\'s a violation of workplace safety. Just because we\'re schoolmates doesn\'t make you exempt. I\'m gonna have to dock ${(20 * 6) - pay} off your pay, both for the violation and wasting forklift fuel. Don\'t be a fucking idiot next shift! -,..,-\nUmbra', color = Const.COL.VERMILION)
					
					await ctx.send(f'```css\n${pay} has been deposited into your bank```')
					await ctx.send(embed = embed10)
			
				elif ammount in range(11, 15):
					embed10 = discord.Embed(title = "Go To Work: Warehouse", description = f'Seriously {usr.mention}? You labeled _all_ of the boxes wrong today, is this some kind of joke to you?! Gods damn it man, ${20 * 6 - pay} docked from your pay for that little stunt. You\'re lucky we\'re schoolmates, you jackass. e,..,e\nUmbra', color = Const.COL.VERMILION)
				
					await ctx.send(f'```css\n${pay} has been deposited into your bank```')
					await ctx.send(embed = embed10)
				
				elif ammount in range(16, 20):
					embed10 = discord.Embed(title = "Go To Work: Warehouse", description = f'Nice work today, {usr.mention}, you made about ${pay} for the work you did. Thanks for the help.\nUmbra', color = Const.COL.LIME)
					
					await ctx.send(f'```css\n${pay} has been deposited into your bank```')
					await ctx.send(embed = embed10)
				
				elif ammount in range(21, 25):
					embed10 = discord.Embed(title = "Go To Work: Warehouse", description = f'\nKiller job with the sales today, {usr.mention}, you get some serious extra pay tacked on to your cheque for them smooth ass moves. ${pay} for ya. once again, great work!. ^,..,^\nUmbra', color = Const.COL.LIME)
				
					await ctx.send(f'```css\n${pay} has been deposited into your bank```')
					await ctx.send(embed = embed10)
		
		elif option == 2:
			if fuckup == 2:
				payment = round(pay * fuckup / 2)
			
				embed10 = discord.Embed(title = "Go To Work: Nail Salon", description = f'<@{id_str}>\nYou got hired at a nail salon! The fumes made you high though and you broke their aquarium when you tripped, instead of suing you decide to get a Mani/Pedi. You want da cryto-gel? You tipped ${payment / 2} in your high state.\nRisa', color = Const.COL.FUCHA)
			
				await ctx.send(f'```css\n${payment} has been deducted from your bank```')
				await ctx.send(embed = embed10)
			
				bank[id_str]["bank"] -= payment
				await DankBank.set_bank_data(bank)
				
				return
			
			elif fuckup == 1:
				tip = random.randint(20, 40)
			
				embed10 = discord.Embed(title = "Go To Work: Nail Salon", description = f'<@{id_str}>\nYou got hired at a nail salon! You gave some clearly methed out old bag a pedicure, man those feet where pure nast and smelled like two month expired curd-milk, but you somehow turned those horrors from hell into "Les Pieds D\'un Mannequin" and got ${pay} plus a {tip} tip! Killer job bish!\nUmbra', color = Const.COL.LIME)
			
				pay += tip
			
				await ctx.send(f'```css\n${pay} has been despositied to your bank```')
				await ctx.send(embed = embed10)
		
		bank[id_str]["bank"] += pay
		await DankBank.set_bank_data(bank)

def setup(client):
	client.add_cog(WorkYourAssOff(client))
