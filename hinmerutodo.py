import tkinter
from tkinter import font

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()
        
    def create_widgets(self):
        # タスクの例を表示するラベル
        example_label = tkinter.Label(self, text='(例)ごみを捨てる')
        example_label.pack()
        
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
        
        # テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 20
        self.text_box.pack()
        
        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.input_handler
        submit_btn.pack()
        
        # メッセージ出力
        self.message = tkinter.Label(self, fg='red', font=("Helvetica", 12, "bold"))
        self.message.pack()
        
        # プログラムの説明
        description = tkinter.Label(self, text="「やるべきことを書き込むと「ヒンメルならそうする。」とやる気のある感じのメッセージが返ってきます。」", wraplength=300, justify='left')
        description.pack(side='bottom')
        
    def input_handler(self):
        text = self.text_box.get()
        if text:
            self.message['text'] = text + '。ヒンメルならそうする。'
        else:
            self.message['text'] = 'たまには休むといいよ。'
            self.message.config(fg='blue', font=("Helvetica", 15, "italic"))

root = tkinter.Tk()  # ウィジェット作成
root.title('ヒンメルならどうする？')
root.geometry('400x300')
app = Application(root=root)
app.mainloop()
