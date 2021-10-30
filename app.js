require('dotenv').config();

const { Client, Intents, Channel } = require('discord.js'); //import discord.js

const bot = new Client({ intents: [Intents.FLAGS.GUILD_MEMBERS] }); //create new client

bot.on('ready', () => {
    console.log(`Logged in as ${bot.user.tag}`);
    
});


bot.on('guildMemberAdd', member => {
    bot.channels.fetch('782228216554455070').then(channel => channel.send(`Hey <@${member.id}>, Merhba biik M3ana.`));
    
    member.roles.add("893976972890370048");

});

bot.login(process.env.CLIENT_TOKEN);