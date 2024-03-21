import telebot
import datetime
import time
import threading
import random

#print ("hello")



bot = telebot.TeleBot("6852693433:AAE8BdxZCNfoe5PApiiTAyTr44Z7jaz02Ms")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который поможет Вам с выбором товаров на сайте www.plitkanadom.ru!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = [
        "Керамическая плитка имеет долгую историю и была использована людьми в разных культурах на протяжении многих веков. Вот факты о появлении керамической плитки: Древний Восток: Одним из первых регионов, где была использована керамическая плитка, был Древний Восток, включая Месопотамию, Египет, Индию и Китай. В этих цивилизациях керамическая плитка использовалась для украшения стен, полов, фонтанов и многое другое. Ее цвета и узоры отражали местные традиции и художественный стиль.",
        "Керамическая плитка имеет долгую историю и была использована людьми в разных культурах на протяжении многих веков. Вот факты о появлении керамической плитки: Древний Рим: В Римской империи керамическая плитка стала широко использоваться как декоративный элемент в общественных зданиях, банях, храмах и виллах. Римляне создавали красивые мозаичные узоры из керамической плитки на полах и стенах.",
        "Керамическая плитка имеет долгую историю и была использована людьми в разных культурах на протяжении многих веков. Вот факты о появлении керамической плитки: Средние века и Ренессанс: Во время Средних веков керамическая плитка была популярным материалом в архитектуре и дизайне. В европейских замках и церквях можно увидеть уникальные образцы керамической плитки, созданные мастерами-керамистами.",
        "Керамическая плитка имеет долгую историю и была использована людьми в разных культурах на протяжении многих веков. Вот факты о появлении керамической плитки: Промышленная революция и современность: В XIX веке с развитием промышленности керамическая плитка стала производиться массово и стала доступной для широкого круга потребителей. С появлением новых технологий и материалов керамическая плитка стала более прочной, устойчивой к влажности и легкой в уходе.",
        "Керамическая плитка имеет долгую историю и была использована людьми в разных культурах на протяжении многих веков. Вот факты о появлении керамической плитки: Сегодня керамическая плитка широко используется в дизайне интерьеров, строительстве, облицовке стен и полов благодаря своей прочности, разнообразию дизайна и функциональным характеристикам. Ее история отражает эволюцию мировой культуры и технологий.",
        "Сантехника – это часть быта, без которой мы уже не можем представить современную жизнь. Она пришла к нам издалека и имеет древние корни. История сантехники началась задолго до нашей эры, когда люди начали понимать важность гигиены и комфорта в своем жилище. Древние цивилизации, такие как древние египтяне, греки и римляне, уже использовали системы водоснабжения и канализации. В Греции даже существовала профессия водопроводчика, который занимался обслуживанием и ремонтом водопроводных систем.",
        "Сантехника – это часть быта, без которой мы уже не можем представить современную жизнь. Она пришла к нам издалека и имеет древние корни. История сантехники началась задолго до нашей эры, когда люди начали понимать важность гигиены и комфорта в своем жилище. Сантехника в современном понимании начала активно развиваться с появлением промышленной революции в XIX веке. Первые водонапорные башни и системы водоснабжения появились во многих странах Европы, обеспечивая население чистой питьевой водой. Великий вклад в развитие сантехники внесли ученые и инженеры, такие как Джон Сноу, который провел первое научное исследование эпидемии холеры и выявил ее причину – загрязненную воду.",
        "Сантехника – это часть быта, без которой мы уже не можем представить современную жизнь. Она пришла к нам издалека и имеет древние корни. История сантехники началась задолго до нашей эры, когда люди начали понимать важность гигиены и комфорта в своем жилище. С развитием технологий и инженерных решений сантехника стала более совершенной и удобной. Сегодня сантехнические системы не только обеспечивают нас чистой водой и удобствами в быту, но также помогают экономить ресурсы и сохранять окружающую среду.",
        "Сантехника – это часть быта, без которой мы уже не можем представить современную жизнь. Она пришла к нам издалека и имеет древние корни. История сантехники началась задолго до нашей эры, когда люди начали понимать важность гигиены и комфорта в своем жилище. История сантехники – это история постоянного совершенствования и развития, которое принесло нам комфорт и удобство в нашей повседневной жизни.",
        "Паркет – это красивое и прочное покрытие пола, которое имеет древние корни и богатую историю. Его появление связано с желанием людей улучшить комфорт и красоту своих жилищ. История паркета восходит к древним временам, когда люди начали использовать дерево как строительный материал. Первые упоминания о паркете можно найти в древних римских домах, где полы украшались сложными узорами из различных пород дерева. В Средние века паркет стал популярным во Франции и Италии, где мастера создавали шедевры из дерева для дворцов и замков. В XIX веке паркет стал доступным не только для знати, но и для широких масс. С появлением промышленных методов производства и технологических новшеств паркет стал массово производиться и укладываться в жилых домах и общественных зданиях. Сегодня паркет остается популярным и востребованным материалом для отделки полов. Он не только придает помещению элегантность и уют, но также обладает высокой прочностью и долговечностью. Современные технологии позволяют создавать паркетные покрытия различных форм, цветов и текстур, удовлетворяя потребности даже самых требовательных клиентов. Таким образом, история паркета – это история традиций и мастерства, которые пришли к нам из древних времен и продолжают радовать нас своей красотой и утонченностью.",
        "Ламинат – популярный и практичный материал для напольного покрытия, который имеет относительно недавнюю историю. Его появление связано с развитием технологий и инноваций в области строительных материалов. История ламината началась в 1977 году в Швеции, когда компания Perstorp разработала новый вид напольного покрытия, объединяющий деревянный слой, спрессованный целлюлозный картон и защитный слой ламинации. Этот материал получил название - ламинат и был представлен на рынке как доступная альтернатива натуральному дереву. Первоначально ламинат был представлен в виде одноцветных плиток, имитирующих текстуру дерева. Однако с развитием технологий подделки и дизайна, ламинат стал имитировать различные виды дерева, камень, плитку и другие материалы, благодаря чему стал широко востребованным в отделке интерьеров. С появлением ламината на рынке строительных материалов, он быстро завоевал популярность благодаря своей прочности, стойкости к истиранию, легкости ухода и возможности быстрой укладки. Ламинат стал отличной альтернативой деревянным полам, так как он обладает более высокой стабильностью и не требует особого ухода. Сегодня ламинат представлен на рынке в широком ассортименте цветов, текстур и фактур, что позволяет подобрать его под любой интерьер и стиль помещения. Он остается популярным материалом для напольных покрытий благодаря своей доступности, практичности и эстетическим качествам.",
        "История появления кварцвиниловой плитки началась в 1980-х годах, когда инженеры и ученые начали разрабатывать новые материалы для напольных покрытий, которые были бы прочными, износостойкими и легкими в уходе. В результате исследований был создан материал, состоящий из кварцевого песка и виниловой смолы, который обладал всеми необходимыми свойствами. Кварцвиниловая плитка быстро завоевала популярность благодаря своей прочности, устойчивости к влаге и химическим веществам, а также широкому выбору дизайнов. Она стала использоваться не только в жилых помещениях, но и в коммерческих и общественных зданиях. С появлением современных технологий производства, кварцвиниловая плитка стала еще более популярной, благодаря своей легкости укладки, возможности установки на различные поверхности и длительному сроку эксплуатации. Сегодня она является одним из самых популярных видов напольных покрытий и используется в различных интерьерах по всему миру."
    ]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Факт: {random_fact}')

def send_reminders(chat_id):
    first_rem = "10:00"
    second_rem = "14:00"
    end_rem = "17:30"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Пора заказывать плитку, сантехнику или напольное покрытие!")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)