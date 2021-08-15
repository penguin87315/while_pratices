password = 'a123456'
chance = 3

while True:
	pw = input('請輸入你的密碼：')
	if pw == password:
		print('密碼正確，登入中...')
		break
	else:
		chance = chance - 1
		print('密碼錯誤，你還剩下', chance, '次機會')
		if chance <= 0:
			print('錯誤次數過多，請稍候再試')
			break