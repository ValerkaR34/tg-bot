a = ['Колобок повесился','Мужик нашёл шляпу, а она ему как раз', '"Вставьте деньги пачкой," — шутит банкомат','Переодеваться в разных персонажей и ходить от дома к дому, выпрашивая вкусности - это сатанинский ритуал, но только в октябре. В январе это называется - колядовать.']
stirlitz = [
    'Штирлиц напоил собаку бензином. Она порбежала двести метров и упала. «Бензин кончился» — подумал Штирлиц.',
    'Штирлиц и Скрипаль сидели и допивали уже по второй бутылке водки. Скрипаль встал и упал, как убитый. «Новичок» - подумал Штирлиц.',
    'Штирлиц шел по Берлину. Где-то слева прогремел взрыв, справа послышались выстрелы, за спиной кто-то громко кричал. «Dolby Surround», — с восхищением заметил Штирлиц.',
    'Гестапо обложило все выходы в доме Штирлица. Штирлицу пришлось уходить через вход.',
    'Штирлиц постучал в дверь. Дверь не открылась. Штирлиц подёргал дверь. Штирлиц потолкал дверь. Дверь не открылась. «Заперто», — догадался Штирлиц. И только Мюллер знал, что дверь открывается в другую сторону.',
    'Штирлиц шагал по Берлину. На груди у него болтались советские ордена, а позади волочился парашют. В этот день он как никогда был близок к провалу.',
    'Штирлиц пошёл в лес за грибами. Поискал на полянах. Не нашёл. Поискал под деревьями. Не нашёл. Поискал в кустах. Не нашёл. «Не сезон», — подумал Штирлиц, и сел в сугроб.',
    'Штирлиц гулял по весеннему лесу. На деревьях почки. "Гестапо" - подумал Штирлиц.',
    'Штирлиц открыл дверь - свет включился. Закрыл - свет выключился. Опять открыл - свет включился. "Холодильник" - подумал Штирлиц.',
    'Штирлиц гулял с Кэт в лесу. Вдруг, прозвучал выстрел и Кэт упала обливаясь кровью. «Стреляют» — подумал Штирлиц.',
    '— Стой, кто идет? — крикнул часовой.'
    '\n— Дождь, — ответил Штирлиц и забарабанил пальцами по стеклу.',
    'По улицам Берлина на бешенной скорости мчался «Мерседес» Мюллера. А рядом бежал Штирлиц и делал вид, что прогуливается.',
    'Штирлиц очнулся после сильной попойки за решёткой. «Если зайдут в форме НКВД — скажу, что меня зовут Максим Исаев. Если зайдут в немецкой, то скажу, что я Штирлиц». В этот момент в камеру заходит советский милиционер и говорит: «Ну и надрались же вы вчера, товарищ Тихонов».(вариант: Штирлиц проснулся в тюремной камере. Он совершенно не помнил,как сюда попал, какое сегодня число и какая в городе власть. После долгих размышлений он наконец решил, что если войдет гестаповец, надо будет сказать: "Хайль Гитлер, я - штандартенфюрер СС фон Штирлиц", а если войдет советский солдат - представиться: "Я - полковник Исаев". В этот момент входит милиционер и говорит: "Ну и нажрались Вы вчера, товарищ Тихонов".)',
    'Штирлиц шел по Цветочной улице, как вдруг из окна дома напротив упал профессор Плейшнер. Штирлиц ускорил шаг. Из окна следующего дома опять упал профессор Плейшнер. Штирлиц уже бежал по Цветочной улице, а Плейшнеры все падали и падали.',
    'Профессор Плейшнер третий раз выбрасывался из окна, но яд все не действовал.',
    '- Штирлиц, - устало сказал Мюллер, - Вы отвертелись, когда мы обнаружили Ваши пальчики на чемодане русской пианистки. Вы отвертелись, когда мы нашли их на трубке телефона правительственной связи. Но сейчас Вам не отвертеться! Почему Ваше удостоверение пахнет русской водкой?!!'
    '\n- Вы знаете, Мюллер, - не менее устало ответил Штирлиц, - когда Шелленберг ставил на мое удостоверение печать, он предварительно подышал на нее.',
    'Швейцарская народная примета. Если на окне стоит цветок, значит оттуда выпадет Плейшнер.',
    'Штирлиц пришел домой уставший, сел и уронил голову на стол. Кэт в ужасе закричала. Это была голова Холтоффа.',
    '— Кэт, вы любите фильмы о любви?'
    '\n— Да, бесспорно. А вы, Штирлиц?'
    '\n— А я с порно',
    'На допросе Штирлиц порол чушь. Чушь тихо повизгивала.',
    'Штирлиц упал с балкона, но чудом успел зацепиться за карниз. На следующее утро чудо распухло и мешало ходить.',
    'Штирлиц вызвал машину и сказал водителю — «Трогай!», водитель потрогал и сказал — «Ого!» (Штирлиц садится в машину и говорит шоферу "Трогай". Шофер потрогал, Штирлиц поехал.)',
    'Штирлиц заложил ногу за ногу. На следующий день Ногу-за-ногу взяли.',
    'Штирлиц встал спозаранку и отдернул занавеску. Позаранку и Занавеску были румынскими разведчицами.',
    'Штирлиц вышел из моря и лег на гальку. Светка обиделась и ушла.',
    'Штирлиц шел по лесу и увидел людей сидящих у костра. 《Костраты!》 - подумал Штирлиц.',
    'Штирлиц и Мюллер стреляли по очереди. Очередь быстро редела, но не расходилась.',
    'У Штирлица было два танка, он ездил на них по очереди. Очередь возмущалась но не расходилась.',
    'Штирлиц взял записку Мюллера. Мюллер кричал и сопротивлялся.',
    'Штирлиц стоял на своём… Это была любимая пытка Мюллера.',
    'Штирлиц выстрелил вслепую. Слепая упала как подкошенная. Подкошенную он застрелил еще неделю назад.',
    'Штирлиц подошёл к окну. Из окна дуло. Штирлиц закрыл окно. Дуло исчезло.',
    'Штирлиц выстрелил в упор. Упор упал навзничь. Взничь бросился наутек. Утек стал защищаться как мог. Мог был парень крутой, а Крутая слабаков не держала. Взнич вскочил и побежал вприпрыжку. Припрыжка оказалась закрыта.',
    'Штирлиц вышел наружу. Ружа была его польским агентом.',
    'Штирлиц выпил стакан водки и наклонился над картой СССР. Его неудержимо рвало на Родину.',
    'Штирлиц зашёл в лес и увидел голубые ели. Он присмотрелся и заметил, что голубые не только ели, но и пили.',
    'Штирлиц схватил топор и закричал — «Порублю суки!» Суки скинулись по рублю и разбежались.',
    'Штирлиц сел враскарячку. Раскарячка завелась и полетела.',
    'Связной дал Штирлицу наводку. «Немного, зато в рейхсмарках», подумал Штирлиц.',
    'Штирлиц бежал вприпрыжку. В «Припрыжку» завезли разливное «Жигулёвское».',
    'Штирлиц выглянул в окно. На улице немцы ставили танк на попа. «Бедный пастор Шлаг» — подумал Штирлиц.',
    'Штирлиц встретил врага свинцом. Винцо врагу понравилось.',
    'Штирлиц шёл по улице и вдруг почувствовал, что сзади с леденящим душу звуком летит свинец. Штирлиц быстро свернул за угол и свинец с громким хрюканьем пронесся мимо.',
    'Штирлиц бежал скачками. Внезапно он повернул за угол и затихарился — качки пробежали мимо.',
    'Штирлиц гнал в своей машине. Дома гнать было слишком рискованно.',
    'Штирлиц сел в машину и крикнул водителю «Гони!». Водитель открыл краник, и в нос ударил запах свежевыгнанного самогона.',
    'Штирлиц впопыхах застрелил Мюллера. Наутро в Попыхи приехало два взвода карателей.',
    'Лампочка горела, но света не давала. Штирлиц выключил лампочку, и Света дала.',
    'Штирлиц всю ночь топил печь, наутро она все-таки утонула.',
    'Штирлиц украдкой кормил немецких детей. От украдки немецкие дети пухли и дохли.',
    'Штирлиц шел ночью по лесу и наткнулся на сук. У них и заночевал.',
    'Штирлиц шел ночью по лесу и напоролся на сук. Суки с визгом разбежались. Визг бежал первым.',
    'Штирлиц шел ночью по лесу и напоролся на сук. -Шли бы вы домой девочки, сказал Штирлиц.',
    'Штирлиц шёл, с трудом разбирая дорогу. Наутро железная дорога Берлин-Дрезден была разобрана.',
    'Штирлиц и Мюллер прогуливались по Курфюрстендамм, и негромко переговаривались:'
    '\n— Ну что, может снимем вон тех девок?'
    '\n— Да ну их, пусть ещё поболтаются денёк!',
    'Штирлиц приехал в гестапо навеселе. Весело он оставил под окнами Мюллера.',
    'Штирлиц шел по Цветочной улице. У дома номер 33 он остановился и поднял глаза. Это были глаза профессора Плейшнера.',
    'Штирлиц бил наверняка. Наверняк защищался как мог, а Мог был сильный парень.',
    'Штирлиц валял дурака. После часа валяния на гвоздях дурак признался что он работает на японскую разведку.',
    'Мюллер раскрыл явку Штирлица, но получил по морде и больше не брал чужих сигарет.',
    'Штирлиц целый день колесил по городу в поисках явки, но сигареты "Ява" продавались только в Москве.',
    'Штирлиц топил буржуйку. На следующий день в газетах появилась заметка о зверском убийстве сотрудницы Гестапо.',
    'Штирлица бил озноб. Озноб служил в Гестапо.',
    'Штирлиц исподтишка спёр сигареты Мюллера. Больше Мюллер сигареты под тишок не клал.',
    'Штирлиц шёл по Берлину в обнимку с Кэт. Обнимка была последней нераскрытой явкой.',
    'Штирлиц дал Мюллеру взаймы. Наутро займы у Мюллера посинели и опухли.',
    'Штирлица поздравили с днем рождения и дали ему папаху. Пах болел еще две недели.',
]

c = ['Дама рассказывает подруге: - Накрасила брови, ресницы, губы, ногти на руках и на ногах… Остановиться не могу! Пошла во двор и забор ещё покрасила.','Еще вчера я был уверен в завтрашнем дне, а сегодня - только во вчерашнем',
     '- Подскажите, что такое куртка бейн? Часто слышала от фанатов рока. Как она выглядит?']