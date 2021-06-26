import discord
import os
import random
from discord.ext import commands
import pandas as pd

global randnum

global correctanswer

global action 

global accuracy

global player_health

global game_in_progress

global row_amount



client = commands.Bot(command_prefix = 's.')

questions = {
            "question":['1+1','2+2','3+3','4+4','5+5','6+6'], 
            "answer":['2','4','6','8','10','12']}


global kb
kb = pd.DataFrame(questions)

@client.event
async def on_ready():
  global game_in_progress
  global kb
  game_in_progress = 0
  kb = pd.read_json("./kb.json",orient='index')
  print('The Bot is Online.')

@client.command()
async def start(ctx):
  global player_health
  global enemy_health
  global game_in_progress
  game_in_progress = 1
  player_health = 10
  enemy_health = 10
  await ctx.send('You have started a game of **Studémon**\nWould you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
 
@client.command()
async def punch(ctx):
  global row_amount
  global kb
  row_amount = (len(kb.index)) - 1
  global action 
  if game_in_progress == 1:
    action = 'punch'
    randnum = random.randrange(0, row_amount)
    await ctx.send(f'{kb.loc[:,"question"][randnum]}\nType **s.answer** with your answer to answer the question')
    global correctanswer
    correctanswer = kb.loc[:,"answer"][randnum]
  else:
    await ctx.send('**There is no game in progress!**')

@client.command()
async def kick(ctx):
  global kb
  global row_amount
  row_amount = (len(kb.index)) - 1
  global action 
  if game_in_progress == 1:
    action = 'kick'
    randnum = random.randrange(0, row_amount)
    await ctx.send(f'{kb.loc[:,"question"][randnum]}\nType **s.answer** with your answer to answer the question')
    global correctanswer
    correctanswer = kb.loc[:,"answer"][randnum]
  else:
    await ctx.send('**There is no game in progress!**')

@client.command()
async def heal(ctx):
  global kb
  global row_amount
  row_amount = (len(kb.index)) - 1
  global action
  if game_in_progress == 1: 
    if player_health < 10:
      action = 'heal'
      randnum = random.randrange(0, row_amount)
      await ctx.send(f'{kb.loc[:,"question"][randnum]}\nType **s.answer** with your answer to answer the question')
      global correctanswer
      correctanswer = kb.loc[:,"answer"][randnum]
    else: 
      await ctx.send('**You are at full health!**')
  else:
    await ctx.send('**There is no game in progress!**')

@client.command()
async def run(ctx):
  global game_in_progress
  if game_in_progress == 1:
    game_in_progress = 0
    await ctx.send('**You have ended the game!**')
  else:
    await ctx.send('**There is no game in progress!**')

def playerbar():
  global player_healthbar
  if player_health == 10:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square:'
  if player_health == 9:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square:'
  if player_health == 8:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square:'
  if player_health == 7:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square:'
  if player_health == 6:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 5:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 4:
      player_healthbar = ':green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 3:
      player_healthbar = ':green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 2:
      player_healthbar = ':green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 1:
      player_healthbar = ':green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if player_health == 0:
      player_healthbar = ':red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'

def enemybar():
  global enemy_healthbar
  if enemy_health == 10:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square:'
  if enemy_health == 9:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square:'
  if enemy_health == 8:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square:'
  if enemy_health == 7:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square:'
  if enemy_health == 6:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 5:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 4:
      enemy_healthbar = ':green_square: :green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 3:
      enemy_healthbar = ':green_square: :green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 2:
      enemy_healthbar = ':green_square: :green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 1:
      enemy_healthbar = ':green_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'
  if enemy_health == 0:
      enemy_healthbar = ':red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square: :red_square:'

@client.command()
async def answer(ctx, answer):
  global accuracy
  global player_health
  global enemy_health
  global game_in_progress
  global player_healthbar
  global enemy_healthbar
  if game_in_progress == 1:
    if answer == str(correctanswer):
      if action == 'punch':
        accuracy = random.randrange(1, 15)
        if accuracy != 15:
          enemy_health = enemy_health - 1
          playerbar()
          enemybar()
          await ctx.send('You dealt **1 damage** to the enemy!')
          await ctx.send(f'Your Health: {player_healthbar}\n\nEnemys Health: {enemy_healthbar}')
          await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
        else:
          await ctx.send('Your attack missed!')
          await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
      if action == 'kick':
        accuracy = random.randrange(1, 3)
        if accuracy == 1:
          enemy_health = enemy_health - 3
          playerbar()
          enemybar()
          await ctx.send('You dealt **3 damage** to the enemy!')
          await ctx.send(f'Your Health: {player_healthbar}\n\nEnemys Health: {enemy_healthbar}')
          await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
        else:
          await ctx.send('Your attack missed!')
          await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
      if action == 'heal':
          amount_healed = 1
          player_health = player_health + amount_healed
          playerbar()
          enemybar()
          await ctx.send(f'You healed **{amount_healed} Health Point!**')
          await ctx.send(f'Your Health: {player_healthbar}\n\nEnemys Health: {enemy_healthbar}')
          await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
    else:
      await ctx.send('That is incorrect!')
      player_health = player_health - 1
      playerbar()
      enemybar()
      await ctx.send(f'Your Health: {player_healthbar}\n\nEnemys Health: {enemy_healthbar}')
      await ctx.send('Would you like to **s.punch**, **s.kick**, **s.heal**, or **s.run**')
    if player_health <= 0:
      await ctx.send('**You lost... But dont get discouraged!**')
      game_in_progress = 0
    if enemy_health <= 0:
      await ctx.send('**You won!!!**')
      game_in_progress = 0
  else:
    await ctx.send('**There is no game in progress!**')

@client.command()
async def add(ctx, question, answer):
  global kb
  new_question = [question,answer]
  kb.loc[len(kb)] = new_question
  kb.to_json("./kb.json",orient='index')
  kb = pd.read_json("./kb.json",orient='index')
  
  await ctx.send('**Your question has been added!**')

@client.command()
async def list(ctx):
  global kb
  await ctx.send(kb)

@client.command()
async def remove(ctx, questionremoved):
  global kb
  kb = kb.drop([int(questionremoved)])
  kb.to_json("./kb.json",orient='index')
  kb = pd.read_json("./kb.json",orient='index')
  await ctx.send(f'Question Number **{questionremoved}** has been removed!')



client.run(os.getenv('TOKEN'))



