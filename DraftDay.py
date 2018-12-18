import discord
from discord.ext import commands
import asyncio
import json

class DraftDay:
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def cut(self, ctx, role: discord.Role, user: discord.Member):
		"""Removes a role."""
		
		role = discord.utils.get(ctx.message.server.roles, id=self.settings[ctx.message.server.id][role])
		await self.bot.remove_roles(user, role)
		await self.bot.say("Role removed.")
		
	@commands.command()
	async def list_role_ids(self, ctx):
		"""Lists role IDs."""
		
		data.discord.Embed()
		data.add_field(name = "Roles", value = len(server.roles))
		data.add_field(name = "IDs", value = str(server.roles.id))
		
		try:
			await self.bot.say(embed=data)
			#if the one above doesn't work, try this one:
			#await client.send_message(message.channel, embed=data) 
		except discord.HTTPException:
			await self.bot.say("'Embed Links' permission needed")
	
	@commands.command()
	async def move_role(self, ctx, role, position):
		"""Tools for manipulating the order of roles.
		
		Requires the manage roles permission."""
		server = ctx.message.server
		role = discord.utils.get(ctx.message.server.roles, id=self.settings[ctx.message.server.id][role])
		position = role.position(ctx.message.server.roles.position)
		
		await self.bot.move_role(server, role, position)
		await self.bot.say("Role positions updated.")

def setup(bot):
	bot.add_cog(DraftDay(bot))
