from telebot import types
class INLINE:
    def __init__(self,row,*args):
        self.row = row
        self.args = args
    def inline(self):
        inline = types.InlineKeyboardMarkup(row_width = self.row)
        lis = []
        for i in self.args:
            btn = types.InlineKeyboardButton(i, callback_data=i)
            lis.append(btn)
        inline.add(*lis)
        return inline

class KEYBORD:
    def __init__(self,row,one_time=False,*args):
        self.args = args
        self.row = row
        self.one_time=one_time
    def mark_up(self):
        mark_up=types.ReplyKeyboardMarkup(row_width=self.row,resize_keyboard=True, one_time_keyboard=self.one_time)
        mark_up.add(self.args)
        return mark_up