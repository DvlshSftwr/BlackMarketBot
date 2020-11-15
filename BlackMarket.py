import Constants
import discord
import os
import sys
import subprocess
import random

from discord.ext import commands
from Constants import *
from cog.DankBank import DankBank
from cog.Store import Store


BlackMarket = commands.Bot(command_prefix = Const.PREFIX, description = Const.APP_DESC)


@BlackMarket.event
async def on_ready():
	cmd = BlackMarket.command
	name = BlackMarket.user
	id = str(BlackMarket.user.id)
	
	print(Const.Login.LOGGED_IN.format(name, id))
	print(Const.Login.LOADING.format(cmd))
	
	await BlackMarket.change_presence(status = discord.Status.online, activity = discord.Game(Const.GAME))
	
	print(Const.Login.OPEN.format(name.name))


@BlackMarket.event
async def on_message(message : discord.Message):
		usr = message.author
		bot_name = BlackMarket.user.name
		if usr.bot:
			print(f'{bot_name}    : Output Sent')
			return
			
		else:
			bank = await DankBank.get_bank_data()
			member = message.author
			msg_len = len(message.content)
			rand_num = random.randint(1, 4)
			munnies = msg_len * rand_num / 10
			cap = 150
			
			while munnies > cap:
				rand_num = random.randint(1, 5)
				munnies = int(msg_len * rand_num / 10)
			
			print(f"\n\nUSER           : {usr}\nID             : {usr.id}\nMessage Length : {msg_len}\nPayout         : {munnies}")
			
			if not message.content.startswith(Const.PREFIX):
				bank[str(member.id)]["bank"] += munnies
				print(f'{bot_name}    : payout deposited into bank account of : {usr.name}')
			
			else:
				print(f'{bot_name}    : "{message.content}" is a command, so payout not deposited')
			
			await DankBank.set_bank_data(bank)
			await BlackMarket.process_commands(message)



"""
                  ==============================================================================================================
                  ||     AA     PPPPPP  pppppp     CCCCCCC  OOOOOO  MM      MM MM      MM     AA     NN    NN DDDDDD   SSSSSS ||
                  ||    AAAA    PP   PP pp   pp   CC       OO    OO MMMM  MMMM MMMM  MMMM    AAAA    NNNN  NN DD   DD SS      ||
                  ||   AA  AA   PPPPPP  pppppp    CC       OO    OO MM MMMM MM MM MMMM MM   AA  AA   NN NN NN DD   DD  SSSSS  ||
                  ||  AAAAAAAA  PP      pp        CC       OO    OO MM  MM  MM MM  MM  MM  AAAAAAAA  NN  NNNN DD   DD      SS ||
                  || AA      AA PP      pp         CCCCCCC  OOOOOO  MM      MM MM      MM AA      AA NN    NN DDDDDD  SSSSSS  ||
                  ==============================================================================================================
"""


@BlackMarket.command(name = 'ld=')
async def ld_extntn(ctx : commands.Context, extension):
	"""Load an extention to the bot"""
	
	id_str = str(ctx.author.id)
	usr = ctx.author.name
	
	if id_str == MY_ID():
		BlackMarket.load_extension(f'cog.{extension}')
		print(f'{BlackMarket.user.name}    : loading extention\nStatus         : extension {extension} loaded')
		await ctx.send(f"```css\nLoading Extension : cog.{extension} ```")
	
	else:
		await ctx.send(Const.ERR.ERR_STR.format(usr))
		print(Const.ERR.WARN_STR.format(usr, id_str, ))



@BlackMarket.command(name = 'uld=')
async def ld_extntn(ctx : commands.Context, extension):
	"""Unload an extention from the bot"""
	
	id_str = str(ctx.author.id)
	usr = ctx.author.name
	
	if id_str == MY_ID():
		BlackMarket.unload_extension(f'cog.{extension}')
		print(f'{BlackMarket.user.name}    : unloading extention\nStatus         : extension {extension} unloaded')
		await ctx.send(f"```css\nUnloading Extension : cog.{extension}```")
	
	else:
		await ctx.send(Const.ERR.ERR_STR.format(usr))
		print(Const.ERR.WARN_STR.format(usr, id_str, ))


@BlackMarket.command(name = Const.CMD.EXT)
async def shutdown(ctx : commands.Context, arg = "0"):
	"""shuts down BlackMarket bot."""
	
	id = str(ctx.author.id)
	usr = ctx.author.name
	bot = BlackMarket.user.name
	
	if id == MY_ID():
		await ctx.send(Const.Logout.INIT_SHUTDOWN.format(arg))
		await ctx.bot.logout()
		print(Const.Logout.END_SHUTDOWN.format(bot))
	
	else:
		await ctx.send(Const.ERR.ERR_STR.format(usr))
		print(Const.ERR.WARNING.format(usr, id, Const.CMD.EXT, arg))
		
		if arg.isnumeric():
			sys.exit(arg)
		
		else:
			sys.exit(2)


@BlackMarket.command(name = Const.CMD.RST)
async def reset_bot(ctx : commands.Context, arg = 0):
	"""Resets BlackMarket"""
	
	id = str(ctx.author.id)
	usr = ctx. author.name
	bot = BlackMarket.user.name
	
	if id == MY_ID():
		await ctx.send(Const.Logout.INIT_RESET.format(arg))
		await ctx.bot.logout()
		print(f'\nResetting {bot} ?,..,?')
		
		subprocess.call([sys.executable, Const.BOT_EXEC])
	
	else:
		await ctx.send(ERR.ERR_STR.format(usr))
		print(ERR.WARNING.format(usr, id, Const.CMD.EXT, arg))



