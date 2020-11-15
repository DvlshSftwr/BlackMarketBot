import discord
import random

from discord.ext import commands
from Constants import *
from RandomNumberGenerator import RNG

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
		rand_num = random.randint(1, 7)
		habeeb_it = f"Habeeb it, {member.name}!"
		i_dont = f'{member} : \"I don\'t believe it!\"'
		img = discord.File(f"img/twinkie-house{rand_num}.png", "image.png")
		
		embed6.set_image(url = 'attachment://image.png')
		embed6.add_field(name=i_dont, value=habeeb_it, inline=False)
		embed6.set_footer(text=str(reason))
		
		await ctx.send(file = img, embed = embed6)
	
	
	@commands.command(name = Const.CMD.MTL_BENDING)
	async def metal_bending(self, ctx : commands.Context):
		"""Gat Bending Motherfucker"""
		
		embed11 = discord.Embed(title = "Gat Bending", description = "Aang is metal bending", color = Const.COL.VERMILION)
		embed11.set_image(url = 'https://media.discordapp.net/attachments/709438676647673948/776701867161419786/124520260_10223642640195657_2541179891297595795_o.png?width=478&height=478')
		
		await ctx.send(embed = embed11)
	
	
	@commands.command(name = 'amd-cpu-tutorial')
	async def amd_cpu_tutorial(self, ctx : commands.Context):
		"""how to modify an intel mobo to take an amd cpu"""
		
		stoopid_embed = discord.Embed(title = "HOW TO INSTALL AN AMD CPU INTO AN INTEL MOBO", description = "```css\nhow to modify an intel motherboard to take an amd cpu```", color = 0x9933FF)
		
		await ctx.send(embed = stoopid_embed)
		await ctx.send('https://unixism.xyz/share/amd_guide.mp4')
	
	
	@commands.command(name='rand=')
	async def rand_hex(self, ctx, base = 'dec', str_len = 2):
		"""generate random number strings"""
		
		result = RNG.generate(base, str_len)
    
		if base == 'hex':
			await ctx.send(f'```cpp\nYour numerical string is :\n0x{result.upper()}```')
	
		else:
			await ctx.send(f'```cpp\nYour numerical string is :\n{result}```')
	
	
	


def setup(client):
		client.add_cog(MemeFunk(client))
