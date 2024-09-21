import logging
from random import randint
from typing import Optional, List

import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from Star_Utils import Cog

from .utils import add_footer, kawaiiembed, rstats_embed, send_embed

log = logging.getLogger("star.perform")


class Perform(Cog):
    """
    Perform different actions, like cuddle, poke, etc.
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=8423644625413, force_registration=True
        )
        default_global = {
            "feed": [
                "https://media1.tenor.com/images/93c4833dbcfd5be9401afbda220066ee/tenor.gif?itemid=11223742",
                "https://media1.tenor.com/images/33cfd292d4ef5e2dc533ff73a102c2e6/tenor.gif?itemid=12165913",
                "https://media1.tenor.com/images/72268391ffde3cd976a456ee2a033f46/tenor.gif?itemid=7589062",
                "https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977",
                "https://media1.tenor.com/images/187ff5bc3a5628b6906935232898c200/tenor.gif?itemid=9340097",
                "https://media1.tenor.com/images/15e7d9e1eb0aad2852fabda1210aee95/tenor.gif?itemid=12005286",
                "https://media1.tenor.com/images/d08d0825019c321f21293c35df8ed6a9/tenor.gif?itemid=9032297",
                "https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244",
                "https://media1.tenor.com/images/6bde17caa5743a22686e5f7b6e3e23b4/tenor.gif?itemid=13726430",
                "https://media1.tenor.com/images/fd3616d34ade61e1ac5cd0975c25a917/tenor.gif?itemid=13653906",
                "https://imgur.com/v7jsPrv",
            ],
            "spank": [
                "https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259",
                "https://media1.tenor.com/images/fa2472b2cca1e4a407b7772b329eafb4/tenor.gif?itemid=21468457",
                "https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904",
                "https://media1.tenor.com/images/86b5a47d495c0e8c5c3a085641a91aa4/tenor.gif?itemid=15964704",
                "https://media1.tenor.com/images/31d58e53313dc9bbd6435d824d2a5933/tenor.gif?itemid=11756736",
                "https://media1.tenor.com/images/97624764cb41414ad2c60d2028c19394/tenor.gif?itemid=16739345",
                "https://media1.tenor.com/images/f21c5c56e36ce0dfcdfe7c7993578c46/tenor.gif?itemid=21371415",
                "https://media1.tenor.com/images/58f5dcc2123fc73e8fb6b76f149441bc/tenor.gif?itemid=12086277",
                "https://media1.tenor.com/images/eafb13b900645ddf3b30cf9cc28e9f91/tenor.gif?itemid=4603671",
                "https://media1.tenor.com/images/be2bb9db1c8b8dc2194ec6a1b3d96b89/tenor.gif?itemid=18811244",
                "https://media.giphy.com/media/OoCuLoM6iEhYk/giphy.gif",
                "https://media.giphy.com/media/Qo3qovmbqaKT6/giphy.gif",
            ],
            "nut": [
                "https://c.tenor.com/2U9tTXuO_gUAAAAC/kick-anime.gif",
                "https://c.tenor.com/uHQL8xtAwaUAAAAd/kick-in-the-balls-anime.gif",
                "https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif",
                "https://c.tenor.com/_mW88MVAnrYAAAAC/heion-sedai-no-idatentachi-paula.gif",
                "https://c.tenor.com/CZT8alpjzzwAAAAd/ball-kick.gif",
                "https://c.tenor.com/KlvWYCEumXAAAAAd/kick-anime.gif",
                "https://c.tenor.com/9x-loeWpLyoAAAAC/talho-eureka-seven.gif",
                "https://c.tenor.com/6qtGbz6_894AAAAC/kick.gif",
                "https://c.tenor.com/NpMUvPFLwCEAAAAC/ow-balls-kick.gif",
                "https://c.tenor.com/pbyIf8fSIJsAAAAC/kick-balls-kick-in-the-balls.gif",
            ],
            "footer": True,
        }
        default_member = {
            "cuddle_s": 0,
            "poke_s": 0,
            "kiss_s": 0,
            "hug_s": 0,
            "slap_s": 0,
            "pat_s": 0,
            "tickle_s": 0,
            "smug_s": 0,
            "lick_s": 0,
            "cry": 0,
            "sleep": 0,
            "spank_s": 0,
            "pout": 0,
            "blush": 0,
            "feed_s": 0,
            "punch_s": 0,
            "confused": 0,
            "amazed": 0,
            "highfive_s": 0,
            "plead_s": 0,
            "clap": 0,
            "facepalm": 0,
            "facedesk": 0,
            "kill_s": 0,
            "love_s": 0,
            "hide": 0,
            "laugh": 0,
            "lurk": 0,
            "bite_s": 0,
            "dance": 0,
            "yeet_s": 0,
            "dodge": 0,
            "happy": 0,
            "cute": 0,
            "lonely": 0,
            "mad": 0,
            "nosebleed": 0,
            "protect_s": 0,
            "run": 0,
            "scared": 0,
            "shrug": 0,
            "scream": 0,
            "stare": 0,
            "wave_s": 0,
            "nut_s": 0,
        }
        default_target = {
            "cuddle_r": 0,
            "poke_r": 0,
            "kiss_r": 0,
            "hug_r": 0,
            "slap_r": 0,
            "pat_r": 0,
            "tickle_r": 0,
            "smug_r": 0,
            "lick_r": 0,
            "spank_r": 0,
            "feed_r": 0,
            "punch_r": 0,
            "highfive_r": 0,
            "plead_r": 0,
            "kill_r": 0,
            "love_r": 0,
            "bite_r": 0,
            "yeet_r": 0,
            "protect_r": 0,
            "wave_r": 0,
            "nut_r": 0,
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_member)
        self.config.init_custom("Target", 2)
        self.config.register_custom("Target", **default_target)
        self.cache = {}

        self.COMMANDS = [i.rstrip("_r") for i in default_target if i.endswith("_r")]

    def get_random_image(self, action: str) -> str:
        """Get a random image URL for the specified action."""
        images = getattr(self.config, action, [])
        if not images:
            return ""
        return images[randint(0, len(images) - 1)]

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def cuddle(self, ctx: commands.Context, *users: discord.Member):
        """
        Cuddle one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to cuddle.")

        description = f"**{ctx.author.mention}** cuddles "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("feed"))

        used = await self.config.user(ctx.author).cuddle_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).cuddle_r()
            await self.config.user(ctx.author).cuddle_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).cuddle_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "cuddles", target=target, word2="cuddled", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pokes")
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx: commands.Context, *users: discord.Member):
        """
        Poke one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to poke.")

        description = f"**{ctx.author.mention}** pokes "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("poke"))

        used = await self.config.user(ctx.author).poke_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).poke_r()
            await self.config.user(ctx.author).poke_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).poke_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "pokes", target=target, word2="poked", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="kiss")
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx: commands.Context, *users: discord.Member):
        """
        Kiss one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to kiss.")

        description = f"**{ctx.author.mention}** kisses "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("kiss"))

        used = await self.config.user(ctx.author).kiss_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).kiss_r()
            await self.config.user(ctx.author).kiss_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).kiss_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "kisses", target=target, word2="kissed", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hug")
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx: commands.Context, *users: discord.Member):
        """
        Hug one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to hug.")

        description = f"**{ctx.author.mention}** hugs "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("hug"))

        used = await self.config.user(ctx.author).hug_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).hug_r()
            await self.config.user(ctx.author).hug_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).hug_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "hugs", target=target, word2="hugged", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pat")
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx: commands.Context, *users: discord.Member):
        """
        Pat one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to pat.")

        description = f"**{ctx.author.mention}** pats "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("pat"))

        used = await self.config.user(ctx.author).pat_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).pat_r()
            await self.config.user(ctx.author).pat_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).pat_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "pats", target=target, word2="patted", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="tickle")
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx: commands.Context, *users: discord.Member):
        """
        Tickle one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to tickle.")

        description = f"**{ctx.author.mention}** tickles "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("tickle"))

        used = await self.config.user(ctx.author).tickle_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).tickle_r()
            await self.config.user(ctx.author).tickle_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).tickle_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "tickles", target=target, word2="tickled", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="smug")
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx: commands.Context):
        """
        Be smug towards someone!
        """
        embed = await kawaiiembed(self, ctx, "is acting so smug!", "smug")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).smug_s()
        await add_footer(self, ctx, embed, used, "smugs")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).smug_s.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lick")
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx: commands.Context, *users: discord.Member):
        """
        Lick one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to lick.")

        description = f"**{ctx.author.mention}** licks "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("lick"))

        used = await self.config.user(ctx.author).lick_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).lick_r()
            await self.config.user(ctx.author).lick_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).lick_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "licks", target=target, word2="licked", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="slap")
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx: commands.Context, *users: discord.Member):
        """
        Slap one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to slap.")

        description = f"**{ctx.author.mention}** slaps "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("slap"))

        used = await self.config.user(ctx.author).slap_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).slap_r()
            await self.config.user(ctx.author).slap_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).slap_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "slaps", target=target, word2="slapped", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cry")
    @commands.bot_has_permissions(embed_links=True)
    async def cry(self, ctx: commands.Context):
        """
        Start crying!
        """
        embed = await kawaiiembed(self, ctx, "is crying!", "cry")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).cry()
        await add_footer(self, ctx, embed, used, "cries")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).cry.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="sleep")
    @commands.bot_has_permissions(embed_links=True)
    async def sleep(self, ctx: commands.Context):
        """
        Act sleepy!
        """
        embed = await kawaiiembed(self, ctx, "is sleepy!", "sleepy")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).sleep()
        await add_footer(self, ctx, embed, used, "sleeps")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).sleep.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="spank")
    @commands.bot_has_permissions(embed_links=True)
    async def spank(self, ctx: commands.Context, *users: discord.Member):
        """
        Spank one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to spank.")

        description = f"**{ctx.author.mention}** spanks "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("spank"))

        used = await self.config.user(ctx.author).spank_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).spank_r()
            await self.config.user(ctx.author).spank_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).spank_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "spanks", target=target, word2="spanked", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="pout")
    @commands.bot_has_permissions(embed_links=True)
    async def pout(self, ctx: commands.Context):
        """
        Act pout!
        """
        embed = await kawaiiembed(self, ctx, "is acting pout!", "pout")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).pout()
        await add_footer(self, ctx, embed, used, "pouts")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).pout.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="blush")
    @commands.bot_has_permissions(embed_links=True)
    async def blush(self, ctx: commands.Context):
        """
        Act blush!
        """
        embed = await kawaiiembed(self, ctx, "is blushing!", "blush")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).blush()
        await add_footer(self, ctx, embed, used, "blushes")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).blush.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="feed")
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx: commands.Context, *users: discord.Member):
        """
        Feed one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to feed.")

        description = f"**{ctx.author.mention}** feeds "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("feed"))

        used = await self.config.user(ctx.author).feed_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).feed_r()
            await self.config.user(ctx.author).feed_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).feed_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "feeds", target=target, word2="fed", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="punch")
    @commands.bot_has_permissions(embed_links=True)
    async def punch(self, ctx: commands.Context, *users: discord.Member):
        """
        Punch one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to punch.")

        description = f"**{ctx.author.mention}** punches "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("punch"))

        used = await self.config.user(ctx.author).punch_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).punch_r()
            await self.config.user(ctx.author).punch_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).punch_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "punches", target=target, word2="punched", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="confuse", aliases=["confused"])
    async def confuse(self, ctx: commands.Context):
        """
        Act confused!
        """
        embed = await kawaiiembed(self, ctx, "is confused!", "confused")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).confused()
        await add_footer(self, ctx, embed, used, "confuses")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).confused.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="amazed", aliases=["amazing"])
    async def amazed(self, ctx: commands.Context):
        """
        Act amazed!
        """
        embed = await kawaiiembed(self, ctx, "is amazed!", "amazing")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).amazed()
        await add_footer(self, ctx, embed, used, "amazes")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).amazed.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def highfive(self, ctx: commands.Context, *users: discord.Member):
        """
        Highfive one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to highfive.")

        description = f"**{ctx.author.mention}** highfives "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("highfive"))

        used = await self.config.user(ctx.author).highfive_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).highfive_r()
            await self.config.user(ctx.author).highfive_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).highfive_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "highfives", target=target, word2="highfived", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="plead")
    async def plead(self, ctx: commands.Context, *users: discord.Member):
        """
        Plead to one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to plead to.")

        description = f"**{ctx.author.mention}** pleads to "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("plead"))

        used = await self.config.user(ctx.author).plead_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).plead_r()
            await self.config.user(ctx.author).plead_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).plead_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "pleads", target=target, word2="pleaded", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="clap")
    async def clap(self, ctx: commands.Context):
        """
        Clap for someone!
        """
        embed = await kawaiiembed(self, ctx, "is clapping!", "clap")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).clap()
        await add_footer(self, ctx, embed, used, "claps")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).clap.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="facepalm")
    async def facepalm(self, ctx: commands.Context):
        """
        Do a facepalm!
        """
        embed = await kawaiiembed(self, ctx, "is facepalming!", "facepalm")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).facepalm()
        await add_footer(self, ctx, embed, used, "facepalms")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).facepalm.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="headdesk", aliases=["facedesk"])
    async def facedesk(self, ctx: commands.Context):
        """
        Do a facedesk!
        """
        embed = await kawaiiembed(self, ctx, "is facedesking!", "facedesk")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).facedesk()
        await add_footer(self, ctx, embed, used, "facedesks")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).facedesk.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def kill(self, ctx: commands.Context, *users: discord.Member):
        """
        Kill one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to kill.")

        description = f"**{ctx.author.mention}** kills "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("kill"))

        used = await self.config.user(ctx.author).kill_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).kill_r()
            await self.config.user(ctx.author).kill_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).kill_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "kills", target=target, word2="killed", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def love(self, ctx: commands.Context, *users: discord.Member):
        """
        Love one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to love.")

        description = f"**{ctx.author.mention}** loves "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("love"))

        used = await self.config.user(ctx.author).love_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).love_r()
            await self.config.user(ctx.author).love_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).love_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "loves", target=target, word2="loved", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="hide")
    async def hide(self, ctx: commands.Context):
        """
        Hide yourself!
        """
        embed = await kawaiiembed(self, ctx, "is hiding!", "hide")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).hide()
        await add_footer(self, ctx, embed, used, "hides")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).hide.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="laugh")
    async def laugh(self, ctx: commands.Context):
        """
        Start laughing!
        """
        embed = await kawaiiembed(self, ctx, "is laughing!", "laugh")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).laugh()
        await add_footer(self, ctx, embed, used, "laughs")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).laugh.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="peek", aliases=["lurk"])
    async def lurk(self, ctx: commands.Context):
        """
        Start lurking!
        """
        embed = await kawaiiembed(self, ctx, "is lurking!", "peek")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).lurk()
        await add_footer(self, ctx, embed, used, "lurks")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).lurk.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def bite(self, ctx: commands.Context, *users: discord.Member):
        """
        Bite one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to bite.")

        description = f"**{ctx.author.mention}** bites "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("bite"))

        used = await self.config.user(ctx.author).bite_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).bite_r()
            await self.config.user(ctx.author).bite_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).bite_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "bites", target=target, word2="bit", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dance")
    async def dance(self, ctx: commands.Context):
        """
        Start dancing!
        """
        embed = await kawaiiembed(self, ctx, "is dancing", "dance")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).dance()
        await add_footer(self, ctx, embed, used, "dances")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).dance.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def yeet(self, ctx: commands.Context, *users: discord.Member):
        """
        Yeet one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to yeet.")

        description = f"**{ctx.author.mention}** yeets "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("yeet"))

        used = await self.config.user(ctx.author).yeet_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).yeet_r()
            await self.config.user(ctx.author).yeet_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).yeet_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "yeets", target=target, word2="yeeted", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="dodge")
    async def dodge(self, ctx: commands.Context):
        """
        Dodge something!
        """
        embed = await kawaiiembed(self, ctx, "is dodging!", "dodge")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).dodge()
        await add_footer(self, ctx, embed, used, "dodges")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).dodge.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="happy")
    async def happy(self, ctx: commands.Context):
        """
        Act happy!
        """
        embed = await kawaiiembed(self, ctx, "is happy!", "happy")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).happy()
        await add_footer(self, ctx, embed, used, "happiness")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).happy.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="cute")
    async def cute(self, ctx: commands.Context):
        """
        Act cute!
        """
        embed = await kawaiiembed(self, ctx, "is acting cute!", "cute")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).cute()
        await add_footer(self, ctx, embed, used, "cuteness")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).cute.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="lonely", aliases=["alone"])
    async def lonely(self, ctx: commands.Context):
        """
        Act lonely!
        """
        embed = await kawaiiembed(self, ctx, "is lonely!", "lonely")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).lonely()
        await add_footer(self, ctx, embed, used, "loneliness")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).lonely.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="mad", aliases=["angry"])
    async def mad(self, ctx: commands.Context):
        """
        Act angry!
        """
        embed = await kawaiiembed(self, ctx, "is angry!", "mad")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).mad()
        await add_footer(self, ctx, embed, used, "madness")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).mad.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="nosebleed")
    async def nosebleed(self, ctx: commands.Context):
        """
        Start bleeding from nose!
        """
        embed = await kawaiiembed(self, ctx, "'s nose is bleeding!", "nosebleed")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).nosebleed()
        await add_footer(self, ctx, embed, used, "nosebleeds")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).nosebleed.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def protect(self, ctx: commands.Context, *users: discord.Member):
        """
        Protect one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to protect.")

        description = f"**{ctx.author.mention}** protects "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("protect"))

        used = await self.config.user(ctx.author).protect_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).protect_r()
            await self.config.user(ctx.author).protect_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).protect_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "protects", target=target, word2="protected", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="run")
    async def run(self, ctx: commands.Context):
        """
        Start running!
        """
        embed = await kawaiiembed(self, ctx, "is running!", "run")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).run()
        await add_footer(self, ctx, embed, used, "runs")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).run.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scared")
    async def scared(self, ctx: commands.Context):
        """
        Act scared!
        """
        embed = await kawaiiembed(self, ctx, "is scared!", "scared")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).scared()
        await add_footer(self, ctx, embed, used, "scaredness")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).scared.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="shrug")
    async def shrug(self, ctx: commands.Context):
        """
        Start shrugging!
        """
        embed = await kawaiiembed(self, ctx, "is shrugging!", "shrug")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).shrug()
        await add_footer(self, ctx, embed, used, "shrugs")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).shrug.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="scream")
    async def scream(self, ctx: commands.Context):
        """
        Start screaming!
        """
        embed = await kawaiiembed(self, ctx, "is screaming!", "scream")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).scream()
        await add_footer(self, ctx, embed, used, "screams")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).scream.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="stare")
    async def stare(self, ctx: commands.Context):
        """
        Stare someone!
        """
        embed = await kawaiiembed(self, ctx, "is staring!", "stare")
        if not isinstance(embed, discord.Embed):
            return await ctx.send(embed)
        used = await self.config.user(ctx.author).stare()
        await add_footer(self, ctx, embed, used, "stares")
        await send_embed(self, ctx, embed)
        await self.config.user(ctx.author).stare.set(used + 1)

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command()
    async def wave(self, ctx: commands.Context, *users: discord.Member):
        """
        Wave to one or more users!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to wave to.")

        description = f"**{ctx.author.mention}** waves to "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("wave"))

        used = await self.config.user(ctx.author).wave_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).wave_r()
            await self.config.user(ctx.author).wave_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).wave_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "waves", target=target, word2="waved", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="nutkick", aliases=["kicknuts"])
    @commands.bot_has_permissions(embed_links=True)
    async def kicknuts(self, ctx: commands.Context, *users: discord.Member):
        """
        Kick one or more users in the nuts!
        """
        if not users:
            return await ctx.send("You need to mention at least one user to kick in the nuts.")

        description = f"**{ctx.author.mention}** kicks nuts of "
        description += ", ".join(f"**{user.mention}**" for user in users) + "!"

        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=self.get_random_image("nut"))

        used = await self.config.user(ctx.author).nut_s()

        for user in users:
            target = await self.config.custom("Target", ctx.author.id, user.id).nut_r()
            await self.config.user(ctx.author).nut_s.set(used + 1)
            await self.config.custom("Target", ctx.author.id, user.id).nut_r.set(target + 1)

        await add_footer(self, ctx, embed, used, "nutkicks", target=target, word2="nutkicked", user=users[0])
        await send_embed(self, ctx, embed, users[0])

    @commands.is_owner()
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def performapi(self, ctx: commands.Context):
        """
        Steps to get the API token needed for few commands.
        """
        embed = discord.Embed(
            title="How to set API for perform cog",
            description=(
                """
                1. Go to https://kawaii.red/\n
                2. Login using your discord account\n
                3. Click on dashboard and copy your token\n
                4. Use `[p]set api perform api_key <token>`,
            """
            ),
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["rstats", "pstats", "roleplaystats"])
    @commands.bot_has_permissions(embed_links=True)
    async def performstats(
        self, ctx: commands.Context, action: str, user: Optional[discord.User]
    ):
        """View your roleplay stats"""
        if user is None:
            user = ctx.author
        if action not in self.COMMANDS:
            return await ctx.send(
                f"The valid choices to view stats for are {', '.join(f'`{c}`' for c in self.COMMANDS)}"
            )
        embed = await rstats_embed(self, ctx, action, user)
        await ctx.send(embed=embed)

    @commands.group(aliases=["pset", "rset", "roleplayset"])
    @commands.is_owner()
    async def performset(self, ctx: commands.Context):
        """Settings for roleplay stats"""

    @performset.command()
    async def footer(self, ctx: commands.Context):
        """Toggle showing footers for roleplay stats"""
        value = await self.config.footer()
        await self.config.footer.set(not value)
        if value:
            await ctx.send("Footers will no longer be shown")
        else:
            await ctx.send("Footers will now be shown")

    def cog_unload(self):
        pass


async def setup(bot: Red):
    await bot.add_cog(Perform(bot))