@BlackMarket.command(name = Const.CMD.PING)
async def latency_test(ctx : commands.Context, arg = '1'):
	"""test latency!"""
	
	id = ctx.author.id
	usr = ctx.author.name
	
	if str(id) == MY_ID():
		if arg.isnumeric():
			for num in range(0, int(arg)):
				await ctx.send(Const.LATENCY.format(BlackMarket))
				print(f"Latency : {BlackMarket.latency}")
	
	else:
		await ctx.send(Const.ERR.ERR_STR.format(usr))
		print(Const.ERR.WARNING.format(usr, id, Const.CMD.PING, None))


@BlackMarket.command(name = Const.CMD.DAD)
async def daddy(ctx : commands.Context):
	"""BlackMarket's creator"""
	 
	embed0 = discord.Embed(color = Const.COL.LIME)
	
	embed0.set_author(name = Const.BotAuthor.AUTHOR, url = Const.URL.AUTHOR_GITHUB, icon_url = Const.URL.AUTHOR_ICON)
	embed0.add_field(name = "Email", value = Const.BotAuthor.E_MAIL , inline = False)
	embed0.add_field(name = "Discord", value = Const.BotAuthor.DISCORD, inline = False)
	embed0.add_field(name = "Bot 0Auth2 Portal", value = Const.URL.BOT_PORTAL, inline = False)
	embed0.set_footer(text = "Have a bug to report? Want to contribute? Find me here!\nJust...don't bug me for no reason, you degens e,..,e")
	
	await ctx.send(embed = embed0)


# this function allows a user to send another server member a treat

@BlackMarket.command(name = Const.CMD.FOOD)
async def send_food(ctx : commands.Context, arg, member : discord.Member):
	"""Send someone food"""
	
	await Store.open_inventory(member)
	
	usr = ctx.author
	inv = await Store.get_inventory_data()
	items = inv[f'{member.id}']["food"].keys()
	index = 0
	
	for key in items:
		if arg == key:
			img_file = discord.File(f'img/{key}.png', filename = 'image.png')
			
			embed7 = discord.Embed(title = f'{usr.name} gave you a {key}!', color = Const.COL.GOLD)
			
			inv[f"{member.id}"]["food"][key] += 1
			
			embed7 = discord.Embed(title = f'{usr.name} gave you a {key.capitalize()}!', color = Const.COL.GOLD)
			
			embed7.add_field(name = f':{Const.EMJ.FOOD_EMOJI[index]}: = [{inv[f"{member.id}"]["food"][key]}]', value = f'```css\n Enjoy your munchies, you fatass! ^,..,^```', inline = False)
			embed7.set_thumbnail(url = f'attachment://image.png')
			break
		
		else:
			index += 1
		
	
	await Store.set_inventory_data(inv)
	await ctx.send(f'<@{member.id}>')
	await ctx.send(file = img_file, embed = embed7)


# this function pulls up the user's inventory

@BlackMarket.command(name = Const.CMD.INV)
async def view_inventory(ctx : commands.Context):
	"""View your inventory"""
	
	usr = ctx.author
	
	await Store.open_inventory(usr)
	
	inv = await Store.get_inventory_data()
	name1 = "ability"
	name2 = "talent"
	ability_keys = list(inv[str(usr.id)][name1].keys())
	talent_keys = list(inv[str(usr.id)][name2].keys())
	cnt = 0
	
	embed2 = discord.Embed(title = "Your Item Inventory!", description = "```css\nTo use an item, type : --use= [item option]```", color = Const.COL.EGG_PLANT)
	
	
	embed2.add_field(name = Const.Field.INVENTORY_NAMES[0], value = Const.Field.STORE_VALUES[0], inline = False)
	
	for number in range(1, 6):
		embed2.add_field(name = Const.Field.INVENTORY_NAMES[number].format(inv[str(usr.id)][name1][ability_keys[cnt]]), value = Const.Field.STORE_VALUES[number], inline = True)
		
		cnt += 1
	
	embed2.add_field(name = Const.Field.INVENTORY_NAMES[7], value = Const.Field.STORE_VALUES[7], inline = False)
	
	cnt = 0
	
	for number in range(8, 21):
		embed2.add_field(name = Const.Field.INVENTORY_NAMES[number].format(inv[str(usr.id)][name2][talent_keys[cnt]]), value = Const.Field.STORE_VALUES[number], inline = True)
		
		cnt += 1
	
	embed2.set_thumbnail(url = usr.avatar_url)
	
	await ctx.send(usr.mention)
	await ctx.send(embed = embed2)



"""
                         ===============================================================================
                         ||     AA     PPPPPP  pppppp     SSSSSSS TTTTTTTT    AA     RRRRRR  TTTTTTTT ||
                         ||    AAAA    PP   PP pp   pp   SS          TT      AAAA    RR   RR    TT    ||
                         ||   AA  AA   PPPPPP  pppppp     SSSSSS     TT     AA  AA   RRRRRR     TT    ||
                         ||  AAAAAAAA  PP      pp               S    TT    AAAAAAAA  RR  RR     TT    ||
                         || AA      AA PP      pp        SSSSSSS     TT   AA      AA RR   RR    TT    ||
                         ===============================================================================
"""


def main_function():
	
	for file_name in os.listdir("./cog"):
		if file_name.endswith(".py"):
			BlackMarket.load_extension(f'cog.{file_name[:-3]}')
	
	BlackMarket.run(Const.TOKEN)
	
	return 0


sys.exit(main_function())
