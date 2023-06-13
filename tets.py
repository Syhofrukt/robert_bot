
str = '!event_create имя дата.месяц.год часы:минуты'


lst = ['GENERATE.KEY','имя','дата.месяц.год', 'часы:минуты','message.author','message.server']

str2 = str.split()

lst2 = ['ключ', str2[1], str2[2], str2[3], 'автор', 'сервер']

#проверять корректную дату и время, сделать модель списка, и выходной список проверять с моделью

print(len(str2))
# if len(str2) != 2
#     async channel.send('Вы ввели комманду неправильно, пример: !event_create [имя_события] {дата.месяц.год часы:минуты} )
print(str2, type(str2))