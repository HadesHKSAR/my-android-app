import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# 設定背景顏色（可選）
Window.clearcolor = (0.95, 0.95, 0.97, 1)

class SmartStewardApp(App):
    def build(self):
        # 主畫面：垂直排列的容器
        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # 1. 頂部標題列
        title = Label(
            text="隨行管家 Smart Steward",
            font_size='22sp',
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=40,
            bold=True
        )
        self.main_layout.add_widget(title)

        # 2. 財務與資產概況卡片
        self.net_assets = 0.0  # 先設定初始資產為 0

        self.status_card = Label(
            text=f"【當前淨資產概況】\nHKD ${self.net_assets:,.2f} | 歡迎使用",
            font_size='16sp',
            color=(0.2, 0.4, 0.8, 1),
            size_hint_y=None,
            height=60
        )
        self.main_layout.add_widget(self.status_card)

        # 3. 快速輸入框與按鈕（手動輸入微調）
        input_area = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        self.user_input = TextInput(
            hint_text="輸入如：八達通 $12.5 買咖啡",
            multiline=False,
            font_size='16sp'
        )
        submit_btn = Button(
            text="新增紀錄",
            size_hint_x=0.3,
            background_color=(0.2, 0.6, 1, 1)
        )
        submit_btn.bind(on_press=self.handle_add_entry)

        input_area.add_widget(self.user_input)
        input_area.add_widget(submit_btn)
        self.main_layout.add_widget(input_area)

        # 4. 滾動區塊（顯示提醒與任務接力卡）
        self.scroll_content = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.scroll_content.bind(minimum_height=self.scroll_content.setter('height'))

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(self.scroll_content)
        self.main_layout.add_widget(scroll_view)

        # 初始化預設範例卡片
        self.add_card("系統提示：本地端加密帳本已就緒")
        self.add_card("待確認：週六 12:30 午餐聚會邀請")

        return self.main_layout

    def handle_add_entry(self, instance):
        """當使用者點擊『新增紀錄』時執行的動作"""
        text = self.user_input.text.strip()
        if text:
            self.add_card(f"手動紀錄：{text}")
            self.user_input.text = ""  # 清空輸入框

    def add_card(self, message):
        """在動態列表中新增一張資訊卡片"""
        card = Label(
            text=f"• {message}",
            font_size='15sp',
            color=(0.2, 0.2, 0.2, 1),
            size_hint_y=None,
            height=35,
            halign='left',
            valign='middle'
        )
        card.bind(size=card.setter('text_size'))  # 確保文字靠左對齊
        self.scroll_content.add_widget(card)

if __name__ == '__main__':
    SmartStewardApp().run()