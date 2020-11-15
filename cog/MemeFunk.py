import discord

from discord.ext import commands
from Constants import * 

class MemeFunk(commands.Cog):
	
	def __init__(self, client):
		self.client = client
	
	
	@commands.command(name = Const.CMD.E)
	async def deep_fried_E(self, ctx : commands.Context):
		"""E"""
		
		embed5 = discord.Embed(title = "E!", description = "E", color = Const.COL.FUCHA)
		embed5.set_image(url = Const.URL.E)
		embed5.set_footer(text = "...E...")
		
		await ctx.send(embed = embed5)
	
	
	@commands.command(name = Const.CMD.F)
	async def pay_your_respects(self, ctx : commands.Context):
		"""Pay your respects"""
		
		embed5 = discord.Embed(title = "Press F", description = "to pay your respects", color = Const.COL.FUCHA)
		embed5.set_image(url = Const.URL.F)
		
		await ctx.send(embed = embed5)
	
	
	@commands.command(name = Const.CMD.TWH, pass_context=True)
	async def twinkie_house(self, ctx : commands.Context, member: discord.Member, reason='no reason'):
		""" 'Twinkie House' someone"""
		
		embed6 = discord.Embed(title='Twinkie House!', description='itty bitty baby...itty bitty boat...', color=0xACFA58)
		rand_num = random.randint(0, 5)
		habeeb_it = f"Habeeb it, {member.name}!"
		i_dont = f'{member} : \"I don\'t believe it!\"'
		id = str(member.id)
		
		
		await ctx.send(f'<@{id}>')
		
		if rand_num == 5:
			embed_5.set_image(url = Const.URL.TWINKIE_HOUSES[5])
			embed_5.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		elif rand_num == 4:
			embed6.set_image(url = Const.URL.TWINKIE_HOUSES[4])
			embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		elif rand_num == 3:
			embed6.set_image(url = Const.URL.TWINKIE_HOUSES[3])
			embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		elif rand_num == 2:
			embed6.set_image(url= Const.URL.TWINKIE_HOUSES[2])
			embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		elif rand_num == 1:
			embed6.set_image(url = Const.URL.TWINKIE_HOUSES[1])
			embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		elif rand_num == 0:
			embed6.set_image(url = Const.URL.TWINKIE_HOUSES[0])
			embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		
		embed6.set_footer(text=str(reason))
		
		await set_bank_data(bank)
		
		await ctx.send(embed=embed6)
	
	
	@commands.command(name = Const.CMD.MTL_BENDING)
	async def metal_bending(self, ctx : commands.Context):
		"""Gat Bending Motherfucker"""
		
		embed11 = discord.Embed(title = "Gat Bending", description = "Aang is metal bending", color = Const.COL.VERMILION)
		embed11.set_image(url = 'https://media.discordapp.net/attachments/709438676647673948/776701867161419786/124520260_10223642640195657_2541179891297595795_o.png?width=478&height=478')
		
		await ctx.send(embed = embed11)


def setup(client):
		client.add_cog(MemeFunk(client))
