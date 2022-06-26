from PIL import Image
from reportlib.pdfgen import canvas
from reportlib.pdfbase.ttfonts import TTFont
from reportlib.pdfbase import pdfmeterics
from reportlib.lib.units import cm
import csv

#pdfを作るコード
def pdfBuilder(output_filename):
    POINT = 1
    ##フォントをpdfmetrics.registor()メソッドの引数に入れる
    pdfmetrics.registerFont(TTFont('MSPゴシック',''))
    xofs = 0.1 * cm
    yofs = 0.1 * cm
    paper_height = 29.7 * cm

    c = canvas.Canvas(output_filename,papersize = (21.0 * cm,paper_height))
    c.setStrokeColorRGB(0,0,0)
    c.setLineWidth(1)
    c.setFont('MSPゴシック',10 * POINT)

    header_ary = [['テーマ',1.0],['説明',2.0],['情報先',3.0],['公開日',4.0],['URL',\
5.0],['実施機関',6.0],['募集期間',7.0],['予算',8.0]]
    #1行の高さ
    height_row = 1.5
    start_cm_x = 2 * cm
    start_cm_y = paper_hight - 2 * cm
    tblheight = (len(dicary) + 1) * height_rows * cm
    end_y = start_cm_y - tblheight

    #表のXエンドの一取得
    end_cm_x = start_cm_x
    for tc in header_ary:
        end_cm_x += tc[1] * cm

    #ヘッダの背景色を塗る
    c.setFillColorRGB(0,200,200)
    c.rect(start_cm_x,start_cm_y,end_cm_x - start_cm_x, -height_rows * cm,stroke=1,\
fill = 1)
    c.setFillColorRGB(0,0,0)

    #横線
    dx = start_cm_x
    # 横線
    c.line(start_cm_x, start_cm_y, end_cm_x, start_cm_y)
    for i in range(len(dicary)+1):
        dy = start_cm_y - (i+1) * height_rows * cm
        c.line(start_cm_x, dy, end_cm_x, dy)

    # 縦線
    dx = start_cm_x 
    c.line(dx, start_cm_y, dx, end_y)
    for tc in header_ary:
        dx += tc[1] * cm
        c.line(dx, start_cm_y, dx, end_y)

    # ヘッダー描画
    dx = start_cm_x 
    dy = start_cm_y - height_rows * cm
    for tc in header_ary:
        wx = dx + tc[1] * cm / 2
        # センタリング描画
        c.drawCentredString(wx, dy+yofs, tc[0])
        dx += tc[1] * cm

    # データ描画
    dy = start_cm_y - height_rows * 2 * cm
    for dt in dicary:
        dx = start_cm_x 
        for i, tc in enumerate(header_ary):
            if i == 0 or i == 3:
                wx = dx + tc[1] * cm - xofs
                c.drawRightString(wx, dy+yofs, dt[tc[0]])
            elif i == 5:
                imgpath = './data/' + dt[tc[0]]
                img = Image.open(imgpath)
                sch = img.width / (image_width * cm)
                scv = img.height / (height_rows * cm)
                sc = max(sch, scv)
                c.drawImage(imgpath, dx, dy, 
                    width=int(img.width/sc), height=int(img.height/sc))
            else:
                c.drawString(dx+xofs, dy+yofs, dt[tc[0]])
            dx += tc[1] * cm
        dy -= height_rows * cm
    c.showPage()
    c.save()
