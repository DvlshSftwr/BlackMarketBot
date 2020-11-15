import discord
import random

from discord.ext import commands
from Constants import * 
from cog.DankBank import DankBank


class Crimealicious(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	
	@commands.command(name = Const.CMD.PROS)
	@commands.cooldown(1, 60 * 8, commands.BucketType.user)
	async def prostitiution(self, ctx : commands.Context):
		"""Prostitute yourself for some extra cash"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author.name
		bank = await DankBank.get_bank_data()
		ammount = random.randint(0, 75)
		win_or_lose = random.randint(0, 100)
		
		if ammount < 20:
			if ammount == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE1, color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			else:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE2.format(ammount), color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		elif ammount in range(20, 40):
			check = random.randint(0, 1)
			
			if check == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE3.format(ammount), color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			elif check == 1:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE4.format(ammount), color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		
		
		elif ammount in range(50, 75):
			check = random.randint(0, 5)
			
			if check == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE5.format(ammount), color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 1:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE6.format(ammount), color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 2:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE7.format(ammount), color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 3:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE8.format(ammount), color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
				
				bank[id_str]["wallet"] -= ammount
				return
			
			elif check == 4:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.HOE9.format(ammount), color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 5:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>' + Const.Prompt.format(ammount), color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		await DankBank.set_bank_data(bank)
	
	
	@commands.command(name = 'mug')
	#@commands.cooldown(1, 60 * random.randint(4, 6), commands.BucketType.user)
	async def mug_someone(self, ctx : commands.Context):
		"""Mug someone for some extra munnies...if you can get away with it"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author.name
		bank = await DankBank.get_bank_data()
		win_or_lose = random.randint(0, 100) # <-the win or lose rate
		fuckup = random.randint(0, 5)        # <-how bad they eat it or how well they do
		check = random.randint(1, 2)
		ammount = 0
		if win_or_lose < 30:
			if fuckup == 0:
				if check == 1:
					person = "lady"
				else:
					person = "dude"
				
				ammount = random.randint(250, 300) # <-how much you take home
				bank[id_str]["wallet"] += ammount  # <-where it gets stored
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG1.format(person, ammount), color = Const.COL.LIME)
			
			elif fuckup == 1:
				if check == 1:
					person = "bearded pignose cuntface"
				else:
					person = "bucktoothed shit-stached goof"
				
				ammount = random.randint(150, 200)
				bank[id_str]["wallet"] += ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG2.format(person, ammount), color = Const.COL.LIME)
			
			elif fuckup == 2:
				if check == 1:
					person = "girl"
				else:
					person = "guy"
				
				ammount = random.randint(100, 150)
				bank[id_str]["wallet"] += ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG3.format(person,ammount), color = Const.COL.LIME)
			
			elif fuckup == 3:
				ammount = random.randint(50, 100)
				bank[id_str]["wallet"] += ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG4.format(ammount), color = Const.COL.LIME)
			
			elif fuckup == 4:
				ammount = random.randint(25, 50)
				bank[id_str]["wallet"] += ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG5.format(ammount), color = Const.COL.LIME)
			
			elif fuckup == 5:
				ammount = random.randint(0, 25)
				bank[id_str]["wallet"] += ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG6.format(ammount), color = Const.COL.VERMILION)
				
				await ctx.send(f)
		
		else:
			if fuckup == 0:	
				bank[id_str]["bank"] -= ammount
				ammount = random.randint(150, 200) # <-how much you lose
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG7.format(ammount), color = Const.COL.FUCHA)
			
			elif fuckup == 1:
				ammount = random.randint(100, 150)
				bank[id_str]["bank"] -= ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG8.format(ammount), color = Const.COL.FUCHA)
			
			elif fuckup == 2:
				ammount = random.randint(80, 100)
				bank[id_str]["bank"] -= ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG9.format(ammount), color = Const.COL.FUCHA)
			
			elif fuckup == 3:
				ammount = random.randint(40, 80)
				bank[id_str]["wallet"] -= ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG10.format(ammount), color = Const.COL.VERMILION)
			
			elif fuckup == 4:
				ammount = random.randint(20, 40)
				bank[id_str]["wallet"] -= ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG11.format(ammount), color = Const.COL.VERMILION)
			
			elif fuckup == 5:
				ammount = random.randint(0, 20)
				bank[id_str]["wallet"] -= ammount
				embed15 = discord.Embed(title = "Mugging", description = Const.Prompt.MUG12.format(ammount), color = Const.COL.VERMILION)
		  
		await ctx.send(embed = embed15)
		await DankBank.set_bank_data(bank)
	
	
	@commands.command(name = 'street-fight')
	@commands.cooldown(1, 60 * random.randint(4, 6), commands.BucketType.user)
	async def street_fight(self, ctx : commands.Context):
		"""Mug someone for some extra munnies...if you can get away with it"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author.name
		bank = await DankBank.get_bank_data()
		win_or_lose = random.randint(0, 100) # <-the win or lose rate
		fuckup = random.randint(0, 5)        # <-how bad they eat it or how well they do
		
		
		if win_or_lose < 30:
			if fuckup == 0:
				ammount = random.randint(250, 300) # <-how much you take home
				bank[is_str]["wallet"] += ammount  # <-where it gets stored
			
			elif fuckup == 1:
				ammount = random.randint(150, 200)
				bank[is_str]["wallet"] += ammount
			
			elif fuckup == 2:
				ammount == random.randint(100, 150)
				bank[is_str]["wallet"] += ammount
			
			elif fuckup == 3:
				ammount == random.randint(50, 100)
				bank[is_str]["wallet"] += ammount
			
			elif fuckup == 4:
				ammount == random.randint(25, 50)
				bank[is_str]["wallet"] += ammount
			
			elif fuckup == 5:
				ammount == random.randint(0, 25)
				bank[is_str]["wallet"] += ammount
		
		else:
			if fuckup == 0:
				ammount = random.randint(150, 200) # <-how much you lose
				bank[is_str]["bank"] -= ammount  
			
			elif fuckup == 1:
				ammount = random.randint(100, 150)
				bank[is_str]["bank"] -= ammount
			
			elif fuckup == 2:
				ammount == random.randint(80, 100)
				bank[is_str]["bank"] -= ammount
			
			elif fuckup == 3:
				ammount == random.randint(40, 80)
				bank[is_str]["wallet"] -= ammount
			
			elif fuckup == 4:
				ammount == random.randint(20, 40)
				bank[is_str]["wallet"] -= ammount
			
			elif fuckup == 5:
				ammount == random.randint(0, 20)
				bank[is_str]["wallet"] -= ammount
		
		
		

def setup(client):
	client.add_cog(Crimealicious(client))




