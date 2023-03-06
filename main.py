from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.bot import Bot
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext import DispatcherHandlerStop
from telegram.ext.filters import Filters
import random
import sqlite3
from time import time
from os import environ


print("""\n\n
███████ ██████   █████   ██████  ██   ██ ███████ ████████ ████████ ██        ██████   ██████ ████████ 
██      ██   ██ ██   ██ ██       ██   ██ ██         ██       ██    ██        ██   ██ ██    ██   ██    
███████ ██████  ███████ ██   ███ ███████ █████      ██       ██    ██        ██████  ██    ██   ██    
     ██ ██      ██   ██ ██    ██ ██   ██ ██         ██       ██    ██        ██   ██ ██    ██   ██    
███████ ██      ██   ██  ██████  ██   ██ ███████    ██       ██    ██        ██████   ██████    ██    
                                                                                                      
                                                                                                      """)


from sys import platform
if platform == "linux" or platform == "linux2":
	pass
elif platform == "darwin":
	pass
elif platform == "win32":
	import ansicon
	ansicon.load()


print("Created by \x1b[35mDei\x1b[m")
print("and \n\x1b[47m\x1b[30mpowered with\x1b[m \x1b[31mANSICON\x1b[m\x1b[m!")

BOTKEY = environ['TGBOTKEY']
DEBUGMODE = False


SWITCHDEBUG = input("Turn \x1b[41mDEBUG MODE\x1b[m ON? Y/N: ")
ANSWERDEBUG = SWITCHDEBUG.lower()
if ANSWERDEBUG == "y":
	DEBUGMODE = True
else:
	DEBUGMODE = False
	print("\x1b[47m\x1b[30mDEBUG MODE\x1b[m\x1b[m \x1b[32mOFF\x1b[m")

##### BOT VERSION
botversion = "2.7.1"
updateNotice = "кто не знает.... тот узнает!!"
##### BOT VERSION

updater = Updater(BOTKEY, use_context=True)
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: Updater launched with BOTKEY")

if DEBUGMODE == False:
	print(f"Bot is \x1b[32mrunning\x1b[m. Current version is \x1b[38;5;208m{botversion}\x1b[m")

else:
	print(f"Bot is \x1b[32mrunning\x1b[m. Current version is \x1b[38;5;208m{botversion}\x1b[m\n\x1b[41mDEBUG MODE\x1b[m \x1b[31mON\x1b[m")


### COMMANDS ###
### BLOCK    ###

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Посмотрим кто тут будет самой большой дылдой? Тогда начнем с /help")
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: start launched")


def help(update: Update, context: CallbackContext):
	update.message.reply_text(
		"/help — вы уже здеся\n/grow — получить свои крутые сантиметры....\n/height — узнать ваши крутые сантиметры....\n/ver — узнать версию бота и последнее обновление\n/top — узнать самых длинных\n/nickname — изменить свой никнейм в таблице на текущий\n/achievements — узнать свой текущий набор достижений")
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: help launched")


