# pyt_kivy_image_scale

<br>

## 内容 

imageに表示した画像を拡大・縮小するプログラム。マウスでダブルクリックした場所を中心に画像を拡大したり、画像全体が表示されるように画像を縮小して表示したりします。

<br>

### 1. 画像を表示するImageを、ScrollViewに載せる。

```
        ScrollView:
            id: scrollview
            size: 640, 360
            do_scroll_x: True
            do_scroll_y: True

            Image:
                id: image
                fit_mode: 'scale-down'
                on_touch_down: root.on_image_down(args[1])
                size_hint: None, None
```

<br>

### 2. Imageに画像を表示する

```
    def __init__(self, **kwargs):
        super(ImageTestWidget, self).__init__(**kwargs)

        # 画像ファイルの読み込み
        self.img1 = CoreImage('sample.png')
        # 読み込んだ画像をimageに設定
        self.ids.image.texture = self.img1.texture
        self.ids.image.width = self.ids.scrollview.width
        self.ids.image.height = self.ids.scrollview.height
        self.ids.scrollview.update_from_scroll()
```

<br>

### 3. Image上でのマウスのダブルクリックを認識する。

```
    def on_image_down(self, touch):
        # ダブルクリックであるかの判定
        if touch.is_double_tap:
　　　    # ダブルクリックであった場合の処理
　　　    …
```

<br>

### 4. 画像の全体表示と等倍表示の切り替えをおこなう

```
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
```

<br>

## 実行方法

```
python main.py
```

<br>

## 参考にしたHP
