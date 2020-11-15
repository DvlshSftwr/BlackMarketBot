import discord
import random

from discord.ext import commands
from Constants import * 
from cog.DankBank import DankBank


class Crimealicious(commands.Cog):
	
	def __init__(self, client):
		self.client = client

	@commands.command(name = Const.CMD.PROS)
	@commands.cooldown(1, 14400, commands.BucketType.user)
	async def prostitiution(self, ctx : commands.Context):
		"""Prostitute yourself for some extra cash"""
		
		id_str = str(ctx.author.id)
		usr = ctx.author.name
		bank = await DankBank.get_bank_data()
		ammount = random.randint(5, 120)
		
		if ammount < 20:
			if ammount == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nSometimes, shit just doesnt go your way. You decided "\Ehhh, I know my way arround a dick, why not use my sensational skills to earn some cash?\" Well, you made $120 for sucking some sweaty fat dudes knob! Gross...worse yet, on your way home, you get your ass kicked and lose the whole haul in the mugging! Fuckin A...```', color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			else:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou decided to go work the corner your mom used to and made $120 for a blowjob! Too bad you contracted syphilis. Antibiotics are expensive so youre left with ${ammount} bucks. Bummer```', color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		elif ammount in range(20, 30):
			check = random.randint(0, 1)
			
			if check == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nHard up for cash, you decide to degrade yourself and sell your mouth. Unfortunately you fucking suck at oral and used too much teeth. You made ${ammount} for you to stop and get your skilless mouth off their prick. Good job, loser.```', color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			elif check == 1:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nWorking the night, you managed to make a good $100. Unfortunately, you got busted by an officer. Devious bitch lets you off, but only after forcing you to get her off and confiscating most of your earnings, leaving you with {ammount} to show for your work. Twatting cunt! At least she was sexy...```', color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		
		
		elif ammount in range(50, 120):
			check = random.randint(0, 5)
			
			if check == 0:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou worked as a slut at a bar and the guys loved your thicc thighs with stockings. You received ${ammount} from the men. AND THE WOMEN. Whos bad? {usr}s bad, baby!```', color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 1:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou tried to have sex with an officer cause you were horny, the officer liked it and had sex with you, the officer paid ${ammount}. Skills~~```', color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 2:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou and your significant other decided to make some amateur furry porn. Well recieved, you earned ${ammount}. Niiiice ```', color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 3:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou fell from the pole and embarrassed yourself. Pay {ammount} to fix your leg.```', color = Const.COL.FUCHA)
				
				await ctx.send(embed = embed9)
				
				bank[id_str]["wallet"] -= ammount
				return
			
			elif check == 4:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou took a banana up the ass whilst streaming and earned ${ammount} through donations. Puttin in work, baby.```', color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			elif check == 5:
				embed9 = discord.Embed(title = "Prostitution", description = f'<@{id_str}>```css\nYou used your salacious oral skills to deepthroat a thicc cucumber on stream and earned ${ammount} in donations. What a throat bulge that was! >;3```', color = Const.COL.LIME)
				
				await ctx.send(embed = embed9)
			
			bank[id_str]["wallet"] += ammount
		
		await DankBank.set_bank_data(bank)


def setup(client):
	client.add_cog(Crimealicious(client))