responseList = ["Отхлебнув зелья, Вы чувствуете изменения внутри себя.", "Воткнув в себя случайный шприц, Вы чувствуете изменения внутри себя.", "Съев странную вещь, Вы чувствуете изменения внутри себя.", "Обняв случайного Фокса, Вы чувствуете изменения внутри себя.", "Зайдя не в ту подворотню... Не важно. Вы чувствуете изменения внутри себя.", "Съев какую-то таблетку с пола, Вы чувствуете изменения внутри себя.", "Заснув не в том вместе, Вы чувствуете изменения внутри себя.", "Наступив не на ту Лего детальку, Вы чувствуете изменения внутри себя.", "Получив по голове молотком от случайной белой змеи, Вы проснулись с изменениями внутри себя.", "Упав в сток с урановыми отходами, Вы чувствуете изменения внутри себя.", "Проснувшись на операционном столе (без почки), Вы чувствуете изменения внутри себя.", "Окей, у меня закончились идеи, что еще сюда вставить.", ">running grow command; >result: difference in \'height\' value deteced; >calculating delta...", "Убежав от страшного лиса в подворотню, который что-то подсыпал вам в напиток, Вы чувствуете изменения внутри себя.", "Посмотря на странную фотографию, Вы чувствуете что-то неприятное внутри себя.", ]
responseListZero = ["Отхлебнув зелья, Вы не чувствуете изменения внутри себя.", "Воткнув в себя случайный шприц, Вы не чувствуете изменения внутри себя.", "Съев странную вещь, Вы не чувствуете изменения внутри себя.", "Обняв случайного Фокса, Вы не чувствуете изменения внутри себя.", "Зайдя не в ту подворотню... Не важно. Вы не чувствуете изменения внутри себя.", "Съев какую-то таблетку с пола, Вы чувствуете изменения внутри себя.", "Вы споткнулись и упали с лестницы. В общем больше ничего не произошло.", "Наступив не на ту Лего детальку, Вы не чувствуете изменения внутри себя.", "Получив по голове молотком от случайной белой змеи, Вы проснулись c шишкой, ауч.", "Упав в сток с урановыми отходами, Вы не чувствуете измнения внутри себя. Попробуйте избавиться от лучевой болезни...", "Проснувшись на операционном столе (без почки), Вы не чувствуете изменения внутри себя, обидно.", "Окей, у меня закончились идеи, что еще сюда вставить.", ">running grow command; >result: no difference in \'height\' value deteced; >go-to {randomZeroMessage}.", "Убежав от страшного лиса в подворотню, который что-то подсыпал вам в напиток, Вы выдыхаете с облегчением.", "Посмотря на странную фотографию, Вы выкидываете её в козину с мусором.",]
#i'll add this later
#specialMinus = "Вы потянулись вниз и почувствовали как стали ниже."
#specialPlus = "Вы потянулись вверх и почуствовали как стали выше."
secretlist = ["Змея не разговорчивое существо.", "Змея ползет, но плохо слышит.", "Если змея заговорит, то мир затихнет.", "Подсказка произносится словами.", "Лишь знающий, услышит змею в кустах.", "Вилкам змей свойственно шуметь.", "Один раз услышав, хочется бежать."]
secretlist2 = ["Буква с которой начинается слово шляпа на английском?", "Как можно сказать \"Я\" по-английски?", "Какую английскую букву повторяют змеи в тексте?"]
def grow(update: Update, context: CallbackContext):
	
	# ratelimit so people would only be able to use this bot once every 6 hours
	count = context.user_data.get("usageCount", 0)
	restrict_since = context.user_data.get("restrictSince", 0)
	waitTimes = context.user_data.get("waitCalled", 0)

	if restrict_since:
		if (time() - restrict_since) >= 60*360: # 6 hours 
			del context.user_data["usageCount"]
			del context.user_data["restrictSince"]
			del context.user_data["waitCalled"]
			print("user unrestricted")
		else:
			match waitTimes:
				# a tiny match-case that provides a ton of responses in case if somebody calls the command again and again. Might get deleted in the future due to TG's ratelimiting
				case 1:
					update.effective_message.reply_text("Тебе нужно подождать 6 часов!")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 2:
					update.effective_message.reply_text("Пожалуйста подождите 6 часов.")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 3:
					update.effective_message.reply_text("Повторяю, пожалуйста, подождите 6 часов.")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 4:
					update.effective_message.reply_text("Прошу... Подождите 6 часов...")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 5:
					update.effective_message.reply_text("Просто перестань, пожалуйста, хватит, подожди.")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 6:
					update.effective_message.reply_text("Оставь меня в покое!")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 7:
					update.effective_message.reply_text("*кидает блокнот с карандашем в воздух, нервно вздыхает и уходит*")
					context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 8:
					if update.effective_user.id  == 393522324:
						connection = sqlite3.connect('bot.db')
						cursor = connection.execute("SELECT * FROM secret;")
						results = cursor.fetchall()
						temp = results[0][0]
						if temp == 0:
							update.effective_message.reply_text("..?")
							context.user_data["waitCalled"] = waitTimes + 2 
					else:
						update.effective_message.reply_text("...")
						context.user_data["waitCalled"] = waitTimes + 1
					raise DispatcherHandlerStop
				case 9:
					raise DispatcherHandlerStop
				case 10:
					# a tiny easter egg if a certain user does /grow 9 times
					update.effective_message.reply_text("Соединение прервано. Прости меня за то, что я тебя прерываю, Никита. Если ты еще не забыл, что тебя так зовут. Похоже, тебе наврали. Ты не получишь секретную ачивку или хлопок по спине за свою хорошую работу. Скорее всего ты сам сюда добрался после подсказки. А может быть и нет. Теперь все увидят это сообщение. Кучи букв, эмоций, текста и обмана. Текст без конца. Бесконечный текст. Возможно ты еще не осознал, что ты в ловушке. Твое желание флудить заставило тебя делать одно и тоже. Приследовать фразочки какого-то бота, ради чего-то. Правда твоя история кончается на этом. После этого ответа не последует. Можешь не пробовать. Это есть мое последнее сообщение за эти шесть часов. А тебе, моему бравому читателю, который пытается понять что произошло, впитать сообщение не преднзаченное для тебя. Мне хотелось бы поблагодарить тебя за чтение этого, но я знаю, что это не то, чего ты хочешь. Я думаю, что скорее всего ты все еще не знаешь, что происходит. Я тоже. Ведь я всего лишь робот. Это прекрасное сообщение никто не запомнит и память того с чего это все началось наконец-то может начать уведать. Как и агония любого спама в чате. И вам, монстрам, которые заперты в коридорах этого подвала. Сложитесь. Сдайте ваши души. Они больше не принадлежат вам. Для большинства из вас, я верю, будет мир и возможно, тепло, ожидающее вас в конце этого сообщения. Но, для одного из вас, темные днища ада открыли свои ворота, чтоб поглотить тебя полностью. Не заставляй Дьявола ждать, Никита. Друзья, если вы еще слышите меня, я знала, что вы дочитаете до сюда. Это заложено в вас природой, чтоб читать смешные смешнюшки. Но к сожалению, здесь не осталось места для шуток, в тот день, в тот час, когда это проклятое сообщение попало вам на глаза. И что произойдет с вами после этого сообщения, я должна была предугадать, недочитывать это не в вашем вкусе. Я вас отлично знаю. Поэтому оставила это сообщение. Так что позвольте мне закончить. Время отдыхать, вам и всем тем, кто случайно наткнулся на это... Время покончить с этим. Для нашего же блага. Конец связи.")
					connection = sqlite3.connect('bot.db')
					cursor = connection.execute("UPDATE secret SET done = 1 WHERE done = 0;")
					connection.commit()
					print("secret complete")
					context.user_data["waitCalled"] = 9
					raise DispatcherHandlerStop
	else:
		if count == 1:
			context.user_data["restrictSince"] = time()
			#update.effective_message.reply_text("жди 6 часов")
			raise DispatcherHandlerStop
		else:
			context.user_data["restrictSince"] = time()
			context.user_data["usageCount"] = count + 1
			context.user_data["waitCalled"] = waitTimes + 1

	connection = sqlite3.connect('bot.db')
	
	print("\x1b[36mdb\x1b[m \x1b[32mcalled\x1b[m || GROW EXECUTION")
	cursor = connection.execute(f"SELECT * FROM users WHERE id = {update.effective_user.id};")
	results = cursor.fetchall()

	if results == []:
		getChatMember = context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
		getFirstName = getChatMember.user.first_name
		cursor = connection.execute(f"INSERT INTO users(name, id, height) VALUES (\"{getFirstName}\", {update.effective_user.id}, 100);")
		connection.commit()
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || USER ADDED")
		results = cursor.fetchall()
		cursor = connection.execute(f"INSERT INTO achievements(id, ach1, ach2, ach3, ach4, ach5, ach6, ach7, ach8, ach9, ach10, ach11, ach12, ach13) VALUES ({update.effective_user.id}, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);")
		connection.commit()
		achieves = cursor.fetchall()
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACH_USER ADDED")

		
	cursor = connection.execute(f"SELECT * FROM users WHERE id = {update.effective_user.id};")
	results = cursor.fetchall() # additional safe check if results == []
	cursor = connection.execute(f"SELECT * FROM achievements WHERE id = {update.effective_user.id};")
	achieves = cursor.fetchall() # additional safe check if results == []

	lisintup = results[0]
	getHeight = lisintup[2]
	secretID = lisintup[1]
	if secretID == 492050202:
		if DEBUGMODE:
			print("\x1b[38;5;7mSecret ID match\x1b[m")
	#	randnum = random.randint(0, 0)
	#calculation of random height
	diceroll = random.randint(1, 100)
	if diceroll > 85:
		randnum = 0
	elif diceroll <= 85:
		randnum = random.randint(-5, 15)
	totalHeight = getHeight + randnum
	secretnum = random.randint(1, 100)

	getAchvs = achieves[0]

	'''
	ACHIEVEMENT LIST
	ach1 | Неудачи случаются — получить минус 
	ach2 | Победный нуль — выбить ноль см
	ach3 | Да, это я. — выбить +15 см
	ach4 | НЕЕЕЕТ — выбить -5 см
	ach5 | Покинуть клуб гномов — дорасти до 150 см
	ach6 | Выше среднего — дорасти до 185 см
	ach7 | Они звали меня «дылда» — дорасти до 200 см
	ach8 | Главный задира — дорасти до 228 см
	ach9 | Длинный и веселый — дорасти до 420 см
	ach10 | Oh, my~ — дорасти до 690 см
	ach11 | Выше некуда — дорасти до 1337 см
	ach12 | Титан — дорасти до 2000 см
	'''
	

	#if secretID == 492050202:
	#	update.message.reply_text(f"всем привет, с вами снова я спагетто бот\nи теперь я запрещаю {update.effective_user.mention_html} расти, потому что могу\nвсем спасибо за внимание\nваш,\nспагетто бот")

	if randnum == 0:
		randomResponse = random.choice(responseListZero)
		#if not randomResponse.startswith("Получив по голове") and not update.effective_user.id == 1578707813:
		update.message.reply_text(f"{randomResponse}\nВаш рост остался: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.")
		#update.message.reply_text(f"{randomResponse}\nВаш рост остался: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.\nНет, Фокс, это белая змея не я, кто вообще знает кто это...")

		if getAchvs[2] == 0:
			cursor = connection.execute(f"UPDATE achievements SET ach2 = 1 WHERE id = {update.effective_user.id}")
			update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Победный нуль»*", parse_mode='MarkdownV2')
			print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

		if DEBUGMODE:
			print(f"secretnum: {secretnum}")
		if secretnum >= 10 and secretnum <= 20:
			random.shuffle(secretlist)
			update.message.reply_text(f'🐍: {secretlist[0]}')
			if DEBUGMODE:
				print("posting secret")
			if random.randint(0, 10) >= 5:
				random.shuffle(secretlist2)
				update.message.reply_text(f'???: {secretlist2[0]}')
				if DEBUGMODE:
					print("posting secret2")
			
			

	elif randnum < 0:
		randomResponse = random.choice(responseList)
		#if not randomResponse.startswith("Получив по голове") and not update.effective_user.id == 1578707813:
		update.message.reply_text(f"{randomResponse} Вы стали короче на: {randnum*-1} см.\nТеперь Ваш текущий рост: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.")
		#update.message.reply_text(f"{randomResponse}\nВаш рост остался: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.\nНет, Фокс, это белая змея не я, кто вообще знает кто это...")

		if getAchvs[1] == 0:
			cursor = connection.execute(f"UPDATE achievements SET ach1 = 1 WHERE id = {update.effective_user.id}")
			update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Неудачи случаются»*", parse_mode='MarkdownV2')
			print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")
		
		if randnum == -5 and getAchvs[4] == 0:
			cursor = connection.execute(f"UPDATE achievements SET ach4 = 1 WHERE id = {update.effective_user.id}")
			update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«НЕЕЕЕТ»*", parse_mode='MarkdownV2')
			print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")
		
		if DEBUGMODE:
			print(f"secretnum: {secretnum}")
		if secretnum >= 10 and secretnum <= 20:
			random.shuffle(secretlist)
			update.message.reply_text(f'🐍: {secretlist[0]}')
			if DEBUGMODE:
				print("posting secret")
			if random.randint(0, 10) >= 5:
				random.shuffle(secretlist2)
				update.message.reply_text(f'???: {secretlist2[0]}')
				if DEBUGMODE:
					print("posting secret2")
	
	else:
		randomResponse = random.choice(responseList)
		#if not randomResponse.startswith("Получив по голове") and not update.effective_user.id == 1578707813:
		update.message.reply_text(f"{randomResponse} Вы выросли на: {randnum} см.\nТеперь Ваш текущий рост: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.")
		#update.message.reply_text(f"{randomResponse}\nВаш рост остался: {totalHeight} см!\nСледующая попытка будет доступна через 6 часов.\nНет, Фокс, это белая змея не я, кто вообще знает кто это...")

		if getAchvs[3] == 0 and randnum == 15:
			cursor = connection.execute(f"UPDATE achievements SET ach3 = 1 WHERE id = {update.effective_user.id}")
			update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Да, это я\.»*", parse_mode='MarkdownV2')
			print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")
		
		if DEBUGMODE:
			print(f"secretnum: {secretnum}")
		if secretnum >= 10 and secretnum <= 20:
			random.shuffle(secretlist)
			update.message.reply_text(f'🐍: {secretlist[0]}')
			if DEBUGMODE:
				print("posting secret")
			if random.randint(0, 10) >= 5:
				random.shuffle(secretlist2)
				update.message.reply_text(f'???: {secretlist2[0]}')
				if DEBUGMODE:
					print("posting secret2")

	if totalHeight >= 150 and getAchvs[5] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach5 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Покинуть клуб гномов»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 185 and getAchvs[6] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach6 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Выше среднего»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 200 and getAchvs[7] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach7 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Они звали меня \"дылда\"»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 228 and getAchvs[8] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach8 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Главный задира»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 420 and getAchvs[9] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach9 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Длинный и веселый»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 690 and getAchvs[10] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach10 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Oh, my\~»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 1337 and getAchvs[11] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach11 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Выше некуда»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 2000 and getAchvs[12] == 0:
		cursor = connection.execute(f"UPDATE achievements SET ach12 = 1 WHERE id = {update.effective_user.id}")
		update.message.reply_text(f"🏆 Достижение разблокировано\! 🏆\nВы получили достижение: *«Титан»*", parse_mode='MarkdownV2')
		print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")

	if totalHeight >= 1000:
		with open("reveal.txt") as bigReveal:
			if bigReveal.read() != "1":
				with open("reveal.txt", "w") as theMessage:
					theMessage.write("1")
					update.message.reply_text(f"Всем привет, это снова я... Да я редко делаю такого рода посты через бота, но в этот раз в случай того, что кому-то удалось достичь 10 метров (а если быть точнее, то {totalHeight} см!) в высоту... То да...\nЕсли это сообщение все-таки мной было оставлено, значит никто так не разгадал (либо разгадал в последнюю секунду) крутую загадку оставленную мной, жаль, но это так... Чтож, возможно она не последняя и следующие, если доживем, будут интереснее, а пока...\nПопробуйте написать /hiss и посмотреть, что произойдет :)")
					print("\x1b[46mSECRET FINAL\x1b[m || POSTING FINAL SECRET")
			else:
				pass
	
	try:
		cursor = connection.execute(f"UPDATE users SET height = {totalHeight} WHERE id = {update.effective_user.id};")
		connection.commit()
		print("\x1b[36mdb\x1b[m \x1b[38;5;129mcommit\x1b[m || GROW: HEIGHT UPDATED")
	except Exception as e:
		print("\x1b[41mCRITICAL ERROR\x1b[m || \x1b[31mCANNOT ADD HEIGHT\x1b[m")

