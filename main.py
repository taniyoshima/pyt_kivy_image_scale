# -*- coding: utf-8 -*-

import os
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.properties import ObjectProperty, NumericProperty
from kivy.lang import Builder
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage

kivy.require('2.2.0')

# 画面サイズの指定
Config.set('graphics', 'width', '680')
Config.set('graphics', 'height', '400')

Builder.load_file(os.path.dirname(__file__) + "/interface.kv")


class ImageTestWidget(Widget):
    state = 0

    def __init__(self, **kwargs):
        super(ImageTestWidget, self).__init__(**kwargs)

        print(self.ids.box.size)

        # 画像ファイルの読み込み
        self.img1 = CoreImage('sample.png')
        # 読み込んだ画像をimageに設定
        self.ids.image.texture = self.img1.texture
        self.ids.image.width = self.ids.scrollview.width
        self.ids.image.height = self.ids.scrollview.height
        self.ids.scrollview.update_from_scroll()

    def on_image_down(self, touch):
        # ダブルクリックであるかの判定
        if touch.is_double_tap:

            if self.state == 0:
                # 等倍表示の処理
                self.ids.image.width = self.ids.image.texture.width
                self.ids.image.height = self.ids.image.texture.height

                # 表示位置の変更
                self.ids.scrollview.update_from_scroll()
                self.ids.scrollview.scroll_x = (
                    touch.pos[0] / self.ids.scrollview.width)
                self.ids.scrollview.scroll_y = (
                    touch.pos[1] / self.ids.scrollview.height)
                self.state = 1
            else:
                # 画面に合わせた表示の処理
                self.ids.image.width = self.ids.scrollview.width
                self.ids.image.height = self.ids.scrollview.height
                self.ids.scrollview.update_from_scroll()
                self.state = 0


class ImageTestWidgetApp(App):
    def __init__(self, **kwargs):
        super(ImageTestWidgetApp, self).__init__(**kwargs)
        self.title = 'Image Test'

    def build(self):
        return ImageTestWidget()


if __name__ == '__main__':
    app = ImageTestWidgetApp()
    app.run()
