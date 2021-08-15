while True:
	mode = input('請輸入你要的遊戲模式：')
	if mode == 'q':
		print('正在離開......')
		break
	elif mode == '1':
		print('遊戲模式一正在啟動中......')
	elif mode == '2':
		print('遊戲模式二正在啟動中......')
	else:
		print('只能輸入 1/2/q')