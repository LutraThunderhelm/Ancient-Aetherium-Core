def establish_head(title,page):
	print('<head>')
	print('<meta charset="utf-8">')
	print('<title>' + title + '</title>')
	print('<link href="/Ancient-Aetherium-Core/Styling/style.css" rel="stylesheet" type="text/css"/>')
	print('<style>#banner{background-image:url("/Ancient-Aetherium/Styling/Banners/' + page + '.png")}</style>')
	print('</head>')



def generate_nav(cur_index):
	pages = [
	'Encounters',
	'Tales',
	'Rules',
    'Gear',
    'Faith',
	'Arcana',
	'Characters',
	'Home'
	]
	print('<nav><ul>')
	for x in range(0,len(pages)):
		print('<li><a href="/Ancient-Aetherium-Core/{page}"'.format(page=pages[x]))
		if x == cur_index:
			print(' id="active"')
		print('>{page}</a></li>'.format(page=pages[x]))
	print('</nav></ul>')



def generate_header(title,subtitle):
	print('<div id="banner">')
	print('<h1><!--')

	title_stylings = ['decor','tail','spacer','cap','tail']
	subtitle_stylings = ['tail','spacer','cap','tail','cap']

	for x in range(0,len(title_stylings)):
		print('--><img src="/Ancient-Aetherium-Core/Styling/left-{style}.svg"><!--'.format(style=title_stylings[x]))
	print('--><span>' + title + '</span><!--')
	for x in range(0,len(title_stylings)):
		print('--><img src="/Ancient-Aetherium-Core/Styling/right-{style}.svg"><!--'.format(style=title_stylings[len(title_stylings)-x-1]))

	print('--></h1><h2><!--')

	for x in range(0,len(subtitle_stylings)):
		print('--><img src="/Ancient-Aetherium-Core/Styling/left-{style}.svg"><!--'.format(style=subtitle_stylings[x]))
	print('--><span>' + subtitle + '</span><!--')
	for x in range(0,len(subtitle_stylings)):
		print('--><img src="/Ancient-Aetherium-Core/Styling/right-{style}.svg"><!--'.format(style=subtitle_stylings[len(subtitle_stylings)-x-1]))

	print('--></div>')



def generate_tabs(tabs,tab_index):
	print('<div id="page-tabs"><ul>')
	for x in range(0,len(tabs)):
		print('<li><a')
		if x == tab_index:
			print(' id="current-tab" ')
		print('href="{name}">{name_clean}</a></li>'.format(name=tabs[x],name_clean=tabs[x].replace('-',' ')))
	print('</ul></div>')



def generate_article(title,content):
	print('<h2><span>{title}</span></h2>'.format(title=title))
	print('<div class="description">')
	import json
	dictionary = open('../dictionary.json','r')
	raw_json = dictionary.read()
	dictionary.close()
	dictionary = json.loads(raw_json)["defs"]
	for x in range(0,len(dictionary)):
		content = content.replace('{{' + dictionary[x][0] + '|', '<a href="/Ancient-Aetherium-Core/{link}" title="{description}">'.format(link=dictionary[x][1],description=dictionary[x][2]))
	content = content.replace('}}','</a>')
	content = '<p>' + content.replace('\n\n','</p><p>') + '</p>'
	print(content)

	print('</div>')



def generate_article_list(raw_descriptions):
	print('<div id="article_list">')
	descriptions = raw_descriptions.split('\n\n')
	for x in range(0,len(descriptions)):
		current_description = descriptions[x].split('\n',2)
		print('<div class="stacked-list"><img src="{link}">'.format(link=current_description[1]))
		print('<h3><span>{title}</span></h3>'.format(title=current_description[0]))
		content = current_description[2].split('\n')
		if len(content) > 1:
			if x % 2 == 1:
				for y in range(0,len(content)-1):
					print('<p style="text-align:right">{content}</p>'.format(content=content[y]))
			else:
				for y in range(0,len(content)-1):
					print('<p style="text-align:left">{content}</p>'.format(content=content[y]))
		print('<p style="text-align:justify">{content}</p>'.format(content=content[-1]))
		print('</div>')
	print('</div>')


def generate_buttons(form,sub_pages):
	print('<form action={form}><!--'.format(form=form))
	for x in range(0,len(sub_pages)):
		print('--><input type="submit" name="subpage" value="{page}"/><!--'.format(page=sub_pages[x]))
	print('--></form>')