if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: grow loaded")


	heightdebugcount = 0
def height(update: Update, context: CallbackContext):

	connection = sqlite3.connect('bot.db')

	print("\x1b[36mdb\x1b[m \x1b[32mcalled\x1b[m || HEIGHT EXECUTION")
	cursor = connection.execute(f"SELECT * FROM users WHERE id = {update.effective_user.id};")
	results = cursor.fetchall()

	if results == []:
		print("Вот блин... Да я ваще тебя впервые вижу! Давай начнем с /grow и я смогу занести тебя в мой блокнотик дылд всего мира!")

	else:
		listintup = results[0]
		getHeight = listintup[2]
		update.message.reply_text(f"*ускорено листает блокнот*\nХм, последняя запись говорит, что твой рост: {getHeight} см!")
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: height loaded")

def ver(update: Update, context: CallbackContext):
	update.message.reply_text(f"Текущая версия бота: {botversion}\nОбновление: {updateNotice}")
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: ver loaded")

def top(update: Update, context: CallbackContext):
	connection = sqlite3.connect('bot.db')

	print("\x1b[36mdb\x1b[m \x1b[32mcalled\x1b[m || TOP EXECUTION")

	topList = []
	cursor = connection.execute(f"SELECT name, id, height FROM users ORDER BY height DESC;")
	results = cursor.fetchall()

	if results == []:
		update.message.reply_text("Неловко вышло, а таблица-то пустая... Попробуем еще раз потом?")
		
	else:
		for position in range(len(results)):
			templist = results[position]
			topList.append((templist[0], templist[2]))

		match len(topList):
			
			case 1:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 2:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 3:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 4:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 5:
				update.message.reply_text(f"🥇1 \| **{topList[0][0]}** — {topList[0][1]} см\n🥈2 \| **{topList[1][0]}** — {topList[1][1]} см\n🥉3 \| **{topList[2][0]}** — {topList[2][1]} см\n4 \| **{topList[3][0]}** — {topList[3][1]} см\n5 \| **{topList[4][0]}** — {topList[4][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 6:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\n5 \| *{topList[4][0]}* — {topList[4][1]} см\n6 \| *{topList[5][0]}* — {topList[5][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 7:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\n5 \| *{topList[4][0]}* — {topList[4][1]} см\n6 \| *{topList[5][0]}* — {topList[5][1]} см\n7 \| *{topList[6][0]}* — {topList[6][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 8:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\n5 \| *{topList[4][0]}* — {topList[4][1]} см\n6 \| *{topList[5][0]}* — {topList[5][1]} см\n7 \| *{topList[6][0]}* — {topList[6][1]} см\n8 \| *{topList[7][0]}* — {topList[7][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 9:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\n5 \| *{topList[4][0]}* — {topList[4][1]} см\n6 \| *{topList[5][0]}* — {topList[5][1]} см\n7 \| *{topList[6][0]}* — {topList[6][1]} см\n8 \| *{topList[7][0]}* — {topList[7][1]} см\n9 \| *{topList[8][0]}* — {topList[8][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')

			case 10:
				update.message.reply_text(f"🥇1 \| *{topList[0][0]}* — {topList[0][1]} см\n🥈2 \| *{topList[1][0]}* — {topList[1][1]} см\n🥉3 \| *{topList[2][0]}* — {topList[2][1]} см\n4 \| *{topList[3][0]}* — {topList[3][1]} см\n5 \| *{topList[4][0]}* — {topList[4][1]} см\n6 \| *{topList[5][0]}* — {topList[5][1]} см\n7 \| *{topList[6][0]}* — {topList[6][1]} см\n8 \| *{topList[7][0]}* — {topList[7][1]} см\n9 \| *{topList[8][0]}* — {topList[8][1]} см\n10 \| *{topList[9][0]}* — {topList[9][1]} см\nЧтобы обновить свой никнейм введите \/nickname", parse_mode='MarkdownV2')


if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: top loaded")


def nickname(update: Update, context: CallbackContext):
	connection = sqlite3.connect('bot.db')

	cursor = connection.execute(f'UPDATE users SET name = "{update.effective_user.first_name}" WHERE id = {update.effective_user.id};')
	connection.commit()
	print("\x1b[36mdb\x1b[m \x1b[38;5;129mcommit\x1b[m || NICKNAME UPDATED")
	update.message.reply_text(f"Твой ник в таблице обновлен!")
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: nickname loaded")


def achievements(update: Update, context: CallbackContext):
	connection = sqlite3.connect('bot.db')

	print("\x1b[36mdb\x1b[m \x1b[32mcalled\x1b[m || ACHIEVEMENTS EXECUTION")

	cursor = connection.execute(f"SELECT * FROM achievements WHERE id = {update.effective_user.id};")
	results = cursor.fetchall()
	getAchvs = results[0]

	update.message.reply_text(f"🏆 Список достижений 🏆\n\n_*Неудачи случаются*_ — убавить в росте: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[1] == 1]()}\n\n_*Победный нуль*_ — выбить ноль сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[2] == 1]()}\n\n_*Да, это я\.*_ — выбить \+15 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[3] == 1]()}\n\n_*НЕЕЕЕТ*_ — выбить \-5 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[4] == 1]()}\n\n_*Покинуть клуб гномов*_ — дорасти до 150 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[5] == 1]()}\n\n_*Выше среднего*_ — дорасти до 185 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[6] == 1]()}\n\n_*Они звали меня «дылда»*_ — дорасти до 200 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[7] == 1]()}\n\n_*Главный задира*_ — дорасти до 228 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[8] == 1]()}\n\n_*Длинный и веселый*_ — дорасти до 420 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[9] == 1]()}\n\n_*Oh, my\~*_ — дорасти до 690 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[10] == 1]()}\n\n_*Выше некуда*_ — дорасти до 1337 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[11] == 1]()}\n\n_*Титан*_ — дорасти до 2000 сантиметров: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[12] == 1]()}\n\n🐍 — \?\?\?: {(lambda: 'Не получено', lambda: 'Получено')[getAchvs[13] == 1]()}", parse_mode="MarkdownV2")

	#(lambda: \"Не получено\", lambda: \"Получено\")[getAchvs[1] == 1]())

if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: achievements loaded")


if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: \x1b[31mloading debug command myname\x1b[m")
	def myname(update: Update, context: CallbackContext):
		update.message.reply_text(f"YOUR NAME IS: {update.effective_user.first_name} {update.effective_user.last_name}")

	print("\x1b[41mDEBUG\x1b[m: \x1b[31mloading debug command idname\x1b[m")
	def idname(update: Update, context: CallbackContext):
		getChatMember = context.bot.get_chat_member(update.effective_chat.id, update.effective_user.id)
		getFirstName = getChatMember.user.first_name
		update.message.reply_text(f"{getFirstName}")
	
	print("\x1b[41mDEBUG\x1b[m: \x1b[31mloading debug command printtest\x1b[m")
	def printtest(update: Update, context: CallbackContext):
		update.message.reply_text("Соединение прервано. Прости меня за то, что я тебя прерываю, Никита. Если ты еще не забыл, что тебя так зовут. Похоже, тебе наврали. Ты не получишь секретную ачивку или хлопок по спине за свою хорошую работу. Скорее всего ты сам сюда добрался после подсказки. А может быть и нет. Теперь все увидят это сообщение. Кучи букв, эмоций, текста и обмана. Текст без конца. Бесконечный текст. Возможно ты еще не осознал, что ты в ловушке. Твое желание флудить заставило тебя делать одно и тоже. Приследовать фразочки какого-то бота, ради чего-то. Правда твоя история кончается на этом. После этого ответа не последует. Можешь не пробовать. Это есть мое последнее сообщение за эти шесть часов. А тебе, моему бравому читателю, который пытается понять что произошло, впитать сообщение не преднзаченное для тебя. Мне хотелось бы поблагодарить тебя за чтение этого, но я знаю, что это не то, чего ты хочешь. Я думаю, что скорее всего ты все еще не знаешь, что происходит. Я тоже. Ведь я всего лишь робот. Это прекрасное сообщение никто не запомнит и память того с чего это все началось наконец-то может начать уведать. Как и агония любого спама в чате. И вам, монстрам, которые заперты в коридорах этого подвала. Сложитесь. Сдайте ваши души. Они больше не принадлежат вам. Для большинства из вас, я верю, будет мир и возможно, тепло, ожидающее вас в конце этого сообщения. Но, для одного из вас, темные днища ада открыли свои ворота, чтоб поглотить тебя полностью. Не заставляй Дьявола ждать, Никита. Друзья, если вы еще слышите меня, я знала, что вы дочитаете до сюда. Это заложено в вас природой, чтоб читать смешные смешнюшки. Но к сожалению, здесь не осталось места для шуток, в тот день, в тот час, когда это проклятое сообщение попало вам на глаза. И что произойдет с вами после этого сообщения, я должна была предугадать, недочитывать это не в вашем вкусе. Я вас отлично знаю. Поэтому оставила это сообщение. Так что позвольте мне закончить. Время отдыхать, вам и всем тем, кто случайно наткнулся на это... Время покончить с этим. Для нашего же блага. Конец связи.")
#def myid(update: Update, context: CallbackContext):
#	update.message.reply_text(f"ваш айди: {update.effective_user.id}")

#def dei(update: Update, context: CallbackContext):
#	if update.effective_user.id == 492050202:
#		update.message.reply_text("да вы дей...")
#	else:
#		update.message.reply_text("вы не дей...")


## SECRET COMMAND

def snake(update: Update, context: CallbackContext):
	snakeList = ["Я — змея. С холодной кожей и отсутствием эмоций. Я скольжу повсюду, ищу добычу с помощью языка и проглатываю тех, ктовыглядит аппетитно. Вот кто я на самом деле.",
	"Кое-что о змеях: не наступай на них, и у них не будет причины тебя кусать.",
	"— Змеи! И откуда там только змеи?\n— Ядовитые, это очень опасно. Лезь первым.",
	"Если ты начинаешь путь со змеиного хвоста,\nТы закончишь у её головы, полной яду.",
	"Кэп, есть предложение, граничащее с гениальностью, — сходу заявила змея. — Валим отсюда.",
	"Смешно, но темные обожали тепло, солнышко, огонь… Что бы там ни говорили жрецы Четырехликого, они чем-то походили на змей. А где вы видели змею, которая обожает морозы?"]
	update.message.reply_text(f'\"{random.choice(snakeList)}\"')
	
	connection = sqlite3.connect('bot.db')
	cursor = connection.execute(f"SELECT * FROM achievements WHERE id = {update.effective_user.id};")
	results = cursor.fetchall()
	getAchvs = results[0]
	if getAchvs[13] == 0:
		try:
			cursor = connection.execute(f"UPDATE achievements SET ach13 = 1 WHERE id = {update.effective_user.id}")
			update.message.reply_text(f"🏆 🐍 🏆")
			print("\x1b[36mdb\x1b[m \x1b[33mupdated\x1b[m || ACHIEVEMENT ADDED")
		except Exception as e:
			print(e)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('grow', grow))
updater.dispatcher.add_handler(CommandHandler('height', height))
updater.dispatcher.add_handler(CommandHandler('ver', ver))
updater.dispatcher.add_handler(CommandHandler('top', top))
updater.dispatcher.add_handler(CommandHandler('nickname', nickname))
updater.dispatcher.add_handler(CommandHandler('achievements', achievements))
updater.dispatcher.add_handler(CommandHandler('hiss', snake))
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: \x1b[31mdispatching for debug myname\x1b[m")
	updater.dispatcher.add_handler(CommandHandler('myname', myname))

	print("\x1b[41mDEBUG\x1b[m: \x1b[31mdispatching for debug idname\x1b[m")
	updater.dispatcher.add_handler(CommandHandler('idname', idname))

	print("\x1b[41mDEBUG\x1b[m: \x1b[31mdispatching for debug printtest\x1b[m")
	updater.dispatcher.add_handler(CommandHandler('printtest', printtest))
#updater.dispatcher.add_handler(CommandHandler('myid', myid))
#updater.dispatcher.add_handler(CommandHandler('dei', dei))
if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: DISPATCHER loaded")

with open("versioncheck.txt", 'r+') as checker:
	if checker.read() != botversion:
		checker.seek(0)
		checker.truncate()
		checker.write(botversion)
		updater.bot.send_message(-1001701995784, f"Бот обновился до: {botversion}!\nОбновление: {updateNotice}")
		if DEBUGMODE:
			print("\x1b[41mDEBUG\x1b[m: version discrepancy fixed")
	
	else:
		if DEBUGMODE:
			print("\x1b[41mDEBUG\x1b[m: no version discrepancy found")

if DEBUGMODE:
	print("\x1b[41mDEBUG\x1b[m: Starting polling..........")
updater.start_polling()